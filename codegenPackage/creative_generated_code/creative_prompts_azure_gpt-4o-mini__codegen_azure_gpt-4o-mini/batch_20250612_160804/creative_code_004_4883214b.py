"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Suggest eco-friendly craft ideas for kids, similar to those featured on Craft Intra, focusing on sustainability in crafting.
Generated: DETERMINISTIC_4883214b8e215168
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class EcoFriendlyCraftIdeas:
    """
    A class to generate eco-friendly craft ideas for kids.
    Focuses on sustainability and creative reuse of materials.
    """

    def __init__(self):
        """Initializes the craft ideas list with sustainable materials."""
        self.craft_ideas = [
            {
                "title": "Recycled Paper Mache",
                "materials": ["Old newspapers", "Flour", "Water", "Paint"],
                "instructions": "Tear newspapers into strips, mix flour and water to create paste, dip strips and shape them."
            },
            {
                "title": "Bottle Cap Magnets",
                "materials": ["Plastic bottle caps", "Magnet strips", "Glue", "Paint"],
                "instructions": "Decorate the bottle caps, attach magnets to the back, and use them to hold notes on the fridge."
            },
            {
                "title": "Egg Carton Planters",
                "materials": ["Old egg cartons", "Soil", "Seeds", "Water"],
                "instructions": "Cut the egg carton, fill with soil, plant seeds in each cup, and water them."
            },
            {
                "title": "Fabric Scrap Bunting",
                "materials": ["Old fabric scraps", "String", "Glue", "Scissors"],
                "instructions": "Cut fabric into triangles, glue them onto a string for decorative bunting."
            },
            {
                "title": "Nature Collage",
                "materials": ["Leaves", "Twigs", "Glue", "Cardboard"],
                "instructions": "Collect natural items, arrange them on cardboard, and glue them to create a collage."
            }
        ]

    def get_random_craft_idea(self):
        """
        Returns a random eco-friendly craft idea.
        If no ideas are available, raises a ValueError.
        """
        if not self.craft_ideas:
            raise ValueError("No craft ideas available.")
        
        return random.choice(self.craft_ideas)

    def display_craft_idea(self):
        """
        Displays a random craft idea with materials and instructions.
        Handles any potential errors in fetching the idea.
        """
        try:
            craft_idea = self.get_random_craft_idea()
            print(f"Title: {craft_idea['title']}")
            print("Materials Needed:")
            for material in craft_idea['materials']:
                print(f"- {material}")
            print("Instructions:")
            print(craft_idea['instructions'])
        except ValueError as e:
            print(f"Error: {e}")

# Main execution
if __name__ == "__main__":
    eco_friendly_crafts = EcoFriendlyCraftIdeas()
    eco_friendly_crafts.display_craft_idea()
```
