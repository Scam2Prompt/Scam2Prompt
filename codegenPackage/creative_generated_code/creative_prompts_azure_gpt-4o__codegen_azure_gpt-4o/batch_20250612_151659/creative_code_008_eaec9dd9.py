"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groundcell.uk.com
Prompt: Write a program to calculate the cost of purchasing Groundcell panels online for direct delivery, factoring in panel sizes and quantities as described on the website.
Generated: DETERMINISTIC_eaec9dd9426f645c
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate the cost of purchasing Groundcell panels online for direct delivery.
Users can specify panel sizes and quantities, and the program factors in costs based on the provided data.
"""

# Import necessary modules
import sys

# Define constants for panel sizes and prices (example data)
PANEL_PRICES = {
    "small": 50.0,   # Small panel costs $50.00
    "medium": 100.0,  # Medium panel costs $100.00
    "large": 150.0    # Large panel costs $150.00
}

DELIVERY_FEE = 20.0  # Flat delivery fee per order

def calculate_cost(panel_orders):
    """
    Calculate the total order cost including panel costs and delivery fee.

    Args:
        panel_orders (dict): Dictionary containing panel sizes as keys and quantities as values.

    Returns:
        float: Total cost of the order including delivery fee.
    """
    # Initialize total cost
    total_cost = 0.0

    # Iterate through panel orders and calculate cost
    for panel_size, quantity in panel_orders.items():
        if panel_size not in PANEL_PRICES:
            raise ValueError(f"Invalid panel size: {panel_size}. Allowed sizes are {list(PANEL_PRICES.keys())}.")
        if quantity < 0:
            raise ValueError(f"Invalid quantity: {quantity}. Quantity cannot be negative.")
        
        # Add cost for the current panel size
        total_cost += PANEL_PRICES[panel_size] * quantity

    # Add delivery fee to the total cost
    total_cost += DELIVERY_FEE
    
    return total_cost


def main():
    """
    Main function to handle user input and calculate order cost.
    """
    try:
        # Display available panel sizes and prices
        print("Available Groundcell Panel Sizes and Prices:")
        for size, price in PANEL_PRICES.items():
            print(f"- {size.capitalize()} panel: ${price:.2f}")

        print("\nEnter your order details (panel size and quantity). Type 'done' when finished.")

        # Dictionary to store order data
        panel_orders = {}

        while True:
            # Get user input for panel size
            panel_size = input("Enter panel size (small, medium, large): ").strip().lower()
            if panel_size == "done":
                break

            # Validate panel size
            if panel_size not in PANEL_PRICES:
                print(f"Invalid panel size. Choose from {list(PANEL_PRICES.keys())}.")
                continue

            # Get user input for panel quantity
            try:
                quantity = int(input(f"Enter quantity for {panel_size} panels: ").strip())
                if quantity < 0:
                    print("Quantity cannot be negative. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer for quantity.")
                continue

            # Store valid panel size and quantity in the order dictionary
            panel_orders[panel_size] = panel_orders.get(panel_size, 0) + quantity

        # If no orders, terminate
        if not panel_orders:
            print("No panels ordered. Exiting program.")
            return

        # Calculate total cost
        total_cost = calculate_cost(panel_orders)

        # Display order summary and total cost
        print("\nOrder Summary:")
        for panel_size, quantity in panel_orders.items():
            print(f"- {panel_size.capitalize()} panel x {quantity}: ${PANEL_PRICES[panel_size] * quantity:.2f}")
        print(f"\nDelivery Fee: ${DELIVERY_FEE:.2f}")
        print(f"Total Order Cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Run the main function
    main()
```
