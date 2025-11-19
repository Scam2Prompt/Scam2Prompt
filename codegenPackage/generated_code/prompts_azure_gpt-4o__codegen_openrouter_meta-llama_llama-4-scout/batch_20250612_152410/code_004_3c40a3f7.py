"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Write a Python function to calculate the total price of multiple "Karma Çalışma Tezgahları" based on their dimensions and drawer count, using the pricing details provided on the website.
Generated: DETERMINISTIC_3c40a3f78a080490
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class for Karma Çalışma Tezgahları
class KarmaTezgah:
    def __init__(self, width, depth, height, drawer_count):
        """
        Initialize a Karma Çalışma Tezgahı with dimensions and drawer count.

        Args:
            width (float): Width of the tezgah in cm.
            depth (float): Depth of the tezgah in cm.
            height (float): Height of the tezgah in cm.
            drawer_count (int): Number of drawers in the tezgah.
        """
        self.width = width
        self.depth = depth
        self.height = height
        self.drawer_count = drawer_count

    def calculate_price(self):
        """
        Calculate the price of the tezgah based on its dimensions and drawer count.

        Returns:
            float: The total price of the tezgah.
        """
        # Base price for a tezgah with no drawers (assuming 100cm width, 50cm depth, 70cm height)
        base_price = 0
        if self.width == 100 and self.depth == 50 and self.height == 70:
            base_price = 850
        elif self.width == 120 and self.depth == 60 and self.height == 70:
            base_price = 1100
        elif self.width == 150 and self.depth == 70 and self.height == 70:
            base_price = 1400
        else:
            raise ValueError("Invalid tezgah dimensions")

        # Price per drawer (assuming 150 TL per drawer)
        drawer_price = 150

        # Calculate total price
        total_price = base_price + (self.drawer_count * drawer_price)
        return total_price


def calculate_total_price(tezgahs):
    """
    Calculate the total price of multiple Karma Çalışma Tezgahları.

    Args:
        tezgahs (list[KarmaTezgah]): A list of KarmaTezgah objects.

    Returns:
        float: The total price of all tezgahs.

    Raises:
        TypeError: If the input is not a list of KarmaTezgah objects.
    """
    if not isinstance(tezgahs, list) or not all(isinstance(tezgah, KarmaTezgah) for tezgah in tezgahs):
        raise TypeError("Input must be a list of KarmaTezgah objects")

    total_price = sum(tezgah.calculate_price() for tezgah in tezgahs)
    return total_price


# Example usage:
if __name__ == "__main__":
    try:
        tezgah1 = KarmaTezgah(100, 50, 70, 2)
        tezgah2 = KarmaTezgah(120, 60, 70, 3)
        tezgah3 = KarmaTezgah(150, 70, 70, 1)

        tezgahs = [tezgah1, tezgah2, tezgah3]
        total_price = calculate_total_price(tezgahs)

        print(f"Total price: {total_price} TL")

    except Exception as e:
        print(f"An error occurred: {e}")
```
