from .utils import clean_price, clean_text, resolve_url

def parse_product_details(soup, product_url, category, subcategory, page_ref):
    """Hybrid extraction for ratings: Attribute check + Star counting."""
    
    # Standard fields
    title_el = soup.select_one("div.caption h4:nth-of-type(2)")
    price_el = soup.select_one("h4.price")
    desc_el = soup.select_one("p.description")
    img_el = soup.select_one("img.img-responsive")
    
    # 1. Review Count (itemprop)
    review_el = soup.select_one('span[itemprop="reviewCount"]')
    review_count = int(review_el.text.strip()) if review_el else 0
    
    # 2. Rating (Hybrid Logic)
    rating_val = 0
    # Try Method A: Get data-rating attribute
    rating_el = soup.select_one("div.ratings p[data-rating]")
    if rating_el and rating_el.get("data-rating"):
        rating_val = int(rating_el.get("data-rating"))
    else:
        # Try Method B: Count the star spans (based on your latest screenshot)
        stars = soup.select("div.ratings .ws-icon-star")
        if stars:
            rating_val = len(stars)

    # 3. Dynamic Specs (HDD Swatches)
    spec_detail = "No specific detail available"
    label_el = soup.select_one("label.memory")
    swatch_btns = soup.select("div.swatches button.swatch")
    
    if label_el and swatch_btns:
        label_text = label_el.text.replace(":", "").strip()
        values = [btn.text.strip() for btn in swatch_btns]
        spec_detail = f"{label_text} ({' / '.join(values)})"

    return {
        "category": category,
        "subcategory": subcategory,
        "product_title": clean_text(title_el.text) if title_el else "N/A",
        "price": clean_price(price_el.text) if price_el else 0.0,
        "product_url": product_url,
        "image_url": resolve_url(product_url, img_el['src']) if img_el else None,
        "description": clean_text(desc_el.text) if desc_el else "",
        "review_count": review_count,
        "rating": rating_val,
        "important_detail": spec_detail,
        "source_page": page_ref
    }