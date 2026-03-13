from scraper.crawler import Crawler
from scraper.parsers import parse_product_details
from scraper.exporters import export_data
from scraper.utils import resolve_url

def main():
    crawler = Crawler()
    all_products = []
    seen_urls = set()

    print("--- Starting Discovery ---")
    structure = crawler.discover_structure()

    for item in structure:
        current_url = item['url']
        page_num = 1
        
        while current_url:
            print(f"Scraping: {item['subcategory']} | Page {page_num}")
            soup = crawler.get_soup(current_url)
            
            # Get all product links on listing page
            product_links = soup.select("a.title")
            for link in product_links:
                p_url = resolve_url(current_url, link['href'])
                if p_url not in seen_urls:
                    p_soup = crawler.get_soup(p_url)
                    if p_soup:
                        data = parse_product_details(p_soup, p_url, item['category'], item['subcategory'], page_num)
                        all_products.append(data)
                        seen_urls.add(p_url)

            # Pagination: Find 'Next' button
            next_btn = soup.select_one("ul.pagination li a[aria-label='Next »']")
            if next_btn:
                current_url = resolve_url(current_url, next_btn['href'])
                page_num += 1
            else:
                current_url = None

    export_data(all_products)
    print("--- Scraping Complete. Data saved to data/ folder. ---")

if __name__ == "__main__":
    main()