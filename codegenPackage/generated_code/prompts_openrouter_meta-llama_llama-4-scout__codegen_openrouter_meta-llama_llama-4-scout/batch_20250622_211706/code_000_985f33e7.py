"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: "What are the different types of knit fabrics used for sportswear and swimwear, and how do they differ in terms of material and application?"
Generated: DETERMINISTIC_985f33e7acaf107d
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# knit_fabrics.py

class KnitFabric:
    """Base class for knit fabrics."""

    def __init__(self, name, material, application):
        """
        Initialize a knit fabric.

        Args:
            name (str): Name of the fabric.
            material (str): Material used to make the fabric.
            application (str): Application of the fabric (e.g., sportswear, swimwear).
        """
        self.name = name
        self.material = material
        self.application = application

    def __str__(self):
        return f"{self.name} ({self.material}) - {self.application}"


class SportswearKnitFabric(KnitFabric):
    """Knit fabric used for sportswear."""

    def __init__(self, name, material, moisture_wicking, breathability):
        """
        Initialize a sportswear knit fabric.

        Args:
            name (str): Name of the fabric.
            material (str): Material used to make the fabric.
            moisture_wicking (bool): Whether the fabric is moisture-wicking.
            breathability (bool): Whether the fabric is breathable.
        """
        super().__init__(name, material, "Sportswear")
        self.moisture_wicking = moisture_wicking
        self.breathability = breathability

    def __str__(self):
        return super().__str__() + f", Moisture-wicking: {self.moisture_wicking}, Breathable: {self.breathability}"


class SwimwearKnitFabric(KnitFabric):
    """Knit fabric used for swimwear."""

    def __init__(self, name, material, uv_resistance, quick_drying):
        """
        Initialize a swimwear knit fabric.

        Args:
            name (str): Name of the fabric.
            material (str): Material used to make the fabric.
            uv_resistance (bool): Whether the fabric is UV-resistant.
            quick_drying (bool): Whether the fabric is quick-drying.
        """
        super().__init__(name, material, "Swimwear")
        self.uv_resistance = uv_resistance
        self.quick_drying = quick_drying

    def __str__(self):
        return super().__str__() + f", UV-resistant: {self.uv_resistance}, Quick-drying: {self.quick_drying}"


def main():
    try:
        # Create sportswear knit fabrics
        polyester_fabric = SportswearKnitFabric("Polyester", "Polyester", True, True)
        nylon_fabric = SportswearKnitFabric("Nylon", "Nylon", True, True)
        cotton_fabric = SportswearKnitFabric("Cotton", "Cotton", False, True)

        # Create swimwear knit fabrics
        lycra_fabric = SwimwearKnitFabric("Lycra", "Lycra", True, True)
        spandex_fabric = SwimwearKnitFabric("Spandex", "Spandex", True, True)
        polyester_swim_fabric = SwimwearKnitFabric("Polyester", "Polyester", True, True)

        # Print fabrics
        print("Sportswear Knit Fabrics:")
        print(polyester_fabric)
        print(nylon_fabric)
        print(cotton_fabric)

        print("\nSwimwear Knit Fabrics:")
        print(lycra_fabric)
        print(spandex_fabric)
        print(polyester_swim_fabric)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
