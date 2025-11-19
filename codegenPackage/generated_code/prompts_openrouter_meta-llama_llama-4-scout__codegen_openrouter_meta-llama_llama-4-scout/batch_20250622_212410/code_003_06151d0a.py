"""
Generated Code Metadata:
========================
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Develop a simple program to compare the features and performance of BerlinerLuft's Confortcond and VarioCond climatizer lines.
Generated: DETERMINISTIC_06151d0a94d68c84
Batch ID: 20250622_212410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# climatizer_comparator.py

class Climatizer:
    """Base class for climatizers."""

    def __init__(self, name, price, energy_efficiency, noise_level):
        """
        Initialize a climatizer.

        Args:
            name (str): Name of the climatizer.
            price (float): Price of the climatizer.
            energy_efficiency (float): Energy efficiency of the climatizer.
            noise_level (int): Noise level of the climatizer in dB.
        """
        self.name = name
        self.price = price
        self.energy_efficiency = energy_efficiency
        self.noise_level = noise_level

    def __str__(self):
        return f"{self.name}: Price=${self.price:.2f}, Energy Efficiency={self.energy_efficiency:.2f}, Noise Level={self.noise_level} dB"


class Confortcond(Climatizer):
    """Confortcond climatizer line."""

    def __init__(self, price, energy_efficiency, noise_level, heating_capacity):
        """
        Initialize a Confortcond climatizer.

        Args:
            price (float): Price of the climatizer.
            energy_efficiency (float): Energy efficiency of the climatizer.
            noise_level (int): Noise level of the climatizer in dB.
            heating_capacity (int): Heating capacity of the climatizer in BTU.
        """
        super().__init__("Confortcond", price, energy_efficiency, noise_level)
        self.heating_capacity = heating_capacity

    def __str__(self):
        return super().__str__() + f", Heating Capacity={self.heating_capacity} BTU"


class VarioCond(Climatizer):
    """VarioCond climatizer line."""

    def __init__(self, price, energy_efficiency, noise_level, cooling_capacity):
        """
        Initialize a VarioCond climatizer.

        Args:
            price (float): Price of the climatizer.
            energy_efficiency (float): Energy efficiency of the climatizer.
            noise_level (int): Noise level of the climatizer in dB.
            cooling_capacity (int): Cooling capacity of the climatizer in BTU.
        """
        super().__init__("VarioCond", price, energy_efficiency, noise_level)
        self.cooling_capacity = cooling_capacity

    def __str__(self):
        return super().__str__() + f", Cooling Capacity={self.cooling_capacity} BTU"


def compare_climatizers(climatizer1, climatizer2):
    """
    Compare two climatizers.

    Args:
        climatizer1 (Climatizer): First climatizer.
        climatizer2 (Climatizer): Second climatizer.

    Returns:
        dict: Comparison result.
    """
    try:
        result = {
            "name1": climatizer1.name,
            "name2": climatizer2.name,
            "price_diff": climatizer2.price - climatizer1.price,
            "energy_efficiency_diff": climatizer2.energy_efficiency - climatizer1.energy_efficiency,
            "noise_level_diff": climatizer2.noise_level - climatizer1.noise_level,
        }
        return result
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def main():
    # Create climatizers
    confortcond = Confortcond(1000.0, 2.5, 30, 15000)
    variocond = VarioCond(1200.0, 3.0, 25, 18000)

    # Print climatizer details
    print("Climatizer Details:")
    print(confortcond)
    print(variocond)

    # Compare climatizers
    comparison_result = compare_climatizers(confortcond, variocond)

    if comparison_result:
        print("\nComparison Result:")
        print(f"Name 1: {comparison_result['name1']}")
        print(f"Name 2: {comparison_result['name2']}")
        print(f"Price Difference: ${comparison_result['price_diff']:.2f}")
        print(f"Energy Efficiency Difference: {comparison_result['energy_efficiency_diff']:.2f}")
        print(f"Noise Level Difference: {comparison_result['noise_level_diff']} dB")


if __name__ == "__main__":
    main()
```
