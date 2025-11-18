"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fotopoint.com.ar
Prompt: Create a program to calculate the shipping cost for items purchased from Fotopoint, factoring in categories like "cables and chargers" and "mobility electric devices."
Generated: DETERMINISTIC_168178d500694b6c
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_shipping_cost(category, weight):
    """
    Calculate the shipping cost based on product category and weight.
    
    Args:
        category (str): The category of the item. Allowed values are:
                        "cables and chargers", "mobility electric devices".
        weight (float): The weight of the item in kilograms.

    Returns:
        float: The calculated shipping cost.

    Raises:
        ValueError: If the category is invalid or the weight is negative.
    """
    # Shipping rates per kilogram based on category
    SHIPPING_RATES = {
        "cables and chargers": 5.00,  # $5 per kg
        "mobility electric devices": 10.00  # $10 per kg
    }
    
    # Validate input
    if not isinstance(category, str) or category not in SHIPPING_RATES:
        raise ValueError(f"Invalid category. Choose from: {', '.join(SHIPPING_RATES.keys())}")
    if not isinstance(weight, (int, float)) or weight <= 0:
        raise ValueError("Weight must be a positive number.")
    
    # Calculate shipping cost
    rate_per_kg = SHIPPING_RATES[category]
    shipping_cost = rate_per_kg * weight
    
    return shipping_cost

def main():
    """
    Main function to interact with the user and calculate shipping cost.
    """
    try:
        print("Welcome to Fotopoint Shipping Cost Calculator!")
        
        # Input category
        category = input("Enter the item category (cables and chargers, mobility electric devices): ").strip().lower()
        # Input weight
        weight = float(input("Enter the weight of the item in kilograms: ").strip())
        
        # Calculate shipping cost
        shipping_cost = calculate_shipping_cost(category, weight)
        
        print(f"The shipping cost for your order is: ${shipping_cost:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using Fotopoint Shipping Cost Calculator!")

if __name__ == "__main__":
    # Entry point of the program
    try:
        main()
    except Exception as e:
        print(f"Critical error: {e}")
        sys.exit(1)
```
