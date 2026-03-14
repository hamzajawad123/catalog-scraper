# Catalog Scraper Mini Project

## Project Purpose

The **Catalog Scraper Mini Project** is a professional-grade web scraping solution designed to extract and analyze product data from the **WebScraper.io test site**:

https://webscraper.io/test-sites/e-commerce/static

This project demonstrates a **modular Python architecture** and a **robust engineering workflow**.

The scraper is built to navigate a **hierarchical e-commerce structure**, handling:

- **Category Discovery:** Automatic detection of site sections.
- **Subcategory Traversal:** Moving deeper into product niches.
- **Pagination:** Following "Next" buttons across multiple pages.
- **Detail Enrichment:** Visiting individual product pages to extract specific hardware specs, ratings, and reviews.

---

# Technical Setup & Dependency Management

## Set Up the Project with `uv`

This project uses **uv**, a high-performance Python package manager, to create a **reproducible development environment**.

### 1. Initialize the Project

```bash
uv init
```

### 2. Configure the Environment

The project automatically creates a **virtual environment** inside:

```
.venv
```

This keeps all dependencies isolated from the global Python installation.

---

# Installing Dependencies

All required libraries are defined in the **`pyproject.toml`** file.

Required packages include:

- `requests`
- `beautifulsoup4`
- `pandas`

Install all dependencies using:

```bash
uv sync
```

---

# Running the Scraper

To execute the complete scraping pipeline (from **site discovery → data extraction → CSV generation**), run:

```bash
uv run src/main.py
```

During execution, the scraper will print **progress logs** showing:

- category navigation
- subcategory traversal
- pagination progress
- product extraction status

---

# Git Branch Workflow

This project follows a **structured Git branching strategy** to maintain clean and professional version control.

## Main Branches

### `main`
The **stable production branch** containing the final validated code.

### `dev`
The **development integration branch** where all features and fixes are merged before final release.

---

## Feature Branches

### `feature/catalog-navigation`

Implements logic for:

- category discovery
- subcategory traversal
- structured site navigation

### `feature/product-details`

Implements:

- product page scraping
- pagination handling
- detailed product attribute extraction

---

## Fix Branches

### `fix/url-resolution`

Resolved issues related to:

- relative image paths
- incorrect product page links

### `fix/deduplication`

Added logic to ensure:

- duplicate products are not stored
- the final dataset remains clean and unique

---

# Development Workflow

The workflow used for development was:

```
feature/* or fix/* 
        ↓
      merge into dev
        ↓
   final validation
        ↓
      merge into main
```

This ensures **stable releases and clean commit history**.

---

# Assumptions

### Static Content

The target website serves **static HTML**, allowing efficient scraping without requiring a **headless browser** such as Selenium.

### Consistent Data Attributes

Ratings are assumed to be consistently stored using:

- `data-rating` attribute
- `ws-icon-star` classes

### Specification Locations

Specific hardware details (such as **HDD size**) are assumed to be located within the **"swatches" UI elements** on the product detail pages.

---

# Limitations

### Sequential Execution

The scraper currently runs **synchronously**.

While reliable for small-to-medium datasets, **multi-threading or async execution** would be required for significantly larger catalogs.

### Network Stability

The script assumes a **stable internet connection**.

Basic error handling exists, but the scraper does not currently implement:

- advanced retry logic
- exponential backoff mechanisms

### Anti-Scraping Protections

The scraper does **not implement anti-blocking techniques** such as:

- proxy rotation
- user-agent rotation

This is intentional because the target site is a **dedicated test environment designed for scraping practice**.

---