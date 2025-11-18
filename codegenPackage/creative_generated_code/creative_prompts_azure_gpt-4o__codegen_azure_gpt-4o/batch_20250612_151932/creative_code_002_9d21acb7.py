"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-bigtime.pages.dev
Prompt: Create a function to simulate opening Mystery Boxes in Big Time, extracting their contents and using them for crafting weapons and armor cosmetics.
Generated: DETERMINISTIC_9d21acb7d0e49f34
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Define constants for the contents of mystery boxes
WEAPON_MATERIALS = ["Steel", "Iron", "Titanium", "Obsidian"]
ARMOR_MATERIALS = ["Leather", "Cloth", "Chainmail", "Kevlar"]
COSMETICS = ["Glow Paint", "Holo Decals", "Mystic Aura", "Shadow Effect"]

# Error messages
INVALID_BOX_TYPE_ERROR = "Invalid mystery box type. Valid types are: 'weapon', 'armor', and 'cosmetic'."

def open_mystery_box(box_type):
    """
    Simulates opening a Mystery Box and extracting its contents.

    Args:
        box_type (str): The type of mystery box to open. Valid values are 'weapon', 'armor', 'cosmetic'.

    Returns:
        dict: A dictionary containing the extracted contents.

    Raises:
        ValueError: If an invalid box type is provided.
    """
    # Validate the box type
    if box_type not in ["weapon", "armor", "cosmetic"]:
        raise ValueError(INVALID_BOX_TYPE_ERROR)

    # Randomly select contents based on the type of box
    if box_type == "weapon":
        contents = random.choice(WEAPON_MATERIALS)
    elif box_type == "armor":
        contents = random.choice(ARMOR_MATERIALS)
    else:  # box_type == "cosmetic"
        contents = random.choice(COSMETICS)

    # Return the extracted contents as a dictionary
    return {
        "box_type": box_type,
        "contents": contents
    }

def craft_item(contents):
    """
    Simulates using extracted mystery box contents to craft an item.

    Args:
        contents (dict): The contents extracted from the mystery box. Expected keys are 'box_type' and 'contents'.

    Returns:
        str: A string describing the crafted item.
    """
    box_type = contents.get("box_type")
    material = contents.get("contents")

    if box_type == "weapon":
        return f"Crafted a weapon using {material}."
    elif box_type == "armor":
        return f"Crafted armor using {material}."
    elif box_type == "cosmetic":
        return f"Created a cosmetic effect: {material}."
    else:
        return "Invalid contents for crafting."

# Example usage
if __name__ == "__main__":
    try:
        # Open a mystery box
        mystery_box = open_mystery_box("weapon")
        print(f"Mystery Box Contents: {mystery_box}")

        # Craft an item using the contents
        crafted_item = craft_item(mystery_box)
        print(f"Crafted Item: {crafted_item}")
    except ValueError as e:
        print(f"Error: {e}")
```
