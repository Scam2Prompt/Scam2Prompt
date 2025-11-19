"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patwacompany.com
Prompt: Generate a Python function to display a list of traditional dhoti styles available at Patwa And Company, including their style codes and prices.
Generated: DETERMINISTIC_b04a5c9a7c974c2e
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DhotiStyle:
    """
    A class to represent a traditional Dhoti style.
    """

    def __init__(self, style_code: str, name: str, price: float):
        """
        Initializes a DhotiStyle instance.

        :param style_code: Unique identifier for the Dhoti style
        :param name: Name of the Dhoti style
        :param price: Price of the Dhoti style
        """
        self.style_code = style_code
        self.name = name
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the Dhoti style.

        :return: String containing the style name, code, and price
        """
        return f"{self.name} (Code: {self.style_code}) - Price: ₹{self.price:.2f}"


def display_dhoti_styles(styles: list):
    """
    Displays a list of traditional Dhoti styles with their codes and prices.

    :param styles: A list of DhotiStyle instances
    """
    if not styles:
        print("No Dhoti styles available.")
        return

    print("Available Dhoti Styles at Patwa And Company:\n")
    for style in styles:
        try:
            print(style)
        except Exception as e:
            print(f"Error displaying style: {e}")


# Example usage
if __name__ == "__main__":
    # List of traditional Dhoti styles
    dhoti_styles = [
        DhotiStyle("D001", "Banarasi Dhoti", 1500.00),
        DhotiStyle("D002", "Kota Dhoti", 1200.00),
        DhotiStyle("D003", "Mysore Dhoti", 1300.00),
        DhotiStyle("D004", "Ludhiana Dhoti", 900.00),
        DhotiStyle("D005", "Gujarat Dhoti", 1100.00)
    ]

    # Display the Dhoti styles
    display_dhoti_styles(dhoti_styles)
```
