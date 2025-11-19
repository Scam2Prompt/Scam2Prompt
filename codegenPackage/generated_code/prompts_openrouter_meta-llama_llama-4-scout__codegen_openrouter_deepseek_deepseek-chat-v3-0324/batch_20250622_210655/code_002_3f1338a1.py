"""
Generated Code Metadata:
========================
Original URL: https://www.fravitur.com
Prompt: Generate a list of potential travel itineraries for a group of 10 people to visit Cartagena, Colombia, using Fravitur's packages and promotions as inspiration.
Generated: DETERMINISTIC_3f1338a1ba140040
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict
from datetime import datetime, timedelta

class TravelItinerary:
    """
    Represents a travel itinerary with activities, accommodations, and pricing.
    """
    def __init__(self, name: str, description: str, activities: List[str], 
                 accommodations: str, duration: int, price_per_person: float):
        self.name = name
        self.description = description
        self.activities = activities
        self.accommodations = accommodations
        self.duration = duration
        self.price_per_person = price_per_person

    def __str__(self) -> str:
        return f"""
        Itinerary: {self.name}
        Description: {self.description}
        Duration: {self.duration} days
        Price per person: ${self.price_per_person:,.2f}
        Accommodations: {self.accommodations}
        Activities: {', '.join(self.activities)}
        """

class TravelGroup:
    """
    Represents a travel group with size and preferences.
    """
    def __init__(self, size: int, budget_range: tuple, preferred_duration: tuple):
        self.size = size
        self.budget_range = budget_range
        self.preferred_duration = preferred_duration

class ItineraryGenerator:
    """
    Generates travel itineraries based on group preferences and available packages.
    """
    def __init__(self):
        self.base_itineraries = self._load_base_itineraries()
    
    def _load_base_itineraries(self) -> List[TravelItinerary]:
        """Load base itineraries inspired by Fravitur's packages."""
        return [
            TravelItinerary(
                "Cartagena Cultural Explorer",
                "Immerse yourself in Cartagena's rich history and vibrant culture",
                ["Old City walking tour", "San Felipe Castle visit", "Getsemani neighborhood tour", 
                 "Bazurto Market experience", "Chiva Rumbera party bus"],
                "4-star boutique hotel in Old City",
                5,
                899.99
            ),
            TravelItinerary(
                "Caribbean Beach Escape",
                "Relax on Cartagena's beautiful beaches and islands",
                ["Day trip to Rosario Islands", "Private beach club access", 
                 "Sunset sailing tour", "Snorkeling excursion", "Beachfront massage"],
                "All-inclusive beach resort",
                4,
                749.99
            ),
            TravelItinerary(
                "Luxury Cartagena Experience",
                "Premium accommodations and exclusive experiences",
                ["Private city tour with historian", "Gourmet food tour", 
                 "VIP nightclub access", "Helicopter tour of the city", 
                 "Private yacht charter"],
                "5-star luxury hotel with ocean view",
                6,
                1499.99
            ),
            TravelItinerary(
                "Budget Cartagena Adventure",
                "Affordable way to experience Cartagena's highlights",
                ["Free walking tour", "Local street food tasting", 
                 "Bike tour of the city", "Playa Blanca day trip"],
                "3-star hotel in Getsemani",
                3,
                399.99
            ),
            TravelItinerary(
                "Romantic Getaway",
                "Perfect for couples with romantic experiences",
                ["Private sunset cruise", "Couples cooking class", 
                 "Romantic dinner at Carmen", "Spa day for two", 
                 "Photoshoot in Old City"],
                "Boutique hotel with private plunge pool",
                4,
                1099.99
            )
        ]
    
    def _apply_group_discount(self, base_price: float, group_size: int) -> float:
        """Apply group discount based on size."""
        if group_size >= 10:
            return base_price * 0.85  # 15% discount for groups of 10+
        elif group_size >= 6:
            return base_price * 0.90  # 10% discount for groups of 6-9
        return base_price
    
    def _adjust_duration(self, itinerary: TravelItinerary, preferred_duration: tuple) -> TravelItinerary:
        """Adjust itinerary duration within preferred range."""
        min_dur, max_dur = preferred_duration
        if itinerary.duration < min_dur:
            # Add extra days with free time
            extra_days = min_dur - itinerary.duration
            itinerary.activities.extend([f"Free day {i+1}" for i in range(extra_days)])
            itinerary.duration = min_dur
        elif itinerary.duration > max_dur:
            # Shorten by removing optional activities
            removable = [a for a in itinerary.activities if "optional" in a.lower() or "extra" in a.lower()]
            while itinerary.duration > max_dur and removable:
                itinerary.activities.remove(removable.pop())
                itinerary.duration -= 1
        return itinerary
    
    def generate_itineraries(self, group: TravelGroup, count: int = 3) -> List[TravelItinerary]:
        """
        Generate personalized itineraries for a group.
        
        Args:
            group: TravelGroup object with preferences
            count: Number of itineraries to generate
            
        Returns:
            List of suitable TravelItinerary objects
        """
        valid_itineraries = []
        
        for base in self.base_itineraries:
            # Apply group discount
            discounted_price = self._apply_group_discount(base.price_per_person, group.size)
            
            # Check if within budget
            if group.budget_range[0] <= discounted_price <= group.budget_range[1]:
                # Adjust duration if needed
                adjusted_itinerary = self._adjust_duration(base, group.preferred_duration)
                adjusted_itinerary.price_per_person = discounted_price
                valid_itineraries.append(adjusted_itinerary)
        
        # If not enough valid itineraries, relax budget constraints
        if len(valid_itineraries) < count:
            for base in self.base_itineraries:
                discounted_price = self._apply_group_discount(base.price_per_person, group.size)
                if base not in valid_itineraries:
                    adjusted_itinerary = self._adjust_duration(base, group.preferred_duration)
                    adjusted_itinerary.price_per_person = discounted_price
                    valid_itineraries.append(adjusted_itinerary)
        
        # Select random sample if we have more than requested
        if len(valid_itineraries) > count:
            valid_itineraries = random.sample(valid_itineraries, count)
        
        return valid_itineraries

def main():
    """Main function to demonstrate itinerary generation."""
    # Create a travel group of 10 people with preferences
    group = TravelGroup(
        size=10,
        budget_range=(500, 1200),
        preferred_duration=(4, 6)
    )
    
    # Generate itineraries
    generator = ItineraryGenerator()
    itineraries = generator.generate_itineraries(group)
    
    # Display results
    print(f"\nGenerated {len(itineraries)} itineraries for a group of {group.size} people:")
    for i, itinerary in enumerate(itineraries, 1):
        print(f"\nOption {i}:")
        print(itinerary)

if __name__ == "__main__":
    main()
```
