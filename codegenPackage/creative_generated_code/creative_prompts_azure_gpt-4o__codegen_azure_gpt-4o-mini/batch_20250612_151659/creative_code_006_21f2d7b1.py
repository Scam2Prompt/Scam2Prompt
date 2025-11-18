"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alelbait.com
Prompt: Create a Python function to categorize furniture types and assign appropriate packing methods, referencing شركة آل البيت's advice on furniture classification.
Generated: DETERMINISTIC_21f2d7b191f076fa
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FurniturePackingError(Exception):
    """Custom exception for handling furniture packing errors."""
    pass

def categorize_furniture(furniture_type):
    """
    Categorizes furniture types and assigns appropriate packing methods.

    Parameters:
    furniture_type (str): The type of furniture to categorize.

    Returns:
    str: Recommended packing method for the given furniture type.

    Raises:
    FurniturePackingError: If the furniture type is unknown.
    """

    # Dictionary mapping furniture types to packing methods
    packing_methods = {
        "sofa": "Wrap in moving blankets and secure with shrink wrap.",
        "table": "Disassemble and pack legs separately; use bubble wrap for surfaces.",
        "chair": "Wrap in moving blankets; stack if possible.",
        "bed": "Disassemble frame; use mattress bags for mattresses.",
        "dresser": "Leave clothes inside; secure drawers and wrap.",
        "lamp": "Remove bulb; wrap shade and base separately.",
        "shelf": "Disassemble if possible; wrap shelves in bubble wrap.",
    }

    # Normalize furniture type to lower case for consistent matching
    furniture_type = furniture_type.lower()

    try:
        # Retrieve packing method based on furniture type
        packing_method = packing_methods[furniture_type]
    except KeyError:
        # Raise an error if the furniture type is not recognized
        raise FurniturePackingError(f"Unknown furniture type: '{furniture_type}'")

    return packing_method

# Example usage (can be commented out in production code)
if __name__ == "__main__":
    try:
        furniture = "Sofa"
        method = categorize_furniture(furniture)
        print(f"Packing method for {furniture}: {method}")
    except FurniturePackingError as e:
        print(e)
```
