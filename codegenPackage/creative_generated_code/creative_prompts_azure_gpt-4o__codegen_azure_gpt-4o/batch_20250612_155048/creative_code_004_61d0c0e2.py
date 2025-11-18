"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Create a Python script that uses web scraping to extract product details (e.g., name, category, and price) from CM-Canada's website, focusing on their "Nouveautés et produits populaires."
Generated: DETERMINISTIC_61d0c0e2c148d55c
Batch ID: 20250612_155048
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.cm-canada.com/nouveautes-et-produits-populaires": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup

def scrape_cm_canada_products():
    """
    Scrapes product details (name, category, and price) from CM-Canada's 'Nouveautés et produits populaires' section.
    
    Returns:
        list of dict: A list of dictionaries containing product details.
    """
    # URL of the CM-Canada website's 'Nouveautés et produits populaires' section
    url = "https://www.cm-canada.com/nouveautes-et-produits-populaires"
    
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")
        return []

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize an empty list to store product details
    products = []

    # Find the section containing products (adjust the selector based on the actual HTML structure)
    product_elements = soup.find_all('div', class_='product-item')  # Example CSS class, update as needed

    for product_element in product_elements:
        try:
            # Extract product name
            name = product_element.find('h2', class_='product-title').get_text(strip=True)

            # Extract product category
            category = product_element.find('span', class_='product-category').get_text(strip=True)

            # Extract product price
            price = product_element.find('span', class_='product-price').get_text(strip=True)

            # Append product details to the list
            products.append({
                'name': name,
                'category': category,
                'price': price
            })
        except AttributeError as e:
            # Handle missing information gracefully
            print(f"An error occurred while extracting product details: {e}")
            continue

    return products


if __name__ == "__main__":
    # Scrape products and print the results
    scraped_products = scrape_cm_canada_products()
    if scraped_products:
        print("Scraped Product Details:")
        for product in scraped_products:
            print(product)
    else:
        print("No products found or an error occurred.")
```

**Note:** Be sure to adjust the CSS selectors (e.g., `product-item`, `product-title`, `product-category`, `product-price`) based on the actual structure and class names used on CM-Canada's website. To avoid violating terms of service, confirm that web scraping is permitted on the site. If the website uses JavaScript to dynamically load content, additional tools like Selenium may be required.
