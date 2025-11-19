"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Write a code snippet to calculate the cost of moving furniture based on factors like distance, weight, and type of furniture, similar to how آل البيت provides cost-effective services.
Generated: DETERMINISTIC_f5bb3465869169a1
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# furniture_moving_cost_calculator.py

def calculate_moving_cost(distance_km, weight_kg, furniture_type):
    """
    Calculate the cost of moving furniture based on distance, weight, and type of furniture.

    Parameters:
        distance_km (float): Distance to be covered in kilometers.
        weight_kg (float): Weight of the furniture in kilograms.
        furniture_type (str): Type of furniture (e.g., 'fragile', 'standard', 'bulky').

    Returns:
        float: Total cost of moving the furniture.
    """
    try:
        # Validate inputs
        if distance_km <= 0:
            raise ValueError("Distance must be greater than 0.")
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than 0.")
        if furniture_type not in ['fragile', 'standard', 'bulky']:
            raise ValueError("Furniture type must be 'fragile', 'standard', or 'bulky'.")

        # Base cost per kilometer
        base_cost_per_km = 5.0  # Base rate in currency units

        # Weight multiplier
        if weight_kg <= 50:
            weight_multiplier = 1.0
        elif weight_kg <= 100:
            weight_multiplier = 1.5
        else:
            weight_multiplier = 2.0

        # Furniture type multiplier
        furniture_type_multiplier = {
            'fragile': 2.0,  # Fragile items require extra care
            'standard': 1.0,  # Standard items have no additional cost
            'bulky': 1.5,  # Bulky items require more space and effort
        }

        # Calculate total cost
        total_cost = (
            distance_km * base_cost_per_km * weight_multiplier * furniture_type_multiplier[furniture_type]
        )

        return round(total_cost, 2)  # Return cost rounded to 2 decimal places

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Inputs
    distance = 120.5  # Distance in kilometers
    weight = 75.0  # Weight in kilograms
    furniture = 'fragile'  # Type of furniture

    # Calculate cost
    cost = calculate_moving_cost(distance, weight, furniture)

    if cost is not None:
        print(f"The total cost of moving the furniture is: {cost} currency units.")
    else:
        print("Failed to calculate the moving cost due to input errors.")
```
