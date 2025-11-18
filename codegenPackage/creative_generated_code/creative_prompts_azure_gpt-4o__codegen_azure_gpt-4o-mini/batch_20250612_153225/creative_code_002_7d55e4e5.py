"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Create a function to recommend suitable materials (e.g., acrylic, plaswood, foam board) for 3D printed letters based on user input for durability and aesthetic preferences, as outlined on ThePrintNan.
Generated: DETERMINISTIC_7d55e4e5430afc40
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MaterialRecommendationError(Exception):
    """Custom exception for material recommendation errors."""
    pass

def recommend_material(durability_rating: str, aesthetic_preference: str) -> str:
    """
    Recommend a suitable material for 3D printed letters based on the user's 
    durability and aesthetic preferences.
    
    Args:
        durability_rating (str): User's preference for durability ('high', 'medium', 'low').
        aesthetic_preference (str): User's aesthetic preference ('glossy', 'matte', 'textured').
    
    Returns:
        str: Recommended material for 3D printing.
    
    Raises:
        MaterialRecommendationError: If the input parameters are invalid.
    """
    
    # Define a mapping of materials based on durability and aesthetic preferences
    materials = {
        'high': {
            'glossy': 'Acrylic',
            'matte': 'Plaswood',
            'textured': 'Foam Board'
        },
        'medium': {
            'glossy': 'ABS Plastic',
            'matte': 'PETG',
            'textured': 'Wood PLA'
        },
        'low': {
            'glossy': 'PLA',
            'matte': 'Cardboard',
            'textured': 'Paper Mâché'
        }
    }

    # Validate input parameters
    if durability_rating not in materials:
        raise MaterialRecommendationError(f"Invalid durability rating: {durability_rating}. Must be 'high', 'medium', or 'low'.")
    if aesthetic_preference not in materials[durability_rating]:
        raise MaterialRecommendationError(f"Invalid aesthetic preference: {aesthetic_preference}. Must be 'glossy', 'matte', or 'textured'.")

    # Return the recommended material
    return materials[durability_rating][aesthetic_preference]

# Example usage
if __name__ == "__main__":
    try:
        durability = input("Enter durability preference (high, medium, low): ").strip().lower()
        aesthetic = input("Enter aesthetic preference (glossy, matte, textured): ").strip().lower()
        
        recommended_material = recommend_material(durability, aesthetic)
        print(f"Recommended material for your 3D printed letters: {recommended_material}")
        
    except MaterialRecommendationError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
