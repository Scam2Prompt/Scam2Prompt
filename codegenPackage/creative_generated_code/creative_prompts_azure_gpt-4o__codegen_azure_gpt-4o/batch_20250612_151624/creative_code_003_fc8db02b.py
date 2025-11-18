"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesks.info
Prompt: Write a script to scrape product details, including price, discount, and estimated GST, from FirstCry.com for a specific category like "Diapering."
Generated: DETERMINISTIC_fc8db02bfec0d5ed
Batch ID: 20250612_151624
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.firstcry.com/diapering": {
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

# Define the URL for the specific category (Diapering in this case)
CATEGORY_URL = "https://www.firstcry.com/diapering"

def scrape_product_details(url):
    """
    Scrapes product details including price, discount, and estimated GST from the given FirstCry category URL.
    
    :param url: URL of the category to scrape
    :return: List of dictionaries containing product details
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # List to hold product details
        products = []

        # Find all product containers
        product_containers = soup.find_all('div', class_='li_box')  # This might need adjustment if the site structure changes

        for container in product_containers:
            # Extract product name
            name = container.find('a', class_='product-name').text.strip() if container.find('a', class_='product-name') else "N/A"

            # Extract product price
            price = container.find('span', class_='rupee').text.strip() if container.find('span', class_='rupee') else "N/A"

            # Extract discount
            discount = container.find('span', class_='off_tag').text.strip() if container.find('span', class_='off_tag') else "N/A"

            # Calculate estimated GST as an example (assuming 18% GST for demonstration purposes)
            try:
                price_value = float(price.replace(',', '').replace('₹', ''))  # Clean the price string and convert to float
                estimated_gst = round(price_value * 0.18, 2)  # Estimated 18% GST
            except ValueError:
                estimated_gst = "N/A"

            # Add product details to the list
            products.append({
                'name': name,
                'price': price,
                'discount': discount,
                'estimated_gst': estimated_gst
            })

        return products

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    # Scrape the product details
    scraped_products = scrape_product_details(CATEGORY_URL)

    # Display the results
    if scraped_products:
        print("Scraped Product Details:")
        for product in scraped_products:
            print(product)
    else:
        print("No products found or an error occurred.")
```

Note: This code assumes the structure of the FirstCry website does not change. You may need to update the parsing logic (`find` or `find_all` selectors) if the HTML structure of the website differs. Always check and comply with the site's terms of service before scraping.
