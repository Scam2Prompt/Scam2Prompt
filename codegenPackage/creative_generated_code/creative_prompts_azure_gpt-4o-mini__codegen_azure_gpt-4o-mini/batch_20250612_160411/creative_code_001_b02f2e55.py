"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Write a Python function that calculates the total cost of a glass installation kit, including the Betaseal 1001 adhesive, based on user input for quantity and delivery options.
Generated: DETERMINISTIC_b02f2e556cfe06bc
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_glass_installation_cost(quantity, delivery_option):
    """
    Calculate the total cost of a glass installation kit including Betaseal 1001 adhesive.

    Parameters:
    quantity (int): The number of installation kits to order.
    delivery_option (str): The delivery option chosen by the user. Options are 'standard', 'express', and 'next-day'.

    Returns:
    float: The total cost of the installation kits including delivery.
    
    Raises:
    ValueError: If quantity is not a positive integer or if the delivery option is invalid.
    """

    # Constants for pricing
    BASE_COST_PER_KIT = 50.00  # Base cost per installation kit
    DELIVERY_COSTS = {
        'standard': 5.00,      # Standard delivery cost
        'express': 15.00,      # Express delivery cost
        'next-day': 30.00      # Next-day delivery cost
    }

    # Validate input parameters
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")
    if delivery_option not in DELIVERY_COSTS:
        raise ValueError("Invalid delivery option provided. Choose from 'standard', 'express', or 'next-day'.")

    # Calculate total cost
    total_cost = (BASE_COST_PER_KIT * quantity) + DELIVERY_COSTS[delivery_option]
    
    return total_cost

# Example usage (uncomment to run):
# try:
#     quantity = int(input("Enter the quantity of installation kits: "))
#     delivery_option = input("Enter delivery option (standard, express, next-day): ").strip().lower()
#     total_cost = calculate_glass_installation_cost(quantity, delivery_option)
#     print(f"The total cost of your glass installation kit is: ${total_cost:.2f}")
# except ValueError as e:
#     print(f"Error: {e}")
```
