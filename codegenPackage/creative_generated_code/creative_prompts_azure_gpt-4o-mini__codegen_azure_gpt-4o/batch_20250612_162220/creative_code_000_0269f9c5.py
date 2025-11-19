"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.practisea.com
Prompt: Generate a Python script to scrape product information from Practisea's website, focusing on their unique handcrafted designs and eco-friendly materials.
Generated: DETERMINISTIC_0269f9c578b20573
Batch ID: 20250612_162220
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.practisea.com": {
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

# Constants
BASE_URL = 'https://www.practisea.com'  # Replace with the actual URL of Practisea's website
PRODUCTS_PAGE = '/products'  # Replace with the actual products page URL if necessary

def scrape_practisea_products():
    """
    Scrapes product information from Practisea's website.

    Returns:
        list of dict: A list containing product data, where each product is represented as a dictionary.
    """
    try:
        # Send a GET request to the products page
        response = requests.get(BASE_URL + PRODUCTS_PAGE)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4XX, 5XX)
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Assuming products are listed in a container with class 'product-item'
        product_elements = soup.find_all(class_='product-item')
        
        # List to store the scraped product data
        products = []
        
        # Iterate through each product element and extract details
        for element in product_elements:
            product_name = element.find(class_='product-name').get_text(strip=True) if element.find(class_='product-name') else 'N/A'
            product_price = element.find(class_='product-price').get_text(strip=True) if element.find(class_='product-price') else 'N/A'
            product_materials = element.find(class_='product-materials').get_text(strip=True) if element.find(class_='product-materials') else 'N/A'
            
            # Append the product information to the list as a dictionary
            products.append({
                'Name': product_name,
                'Price': product_price,
                'Materials': product_materials
            })
        
        return products

    except requests.exceptions.RequestException as e:
        print(f"Error while making request: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def save_to_csv(products, file_name='practisea_products.csv'):
    """
    Saves the scraped product information to a CSV file.

    Args:
        products (list of dict): The product data to save.
        file_name (str): The name of the CSV file to create.
    """
    try:
        # Create or overwrite a CSV file
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Materials'])
            writer.writeheader()  # Write the header row
            writer.writerows(products)  # Write the product rows
        
        print(f"Data successfully saved to {file_name}")
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

if __name__ == '__main__':
    # Step 1: Scrape product data
    print("Scraping product information from Practisea...")
    products = scrape_practisea_products()
    
    if products:
        print(f"Scraped {len(products)} products.")
        
        # Step 2: Save to CSV
        print("Saving data to CSV...")
        save_to_csv(products)
    else:
        print("No products found or an error occurred during scraping.")
```

---

### Note:
You will need to adjust the `BASE_URL`, `PRODUCTS_PAGE`, and the class names for the product elements (e.g., `'product-item'`, `'product-name'`, `'product-price'`, `'product-materials'`) according to the actual HTML structure of Practisea's website. Ensure you have permission to scrape their data and that scraping does not violate their terms of service.
