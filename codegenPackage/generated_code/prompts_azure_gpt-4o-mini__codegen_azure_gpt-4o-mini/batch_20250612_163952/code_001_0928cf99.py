"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Write a Python function that calculates the optimal fabric type for sportswear based on user-defined parameters like stretchability and weight.
Generated: DETERMINISTIC_0928cf991b9f2750
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FabricType:
    """Class to represent different types of fabrics for sportswear."""
    def __init__(self, name, stretchability, weight):
        self.name = name
        self.stretchability = stretchability  # Stretchability on a scale of 1-10
        self.weight = weight  # Weight in grams per square meter (gsm)

    def __repr__(self):
        return f"{self.name} (Stretchability: {self.stretchability}, Weight: {self.weight} gsm)"


def calculate_optimal_fabric(stretchability, weight):
    """
    Calculate the optimal fabric type for sportswear based on user-defined parameters.

    Parameters:
    stretchability (int): Desired stretchability on a scale of 1-10.
    weight (int): Desired weight in grams per square meter (gsm).

    Returns:
    FabricType: The optimal fabric type based on the provided parameters.
    
    Raises:
    ValueError: If stretchability is not between 1 and 10, or weight is negative.
    """
    # Validate input parameters
    if not (1 <= stretchability <= 10):
        raise ValueError("Stretchability must be between 1 and 10.")
    if weight < 0:
        raise ValueError("Weight must be a non-negative value.")

    # Define a list of available fabrics
    fabrics = [
        FabricType("Lycra", stretchability=9, weight=200),
        FabricType("Polyester", stretchability=6, weight=150),
        FabricType("Nylon", stretchability=7, weight=180),
        FabricType("Cotton", stretchability=4, weight=120),
        FabricType("Spandex", stretchability=10, weight=220),
        FabricType("Wool", stretchability=5, weight=300),
    ]

    # Find the optimal fabric based on the criteria
    optimal_fabric = None
    for fabric in fabrics:
        if fabric.stretchability >= stretchability and fabric.weight <= weight:
            if optimal_fabric is None or fabric.stretchability > optimal_fabric.stretchability:
                optimal_fabric = fabric

    if optimal_fabric is None:
        raise ValueError("No suitable fabric found for the given parameters.")

    return optimal_fabric


# Example usage
if __name__ == "__main__":
    try:
        user_stretchability = 8  # Example user input for stretchability
        user_weight = 200        # Example user input for weight
        optimal_fabric = calculate_optimal_fabric(user_stretchability, user_weight)
        print(f"The optimal fabric for your sportswear is: {optimal_fabric}")
    except ValueError as e:
        print(f"Error: {e}")
```
