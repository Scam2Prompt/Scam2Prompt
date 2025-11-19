"""
Generated Code Metadata:
========================
Original URL: https://salonlapista.com.ar
Prompt: Create a code snippet to calculate the budget for a party based on the number of guests and services chosen, like those offered by Salon La Pista.
Generated: DETERMINISTIC_bb9be0568ed2d93a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# party_budget_calculator.py

def calculate_party_budget(num_guests, services):
    """
    Calculate the total budget for a party based on the number of guests and selected services.

    Args:
        num_guests (int): The number of guests attending the party.
        services (dict): A dictionary of services with their respective costs per guest.
                         Example: {'catering': 20, 'decoration': 10, 'music': 15}

    Returns:
        float: The total budget for the party.
    """
    try:
        # Validate inputs
        if not isinstance(num_guests, int) or num_guests <= 0:
            raise ValueError("Number of guests must be a positive integer.")
        if not isinstance(services, dict) or not all(isinstance(v, (int, float)) for v in services.values()):
            raise ValueError("Services must be a dictionary with numeric values.")

        # Calculate total cost
        total_cost = 0
        for service, cost_per_guest in services.items():
            total_cost += cost_per_guest * num_guests

        return total_cost

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Number of guests
    num_guests = 50

    # Services offered and their costs per guest
    services = {
        'catering': 25,  # $25 per guest for catering
        'decoration': 10,  # $10 per guest for decoration
        'music': 15  # $15 per guest for music
    }

    # Calculate the budget
    total_budget = calculate_party_budget(num_guests, services)

    if total_budget is not None:
        print(f"The total budget for the party is: ${total_budget:.2f}")
    else:
        print("Failed to calculate the party budget.")
```
