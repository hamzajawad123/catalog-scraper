import requests
from bs4 import BeautifulSoup
from .utils import resolve_url

class Crawler:
    BASE_URL = "https://webscraper.io/test-sites/e-commerce/static"

    def get_soup(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"Error loading {url}: {e}")
            return None

    def discover_structure(self):
        """Finds categories and subcategories."""
        soup = self.get_soup(self.BASE_URL)
        structure = [] # List of (cat_name, subcat_name, subcat_url)
        
        # Finding Categories in the sidebar
        categories = soup.select("#side-menu > li > a")[1:] # Skip 'Home'
        for cat in categories:
            cat_name = cat.text.strip()
            cat_url = resolve_url(self.BASE_URL, cat['href'])
            
            # Visit category to find subcategories
            cat_soup = self.get_soup(cat_url)
            sub_links = cat_soup.select("ul.nav-second-level li a")
            for sub in sub_links:
                structure.append({
                    "category": cat_name,
                    "subcategory": sub.text.strip(),
                    "url": resolve_url(self.BASE_URL, sub['href'])
                })
        return structure