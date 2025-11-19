"""
Generated Code Metadata:
========================
Original URL: https://magicegypttours.com
Prompt: "Generate a Python code to create a 7-day itinerary for a budget tour package in Egypt, including Cairo, Giza, and Luxor, with a similar structure to the 7 Nights Egypt Budget Holiday package offered by Magic Egypt Tours."
Generated: DETERMINISTIC_e90eb25987c5349e
Batch ID: 20250622_205358
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

def generate_itinerary(start_date, budget):
    """
    Generates a 7-day budget tour itinerary for Egypt covering Cairo, Giza, and Luxor.
    
    Args:
        start_date (str): Start date in 'YYYY-MM-DD' format
        budget (float): Total budget for the tour
        
    Returns:
        dict: Complete itinerary with days, activities, and cost breakdown
    """
    try:
        # Validate inputs
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        if budget <= 0:
            raise ValueError("Budget must be positive")
            
        # Calculate daily budget
        daily_budget = budget / 7
        
        # Initialize itinerary
        itinerary = {
            "tour_name": "7 Nights Egypt Budget Holiday",
            "start_date": start_date.strftime('%Y-%m-%d'),
            "end_date": (start_date + timedelta(days=6)).strftime('%Y-%m-%d'),
            "total_budget": budget,
            "daily_budget": round(daily_budget, 2),
            "destinations": ["Cairo", "Giza", "Luxor"],
            "days": []
        }
        
        # Day 1: Arrival in Cairo
        day1 = {
            "day_number": 1,
            "date": start_date.strftime('%Y-%m-%d'),
            "location": "Cairo",
            "activities": [
                {"time": "Morning", "description": "Arrival at Cairo International Airport", "cost": 0},
                {"time": "Afternoon", "description": "Transfer to budget hotel", "cost": round(daily_budget * 0.3, 2)},
                {"time": "Evening", "description": "Free time to explore local area", "cost": 0}
            ],
            "total_cost": round(daily_budget * 0.3, 2)
        }
        itinerary["days"].append(day1)
        
        # Day 2: Cairo Sightseeing
        day2 = {
            "day_number": 2,
            "date": (start_date + timedelta(days=1)).strftime('%Y-%m-%d'),
            "location": "Cairo",
            "activities": [
                {"time": "Morning", "description": "Visit Egyptian Museum", "cost": round(daily_budget * 0.2, 2)},
                {"time": "Afternoon", "description": "Explore Khan el-Khalili bazaar", "cost": round(daily_budget * 0.1, 2)},
                {"time": "Evening", "description": "Nile River dinner cruise (budget option)", "cost": round(daily_budget * 0.4, 2)}
            ],
            "total_cost": round(daily_budget * 0.7, 2)
        }
        itinerary["days"].append(day2)
        
        # Day 3: Giza Pyramids
        day3 = {
            "day_number": 3,
            "date": (start_date + timedelta(days=2)).strftime('%Y-%m-%d'),
            "location": "Giza",
            "activities": [
                {"time": "Morning", "description": "Visit Giza Pyramids and Sphinx", "cost": round(daily_budget * 0.3, 2)},
                {"time": "Afternoon", "description": "Lunch and camel ride", "cost": round(daily_budget * 0.3, 2)},
                {"time": "Evening", "description": "Return to Cairo hotel", "cost": round(daily_budget * 0.1, 2)}
            ],
            "total_cost": round(daily_budget * 0.7, 2)
        }
        itinerary["days"].append(day3)
        
        # Day 4: Travel to Luxor
        day4 = {
            "day_number": 4,
            "date": (start_date + timedelta(days=3)).strftime('%Y-%m-%d'),
            "location": "Luxor",
            "activities": [
                {"time": "Morning", "description": "Flight to Luxor", "cost": round(daily_budget * 0.5, 2)},
                {"time": "Afternoon", "description": "Check-in to budget hotel", "cost": round(daily_budget * 0.3, 2)},
                {"time": "Evening", "description": "Free time", "cost": 0}
            ],
            "total_cost": round(daily_budget * 0.8, 2)
        }
        itinerary["days"].append(day4)
        
        # Day 5: Luxor West Bank
        day5 = {
            "day_number": 5,
            "date": (start_date + timedelta(days=4)).strftime('%Y-%m-%d'),
            "location": "Luxor",
            "activities": [
                {"time": "Morning", "description": "Visit Valley of the Kings", "cost": round(daily_budget * 0.3, 2)},
                {"time": "Afternoon", "description": "See Hatshepsut Temple and Colossi of Memnon", "cost": round(daily_budget * 0.2, 2)},
                {"time": "Evening", "description": "Local market visit", "cost": round(daily_budget * 0.1, 2)}
            ],
            "total_cost": round(daily_budget * 0.6, 2)
        }
        itinerary["days"].append(day5)
        
        # Day 6: Luxor East Bank
        day6 = {
            "day_number": 6,
            "date": (start_date + timedelta(days=5)).strftime('%Y-%m-%d'),
            "location": "Luxor",
            "activities": [
                {"time": "Morning", "description": "Visit Karnak Temple", "cost": round(daily_budget * 0.3, 2)},
                {"time": "Afternoon", "description": "Explore Luxor Temple", "cost": round(daily_budget * 0.2, 2)},
                {"time": "Evening", "description": "Free time", "cost": 0}
            ],
            "total_cost": round(daily_budget * 0.5, 2)
        }
        itinerary["days"].append(day6)
        
        # Day 7: Return to Cairo and Departure
        day7 = {
            "day_number": 7,
            "date": (start_date + timedelta(days=6)).strftime('%Y-%m-%d'),
            "location": "Cairo",
            "activities": [
                {"time": "Morning", "description": "Flight back to Cairo", "cost": round(daily_budget * 0.5, 2)},
                {"time": "Afternoon", "description": "Final shopping and farewell lunch", "cost": round(daily_budget * 0.3, 2)},
                {"time": "Evening", "description": "Transfer to airport for departure", "cost": round(daily_budget * 0.2, 2)}
            ],
            "total_cost": round(daily_budget * 1.0, 2)
        }
        itinerary["days"].append(day7)
        
        # Calculate total planned cost
        total_planned_cost = sum(day["total_cost"] for day in itinerary["days"])
        itinerary["total_planned_cost"] = round(total_planned_cost, 2)
        itinerary["budget_remaining"] = round(budget - total_planned_cost, 2)
        
        return itinerary
        
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    itinerary = generate_itinerary("2023-11-01", 1500)
    if itinerary:
        print(json.dumps(itinerary, indent=2))
```
