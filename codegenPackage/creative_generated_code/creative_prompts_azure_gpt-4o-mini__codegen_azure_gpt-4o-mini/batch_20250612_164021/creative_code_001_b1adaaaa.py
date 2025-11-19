"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Write a code snippet for a booking system that manages the hiring of police uniforms and includes a price match guarantee feature.
Generated: DETERMINISTIC_b1adaaaa8b99a4e8
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UniformBookingSystem:
    """
    A class to manage the booking of police uniforms with a price match guarantee feature.
    """

    def __init__(self):
        self.uniforms = {}
        self.bookings = {}
        self.price_match_enabled = True  # Price match guarantee toggle

    def add_uniform(self, uniform_id, price):
        """
        Add a new uniform to the system.
        
        Parameters:
        uniform_id (str): Unique identifier for the uniform.
        price (float): Price of the uniform.
        """
        if uniform_id in self.uniforms:
            raise ValueError(f"Uniform with ID {uniform_id} already exists.")
        self.uniforms[uniform_id] = price

    def book_uniform(self, uniform_id, customer_id):
        """
        Book a uniform for a customer.
        
        Parameters:
        uniform_id (str): Unique identifier for the uniform.
        customer_id (str): Identifier for the customer making the booking.
        
        Returns:
        str: Confirmation message for the booking.
        """
        if uniform_id not in self.uniforms:
            raise ValueError(f"Uniform with ID {uniform_id} does not exist.")
        if customer_id in self.bookings:
            raise ValueError(f"Customer with ID {customer_id} has already made a booking.")
        
        self.bookings[customer_id] = uniform_id
        return f"Booking confirmed for Customer ID {customer_id} with Uniform ID {uniform_id}."

    def price_match(self, uniform_id, competitor_price):
        """
        Check if the price match guarantee applies and return the adjusted price if applicable.
        
        Parameters:
        uniform_id (str): Unique identifier for the uniform.
        competitor_price (float): Price from a competitor to match.

        Returns:
        float: Adjusted price if a price match occurs; otherwise, original price.
        """
        if uniform_id not in self.uniforms:
            raise ValueError(f"Uniform with ID {uniform_id} does not exist.")
        
        current_price = self.uniforms[uniform_id]
        if self.price_match_enabled and competitor_price < current_price:
            return competitor_price
        return current_price

    def toggle_price_match(self):
        """
        Toggle the price match guarantee feature.
        """
        self.price_match_enabled = not self.price_match_enabled

    def get_uniform_price(self, uniform_id):
        """
        Get the price of a specific uniform.
        
        Parameters:
        uniform_id (str): Unique identifier for the uniform.

        Returns:
        float: Price of the uniform.
        """
        if uniform_id not in self.uniforms:
            raise ValueError(f"Uniform with ID {uniform_id} does not exist.")
        return self.uniforms[uniform_id]

# Example of how to use the UniformBookingSystem
if __name__ == "__main__":
    booking_system = UniformBookingSystem()
    
    # Adding uniforms with prices
    booking_system.add_uniform('001', 50.0)
    booking_system.add_uniform('002', 75.0)
    
    # Booking a uniform
    try:
        print(booking_system.book_uniform('001', 'cust123'))
    except ValueError as e:
        print(e)

    # Price match example
    try:
        new_price = booking_system.price_match('001', 45.0)
        print(f"Adjusted Price: {new_price}")
    except ValueError as e:
        print(e)
```
