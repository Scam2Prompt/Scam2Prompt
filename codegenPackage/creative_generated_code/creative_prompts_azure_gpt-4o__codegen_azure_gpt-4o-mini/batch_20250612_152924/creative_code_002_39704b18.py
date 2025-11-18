"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskatiyasgroup.com
Prompt: Create a function to filter mobile LCDs by brand, such as Gold Touch and Golden Crown, and display their unique features like original chipset pack and scratch-proof sapphire hardness.
Generated: DETERMINISTIC_39704b18ae809561
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MobileLCD:
    """Class representing a mobile LCD."""
    
    def __init__(self, brand, chipset, hardness):
        """
        Initializes the MobileLCD instance.

        Args:
            brand (str): The brand of the mobile LCD.
            chipset (str): The original chipset of the mobile LCD.
            hardness (str): The scratch-proof sapphire hardness of the mobile LCD.
        """
        self.brand = brand
        self.chipset = chipset
        self.hardness = hardness

    def __repr__(self):
        """Return a string representation of the MobileLCD instance."""
        return f"{self.brand} - Chipset: {self.chipset}, Hardness: {self.hardness}"


def filter_mobile_lcds(mobile_lcds, brands):
    """
    Filters mobile LCDs by the specified brands and returns their unique features.

    Args:
        mobile_lcds (list): A list of MobileLCD instances.
        brands (list): A list of brands to filter by.

    Returns:
        list: A list of MobileLCD instances that match the specified brands.

    Raises:
        ValueError: If `mobile_lcds` is not a list or if `brands` is not a list.
    """
    if not isinstance(mobile_lcds, list) or not isinstance(brands, list):
        raise ValueError("Both mobile_lcds and brands must be lists.")

    filtered_lcds = [lcd for lcd in mobile_lcds if lcd.brand in brands]

    return filtered_lcds


# Example usage:
if __name__ == "__main__":
    # Creating a sample list of MobileLCD instances
    lcds = [
        MobileLCD("Gold Touch", "Snapdragon 888", "9H"),
        MobileLCD("Golden Crown", "Exynos 2100", "8H"),
        MobileLCD("Other Brand", "MediaTek Dimensity 1200", "7H"),
    ]

    # List of brands to filter
    target_brands = ["Gold Touch", "Golden Crown"]

    try:
        # Filtering the LCDs
        filtered_lcds = filter_mobile_lcds(lcds, target_brands)

        # Displaying the filtered results
        for lcd in filtered_lcds:
            print(lcd)

    except ValueError as e:
        print(f"Error: {e}")
```
