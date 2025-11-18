"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://registrations-arcium.hq.net
Prompt: Generate code to categorize products into groups such as "화장품," "식료품," and "보건의료품" based on the webpage content, and display them in a user-friendly format.
Generated: DETERMINISTIC_2c5cf617037c7061
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup

def fetch_webpage_content(url):
    """
    Fetch webpage content using requests and return the HTML content.
    :param url: URL of the webpage to fetch
    :return: HTML content of the page
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage content: {e}")
        return None

def categorize_products(html_content):
    """
    Categorize products into groups based on the webpage content.
    :param html_content: HTML content of the webpage
    :return: Dictionary with categories as keys and product lists as values
    """
    categories = {"화장품": [], "식료품": [], "보건의료품": []}
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Example: Assume product data is in <div> elements with class='product'
        products = soup.find_all('div', class_='product')
        
        for product in products:
            name = product.find('h2').text  # Example: Product name in <h2>
            description = product.find('p').text.lower()  # Example: Description in <p>
            
            # Categorize based on keywords in the description
            if 'skin' in description or 'makeup' in description or '화장품' in description:
                categories["화장품"].append(name)
            elif 'food' in description or 'grocery' in description or '식료품' in description:
                categories["식료품"].append(name)
            elif 'medicine' in description or 'health' in description or '보건의료품' in description:
                categories["보건의료품"].append(name)
                
    except Exception as e:
        print(f"Error categorizing products: {e}")
    
    return categories

def display_categories(categories):
    """
    Display categorized products in a user-friendly format.
    :param categories: Dictionary with categories and corresponding products
    """
    for category, products in categories.items():
        print(f"\nCategory: {category}")
        if products:
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product}")
        else:
            print("No products found in this category.")

# Main function
if __name__ == '__main__':
    url = input("Enter the URL of the webpage to scrape: ").strip()
    html_content = fetch_webpage_content(url)
    
    if html_content:
        categories = categorize_products(html_content)
        display_categories(categories)
```

This code is a complete Python script that categorizes products into groups based on webpage content and displays them in a user-friendly format. It uses best practices, proper error handling, and comments for clarity. Adjust parsing logic based on the structure of the actual webpage to ensure accuracy.
