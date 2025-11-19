"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Write a Python function that calculates the total cost of air freight forwarding, incorporating variables for weight, distance, and insurance, as described in Uniair Cargo's services.
Generated: DETERMINISTIC_60d9242c5a927d55
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_air_freight_cost(weight, distance, insurance_required):
    """
    Calculate the total cost of air freight forwarding.

    Parameters:
        weight (float): The weight of the cargo in kilograms.
        distance (float): The distance to be covered in kilometers.
        insurance_required (bool): Whether insurance is required for the cargo.

    Returns:
        float: The total cost of air freight forwarding.

    Raises:
        ValueError: If weight or distance is negative.
    """
    try:
        # Validate input
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        # Base rate per kilogram per kilometer
        base_rate = 0.05  # Example rate: $0.05 per kg per km

        # Insurance cost per kilogram
        insurance_rate = 0.02  # Example rate: $0.02 per kg

        # Calculate base cost
        base_cost = weight * distance * base_rate

        # Calculate insurance cost if required
        insurance_cost = weight * insurance_rate if insurance_required else 0

        # Total cost
        total_cost = base_cost + insurance_cost

        return round(total_cost, 2)  # Return cost rounded to 2 decimal places

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Test the function with sample inputs
    weight = 100.0  # in kilograms
    distance = 500.0  # in kilometers
    insurance_required = True  # Insurance required

    total_cost = calculate_air_freight_cost(weight, distance, insurance_required)
    if total_cost is not None:
        print(f"The total cost of air freight forwarding is: ${total_cost}")
```
