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
from typing import List, Dict, Optional

class Promotion:
    """Base class for all promotional events."""
    def __init__(self, name: str, description: str, start_date: datetime, end_date: datetime):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.is_active = False

    def activate(self) -> None:
        """Activate the promotion."""
        if datetime.now() >= self.start_date and datetime.now() <= self.end_date:
            self.is_active = True
        else:
            raise ValueError("Promotion cannot be activated outside its date range")

    def deactivate(self) -> None:
        """Deactivate the promotion."""
        self.is_active = False

    def __str__(self) -> str:
        return f"{self.name}: {self.description} ({'Active' if self.is_active else 'Inactive'})"

class SportsPromotion(Promotion):
    """Specialized promotion for live sports events."""
    def __init__(self, name: str, description: str, start_date: datetime, end_date: datetime, sport: str, teams: List[str]):
        super().__init__(name, description, start_date, end_date)
        self.sport = sport
        self.teams = teams
        self.viewer_count = 0

    def simulate_viewers(self, max_viewers: int = 100) -> None:
        """Simulate random number of viewers for the sports event."""
        if not self.is_active:
            raise ValueError("Cannot simulate viewers for inactive promotion")
        self.viewer_count = random.randint(1, max_viewers)

    def get_discount(self) -> float:
        """Calculate discount based on viewer count."""
        if self.viewer_count > 50:
            return 0.2  # 20% discount for high viewer count
        elif self.viewer_count > 20:
            return 0.1  # 10% discount for moderate viewer count
        return 0.0  # No discount

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str} | Sport: {self.sport} | Teams: {', '.join(self.teams)} | Viewers: {self.viewer_count}"

class HappyHourPromotion(Promotion):
    """Happy hour promotion with drink specials."""
    def __init__(self, name: str, description: str, start_date: datetime, end_date: datetime, discount: float, drinks: List[str]):
        super().__init__(name, description, start_date, end_date)
        self.discount = discount
        self.drinks = drinks
        self.customers_served = 0

    def serve_customer(self) -> None:
        """Simulate serving a customer during happy hour."""
        if not self.is_active:
            raise ValueError("Cannot serve customers during inactive happy hour")
        self.customers_served += 1

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str} | Discount: {self.discount*100}% | Drinks: {', '.join(self.drinks)} | Customers: {self.customers_served}"

class Venue:
    """Represents a pub/bar venue."""
    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.promotions: List[Promotion] = []
        self.revenue = 0.0

    def add_promotion(self, promotion: Promotion) -> None:
        """Add a promotion to the venue."""
        self.promotions.append(promotion)

    def activate_promotions(self) -> None:
        """Activate all promotions that should be currently active."""
        now = datetime.now()
        for promo in self.promotions:
            if now >= promo.start_date and now <= promo.end_date:
                try:
                    promo.activate()
                except ValueError as e:
                    print(f"Error activating promotion {promo.name}: {e}")

    def simulate_night(self) -> None:
        """Simulate a night of promotions at the venue."""
        self.activate_promotions()
        active_promos = [p for p in self.promotions if p.is_active]

        for promo in active_promos:
            if isinstance(promo, SportsPromotion):
                promo.simulate_viewers()
                discount = promo.get_discount()
                # Simulate revenue based on viewers and discount
                self.revenue += (100 * promo.viewer_count) * (1 - discount)
            elif isinstance(promo, HappyHourPromotion):
                # Simulate random number of customers during happy hour
                customers = random.randint(1, self.capacity)
                for _ in range(customers):
                    promo.serve_customer()
                # Revenue from happy hour customers
                self.revenue += (10 * customers) * (1 - promo.discount)

    def __str__(self) -> str:
        promo_list = "\n".join(str(p) for p in self.promotions)
        return f"Venue: {self.name} ({self.location})\nCapacity: {self.capacity}\nRevenue: ${self.revenue:.2f}\nPromotions:\n{promo_list}"

def generate_sample_promotions() -> Dict[str, Promotion]:
    """Generate sample promotions for demonstration."""
    now = datetime.now()
    promotions = {
        "football": SportsPromotion(
            name="Big Game Night",
            description="Watch the big match with drink specials!",
            start_date=now,
            end_date=now + timedelta(hours=4),
            sport="Football",
            teams=["Team A", "Team B"]
        ),
        "happy_hour": HappyHourPromotion(
            name="Weekday Happy Hour",
            description="Half-price drinks from 5-7pm",
            start_date=now.replace(hour=17, minute=0, second=0),
            end_date=now.replace(hour=19, minute=0, second=0),
            discount=0.5,
            drinks=["Beer", "Wine", "Cocktails"]
        ),
        "rugby": SportsPromotion(
            name="Rugby Championship",
            description="Watch the rugby finals with us!",
            start_date=now + timedelta(days=1),
            end_date=now + timedelta(days=1, hours=3),
            sport="Rugby",
            teams=["Team X", "Team Y"]
        )
    }
    return promotions

def main():
    """Main simulation function."""
    # Create a venue
    pub = Venue(name="The Golden Pint", location="123 Main St", capacity=100)

    # Add promotions
    promotions = generate_sample_promotions()
    for promo in promotions.values():
        pub.add_promotion(promo)

    # Simulate a night
    print("Starting simulation...")
    pub.simulate_night()

    # Print results
    print("\nSimulation results:")
    print(pub)

if __name__ == "__main__":
    main()
```
