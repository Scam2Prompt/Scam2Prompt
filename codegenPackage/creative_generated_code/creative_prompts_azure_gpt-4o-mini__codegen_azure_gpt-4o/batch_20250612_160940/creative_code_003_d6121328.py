"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apipoocoin-tk.blogspot.com
Prompt: Develop a travel itinerary for a family vacation at Toca do Caranguejo, including activities to enjoy at Praia do Patacho and nearby attractions.
Generated: DETERMINISTIC_d612132876cc39a4
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# travel_itinerary.py

from datetime import datetime, timedelta

def generate_itinerary(start_date, end_date):
    """
    Generate a travel itinerary for a family vacation at Toca do Caranguejo.
    
    Args:
        start_date (str): Start date of the vacation in the format 'YYYY-MM-DD'.
        end_date (str): End date of the vacation in the format 'YYYY-MM-DD'.
    
    Returns:
        list: A list of itinerary activities for each day.
    """
    try:
        # Convert input dates to datetime objects
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Ensure end_date is after start_date
        if end_date <= start_date:
            raise ValueError("End date must be after start date.")
        
        # Initialize itinerary list
        itinerary = []
        current_date = start_date
        
        # Generate activities for each day
        while current_date <= end_date:
            day_plan = {
                "date": current_date.strftime("%Y-%m-%d"),
                "activities": [
                    "Breakfast at Toca do Caranguejo's restaurant",
                    "Relax and enjoy Praia do Patacho",
                    "Lunch at a local seafood restaurant",
                    "Explore nearby attractions (e.g., historical sites, nature walks)",
                    "Dinner and family bonding at Toca do Caranguejo"
                ]
            }
            
            # Add special activities for weekends
            if current_date.weekday() in [5, 6]:  # Saturday or Sunday
                day_plan["activities"].append("Special beach games and activities")
            
            itinerary.append(day_plan)
            current_date += timedelta(days=1)
        
        return itinerary
    
    except ValueError as ve:
        # Handle invalid date inputs
        print(f"Error: {ve}")
        return []
    except Exception as e:
        # Handle other unforeseen errors
        print(f"An unexpected error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Define vacation dates
    start_date = "2023-12-18"
    end_date = "2023-12-23"
    
    # Generate itinerary
    itinerary = generate_itinerary(start_date, end_date)
    
    # Print the itinerary
    if itinerary:
        print("Family Vacation Itinerary:")
        for day in itinerary:
            print(f"Date: {day['date']}")
            print("Activities:")
            for activity in day['activities']:
                print(f"  - {activity}")
            print()
    else:
        print("Failed to generate itinerary.")
```
