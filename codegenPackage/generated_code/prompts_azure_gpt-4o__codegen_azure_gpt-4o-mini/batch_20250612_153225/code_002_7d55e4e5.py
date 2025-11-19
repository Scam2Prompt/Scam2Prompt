"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Create a function to recommend suitable materials (e.g., acrylic, plaswood, foam board) for 3D printed letters based on user input for durability and aesthetic preferences, as outlined on ThePrintNan.
Generated: DETERMINISTIC_7d55e4e5430afc40
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MaterialRecommendationError(Exception):
    """Custom exception for material recommendation errors."""
    pass

def recommend_material(durability: str, aesthetic: str) -> str:
    """
    Recommend suitable materials for 3D printed letters based on user input.

    Parameters:
    durability (str): The desired durability level ('low', 'medium', 'high').
    aesthetic (str): The desired aesthetic preference ('glossy', 'matte', 'textured').

    Returns:
    str: Recommended material based on the input criteria.

    Raises:
    MaterialRecommendationError: If the input parameters are invalid.
    """
    
    # Define material options based on durability and aesthetic preferences
    materials = {
        'low': {
            'glossy': 'Foam Board',
            'matte': 'Acrylic',
            'textured': 'Plaswood'
        },
        'medium': {
            'glossy': 'Acrylic',
            'matte': 'Plaswood',
            'textured': 'Foam Board'
        },
        'high': {
            'glossy': 'Plaswood',
            'matte': 'Acrylic',
            'textured': 'Acrylic'
        }
    }

    # Validate input parameters
    if durability not in materials:
        raise MaterialRecommendationError(f"Invalid durability level: {durability}. Choose from {list(materials.keys())}.")
    if aesthetic not in materials[durability]:
        raise MaterialRecommendationError(f"Invalid aesthetic preference: {aesthetic}. Choose from {list(materials[durability].keys())}.")

    # Return the recommended material
    return materials[durability][aesthetic]

# Example usage
if __name__ == "__main__":
    try:
        durability_input = input("Enter durability level (low, medium, high): ").strip().lower()
        aesthetic_input = input("Enter aesthetic preference (glossy, matte, textured): ").strip().lower()
        
        recommended_material = recommend_material(durability_input, aesthetic_input)
        print(f"Recommended material for your 3D printed letters: {recommended_material}")
    except MaterialRecommendationError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
