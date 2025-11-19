"""
Generated Code Metadata:
========================
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Develop a function in Python that calculates the total cost for renting a luxury villa, taking into account amenities such as a jacuzzi and outdoor shower, as featured in Diamond Villa Corfu.
Generated: DETERMINISTIC_d921f7e1b09f2b87
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_villa_rental_cost(base_rate, num_nights, jacuzzi=False, outdoor_shower=False):
    """
    Calculate the total cost for renting a luxury villa.

    Parameters:
        base_rate (float): The nightly base rate for the villa.
        num_nights (int): The number of nights the villa is rented for.
        jacuzzi (bool): Whether the villa includes a jacuzzi (default: False).
        outdoor_shower (bool): Whether the villa includes an outdoor shower (default: False).

    Returns:
        float: The total cost of the villa rental.

    Raises:
        ValueError: If base_rate is negative or num_nights is not a positive integer.
    """
    # Validate inputs
    if base_rate < 0:
        raise ValueError("Base rate cannot be negative.")
    if not isinstance(num_nights, int) or num_nights <= 0:
        raise ValueError("Number of nights must be a positive integer.")

    # Calculate the base cost
    total_cost = base_rate * num_nights

    # Add cost for amenities
    if jacuzzi:
        total_cost += 50 * num_nights  # Additional $50 per night for jacuzzi
    if outdoor_shower:
        total_cost += 30 * num_nights  # Additional $30 per night for outdoor shower

    return total_cost


# Example usage
if __name__ == "__main__":
    try:
        # Example inputs
        base_rate = 300.0  # $300 per night
        num_nights = 5
        jacuzzi = True
        outdoor_shower = False

        # Calculate total cost
        total_cost = calculate_villa_rental_cost(base_rate, num_nights, jacuzzi, outdoor_shower)
        print(f"The total cost for the villa rental is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
