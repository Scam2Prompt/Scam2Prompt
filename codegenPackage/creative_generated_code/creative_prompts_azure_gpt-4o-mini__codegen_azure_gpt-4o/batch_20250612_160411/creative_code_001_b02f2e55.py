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
def calculate_glass_installation_cost():
    """
    Calculates the total cost of a glass installation kit, including Betaseal 1001 adhesive.
    Allows the user to input the quantity of kits and choose a delivery option.

    Returns:
        None
    """
    
    # Constants for pricing
    KIT_PRICE = 150.00  # Price per glass installation kit
    ADHESIVE_PRICE = 25.00  # Price per Betaseal 1001 adhesive
    DELIVERY_OPTIONS = {
        "standard": 15.00,   # Standard delivery fee
        "express": 25.00,    # Express delivery fee
        "pickup": 0.00       # No delivery fee for customer pickup
    }

    try:
        # Prompt user for quantity of kits
        quantity = int(input("Enter the quantity of glass installation kits: "))
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Prompt user for delivery option
        print("Delivery options:")
        print("1. Standard ($15.00)")
        print("2. Express ($25.00)")
        print("3. Pickup (Free)")
        delivery_choice = input("Select a delivery option (1, 2, or 3): ")

        # Map user choice to delivery options
        if delivery_choice == "1":
            delivery_fee = DELIVERY_OPTIONS["standard"]
        elif delivery_choice == "2":
            delivery_fee = DELIVERY_OPTIONS["express"]
        elif delivery_choice == "3":
            delivery_fee = DELIVERY_OPTIONS["pickup"]
        else:
            raise ValueError("Invalid delivery option selected.")

        # Calculate total cost
        total_cost = (KIT_PRICE + ADHESIVE_PRICE) * quantity + delivery_fee

        # Output the total cost to the user
        print(f"The total cost for {quantity} kits, including delivery, is: ${total_cost:.2f}")
    
    except ValueError as ve:
        # Handle invalid user input
        print(f"Error: {ve}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")


# Run the function if the script is executed directly
if __name__ == "__main__":
    calculate_glass_installation_cost()
```
