"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Write a Python script to calculate the cost of building a home studio like Eric Navarro's, considering the prices of equipment such as the Cad E100s microphone and SSL 2 audio interface.
Generated: DETERMINISTIC_9dd6a6ec67d5654c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the cost of building a home studio.
This script includes the prices of specific equipment such as the Cad E100s microphone and SSL 2 audio interface.
"""

# Import necessary modules
import sys

def calculate_total_cost(equipment_prices):
    """
    Calculate the total cost of all equipment.

    Args:
        equipment_prices (dict): A dictionary containing equipment names and their prices.

    Returns:
        float: The total cost of all equipment.
    """
    try:
        # Ensure all prices are valid numbers
        total_cost = sum(equipment_prices.values())
        return total_cost
    except TypeError as e:
        print(f"Error: Invalid price value detected. {e}")
        sys.exit(1)

def main():
    """
    Main function to calculate and display the total cost of building a home studio.
    """
    # Equipment and their respective prices (in USD)
    equipment_prices = {
        "Cad E100s Microphone": 499.00,  # Price of Cad E100s microphone
        "SSL 2 Audio Interface": 229.99,  # Price of SSL 2 audio interface
        "Studio Monitors (Pair)": 300.00,  # Example price for studio monitors
        "Acoustic Treatment": 150.00,  # Example price for acoustic treatment
        "Microphone Stand": 50.00,  # Example price for microphone stand
        "XLR Cable": 25.00,  # Example price for XLR cable
        "Headphones": 100.00,  # Example price for headphones
    }

    # Calculate the total cost
    total_cost = calculate_total_cost(equipment_prices)

    # Display the total cost
    print("Home Studio Equipment Cost Breakdown:")
    for item, price in equipment_prices.items():
        print(f"{item}: ${price:.2f}")
    print(f"\nTotal Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
