"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shishehbalkon.ir
Prompt: Generate code to simulate the pricing model for glass partitions with varying sizes and finishes, referencing the specific price ranges and finishes mentioned on the website.
Generated: DETERMINISTIC_e4806d5cd6f211d9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# glass_partition_pricing_model.py

"""
This program simulates a pricing model for glass partitions with varying sizes and finishes.
It calculates the total price based on user input size and selected finish, referencing predefined price ranges.
"""

# Import necessary modules
import sys

# Define global constants for pricing
SIZE_PRICE_RANGES = {
    "small": 100,  # Price for partitions up to 10 sq ft
    "medium": 250,  # Price for partitions from 10 to 30 sq ft
    "large": 500   # Price for partitions above 30 sq ft
}

FINISH_PRICE_RANGES = {
    "clear": 0,  # No additional cost for clear finish
    "frosted": 50,  # Additional cost for frosted finish
    "tinted": 100  # Additional cost for tinted finish
}

# Function to calculate partition price
def calculate_price(size_in_sqft, finish_type):
    """
    Calculate the price of a glass partition based on its size and finish.
    :param size_in_sqft: float - Size of the partition in square feet
    :param finish_type: str - Type of finish (clear, frosted, tinted)
    :return: float - Total price of the partition
    """
    try:
        # Validate size input
        if size_in_sqft <= 0:
            raise ValueError("Size must be greater than zero.")
        
        # Determine size pricing
        if size_in_sqft <= 10:
            base_price = SIZE_PRICE_RANGES["small"]
        elif size_in_sqft <= 30:
            base_price = SIZE_PRICE_RANGES["medium"]
        else:
            base_price = SIZE_PRICE_RANGES["large"]
        
        # Validate finish input
        if finish_type not in FINISH_PRICE_RANGES:
            raise ValueError("Invalid finish type. Available options: clear, frosted, tinted.")
        
        finish_price = FINISH_PRICE_RANGES[finish_type]
        
        # Calculate total price
        return base_price + finish_price

    except ValueError as ve:
        # Handle input errors
        print(f"Error: {ve}")
        sys.exit(1)

# Main function for user interaction
def main():
    """
    Main function to interact with the user and calculate glass partition pricing.
    """
    try:
        # Get user input for size
        size_in_sqft = float(input("Enter the size of the partition in square feet: "))
        
        # Get user input for finish type
        print("Available finishes: clear, frosted, tinted.")
        finish_type = input("Enter the type of finish: ").lower()
        
        # Calculate price
        total_price = calculate_price(size_in_sqft, finish_type)
        print(f"The total price for your glass partition is: ${total_price:.2f}")
    
    except ValueError:
        # Handle input conversion errors
        print("Error: Invalid input. Please enter numeric values for size and valid strings for finish.")
        sys.exit(1)

# Entry point for the program
if __name__ == "__main__":
    main()
```
