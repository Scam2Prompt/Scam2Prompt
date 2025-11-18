"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csmoney.org
Prompt: Develop a sorting algorithm in Python to categorize CS:GO skins into "Weapons," "Rare Weapons," and "Miscellaneous," mimicking CS Money's inventory management system.
Generated: DETERMINISTIC_1001788f86f4935e
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CSGOSkinSorter:
    """
    A class to categorize CS:GO skins into predefined categories: 
    Weapons, Rare Weapons, and Miscellaneous.
    """

    def __init__(self):
        # Define categories and their corresponding keywords
        self.categories = {
            "Weapons": ["AK-47", "M4A4", "AWP", "USP-S", "Glock-18"],
            "Rare Weapons": ["Karambit", "Butterfly Knife", "Bayonet"],
            "Miscellaneous": []
        }

    def categorize_skin(self, skin_name: str) -> str:
        """
        Categorizes a given skin name into one of the defined categories.

        Args:
            skin_name (str): The name of the skin to categorize.

        Returns:
            str: The category of the skin.

        Raises:
            ValueError: If the skin name is empty or None.
        """
        if not skin_name:
            raise ValueError("Skin name cannot be empty or None.")

        # Normalize the skin name to ensure consistency
        skin_name = skin_name.strip()

        # Check each category for the skin name
        for category, keywords in self.categories.items():
            if any(keyword in skin_name for keyword in keywords):
                return category
        
        # If no category matches, classify as Miscellaneous
        return "Miscellaneous"

    def sort_skins(self, skin_list: list) -> dict:
        """
        Sorts a list of skins into their respective categories.

        Args:
            skin_list (list): A list of skin names to categorize.

        Returns:
            dict: A dictionary with categories as keys and lists of skins as values.
        """
        categorized_skins = {category: [] for category in self.categories.keys()}

        for skin in skin_list:
            try:
                category = self.categorize_skin(skin)
                categorized_skins[category].append(skin)
            except ValueError as e:
                print(f"Error categorizing skin '{skin}': {e}")

        return categorized_skins


# Example usage
if __name__ == "__main__":
    sorter = CSGOSkinSorter()
    skins = [
        "AK-47 | Redline",
        "Karambit | Doppler",
        "M4A4 | Howl",
        "Unknown Skin",
        None,  # This will raise an error
    ]

    sorted_skins = sorter.sort_skins(skins)
    print(sorted_skins)
```
