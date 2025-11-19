"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Write a Python function that calculates the total cost of a glass installation kit, including the Betaseal 1001 adhesive, based on user input for quantity and delivery options.
Generated: DETERMINISTIC_b02f2e556cfe06bc
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_installation_kit_cost():
    """
    Calculates the total cost of a glass installation kit including Betaseal 1001 adhesive.
    
    The function prompts the user for:
    - Quantity of kits
    - Delivery option (standard or express)
    
    Returns:
        float: Total cost including delivery charges
    """
    
    # Constants
    KIT_PRICE = 125.00  # Price per kit
    STANDARD_DELIVERY = 15.00
    EXPRESS_DELIVERY = 25.00
    
    try:
        # Get user input
        quantity = int(input("Enter the number of kits required: "))
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
            
        delivery_option = input("Choose delivery option (standard/express): ").lower()
        if delivery_option not in ['standard', 'express']:
            raise ValueError("Invalid delivery option")
            
        # Calculate costs
        subtotal = quantity * KIT_PRICE
        
        if delivery_option == 'standard':
            delivery_cost = STANDARD_DELIVERY
        else:
            delivery_cost = EXPRESS_DELIVERY
            
        total_cost = subtotal + delivery_cost
        
        # Display results
        print(f"\nOrder Summary:")
        print(f"Number of kits: {quantity}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Delivery cost: ${delivery_cost:.2f}")
        print(f"Total cost: ${total_cost:.2f}")
        
        return total_cost
        
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    calculate_installation_kit_cost()
```
