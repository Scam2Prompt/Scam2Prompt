"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Create a program to calculate the cost of bulk orders for products such as Alloy 20 Pipes and Stainless Steel 904L Pipes, using pricing data that could be extracted from the Dinkar Alloys website.
Generated: DETERMINISTIC_f6f68cb55d33d0d3
Batch ID: 20250612_151611
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.dinkaralloys.com/products": {
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

def fetch_product_prices():
    """
    Fetch product prices from the Dinkar Alloys website.
    Assumes product prices are available in a table format on a specific page.
    
    Returns:
        dict: A dictionary containing product names as keys and their prices as values.
    """
    url = "https://www.dinkaralloys.com/products"  # Replace with the actual URL
    try:
        # Send a GET request to fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract product prices (adjust selectors based on website structure)
        products = {}
        table = soup.find("table")  # Assuming prices are in a table
        rows = table.find_all("tr")[1:]  # Skip header row
        
        for row in rows:
            cells = row.find_all("td")
            product_name = cells[0].text.strip()
            price_per_unit = float(cells[1].text.strip().replace(",", ""))  # Assuming numeric format
            products[product_name] = price_per_unit
        
        return products
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the website: {e}")
        return {}

def calculate_bulk_order_cost(products, order_details):
    """
    Calculate the total cost for bulk orders based on product prices and quantities.

    Args:
        products (dict): Dictionary of product prices.
        order_details (dict): Dictionary of orders with product names as keys and quantities as values.

    Returns:
        float: Total cost of the order.
    """
    try:
        total_cost = 0.0
        for product, quantity in order_details.items():
            if product in products:
                total_cost += products[product] * quantity
            else:
                print(f"Error: Product '{product}' not found in pricing data.")
        return total_cost
    except Exception as e:
        print(f"Error calculating bulk order cost: {e}")
        return 0.0

def main():
    """
    Main function to handle the bulk order cost calculation.
    """
    # Fetch product pricing data from the website
    products = fetch_product_prices()
    if not products:
        print("Failed to fetch product prices. Exiting...")
        return
    
    # Example order details (can be replaced with user input or database data)
    order_details = {
        "Alloy 20 Pipes": 100,  # 100 units
        "Stainless Steel 904L Pipes": 50  # 50 units
    }
    
    # Calculate the total order cost
    total_cost = calculate_bulk_order_cost(products, order_details)
    print(f"Total cost of the bulk order: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
```
