"""
Generated Code Metadata:
========================
Original URL: https://blasterturismo.com
Prompt: "Generate a travel itinerary for a 2-day trip to Ametista do Sul, RS, including 10 tourist attractions and accommodations, inspired by Blaster Agência de Turismo's packages."
Generated: DETERMINISTIC_3977723c08b6900b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class TravelItinerary:
    """
    A class to generate a travel itinerary for Ametista do Sul, RS.
    Inspired by Blaster Agência de Turismo's packages.
    """
    
    def __init__(self):
        self.itinerary = {
            "destination": "Ametista do Sul, RS",
            "duration": "2 days",
            "accommodations": [],
            "attractions": [],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def add_accommodation(self, name, description, contact):
        """Add accommodation to the itinerary"""
        if not all([name, description, contact]):
            raise ValueError("All accommodation fields must be provided")
        
        self.itinerary["accommodations"].append({
            "name": name,
            "description": description,
            "contact": contact
        })
    
    def add_attraction(self, name, description, day, time, fee=0.0):
        """Add tourist attraction to the itinerary"""
        if not all([name, description, day, time]):
            raise ValueError("Name, description, day and time must be provided")
        
        if day not in [1, 2]:
            raise ValueError("Day must be 1 or 2")
        
        self.itinerary["attractions"].append({
            "name": name,
            "description": description,
            "day": day,
            "time": time,
            "fee": fee
        })
    
    def generate_itinerary(self):
        """Generate the complete itinerary"""
        if len(self.itinerary["accommodations"]) == 0:
            raise ValueError("At least one accommodation must be added")
        
        if len(self.itinerary["attractions"]) < 10:
            raise ValueError("At least 10 attractions must be added")
        
        return self.itinerary
    
    def save_to_file(self, filename="itinerary.json"):
        """Save itinerary to JSON file"""
        itinerary = self.generate_itinerary()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(itinerary, f, indent=4, ensure_ascii=False)


def create_sample_itinerary():
    """Create a sample itinerary for Ametista do Sul"""
    itinerary = TravelItinerary()
    
    # Add accommodations
    itinerary.add_accommodation(
        "Hotel Cristal",
        "Comfortable hotel with great views of the city",
        "(55) 1234-5678"
    )
    
    itinerary.add_accommodation(
        "Pousada das Pedras",
        "Charming guesthouse near the mines",
        "(55) 9876-5432"
    )
    
    # Add attractions for Day 1
    itinerary.add_attraction(
        "Mina da Ametista",
        "Visit the famous amethyst mine",
        1, "09:00", 50.00
    )
    
    itinerary.add_attraction(
        "Museu das Pedras",
        "Museum showcasing local minerals",
        1, "11:00", 20.00
    )
    
    itinerary.add_attraction(
        "Parque das Pedras",
        "Beautiful park with mineral formations",
        1, "14:00", 15.00
    )
    
    itinerary.add_attraction(
        "Igreja Matriz",
        "Historic church with amethyst decorations",
        1, "16:00"
    )
    
    itinerary.add_attraction(
        "Mirante da Cidade",
        "Scenic viewpoint overlooking the city",
        1, "18:00"
    )
    
    # Add attractions for Day 2
    itinerary.add_attraction(
        "Mina do Cristal",
        "Another impressive mine to visit",
        2, "09:00", 45.00
    )
    
    itinerary.add_attraction(
        "Ateliê de Artesanato",
        "Local artisan workshop",
        2, "11:00", 10.00
    )
    
    itinerary.add_attraction(
        "Cachoeira do Rio",
        "Beautiful waterfall near the city",
        2, "14:00"
    )
    
    itinerary.add_attraction(
        "Feira de Minerais",
        "Local market selling minerals and crafts",
        2, "16:00"
    )
    
    itinerary.add_attraction(
        "Restaurante Mineiro",
        "Traditional local cuisine",
        2, "19:00"
    )
    
    return itinerary


if __name__ == "__main__":
    try:
        itinerary = create_sample_itinerary()
        itinerary.save_to_file()
        print("Itinerary generated successfully!")
    except Exception as e:
        print(f"Error generating itinerary: {str(e)}")
```
