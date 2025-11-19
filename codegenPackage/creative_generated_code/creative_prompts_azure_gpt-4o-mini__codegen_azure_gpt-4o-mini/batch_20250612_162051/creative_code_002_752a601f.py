"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullport.net
Prompt: Create a function that calculates the total cost of purchasing multiple types of HDMI cables from FullPort, considering different lengths and brands.
Generated: DETERMINISTIC_752a601f266334fa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HDMI_Cable:
    """A class to represent an HDMI cable with its attributes."""
    
    def __init__(self, brand: str, length: float, price_per_meter: float):
        """
        Initialize an HDMI cable with brand, length, and price per meter.

        :param brand: Brand of the HDMI cable
        :param length: Length of the HDMI cable in meters
        :param price_per_meter: Price per meter of the HDMI cable
        """
        self.brand = brand
        self.length = length
        self.price_per_meter = price_per_meter

    def total_cost(self) -> float:
        """
        Calculate the total cost of the HDMI cable.

        :return: Total cost for the given length and price per meter.
        """
        return self.length * self.price_per_meter


def calculate_total_cost(cables: list) -> float:
    """
    Calculate the total cost of purchasing multiple HDMI cables.

    :param cables: A list of HDMI_Cable objects
    :return: Total cost of all HDMI cables
    :raises ValueError: If the list of cables is empty
    """
    if not cables:
        raise ValueError("The list of cables cannot be empty.")

    total = 0.0
    for cable in cables:
        if not isinstance(cable, HDMI_Cable):
            raise TypeError("All items in the cables list must be instances of HDMI_Cable.")

        total += cable.total_cost()

    return total


# Example usage
if __name__ == "__main__":
    try:
        # Create a list of HDMI cables
        cables = [
            HDMI_Cable("FullPort", 1.5, 10.0),  # 1.5 meters at $10 per meter
            HDMI_Cable("FullPort", 2.0, 15.0),  # 2.0 meters at $15 per meter
            HDMI_Cable("OtherBrand", 1.0, 12.0)  # 1.0 meters at $12 per meter
        ]

        # Calculate total cost
        total_cost = calculate_total_cost(cables)
        print(f"Total cost of HDMI cables: ${total_cost:.2f}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
