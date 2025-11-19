"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Write a Python function that calculates the optimal fabric type for sportswear based on user-defined parameters like stretchability and weight.
Generated: DETERMINISTIC_0928cf991b9f2750
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FabricType:
    """A class to represent different fabric types for sportswear."""
    
    def __init__(self, name, stretchability, weight):
        """
        Initializes a fabric type with its name, stretchability, and weight.
        
        :param name: The name of the fabric.
        :param stretchability: The stretchability rating (1-10).
        :param weight: The weight of the fabric in grams per square meter (gsm).
        """
        self.name = name
        self.stretchability = stretchability
        self.weight = weight


def optimal_fabric_type(stretchability, weight):
    """
    Calculates the optimal fabric type for sportswear based on stretchability and weight.
    
    :param stretchability: Desired stretchability rating (1-10).
    :param weight: Desired weight of the fabric in grams per square meter (gsm).
    :return: The name of the optimal fabric type or a message indicating no suitable fabric was found.
    :raises ValueError: If stretchability is not between 1 and 10, or weight is negative.
    """
    # Validate input parameters
    if not (1 <= stretchability <= 10):
        raise ValueError("Stretchability must be between 1 and 10.")
    if weight < 0:
        raise ValueError("Weight must be a non-negative value.")

    # Define available fabric types
    fabrics = [
        FabricType("Lycra", 10, 150),
        FabricType("Nylon", 8, 200),
        FabricType("Polyester", 6, 180),
        FabricType("Cotton", 4, 220),
        FabricType("Wool", 3, 300)
    ]
    
    # Initialize the best fabric type variables
    optimal_fabric = None
    best_score = float('-inf')

    # Calculate the optimal fabric based on user-defined parameters
    for fabric in fabrics:
        # Score calculation based on stretchability and weight
        score = (fabric.stretchability / stretchability) - (fabric.weight / weight)
        
        # Update if the current fabric has a better score
        if score > best_score:
            best_score = score
            optimal_fabric = fabric.name

    return optimal_fabric if optimal_fabric else "No suitable fabric type found."


# Example usage
if __name__ == "__main__":
    try:
        stretch = 8  # Example stretchability input
        weight = 200  # Example weight input
        result = optimal_fabric_type(stretch, weight)
        print(f"The optimal fabric type for stretchability {stretch} and weight {weight} is: {result}")
    except Exception as e:
        print(f"Error: {e}")
```
