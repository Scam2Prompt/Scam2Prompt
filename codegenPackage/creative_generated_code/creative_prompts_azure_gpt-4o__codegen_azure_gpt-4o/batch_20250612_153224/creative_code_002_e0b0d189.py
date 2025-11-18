"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifesty.com.br
Prompt: Generate code to calculate the quantity of beverages needed for a party, referencing Ifesty's blog post on beverage calculation for events.
Generated: DETERMINISTIC_e0b0d1892951af5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Party Beverage Calculator

This script calculates the quantity of beverages needed for a party based on the number of guests, duration 
of the party, and type of beverages desired. It follows general guidelines for beverage needs as described 
in Ifesty's blog post on beverage calculation for events.

Assumptions:
- Guests consume an average of 1 drink per hour.
- Additional beverages are calculated for contingencies (e.g., extra guests, spills).
- Supports water, soda, and alcoholic drinks.

Author: [Your Name]
Date: YYYY-MM-DD
"""

def calculate_beverages(guest_count, party_duration, alcoholic_preference=True, water_preference=True, soda_preference=True):
    """
    Calculate the quantity of beverages needed for a party.

    Args:
        guest_count (int): Number of guests attending.
        party_duration (int): Duration of the party in hours.
        alcoholic_preference (bool): Whether alcoholic drinks are desired.
        water_preference (bool): Whether water is desired.
        soda_preference (bool): Whether soda is desired.

    Returns:
        dict: A dictionary with the quantity of each type of beverage needed.
    """
    try:
        # Validate inputs
        if guest_count <= 0:
            raise ValueError("Guest count must be greater than zero.")
        if party_duration <= 0:
            raise ValueError("Party duration must be greater than zero.")
        
        # Average beverage consumption: 1 drink per person per hour
        base_drinks_needed = guest_count * party_duration
        
        # Calculate contingency drinks (10% extra)
        contingency = round(base_drinks_needed * 0.10)
        total_drinks = base_drinks_needed + contingency

        # Distribute beverages based on preferences
        beverage_distribution = {}
        if alcoholic_preference:
            beverage_distribution['alcoholic_drinks'] = round(total_drinks * 0.4)
        if water_preference:
            beverage_distribution['water_bottles'] = round(total_drinks * 0.3)
        if soda_preference:
            beverage_distribution['soda_cans'] = round(total_drinks * 0.3)

        return beverage_distribution

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

# Example usage:
if __name__ == "__main__":
    # User inputs
    try:
        guest_count = int(input("Enter the number of guests: "))
        party_duration = int(input("Enter the party duration in hours: "))
        alcoholic_preference = input("Include alcoholic drinks? (yes/no): ").strip().lower() == 'yes'
        water_preference = input("Include water? (yes/no): ").strip().lower() == 'yes'
        soda_preference = input("Include soda? (yes/no): ").strip().lower() == 'yes'

        # Calculate beverage quantities
        beverage_needs = calculate_beverages(
            guest_count=guest_count,
            party_duration=party_duration,
            alcoholic_preference=alcoholic_preference,
            water_preference=water_preference,
            soda_preference=soda_preference
        )

        if beverage_needs:
            print("Beverage quantities needed for the party:")
            for beverage, quantity in beverage_needs.items():
                print(f"{beverage}: {quantity}")
        else:
            print("Could not calculate beverage quantities due to input errors.")
    except Exception as e:
        print(f"An unexpected error occurred during user input: {e}")
```
