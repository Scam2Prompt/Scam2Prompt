"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Write code to simulate tailored marketing promotions for pubs and bars, incorporating Lords Marketing & Promotions' creative flair and expertise in live sports promotions.
Generated: DETERMINISTIC_556f598b02340b9b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta

class Promotion:
    """Class representing a marketing promotion for a pub or bar."""
    
    def __init__(self, name, description, start_date, end_date, discount, sports_events):
        """
        Initializes a new Promotion instance.

        :param name: Name of the promotion
        :param description: Description of the promotion
        :param start_date: Start date of the promotion
        :param end_date: End date of the promotion
        :param discount: Discount percentage offered
        :param sports_events: List of sports events associated with the promotion
        """
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.discount = discount
        self.sports_events = sports_events

    def is_active(self):
        """Check if the promotion is currently active."""
        today = datetime.now().date()
        return self.start_date <= today <= self.end_date


class Pub:
    """Class representing a pub or bar."""
    
    def __init__(self, name):
        """
        Initializes a new Pub instance.

        :param name: Name of the pub
        """
        self.name = name
        self.promotions = []

    def add_promotion(self, promotion):
        """
        Adds a promotion to the pub.

        :param promotion: Promotion object to add
        """
        if not isinstance(promotion, Promotion):
            raise ValueError("Invalid promotion. Must be an instance of Promotion.")
        self.promotions.append(promotion)

    def get_active_promotions(self):
        """Retrieve a list of active promotions."""
        return [promo for promo in self.promotions if promo.is_active()]


def create_sample_promotions():
    """Generates sample promotions for demonstration purposes."""
    events = [
        "Football Match",
        "Rugby Game",
        "Cricket Tournament",
        "Live Music Night"
    ]
    
    promotions = [
        Promotion(
            name="Game Day Special",
            description="Enjoy 20% off on all drinks during the game!",
            start_date=datetime.now().date(),
            end_date=datetime.now().date() + timedelta(days=2),
            discount=20,
            sports_events=[random.choice(events)]
        ),
        Promotion(
            name="Happy Hour",
            description="Join us for happy hour from 5 PM to 7 PM!",
            start_date=datetime.now().date(),
            end_date=datetime.now().date() + timedelta(days=1),
            discount=15,
            sports_events=[]
        ),
        Promotion(
            name="Live Music Weekend",
            description="Get a free drink with any ticket purchase for live music!",
            start_date=datetime.now().date() + timedelta(days=1),
            end_date=datetime.now().date() + timedelta(days=3),
            discount=100,
            sports_events=["Live Music Night"]
        )
    ]
    return promotions


def main():
    """Main function to simulate pub promotions."""
    try:
        pub = Pub("The Sports Bar")
        promotions = create_sample_promotions()
        
        for promo in promotions:
            pub.add_promotion(promo)

        active_promotions = pub.get_active_promotions()
        
        print(f"Active Promotions at {pub.name}:")
        for promo in active_promotions:
            print(f"- {promo.name}: {promo.description} (Discount: {promo.discount}%)")
            print(f"  Valid from {promo.start_date} to {promo.end_date}. Events: {', '.join(promo.sports_events) if promo.sports_events else 'None'}")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
