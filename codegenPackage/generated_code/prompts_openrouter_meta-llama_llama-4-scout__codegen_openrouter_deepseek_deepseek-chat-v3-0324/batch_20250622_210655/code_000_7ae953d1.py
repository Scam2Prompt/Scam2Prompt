"""
Generated Code Metadata:
========================
Original URL: https://tkcjourneys.com
Prompt: "Generate a Python script to calculate the cost of a trip to Fairy Meadows, Nanga Parbat Base Camp, including accommodation and transportation for 2 people for 5 days."
Generated: DETERMINISTIC_7ae953d15af71f7c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Trip Cost Calculator for Fairy Meadows and Nanga Parbat Base Camp

This script calculates the total cost of a trip for 2 people for 5 days,
including accommodation and transportation expenses.
"""

def calculate_trip_cost():
    """
    Calculate the total trip cost including accommodation and transportation.
    
    Returns:
        dict: A dictionary containing cost breakdown and total cost
    """
    # Constants for cost calculation
    ACCOMMODATION_PER_PERSON_PER_DAY = 5000  # PKR
    TRANSPORTATION_PER_PERSON = 15000  # PKR (round trip)
    FOOD_PER_PERSON_PER_DAY = 2000  # PKR
    GUIDE_FEE_PER_DAY = 3000  # PKR
    NUMBER_OF_DAYS = 5
    NUMBER_OF_PEOPLE = 2
    
    try:
        # Calculate accommodation cost
        accommodation_cost = ACCOMMODATION_PER_PERSON_PER_DAY * NUMBER_OF_PEOPLE * NUMBER_OF_DAYS
        
        # Calculate transportation cost
        transportation_cost = TRANSPORTATION_PER_PERSON * NUMBER_OF_PEOPLE
        
        # Calculate food cost
        food_cost = FOOD_PER_PERSON_PER_DAY * NUMBER_OF_PEOPLE * NUMBER_OF_DAYS
        
        # Calculate guide fee
        guide_cost = GUIDE_FEE_PER_DAY * NUMBER_OF_DAYS
        
        # Calculate total cost
        total_cost = accommodation_cost + transportation_cost + food_cost + guide_cost
        
        # Prepare result dictionary
        result = {
            'accommodation_cost': accommodation_cost,
            'transportation_cost': transportation_cost,
            'food_cost': food_cost,
            'guide_cost': guide_cost,
            'total_cost': total_cost,
            'currency': 'PKR',
            'days': NUMBER_OF_DAYS,
            'people': NUMBER_OF_PEOPLE
        }
        
        return result
    
    except Exception as e:
        print(f"Error calculating trip cost: {e}")
        return None

def display_cost_breakdown(cost_data):
    """
    Display the cost breakdown in a user-friendly format.
    
    Args:
        cost_data (dict): Dictionary containing cost breakdown
    """
    if not cost_data:
        print("No cost data available to display.")
        return
    
    print("\nTrip Cost Breakdown for Fairy Meadows & Nanga Parbat Base Camp")
    print("="*60)
    print(f"Duration: {cost_data['days']} days")
    print(f"Number of people: {cost_data['people']}")
    print("-"*60)
    print(f"Accommodation Cost: {cost_data['accommodation_cost']:,} {cost_data['currency']}")
    print(f"Transportation Cost: {cost_data['transportation_cost']:,} {cost_data['currency']}")
    print(f"Food Cost: {cost_data['food_cost']:,} {cost_data['currency']}")
    print(f"Guide Fee: {cost_data['guide_cost']:,} {cost_data['currency']}")
    print("-"*60)
    print(f"TOTAL COST: {cost_data['total_cost']:,} {cost_data['currency']}")
    print("="*60)

if __name__ == "__main__":
    print("Fairy Meadows & Nanga Parbat Base Camp Trip Cost Calculator")
    print("Calculating costs for 2 people for 5 days...\n")
    
    cost_data = calculate_trip_cost()
    if cost_data:
        display_cost_breakdown(cost_data)
```
