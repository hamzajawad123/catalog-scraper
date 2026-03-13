from urllib.parse import urljoin
import re

def resolve_url(base_url, relative_url):
    """Correctly joins relative links to absolute URLs."""
    return urljoin(base_url, relative_url)

def clean_price(price_str):
    """Normalizes price into float."""
    if not price_str: return 0.0
    cleaned = re.sub(r'[^\d.]', '', price_str)
    return float(cleaned) if cleaned else 0.0

def clean_text(text):
    """Handles whitespace and empty fields."""
    return text.strip() if text else ""