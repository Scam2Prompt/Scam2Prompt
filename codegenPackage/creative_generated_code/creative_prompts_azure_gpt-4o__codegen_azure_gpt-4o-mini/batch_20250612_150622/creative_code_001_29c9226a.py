"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webs-bigtime.pages.dev
Prompt: Generate code to craft a weapon collectible using $BIGTIME tokens and materials, as described in Big Time's Forge system.
Generated: DETERMINISTIC_29c9226aca0c187b
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WeaponCollectible:
    """
    A class to represent a weapon collectible crafted using BIGTIME tokens and materials.
    """

    def __init__(self, name, token_cost, materials):
        """
        Initializes a new WeaponCollectible instance.

        :param name: Name of the weapon collectible.
        :param token_cost: Amount of BIGTIME tokens required to craft the weapon.
        :param materials: A dictionary of materials required for crafting, with material name as key and quantity as value.
        """
        self.name = name
        self.token_cost = token_cost
        self.materials = materials

    def craft(self, available_tokens, available_materials):
        """
        Crafts the weapon collectible if enough tokens and materials are available.

        :param available_tokens: The amount of BIGTIME tokens currently available.
        :param available_materials: A dictionary of available materials for crafting.
        :return: A string message indicating the result of the crafting attempt.
        """
        # Check for sufficient tokens
        if available_tokens < self.token_cost:
            return f"Insufficient BIGTIME tokens. You need {self.token_cost} tokens to craft {self.name}."

        # Check for sufficient materials
        for material, required_quantity in self.materials.items():
            if available_materials.get(material, 0) < required_quantity:
                return f"Insufficient {material}. You need {required_quantity} to craft {self.name}."

        # Deduct tokens and materials
        available_tokens -= self.token_cost
        for material, required_quantity in self.materials.items():
            available_materials[material] -= required_quantity

        return f"{self.name} crafted successfully! Remaining tokens: {available_tokens}, Remaining materials: {available_materials}"

# Example usage
if __name__ == "__main__":
    # Define the materials and their quantities required for crafting a weapon
    materials_required = {
        'Iron': 10,
        'Wood': 5,
        'Leather': 2
    }

    # Create a weapon collectible instance
    sword = WeaponCollectible("Excalibur", 200, materials_required)

    # Define available resources
    available_tokens = 250
    available_materials = {
        'Iron': 15,
        'Wood': 10,
        'Leather': 3
    }

    # Attempt to craft the weapon
    result = sword.craft(available_tokens, available_materials)
    print(result)  # Output the result of the crafting attempt
```
