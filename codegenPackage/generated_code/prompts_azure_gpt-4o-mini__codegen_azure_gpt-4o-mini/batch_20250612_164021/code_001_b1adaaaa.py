"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Write a code snippet for a booking system that manages the hiring of police uniforms and includes a price match guarantee feature.
Generated: DETERMINISTIC_b1adaaaa8b99a4e8
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PoliceUniformBookingSystem:
    def __init__(self):
        """Initialize the booking system with an empty inventory and price match guarantee."""
        self.inventory = {}  # Dictionary to hold uniform availability
        self.price_match_guarantee = True  # Enable price match guarantee

    def add_uniform(self, uniform_type, quantity, price):
        """
        Add a uniform type to the inventory.

        :param uniform_type: str - Type of the police uniform
        :param quantity: int - Number of uniforms available
        :param price: float - Price per uniform
        """
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")
        
        self.inventory[uniform_type] = {
            'quantity': quantity,
            'price': price
        }

    def book_uniform(self, uniform_type, requested_quantity, competitor_price=None):
        """
        Book a specified quantity of uniforms.

        :param uniform_type: str - Type of the police uniform to book
        :param requested_quantity: int - Number of uniforms to book
        :param competitor_price: float - Price from a competitor for price matching
        :return: str - Confirmation message
        """
        if uniform_type not in self.inventory:
            raise ValueError("Requested uniform type is not available.")
        
        available_quantity = self.inventory[uniform_type]['quantity']
        if requested_quantity > available_quantity:
            raise ValueError("Requested quantity exceeds available inventory.")
        
        # Check for price match guarantee
        if self.price_match_guarantee and competitor_price is not None:
            if competitor_price < self.inventory[uniform_type]['price']:
                self.inventory[uniform_type]['price'] = competitor_price
        
        # Deduct the booked quantity from inventory
        self.inventory[uniform_type]['quantity'] -= requested_quantity
        
        return f"Successfully booked {requested_quantity} {uniform_type}(s). Total price: ${self.inventory[uniform_type]['price'] * requested_quantity:.2f}"

    def get_inventory(self):
        """
        Get the current inventory of uniforms.

        :return: dict - Current inventory status
        """
        return self.inventory

    def restock_uniform(self, uniform_type, additional_quantity):
        """
        Restock a specific uniform type.

        :param uniform_type: str - Type of the police uniform to restock
        :param additional_quantity: int - Number of uniforms to add to inventory
        """
        if additional_quantity < 0:
            raise ValueError("Additional quantity must be non-negative.")
        
        if uniform_type in self.inventory:
            self.inventory[uniform_type]['quantity'] += additional_quantity
        else:
            raise ValueError("Uniform type does not exist in inventory.")

# Example usage
if __name__ == "__main__":
    booking_system = PoliceUniformBookingSystem()
    
    # Adding uniforms to the inventory
    booking_system.add_uniform("Standard Uniform", 10, 50.00)
    booking_system.add_uniform("Tactical Uniform", 5, 75.00)

    # Booking uniforms
    try:
        print(booking_system.book_uniform("Standard Uniform", 2, competitor_price=45.00))
    except ValueError as e:
        print(f"Error: {e}")

    # Display current inventory
    print(booking_system.get_inventory())
    
    # Restocking uniforms
    try:
        booking_system.restock_uniform("Tactical Uniform", 3)
        print("Restocked Tactical Uniform.")
    except ValueError as e:
        print(f"Error: {e}")

    # Display updated inventory
    print(booking_system.get_inventory())
```
