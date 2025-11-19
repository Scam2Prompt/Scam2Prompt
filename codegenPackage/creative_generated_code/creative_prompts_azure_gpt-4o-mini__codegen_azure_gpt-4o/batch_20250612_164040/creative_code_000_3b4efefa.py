"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaniti-shop.com
Prompt: Generate a Python script to scrape product details from an online toy store, focusing on categories like "צעצועי ילדים" and "אלקטרוניקה".
Generated: DETERMINISTIC_3b4efefa3924aab0
Batch ID: 20250612_164040
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.exampletoystore.com": {
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
import csv
import os

# Define constants
BASE_URL = "https://www.exampletoystore.com"  # Replace with the actual toy store's URL
CATEGORIES = ["צעצועי ילדים", "אלקטרוניקה"]  # Categories to scrape
OUTPUT_FILE = "product_details.csv"  # Output CSV file

# Function to fetch the HTML content of a page
def fetch_page_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

# Function to parse product details from category pages
def parse_category_page(html_content, category):
    soup = BeautifulSoup(html_content, "html.parser")
    products = []

    # Modify these selectors based on the website's structure
    product_elements = soup.select(".product-item")
    for product in product_elements:
        try:
            name = product.select_one(".product-name").get_text(strip=True)
            price = product.select_one(".product-price").get_text(strip=True)
            link = product.select_one(".product-name a").get("href")
            if link and not link.startswith("http"):
                link = BASE_URL + link
            
            # Append the product details as a dictionary
            products.append({
                "Category": category,
                "Name": name,
                "Price": price,
                "Link": link
            })
        except AttributeError as e:
            # Skip the current product if any required field is missing
            print(f"Error parsing product details: {e}")
            continue
    return products

# Function to write product details to a CSV file
def write_to_csv(products, file_name):
    file_exists = os.path.isfile(file_name)
    with open(file_name, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Category", "Name", "Price", "Link"])
        if not file_exists:
            writer.writeheader()  # Write header only if the file is new
        writer.writerows(products)

# Main function to orchestrate the scraping process
def main():
    all_products = []
    for category in CATEGORIES:
        print(f"Scraping category: {category}")
        category_url = f"{BASE_URL}/search?q={category}"  # Modify URL structure as needed
        html_content = fetch_page_content(category_url)
        
        if not html_content:
            print(f"Skipping category {category} due to errors.")
            continue
        
        category_products = parse_category_page(html_content, category)
        all_products.extend(category_products)
    
    if all_products:
        write_to_csv(all_products, OUTPUT_FILE)
        print(f"Scraping completed. Data saved to {OUTPUT_FILE}.")
    else:
        print("No products found. No data written to file.")

# Run the script
if __name__ == "__main__":
    main()
```
