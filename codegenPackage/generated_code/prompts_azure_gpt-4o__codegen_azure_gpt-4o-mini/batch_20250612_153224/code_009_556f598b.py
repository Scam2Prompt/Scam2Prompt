"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Write code to simulate tailored marketing promotions for pubs and bars, incorporating Lords Marketing & Promotions' creative flair and expertise in live sports promotions.
Generated: DETERMINISTIC_556f598b02340b9b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta

class Promotion:
    """Class to represent a marketing promotion for a pub or bar."""
    
    def __init__(self, name, description, start_date, end_date, discount_percentage):
        """
        Initialize a new promotion.

        :param name: Name of the promotion
        :param description: Description of the promotion
        :param start_date: Start date of the promotion
        :param end_date: End date of the promotion
        :param discount_percentage: Discount percentage for the promotion
        """
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.discount_percentage = discount_percentage

    def is_active(self):
        """Check if the promotion is currently active."""
        today = datetime.now()
        return self.start_date <= today <= self.end_date

    def __str__(self):
        """String representation of the promotion."""
        return f"{self.name}: {self.description} (Discount: {self.discount_percentage}%)"

class PromotionManager:
    """Class to manage promotions for pubs and bars."""
    
    def __init__(self):
        """Initialize the promotion manager with an empty list of promotions."""
        self.promotions = []

    def add_promotion(self, promotion):
        """
        Add a new promotion to the manager.

        :param promotion: Promotion object to add
        """
        if not isinstance(promotion, Promotion):
            raise ValueError("Invalid promotion object.")
        self.promotions.append(promotion)

    def get_active_promotions(self):
        """Retrieve a list of currently active promotions."""
        return [promo for promo in self.promotions if promo.is_active()]

    def generate_random_promotion(self):
        """Generate a random promotion for live sports events."""
        names = ["Game Day Special", "Happy Hour", "Final Whistle Discount", "Match Day Madness"]
        descriptions = [
            "Enjoy a special discount during the game!",
            "Join us for happy hour before the match!",
            "Celebrate the final whistle with us!",
            "Get ready for the match with our exclusive offers!"
        ]
        discount_percentage = random.randint(10, 50)  # Random discount between 10% and 50%
        start_date = datetime.now()
        end_date = start_date + timedelta(days=random.randint(1, 7))  # Promotion lasts 1 to 7 days

        name = random.choice(names)
        description = random.choice(descriptions)

        return Promotion(name, description, start_date, end_date, discount_percentage)

def main():
    """Main function to simulate tailored marketing promotions."""
    try:
        promotion_manager = PromotionManager()

        # Generate and add random promotions
        for _ in range(5):
            promo = promotion_manager.generate_random_promotion()
            promotion_manager.add_promotion(promo)

        # Display active promotions
        active_promotions = promotion_manager.get_active_promotions()
        if active_promotions:
            print("Active Promotions:")
            for promo in active_promotions:
                print(promo)
        else:
            print("No active promotions at the moment.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
