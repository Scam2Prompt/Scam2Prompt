"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Write a Python function to calculate rental costs based on the selected boat (e.g., "Panache Alpha") and watersports accessories (e.g., slalom ski or kneeboard), including daily rates.
Generated: DETERMINISTIC_99775cf69533c917
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library for error handling
from typing import List

def calculate_rental_cost(boat: str, accessories: List[str], days: int) -> float:
    """
    Calculate rental costs for a selected boat and watersports accessories based on daily rates.
    
    Parameters:
        boat (str): The name of the selected boat.
        accessories (List[str]): A list of watersports accessories (e.g., slalom ski, kneeboard).
        days (int): The number of days for the rental.
    
    Returns:
        float: The total rental cost.
        
    Raises:
        ValueError: If boat or accessories are invalid or if days is not positive.
    """
    # Define daily rates for boats
    boat_rates = {
        "Panache Alpha": 100.0,
        "Wave Runner X": 120.0,
        "Ocean Breeze": 80.0
    }
    
    # Define daily rates for watersports accessories
    accessory_rates = {
        "Slalom Ski": 15.0,
        "Kneeboard": 12.0,
        "Wakeboard": 20.0,
        "Inflatable Tube": 10.0
    }
    
    # Input validation
    if boat not in boat_rates:
        raise ValueError(f"Invalid boat selection: {boat}. Available options are: {', '.join(boat_rates.keys())}")
    if not all(accessory in accessory_rates for accessory in accessories):
        raise ValueError(f"Invalid accessory selection. Available options are: {', '.join(accessory_rates.keys())}")
    if days <= 0:
        raise ValueError("Number of days must be a positive integer.")
    
    # Calculate total cost
    boat_cost = boat_rates[boat] * days
    accessory_cost = sum(accessory_rates[accessory] * days for accessory in accessories)
    total_cost = boat_cost + accessory_cost
    
    # Return result
    return total_cost

# Example usage:
# Uncomment the lines below to test the function
# total = calculate_rental_cost("Panache Alpha", ["Slalom Ski", "Kneeboard"], 3)
# print(f"Total rental cost: ${total:.2f}")
```
