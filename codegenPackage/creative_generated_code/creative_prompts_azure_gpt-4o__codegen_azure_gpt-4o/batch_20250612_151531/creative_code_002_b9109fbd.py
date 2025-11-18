"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Generate a Python script to automate online order processing for thermal paper rolls, incorporating features like customer-specific customization and bulk discounts as highlighted by Apos Chile.
Generated: DETERMINISTIC_b9109fbd42a665d2
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sys
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants for bulk discount thresholds
BULK_DISCOUNT_THRESHOLD = 50  # Minimum quantity for bulk discount
BULK_DISCOUNT_RATE = 0.10     # 10% bulk discount

# Predefined customer-specific customizations
CUSTOMIZATION_OPTIONS = {
    "standard": {"width": 80, "length": 70},  # Standard thermal paper size
    "custom": {"width": None, "length": None}  # Allows flexible customization
}

# Sample price per roll (could be fetched from a database in production)
PRICE_PER_ROLL = 2.00

def calculate_price(quantity: int, customer_type: str) -> float:
    """
    Calculate the total price for an order, applying bulk discounts if applicable.
    :param quantity: Number of rolls ordered
    :param customer_type: Type of customer ('standard' or 'custom')
    :return: Total price after applicable discounts
    """
    try:
        base_price = quantity * PRICE_PER_ROLL
        if quantity >= BULK_DISCOUNT_THRESHOLD:
            discount = base_price * BULK_DISCOUNT_RATE
            logging.info(f"Bulk discount applied: ${discount:.2f}")
            return base_price - discount
        return base_price
    except Exception as e:
        logging.error(f"Error calculating price: {e}")
        raise

def process_order(order: Dict) -> Dict:
    """
    Process the order and generate a summary.
    :param order: Dictionary containing order details
    :return: Order summary as a dictionary
    """
    try:
        customer_name = order.get("customer_name", "Unknown")
        quantity = order.get("quantity", 0)
        customer_type = order.get("customer_type", "standard")
        
        if customer_type not in CUSTOMIZATION_OPTIONS:
            raise ValueError("Invalid customer type provided.")
        
        # Ensure customization values are valid
        customization = CUSTOMIZATION_OPTIONS[customer_type]
        if customer_type == "custom":
            customization["width"] = order.get("width", 80)
            customization["length"] = order.get("length", 70)
        
        total_price = calculate_price(quantity, customer_type)
        
        order_summary = {
            "customer_name": customer_name,
            "quantity": quantity,
            "customization": customization,
            "total_price": total_price
        }
        
        logging.info(f"Order processed successfully: {order_summary}")
        return order_summary
    except Exception as e:
        logging.error(f"Error processing order: {e}")
        raise

def main():
    # Example order (In production, this could be read from an API or database)
    sample_order = {
        "customer_name": "Apos Chile",
        "quantity": 60,
        "customer_type": "custom",
        "width": 80,
        "length": 75
    }
    
    try:
        # Process the sample order
        order_summary = process_order(sample_order)
        
        # Output the order summary as JSON
        print(json.dumps(order_summary, indent=4))
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)  # Exit with an error code in case of failure

if __name__ == "__main__":
    main()
```
