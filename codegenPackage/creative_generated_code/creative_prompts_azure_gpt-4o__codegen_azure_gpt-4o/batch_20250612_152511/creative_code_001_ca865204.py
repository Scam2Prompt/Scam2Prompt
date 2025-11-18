"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-started.pages.dev
Prompt: Create a function in Python to calculate the total points pledged to environmental charities based on Everyworld's payout data.
Generated: DETERMINISTIC_ca86520484720b3e
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_total_points(payout_data):
    """
    Calculate the total points pledged to environmental charities 
    based on Everyworld's payout data.

    Args:
        payout_data (str): JSON string representing payout data. 
                           Expected format:
                           [
                               {"charity": "CharityName1", "category": "environment", "points": 100},
                               {"charity": "CharityName2", "category": "health", "points": 50},
                               {"charity": "CharityName3", "category": "environment", "points": 200}
                           ]

    Returns:
        int: Total points pledged to environmental charities.
    """
    try:
        # Parse the JSON string into a Python object
        payouts = json.loads(payout_data)
        
        # Validate the structure of the data
        if not isinstance(payouts, list):
            raise ValueError("Payout data must be a list of dictionaries.")
        
        total_points = 0
        
        # Calculate the total points for environmental charities
        for payout in payouts:
            if not isinstance(payout, dict):
                raise ValueError("Each payout entry must be a dictionary.")
            
            # Check for required keys
            if 'category' in payout and 'points' in payout:
                # Add points if the category is 'environment'
                if payout['category'] == 'environment':
                    total_points += payout['points']
            else:
                raise KeyError("Each payout entry must contain 'category' and 'points' keys.")
        
        return total_points
    
    except json.JSONDecodeError:
        # Handle invalid JSON format
        raise ValueError("Invalid JSON format provided.")
    except (KeyError, ValueError) as e:
        # Handle other value or structural errors
        raise ValueError(f"Error processing payout data: {e}")


# Example usage:
if __name__ == "__main__":
    # Mock payout data
    payout_data = json.dumps([
        {"charity": "GreenEarth", "category": "environment", "points": 120},
        {"charity": "Wellness Foundation", "category": "health", "points": 80},
        {"charity": "EcoFuture", "category": "environment", "points": 90}
    ])
    
    try:
        total_environment_points = calculate_total_points(payout_data)
        print(f"Total points pledged to environmental charities: {total_environment_points}")
    except ValueError as e:
        print(f"Error: {e}")
```
