"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitepinesinn.com
Prompt: Develop a function that calculates the total cost for a wedding package at White Pines Lodge, considering different outdoor ceremony settings and reception options.
Generated: DETERMINISTIC_2cf65255d35837e4
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code for Calculating the Total Cost for a Wedding Package at White Pines Lodge

def calculate_wedding_cost(ceremony_type, reception_type, guest_count):
    """
    Calculate the total cost of a wedding package based on ceremony type, reception type, and guest count.

    Parameters:
        ceremony_type (str): Type of ceremony setting. Options: 'garden', 'beach', 'forest'.
        reception_type (str): Type of reception option. Options: 'buffet', 'sit_down', 'cocktail'.
        guest_count (int): Number of guests attending the wedding.

    Returns:
        float: Total cost of the wedding package.
    
    Raises:
        ValueError: If invalid ceremony_type, reception_type, or guest_count are provided.
    """

    # Base cost for ceremony settings
    ceremony_costs = {
        'garden': 1500,
        'beach': 2000,
        'forest': 1800
    }

    # Base cost for reception options per guest
    reception_cost_per_guest = {
        'buffet': 50,
        'sit_down': 80,
        'cocktail': 40
    }

    # Validate ceremony_type
    if ceremony_type not in ceremony_costs:
        raise ValueError(f"Invalid ceremony type. Choose from {list(ceremony_costs.keys())}.")

    # Validate reception_type
    if reception_type not in reception_cost_per_guest:
        raise ValueError(f"Invalid reception type. Choose from {list(reception_cost_per_guest.keys())}.")

    # Validate guest_count
    if not isinstance(guest_count, int) or guest_count <= 0:
        raise ValueError("Guest count must be a positive integer.")

    # Calculate total cost
    ceremony_cost = ceremony_costs[ceremony_type]
    reception_cost = reception_cost_per_guest[reception_type] * guest_count
    total_cost = ceremony_cost + reception_cost

    return total_cost


# Example usage
if __name__ == "__main__":
    try:
        # Inputs
        ceremony = 'beach'
        reception = 'sit_down'
        guests = 120

        # Calculate and display total cost
        total = calculate_wedding_cost(ceremony, reception, guests)
        print(f"The total cost for the wedding package is: ${total:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
