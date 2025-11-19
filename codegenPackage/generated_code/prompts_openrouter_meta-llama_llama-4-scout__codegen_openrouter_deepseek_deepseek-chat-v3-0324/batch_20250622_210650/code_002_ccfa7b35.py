"""
Generated Code Metadata:
========================
Original URL: https://reveindiatours.com
Prompt: "Generate a sample itinerary for a 7-day Rajasthan tour package, including visits to top desert safari destinations, forts, and temples, using Reve India Tours' expertise and services."
Generated: DETERMINISTIC_ccfa7b35fce98d70
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Rajasthan 7-Day Tour Itinerary Generator for Reve India Tours
This script generates a sample itinerary for a 7-day Rajasthan tour package.
"""

from datetime import datetime, timedelta
from typing import List, Dict

class RajasthanTourItinerary:
    """
    Generates a detailed 7-day Rajasthan tour itinerary including desert safaris,
    forts, temples, and cultural experiences.
    """
    
    def __init__(self, start_date: str):
        """
        Initialize the itinerary with start date and basic information.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
        """
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.tour_details = {
            "package_name": "Royal Rajasthan Experience",
            "duration": "7 Days / 6 Nights",
            "inclusions": [
                "Accommodation in 4-star hotels",
                "Daily breakfast and dinner",
                "All transfers in AC vehicles",
                "Professional English-speaking guide",
                "Entrance fees to monuments",
                "Desert safari with cultural show"
            ]
        }
    
    def _generate_day_plan(self, day_num: int, title: str, activities: List[str], 
                          meals: List[str], overnight: str) -> Dict:
        """
        Generate a structured day plan.
        
        Args:
            day_num (int): Day number in the itinerary
            title (str): Title/theme of the day
            activities (List[str]): List of activities
            meals (List[str]): Meals included
            overnight (str): Overnight stay location
            
        Returns:
            Dict: Structured day plan
        """
        date = self.start_date + timedelta(days=day_num-1)
        return {
            "day": day_num,
            "date": date.strftime("%A, %B %d, %Y"),
            "title": title,
            "activities": activities,
            "meals": meals,
            "overnight": overnight
        }
    
    def generate_itinerary(self) -> List[Dict]:
        """
        Generate the complete 7-day itinerary.
        
        Returns:
            List[Dict]: Complete itinerary with day-wise details
        """
        itinerary = []
        
        # Day 1: Arrival in Jaipur
        itinerary.append(self._generate_day_plan(
            day_num=1,
            title="Arrival in Jaipur - The Pink City",
            activities=[
                "Meet and greet at Jaipur International Airport",
                "Transfer to hotel and check-in",
                "Evening visit to Chokhi Dhani (ethnic village resort)",
                "Cultural dinner with folk performances"
            ],
            meals=["Dinner"],
            overnight="Jaipur"
        ))
        
        # Day 2: Jaipur Sightseeing
        itinerary.append(self._generate_day_plan(
            day_num=2,
            title="Jaipur - Forts and Palaces",
            activities=[
                "Visit Amber Fort with elephant ride",
                "Explore City Palace and Jantar Mantar",
                "Photo stop at Hawa Mahal",
                "Shopping at local markets for handicrafts"
            ],
            meals=["Breakfast", "Dinner"],
            overnight="Jaipur"
        ))
        
        # Day 3: Jaipur to Bikaner
        itinerary.append(self._generate_day_plan(
            day_num=3,
            title="Transfer to Bikaner - Desert Gateway",
            activities=[
                "Drive to Bikaner (approx 5 hours)",
                "Visit Junagarh Fort",
                "Explore Karni Mata Temple (Rat Temple)",
                "Evening camel ride in the sand dunes"
            ],
            meals=["Breakfast", "Dinner"],
            overnight="Bikaner"
        ))
        
        # Day 4: Bikaner to Jaisalmer
        itinerary.append(self._generate_day_plan(
            day_num=4,
            title="Golden City of Jaisalmer",
            activities=[
                "Drive to Jaisalmer (approx 6 hours)",
                "Visit Jaisalmer Fort (Sonar Quila)",
                "Explore Patwon Ki Haveli and Salim Singh Ki Haveli",
                "Evening cultural show at Desert Cultural Centre"
            ],
            meals=["Breakfast", "Dinner"],
            overnight="Jaisalmer"
        ))
        
        # Day 5: Jaisalmer Desert Safari
        itinerary.append(self._generate_day_plan(
            day_num=5,
            title="Sam Sand Dunes Experience",
            activities=[
                "Morning at leisure",
                "Afternoon desert safari to Sam Sand Dunes",
                "Camel ride and dune bashing",
                "Evening folk performance and dinner under the stars"
            ],
            meals=["Breakfast", "Dinner"],
            overnight="Desert Camp (Jaisalmer)"
        ))
        
        # Day 6: Jaisalmer to Jodhpur
        itinerary.append(self._generate_day_plan(
            day_num=6,
            title="Jodhpur - The Blue City",
            activities=[
                "Drive to Jodhpur (approx 5 hours)",
                "Visit Mehrangarh Fort",
                "Explore Jaswant Thada",
                "Walk through the blue-painted old city"
            ],
            meals=["Breakfast", "Dinner"],
            overnight="Jodhpur"
        ))
        
        # Day 7: Jodhpur to Udaipur
        itinerary.append(self._generate_day_plan(
            day_num=7,
            title="Udaipur - City of Lakes",
            activities=[
                "Drive to Udaipur (approx 5 hours)",
                "Visit City Palace and Jagdish Temple",
                "Boat ride on Lake Pichola",
                "Evening farewell dinner with lake view"
            ],
            meals=["Breakfast", "Dinner"],
            overnight="Udaipur"
        ))
        
        return itinerary
    
    def print_itinerary(self):
        """Print the formatted itinerary."""
        print(f"\n{'*' * 50}")
        print(f"{' ' * 15}REVE INDIA TOURS")
        print(f"{' ' * 10}RAJASTHAN 7-DAY TOUR ITINERARY")
        print(f"{'*' * 50}\n")
        
        print(f"Package: {self.tour_details['package_name']}")
        print(f"Duration: {self.tour_details['duration']}")
        print("\nInclusions:")
        for item in self.tour_details['inclusions']:
            print(f"- {item}")
        print("\n")
        
        itinerary = self.generate_itinerary()
        for day in itinerary:
            print(f"\nDAY {day['day']}: {day['date']}")
            print(f"{'=' * 30}")
            print(f"{day['title'].upper()}")
            print(f"\nActivities:")
            for i, activity in enumerate(day['activities'], 1):
                print(f"{i}. {activity}")
            print(f"\nMeals: {', '.join(day['meals'])}")
            print(f"Overnight: {day['overnight']}")
            print(f"{'-' * 50}")


# Example usage
if __name__ == "__main__":
    try:
        tour = RajasthanTourItinerary("2023-11-01")
        tour.print_itinerary()
    except ValueError as e:
        print(f"Error: Invalid date format. Please use YYYY-MM-DD format. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
