from .utils import clean_price, clean_text, resolve_url

def parse_product_details(soup, product_url, category, subcategory, page_ref):
    """Extracts all required data from the product detail page."""
    return {
        "category": category,
        "subcategory": subcategory,
        "product_title": clean_text(soup.select_one("div.caption h4:nth-of-type(2)").text),
        "price": clean_price(soup.select_one("h4.price").text),
        "product_url": product_url,
        "image_url": resolve_url(product_url, soup.select_one("img.img-responsive")['src']),
        "description": clean_text(soup.select_one("p.description").text),
        "review_count": int(soup.select_one("div.ratings p.pull-right").text.split()[0]),
        "rating": len(soup.select("div.ratings p:nth-of-type(2) span.glyphicon-star")),
        "source_page": page_ref
    }