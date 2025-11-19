"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Write a Python script to generate a customized Tanzania safari itinerary based on user input for budget, destinations, and activities.
Generated: DETERMINISTIC_06369a5059798cb2
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class SafariItineraryGenerator:
    """
    Generates a customized Tanzania safari itinerary based on user preferences.
    """
    
    def __init__(self):
        self.destinations = {
            "Serengeti": {
                "activities": ["Game Drives", "Hot Air Balloon Safari", "Walking Safari"],
                "budget_range": {"low": 500, "medium": 1000, "high": 2000},
                "days_recommended": 3
            },
            "Ngorongoro": {
                "activities": ["Crater Tour", "Cultural Visits", "Bird Watching"],
                "budget_range": {"low": 400, "medium": 800, "high": 1500},
                "days_recommended": 2
            },
            "Zanzibar": {
                "activities": ["Beach Relaxation", "Spice Tour", "Snorkeling"],
                "budget_range": {"low": 300, "medium": 600, "high": 1200},
                "days_recommended": 4
            },
            "Tarangire": {
                "activities": ["Game Drives", "Elephant Spotting", "Night Safari"],
                "budget_range": {"low": 350, "medium": 700, "high": 1300},
                "days_recommended": 2
            }
        }
    
    def get_user_input(self) -> Dict:
        """
        Collects user preferences for the safari itinerary.
        
        Returns:
            Dict: User preferences including budget, destinations, and activities
        """
        print("Welcome to Tanzania Safari Itinerary Generator!")
        print("Please provide your preferences for your dream safari.\n")
        
        # Get budget level
        while True:
            try:
                budget = input("Enter your budget level (low/medium/high): ").lower()
                if budget not in ["low", "medium", "high"]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter 'low', 'medium', or 'high'.")
        
        # Get selected destinations
        print("\nAvailable destinations:")
        for i, destination in enumerate(self.destinations.keys(), 1):
            print(f"{i}. {destination}")
        
        selected_destinations = []
        while True:
            try:
                choices = input("\nEnter destination numbers (comma separated, e.g., 1,3): ")
                indices = [int(c.strip()) - 1 for c in choices.split(",")]
                selected_destinations = [list(self.destinations.keys())[i] for i in indices]
                if not selected_destinations:
                    raise ValueError
                break
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
        
        # Get preferred activities
        print("\nAvailable activities:")
        all_activities = set()
        for dest in selected_destinations:
            all_activities.update(self.destinations[dest]["activities"])
        
        for i, activity in enumerate(all_activities, 1):
            print(f"{i}. {activity}")
        
        selected_activities = []
        while True:
            try:
                choices = input("\nEnter activity numbers you're interested in (comma separated): ")
                activity_list = list(all_activities)
                indices = [int(c.strip()) - 1 for c in choices.split(",")]
                selected_activities = [activity_list[i] for i in indices]
                if not selected_activities:
                    raise ValueError
                break
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
        
        # Get trip duration
        while True:
            try:
                days = int(input("\nEnter total trip duration in days (5-14): "))
                if days < 5 or days > 14:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 5 and 14.")
        
        return {
            "budget": budget,
            "destinations": selected_destinations,
            "activities": selected_activities,
            "days": days
        }
    
    def generate_itinerary(self, preferences: Dict) -> Dict:
        """
        Generates itinerary based on user preferences.
        
        Args:
            preferences: Dictionary containing user preferences
            
        Returns:
            Dict: Generated itinerary with day-by-day plan
        """
        itinerary = {
            "summary": {
                "total_cost": 0,
                "destinations_visited": [],
                "activities_included": []
            },
            "daily_plans": []
        }
        
        budget = preferences["budget"]
        days_remaining = preferences["days"]
        destinations = preferences["destinations"]
        activities = preferences["activities"]
        
        # Sort destinations by recommended days (descending)
        sorted_dests = sorted(
            destinations,
            key=lambda x: self.destinations[x]["days_recommended"],
            reverse=True
        )
        
        day_counter = 1
        for dest in sorted_dests:
            if days_remaining <= 0:
                break
                
            dest_info = self.destinations[dest]
            days_to_spend = min(dest_info["days_recommended"], days_remaining)
            
            # Filter activities available at this destination
            dest_activities = [a for a in activities if a in dest_info["activities"]]
            if not dest_activities:
                dest_activities = dest_info["activities"][:2]  # Default activities
            
            # Calculate cost for this destination
            cost = dest_info["budget_range"][budget] * days_to_spend
            
            # Add to itinerary
            itinerary["summary"]["total_cost"] += cost
            itinerary["summary"]["destinations_visited"].append(dest)
            itinerary["summary"]["activities_included"].extend(dest_activities)
            
            # Create daily plans
            for day in range(days_to_spend):
                daily_plan = {
                    "day": day_counter,
                    "destination": dest,
                    "activities": dest_activities[:2],  # Max 2 activities per day
                    "estimated_cost": dest_info["budget_range"][budget]
                }
                itinerary["daily_plans"].append(daily_plan)
                day_counter += 1
            
            days_remaining -= days_to_spend
        
        # Add summary
        itinerary["summary"]["destinations_visited"] = list(set(itinerary["summary"]["destinations_visited"]))
        itinerary["summary"]["activities_included"] = list(set(itinerary["summary"]["activities_included"]))
        
        return itinerary
    
    def display_itinerary(self, itinerary: Dict) -> None:
        """
        Displays the generated itinerary in a user-friendly format.
        
        Args:
            itinerary: Generated itinerary to display
        """
        print("\n\n=== YOUR TANZANIA SAFARI ITINERARY ===")
        print(f"\nSUMMARY:")
        print(f"Total estimated cost: ${itinerary['summary']['total_cost']}")
        print(f"Destinations: {', '.join(itinerary['summary']['destinations_visited'])}")
        print(f"Activities: {', '.join(itinerary['summary']['activities_included'])}")
        
        print("\nDAILY PLANS:")
        for day in itinerary["daily_plans"]:
            print(f"\nDay {day['day']}: {day['destination']}")
            print(f"  Activities: {', '.join(day['activities'])}")
            print(f"  Estimated cost: ${day['estimated_cost']}")
        
        print("\nEnjoy your Tanzanian adventure!\n")

def main():
    try:
        generator = SafariItineraryGenerator()
        preferences = generator.get_user_input()
        itinerary = generator.generate_itinerary(preferences)
        generator.display_itinerary(itinerary)
        
        # Option to save itinerary to file
        save = input("\nWould you like to save this itinerary to a file? (yes/no): ").lower()
        if save == "yes":
            with open("safari_itinerary.json", "w") as f:
                json.dump(itinerary, f, indent=4)
            print("Itinerary saved to 'safari_itinerary.json'")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please try again or contact support.")

if __name__ == "__main__":
    main()
```
