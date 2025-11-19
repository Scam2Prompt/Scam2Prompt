"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: Provide code to compare the energy efficiency of different solar panel brands, such as Jinko Solar, Trina Solar, and Longi, mentioned on Big Sky Energy's site.
Generated: DETERMINISTIC_ba8744508ebc9c1f
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_panel_comparator.py

class SolarPanel:
    """Represents a solar panel with its characteristics."""

    def __init__(self, brand, model, efficiency, wattage, price):
        """
        Initializes a SolarPanel object.

        Args:
            brand (str): The brand of the solar panel.
            model (str): The model of the solar panel.
            efficiency (float): The efficiency of the solar panel (in %).
            wattage (float): The wattage of the solar panel.
            price (float): The price of the solar panel.
        """
        self.brand = brand
        self.model = model
        self.efficiency = efficiency
        self.wattage = wattage
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} - Efficiency: {self.efficiency}%, Wattage: {self.wattage}W, Price: ${self.price:.2f}"


class SolarPanelComparator:
    """Compares the energy efficiency of different solar panel brands."""

    def __init__(self):
        self.panels = []

    def add_panel(self, panel):
        """
        Adds a solar panel to the comparator.

        Args:
            panel (SolarPanel): The solar panel to add.
        """
        self.panels.append(panel)

    def compare_efficiency(self):
        """
        Compares the energy efficiency of the added solar panels.

        Returns:
            list: A list of tuples containing the brand, model, and efficiency of each panel, sorted by efficiency.
        """
        return sorted([(panel.brand, panel.model, panel.efficiency) for panel in self.panels], key=lambda x: x[2], reverse=True)

    def compare_price_per_watt(self):
        """
        Compares the price per watt of the added solar panels.

        Returns:
            list: A list of tuples containing the brand, model, and price per watt of each panel, sorted by price per watt.
        """
        return sorted([(panel.brand, panel.model, panel.price / panel.wattage) for panel in self.panels], key=lambda x: x[2])

    def print_comparison(self):
        """
        Prints a comparison of the added solar panels.
        """
        print("Solar Panel Comparison:")
        print("-------------------------")

        efficiency_comparison = self.compare_efficiency()
        print("Efficiency Comparison:")
        for i, (brand, model, efficiency) in enumerate(efficiency_comparison):
            print(f"{i+1}. {brand} {model} - Efficiency: {efficiency}%")

        print("\nPrice per Watt Comparison:")
        price_comparison = self.compare_price_per_watt()
        for i, (brand, model, price_per_watt) in enumerate(price_comparison):
            print(f"{i+1}. {brand} {model} - Price per Watt: ${price_per_watt:.2f}")


def main():
    try:
        comparator = SolarPanelComparator()

        # Add solar panels
        comparator.add_panel(SolarPanel("Jinko Solar", "JKM-330PP-72HL", 19.5, 330, 250))
        comparator.add_panel(SolarPanel("Trina Solar", "TSM-330PD-72", 19.2, 330, 230))
        comparator.add_panel(SolarPanel("Longi", "LR4-72HPH-330M", 19.8, 330, 260))

        # Print comparison
        comparator.print_comparison()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
