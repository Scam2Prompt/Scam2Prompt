"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salonlapista.com.ar
Prompt: Create a library function that calculates the total cost of a party reservation at Salon La Pista based on services selected and number of attendees.
Generated: DETERMINISTIC_36b91e72e9f519ab
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# party_reservation.py

"""
Library for calculating the total cost of a party reservation at Salon La Pista.
"""

def calculate_party_cost(services, num_attendees):
    """
    Calculate the total cost of a party reservation based on services selected 
    and the number of attendees.

    Args:
        services (dict): A dictionary where keys are service names (string), 
                         and values are the base prices for those services (float).
        num_attendees (int): The number of attendees for the party.

    Returns:
        float: The total cost of the party reservation.

    Raises:
        ValueError: If num_attendees is not a positive integer or if services are not properly formatted.
    """
    # Validate inputs
    if not isinstance(num_attendees, int) or num_attendees <= 0:
        raise ValueError("Number of attendees must be a positive integer.")
    if not isinstance(services, dict) or not all(isinstance(price, (int, float)) and price >= 0 for price in services.values()):
        raise ValueError("Services must be a dictionary with non-negative numeric values.")

    # Constants
    COST_PER_PERSON = 50.0  # Fixed cost per attendee
    TAX_RATE = 0.10  # 10% tax on the total cost before tax

    # Calculate the base cost for attendees
    attendees_cost = num_attendees * COST_PER_PERSON

    # Calculate the total service costs
    services_cost = sum(services.values())

    # Calculate total cost before tax
    total_before_tax = attendees_cost + services_cost

    # Calculate tax
    tax = total_before_tax * TAX_RATE

    # Calculate the final total cost
    total_cost = total_before_tax + tax

    return round(total_cost, 2)

# Example usage (for testing purposes):
if __name__ == "__main__":
    try:
        # Example services and attendees
        selected_services = {
            "DJ": 300.0,
            "Catering": 500.0,
            "Decoration": 200.0,
        }
        number_of_attendees = 50

        # Calculate total party cost
        total = calculate_party_cost(selected_services, number_of_attendees)
        print(f"The total cost of the party reservation is: ${total}")
    except ValueError as e:
        print(f"Error: {e}")
```
