"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://africarisesafaris.com
Prompt: Write a code snippet that calculates the cost of a 5-day Tanzania Big 5 Safari based on the number of participants and accommodation type (budget, mid-range, luxury).
Generated: DETERMINISTIC_38608e77301a5b56
Batch ID: 20250612_164057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Tanzania Big 5 Safari Cost Calculator
# This program calculates the cost of a 5-day safari based on 
# the number of participants and chosen accommodation type.

def calculate_safari_cost(participants, accommodation_type):
    """
    Calculates the total cost for a 5-day Tanzania Big 5 Safari.

    :param participants: int - Number of participants in the safari
    :param accommodation_type: str - Type of accommodation ("budget", "mid-range", "luxury")
    :return: float - Total cost in USD
    :raises ValueError: If the participants number is invalid or accommodation type is unrecognized
    """
    # Validate input
    if participants <= 0:
        raise ValueError("Number of participants must be greater than zero.")
    
    # Accommodation pricing per participant per day
    accommodation_costs = {
        "budget": 150,     # USD per person per day
        "mid-range": 300,  # USD per person per day
        "luxury": 600      # USD per person per day
    }
    
    # Check if accommodation type is valid
    if accommodation_type not in accommodation_costs:
        raise ValueError(f"Invalid accommodation type: {accommodation_type}. "
                         "Choose from 'budget', 'mid-range', or 'luxury'.")
    
    # Calculate total cost
    daily_cost = accommodation_costs[accommodation_type]
    safari_days = 5  # Fixed number of safari days
    total_cost = participants * daily_cost * safari_days
    
    return total_cost


# Example usage
if __name__ == "__main__":
    try:
        # Input: Number of participants and accommodation type
        num_participants = int(input("Enter the number of participants: "))
        accommodation = input("Enter accommodation type (budget, mid-range, luxury): ").strip().lower()
        
        # Calculate and display the cost
        total_safari_cost = calculate_safari_cost(num_participants, accommodation)
        print(f"The total cost for the {num_participants}-participant, 5-day safari "
              f"with {accommodation} accommodation is: ${total_safari_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
