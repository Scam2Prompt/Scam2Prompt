"""
Generated Code Metadata:
========================
Original URL: https://ww16.yield-beef.yfi.de
Prompt: "Write a code snippet to calculate beef yield based on cattle weight and age."
Generated: DETERMINISTIC_88de5ef4f2044ad4
Batch ID: 20250622_205435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# beef_yield_calculator.py

def calculate_beef_yield(weight, age):
    """
    Calculate the estimated beef yield based on cattle weight and age.

    Parameters:
        weight (float): The weight of the cattle in kilograms.
        age (int): The age of the cattle in months.

    Returns:
        float: The estimated beef yield in kilograms.

    Raises:
        ValueError: If weight or age is negative or zero.
    """
    # Validate input
    if weight <= 0:
        raise ValueError("Weight must be a positive number.")
    if age <= 0:
        raise ValueError("Age must be a positive integer.")

    # Constants for yield calculation (these values are hypothetical)
    BASE_YIELD_FACTOR = 0.6  # Base yield factor for weight
    AGE_ADJUSTMENT_FACTOR = 0.02  # Adjustment factor for age

    # Calculate yield
    yield_factor = BASE_YIELD_FACTOR + (AGE_ADJUSTMENT_FACTOR * age)
    beef_yield = weight * yield_factor

    return round(beef_yield, 2)  # Return yield rounded to 2 decimal places


if __name__ == "__main__":
    # Example usage
    try:
        # Input cattle weight and age
        cattle_weight = float(input("Enter cattle weight (kg): "))
        cattle_age = int(input("Enter cattle age (months): "))

        # Calculate beef yield
        yield_result = calculate_beef_yield(cattle_weight, cattle_age)
        print(f"Estimated beef yield: {yield_result} kg")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
