"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Generate code for a character customization system in a game like Moon Tropica, with options for wearables and limited edition assets.
Generated: DETERMINISTIC_9690f7e03372bd8c
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class CharacterCustomization:
    """
    A class to handle character customization in a game.
    Includes options for wearables and limited edition assets.
    """

    def __init__(self):
        """
        Initialize the customization system with default options.
        """
        self.character = {
            "name": "Default Character",
            "wearables": [],
            "limited_assets": []
        }
        self.available_wearables = ["Hat", "Shirt", "Pants", "Shoes"]
<<<<<<< HEAD
        self.limited_assets = ["Golden Crown", "Diamond Necklace", "Platinum Ring"]

=======
        self.limited_assets = ["Golden Crown", "Diamond Necklace"]
    
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    def set_character_name(self, name):
        """
        Set the name of the character.
        :param name: str - The name of the character.
        """
        if not name or not isinstance(name, str):
            raise ValueError("Character name must be a non-empty string.")
        self.character["name"] = name

    def add_wearable(self, wearable):
        """
        Add a wearable item to the character.
<<<<<<< HEAD
        :param wearable: str - The wearable item to add.
        """
        if wearable not in self.available_wearables:
            raise ValueError(f"'{wearable}' is not an available wearable.")
        if wearable in self.character["wearables"]:
            raise ValueError(f"'{wearable}' is already equipped.")
        self.character["wearables"].append(wearable)

    def remove_wearable(self, wearable):
        """
        Remove a wearable item from the character.
        :param wearable: str - The wearable item to remove.
=======
        :param wearable: str - The name of the wearable item.
        """
        if wearable not in self.available_wearables:
            raise ValueError(f"'{wearable}' is not an available wearable.")
        self.character["wearables"].append(wearable)

    def add_limited_asset(self, asset):
        """
        Add a limited edition asset to the character.
        :param asset: str - The name of the limited edition asset.
        """
        if asset not in self.limited_assets:
            raise ValueError(f"'{asset}' is not a valid limited edition asset.")
        self.character["limited_assets"].append(asset)

    def remove_wearable(self, wearable):
        """
        Remove a wearable item from the character.
        :param wearable: str - The name of the wearable item.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        if wearable not in self.character["wearables"]:
            raise ValueError(f"'{wearable}' is not currently equipped.")
        self.character["wearables"].remove(wearable)

<<<<<<< HEAD
    def add_limited_asset(self, asset):
        """
        Add a limited edition asset to the character.
        :param asset: str - The limited edition asset to add.
        """
        if asset not in self.limited_assets:
            raise ValueError(f"'{asset}' is not a valid limited edition asset.")
        if asset in self.character["limited_assets"]:
            raise ValueError(f"'{asset}' is already equipped.")
        self.character["limited_assets"].append(asset)

    def remove_limited_asset(self, asset):
        """
        Remove a limited edition asset from the character.
        :param asset: str - The limited edition asset to remove.
=======
    def remove_limited_asset(self, asset):
        """
        Remove a limited edition asset from the character.
        :param asset: str - The name of the limited edition asset.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        if asset not in self.character["limited_assets"]:
            raise ValueError(f"'{asset}' is not currently equipped.")
        self.character["limited_assets"].remove(asset)

    def save_character(self, file_path):
        """
<<<<<<< HEAD
        Save the character customization to a file.
        :param file_path: str - The path to save the character data.
=======
        Save the character's customization to a file.
        :param file_path: str - The path to the file where the character data will be saved.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.character, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save character data: {e}")

    def load_character(self, file_path):
        """
<<<<<<< HEAD
        Load character customization from a file.
        :param file_path: str - The path to load the character data from.
=======
        Load the character's customization from a file.
        :param file_path: str - The path to the file where the character data is stored.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        try:
            with open(file_path, 'r') as file:
                self.character = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load character data: {e}")

    def display_character(self):
        """
<<<<<<< HEAD
        Display the current character customization.
=======
        Display the current character's customization.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        print(json.dumps(self.character, indent=4))


# Example usage:
if __name__ == "__main__":
    try:
        customization = CharacterCustomization()
        customization.set_character_name("Hero")
        customization.add_wearable("Hat")
        customization.add_wearable("Shirt")
        customization.add_limited_asset("Golden Crown")
        customization.display_character()

<<<<<<< HEAD
        # Save to file
        customization.save_character("character_data.json")

        # Load from file
=======
        # Save character to file
        customization.save_character("character_data.json")

        # Load character from file
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        customization.load_character("character_data.json")
        customization.display_character()
    except Exception as e:
        print(f"Error: {e}")
```
