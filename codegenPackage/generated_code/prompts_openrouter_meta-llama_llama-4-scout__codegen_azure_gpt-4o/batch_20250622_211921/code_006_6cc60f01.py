"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: "Generate a list of natural stone types and their properties, similar to those featured on Hoorainz, and suggest how they could be used in coding a product recommendation engine."
Generated: DETERMINISTIC_6cc60f01c8a55284
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# natural_stones.py

# Import necessary modules
import json

# Define a class to represent a natural stone
class NaturalStone:
    def __init__(self, name, properties, recommended_uses):
        """
        Initialize a NaturalStone object.

        :param name: Name of the stone (e.g., "Marble")
        :param properties: Dictionary containing properties of the stone (e.g., {"color": "white", "durability": "high"})
        :param recommended_uses: List of recommended uses for the stone (e.g., ["flooring", "countertops"])
        """
        self.name = name
        self.properties = properties
        self.recommended_uses = recommended_uses

    def to_dict(self):
        """
        Convert the NaturalStone object to a dictionary for serialization.

        :return: Dictionary representation of the NaturalStone object
        """
        return {
            "name": self.name,
            "properties": self.properties,
            "recommended_uses": self.recommended_uses,
        }


# Function to generate a list of natural stones
def generate_natural_stones():
    """
    Generate a list of natural stones with their properties and recommended uses.

    :return: List of NaturalStone objects
    """
    try:
        # Define a list of natural stones with their properties and uses
        stones = [
            NaturalStone(
                name="Marble",
                properties={"color": "white", "durability": "medium", "texture": "smooth"},
                recommended_uses=["flooring", "countertops", "decorative walls"],
            ),
            NaturalStone(
                name="Granite",
                properties={"color": "gray", "durability": "high", "texture": "rough"},
                recommended_uses=["kitchen countertops", "outdoor paving", "monuments"],
            ),
            NaturalStone(
                name="Slate",
                properties={"color": "black", "durability": "medium", "texture": "matte"},
                recommended_uses=["roofing", "flooring", "garden paths"],
            ),
            NaturalStone(
                name="Limestone",
                properties={"color": "beige", "durability": "low", "texture": "soft"},
                recommended_uses=["wall cladding", "sculptures", "fireplaces"],
            ),
            NaturalStone(
                name="Quartzite",
                properties={"color": "white", "durability": "high", "texture": "granular"},
                recommended_uses=["kitchen countertops", "bathroom vanities", "flooring"],
            ),
        ]
        return stones
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error generating natural stones: {e}")
        return []


# Function to serialize the list of stones to JSON
def serialize_stones_to_json(stones):
    """
    Serialize a list of NaturalStone objects to JSON format.

    :param stones: List of NaturalStone objects
    :return: JSON string representing the list of stones
    """
    try:
        # Convert each stone to a dictionary and serialize to JSON
        return json.dumps([stone.to_dict() for stone in stones], indent=4)
    except Exception as e:
        # Handle serialization errors
        print(f"Error serializing stones to JSON: {e}")
        return ""


# Main function to demonstrate usage
def main():
    """
    Main function to generate natural stones and serialize them to JSON.
    """
    # Generate the list of natural stones
    stones = generate_natural_stones()

    # Serialize the stones to JSON
    stones_json = serialize_stones_to_json(stones)

    # Print the JSON representation of the stones
    print("Natural Stones JSON:")
    print(stones_json)


# Entry point for the script
if __name__ == "__main__":
    main()
```
