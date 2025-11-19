"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canguldemir.com.tr
Prompt: Write a Python script to calculate the total cost of purchasing different sizes of construction steel bars based on the pricing information from Cangül Demir Çelik A.Ş.
Generated: DETERMINISTIC_ad40dc1d8d97a338
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the total cost of purchasing different sizes of construction steel bars.
Pricing information is based on the rates provided by Cangül Demir Çelik A.Ş.
"""

# Import necessary modules
import sys

def get_pricing_data():
    """
    Returns a dictionary representing the pricing structure for different steel bar sizes.
    Prices are assumed to be in TRY per meter.
    
    Returns:
        dict: A dictionary where keys are bar sizes (in mm) and values are prices per meter.
    """
    return {
        12: 25.00,  # 12mm steel bar costs 25 TRY per meter
        16: 35.00,  # 16mm steel bar costs 35 TRY per meter
        20: 45.00,  # 20mm steel bar costs 45 TRY per meter
        25: 55.00,  # 25mm steel bar costs 55 TRY per meter
        32: 75.00   # 32mm steel bar costs 75 TRY per meter
    }

def calculate_total_cost(order_details, pricing_data):
    """
    Calculates the total cost for the steel bars based on order details and pricing data.

    Args:
        order_details (dict): A dictionary where keys are bar sizes (in mm) and values are quantities (in meters).
        pricing_data (dict): A dictionary with pricing information where keys are bar sizes (in mm)
                             and values are prices per meter.

    Returns:
        float: The total cost of the order.
    """
    total_cost = 0.0
    # Calculate total cost based on order details and pricing data
    for bar_size, quantity in order_details.items():
        if bar_size not in pricing_data:
            raise ValueError(f"Invalid bar size: {bar_size}. No pricing data available for this size.")
        
        # Calculate cost for this bar size and add to total
        total_cost += pricing_data[bar_size] * quantity
    
    return total_cost

def main():
    """
    Main function to execute the script.
    Allows user to input order details and calculates the total cost of the order.
    """
    print("Welcome to the Steel Bar Cost Calculator!")
    print("Available steel bar sizes and their prices (TRY/m):")
    
    # Fetch pricing data and display it
    pricing_data = get_pricing_data()
    for bar_size, price in pricing_data.items():
        print(f"{bar_size}mm: {price:.2f} TRY/m")
    
    print("\nPlease enter your order details.")
    print("For each bar size, specify the quantity (in meters). Enter 0 if you don't need a particular size.")
    
    # Capture user's order details
    order_details = {}
    for bar_size in pricing_data.keys():
        while True:
            try:
                quantity = float(input(f"Enter quantity for {bar_size}mm steel bars (meters): "))
                if quantity < 0:
                    raise ValueError("Quantity cannot be negative. Please enter a valid number.")
                order_details[bar_size] = quantity
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
    
    # Calculate total cost
    try:
        total_cost = calculate_total_cost(order_details, pricing_data)
        print(f"\nThe total cost of your order is: {total_cost:.2f} TRY")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
