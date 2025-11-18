"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pavainc.com
Prompt: Generate a script to automate customer quotes for bulk salt and UltraGLOW™ Snow and Ice Melt orders, factoring in delivery zones and product availability.
Generated: DETERMINISTIC_ab3a444480ca25ed
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Constants for delivery zones and rates
DELIVERY_ZONES = {
    "Zone A": 0.05,  # 5% surcharge
    "Zone B": 0.10,  # 10% surcharge
    "Zone C": 0.15   # 15% surcharge
}

# Product pricing and availability
PRODUCTS = {
    "Bulk Salt": {
        "price_per_unit": 50,  # Price in USD per ton
        "availability": 1000  # Maximum quantity available (in tons)
    },
    "UltraGLOW™ Snow and Ice Melt": {
        "price_per_unit": 120,  # Price in USD per ton
        "availability": 500  # Maximum quantity available (in tons)
    }
}

def get_quote(product_name, quantity, delivery_zone):
    """
    Calculate the cost for a bulk order, factoring in delivery zone surcharge and availability.
    
    Args:
        product_name (str): Name of the product ('Bulk Salt' or 'UltraGLOW™ Snow and Ice Melt')
        quantity (int): Quantity in tons the customer wants to order
        delivery_zone (str): Delivery zone ('Zone A', 'Zone B', 'Zone C')
        
    Returns:
        dict: Quote details including total cost and any error messages if applicable.
    """
    # Validate product name
    if product_name not in PRODUCTS:
        return {"error": "Invalid product name. Please choose either 'Bulk Salt' or 'UltraGLOW™ Snow and Ice Melt'."}
    
    # Validate delivery zone
    if delivery_zone not in DELIVERY_ZONES:
        return {"error": f"Invalid delivery zone. Available zones are: {', '.join(DELIVERY_ZONES.keys())}"}
    
    # Validate quantity
    if quantity <= 0:
        return {"error": "Invalid quantity. Quantity must be a positive number."}
    
    # Check product availability
    product_info = PRODUCTS[product_name]
    if quantity > product_info["availability"]:
        return {"error": f"Requested quantity exceeds availability. Max available: {product_info['availability']} tons."}
    
    # Calculate base cost and delivery surcharge
    base_cost = product_info["price_per_unit"] * quantity
    delivery_surcharge = base_cost * DELIVERY_ZONES[delivery_zone]
    total_cost = base_cost + delivery_surcharge
    
    # Generate quote
    quote = {
        "product": product_name,
        "quantity": quantity,
        "delivery_zone": delivery_zone,
        "base_cost": base_cost,
        "delivery_surcharge": delivery_surcharge,
        "total_cost": total_cost,
        "message": "Quote successfully generated."
    }
    return quote

def main():
    """
    Main function to interact with the user and generate quotes.
    """
    print("Welcome to the Bulk Salt and UltraGLOW™ Snow and Ice Melt Quote Generator!")
    
    try:
        # Prompt user for input
        product_name = input("Enter the product name ('Bulk Salt' or 'UltraGLOW™ Snow and Ice Melt'): ").strip()
        quantity = int(input("Enter the quantity in tons: ").strip())
        delivery_zone = input("Enter the delivery zone ('Zone A', 'Zone B', 'Zone C'): ").strip()
        
        # Generate quote
        quote = get_quote(product_name, quantity, delivery_zone)
        
        # Check for errors
        if "error" in quote:
            print(f"Error: {quote['error']}")
        else:
            # Display the quote
            print(json.dumps(quote, indent=4))
    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for quantity.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
