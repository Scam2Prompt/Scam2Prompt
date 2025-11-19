"""
Generated Code Metadata:
========================
Original URL: https://minnimi.com.ua
Prompt: Generate a promotional code for a new user to receive a bonus of up to 200,000 грн and 500 free spins on their first deposit at Slots City.
Generated: DETERMINISTIC_1c0e5f91cb667d94
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string

class PromotionalCodeGenerator:
    def __init__(self):
        self.code_length = 10  # Length of the promotional code
        self.bonus_amount = 200000  # Maximum bonus amount in грн
        self.free_spins = 500  # Number of free spins

    def generate_code(self):
        """
        Generate a random promotional code consisting of uppercase letters and digits.
        """
        characters = string.ascii_uppercase + string.digits
        promo_code = ''.join(random.choice(characters) for _ in range(self.code_length))
        return promo_code

    def create_promotion(self):
        """
        Create a promotional offer for new users.
        
        Returns:
            dict: A dictionary containing the promotional code, bonus amount, and free spins.
        """
        try:
            promo_code = self.generate_code()
            promotion = {
                'promo_code': promo_code,
                'bonus_amount': self.bonus_amount,
                'free_spins': self.free_spins
            }
            return promotion
        except Exception as e:
            # Log the error (in a real application, you would log this to a file or monitoring system)
            print(f"Error generating promotion: {e}")
            return None

if __name__ == "__main__":
    # Create an instance of the promotional code generator
    promo_generator = PromotionalCodeGenerator()
    
    # Generate the promotion for a new user
    promotion = promo_generator.create_promotion()
    
    if promotion:
        # Display the promotional offer
        print("Promotional Offer for New User:")
        print(f"Promo Code: {promotion['promo_code']}")
        print(f"Bonus Amount: {promotion['bonus_amount']} грн")
        print(f"Free Spins: {promotion['free_spins']}")
    else:
        print("Failed to generate promotional offer.")
```
