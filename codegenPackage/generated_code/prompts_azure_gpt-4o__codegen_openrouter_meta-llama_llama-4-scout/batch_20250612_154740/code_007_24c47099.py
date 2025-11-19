"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write code to generate a free measure and quote for carpet installation, using the pricing and service details provided by Perfect Melbourne Carpet.
Generated: DETERMINISTIC_24c470999be1b660
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# carpet_quote_generator.py

class CarpetQuote:
    def __init__(self, length, width, carpet_price_per_sqm, installation_cost_per_sqm, 
                 underlay_cost_per_sqm=0, old_carpet_removal_cost=0):
        """
        Initialize a CarpetQuote object.

        Args:
            length (float): Length of the room in meters.
            width (float): Width of the room in meters.
            carpet_price_per_sqm (float): Price of carpet per square meter.
            installation_cost_per_sqm (float): Installation cost per square meter.
            underlay_cost_per_sqm (float, optional): Underlay cost per square meter. Defaults to 0.
            old_carpet_removal_cost (float, optional): Old carpet removal cost. Defaults to 0.
        """
        self.length = length
        self.width = width
        self.carpet_price_per_sqm = carpet_price_per_sqm
        self.installation_cost_per_sqm = installation_cost_per_sqm
        self.underlay_cost_per_sqm = underlay_cost_per_sqm
        self.old_carpet_removal_cost = old_carpet_removal_cost

    def calculate_area(self):
        """
        Calculate the area of the room.

        Returns:
            float: Area of the room in square meters.
        """
        return self.length * self.width

    def calculate_carpet_cost(self):
        """
        Calculate the total carpet cost.

        Returns:
            float: Total carpet cost.
        """
        return self.calculate_area() * self.carpet_price_per_sqm

    def calculate_installation_cost(self):
        """
        Calculate the total installation cost.

        Returns:
            float: Total installation cost.
        """
        return self.calculate_area() * self.installation_cost_per_sqm

    def calculate_underlay_cost(self):
        """
        Calculate the total underlay cost.

        Returns:
            float: Total underlay cost.
        """
        return self.calculate_area() * self.underlay_cost_per_sqm

    def calculate_total_cost(self):
        """
        Calculate the total cost of the carpet installation.

        Returns:
            float: Total cost of the carpet installation.
        """
        return (self.calculate_carpet_cost() + 
                self.calculate_installation_cost() + 
                self.calculate_underlay_cost() + 
                self.old_carpet_removal_cost)

    def generate_quote(self):
        """
        Generate a quote for the carpet installation.

        Returns:
            dict: Quote details.
        """
        quote = {
            "Room Dimensions": f"{self.length}m x {self.width}m",
            "Area": f"{self.calculate_area():.2f} sqm",
            "Carpet Cost": f"${self.calculate_carpet_cost():.2f}",
            "Installation Cost": f"${self.calculate_installation_cost():.2f}",
            "Underlay Cost": f"${self.calculate_underlay_cost():.2f}",
            "Old Carpet Removal Cost": f"${self.old_carpet_removal_cost:.2f}",
            "Total Cost": f"${self.calculate_total_cost():.2f}",
        }
        return quote


def main():
    try:
        # Perfect Melbourne Carpet pricing and service details
        carpet_price_per_sqm = 45.00
        installation_cost_per_sqm = 20.00
        underlay_cost_per_sqm = 10.00
        old_carpet_removal_cost = 200.00

        length = float(input("Enter the length of the room in meters: "))
        width = float(input("Enter the width of the room in meters: "))

        quote = CarpetQuote(length, width, carpet_price_per_sqm, installation_cost_per_sqm, 
                            underlay_cost_per_sqm, old_carpet_removal_cost)

        print("\nCarpet Installation Quote:")
        for key, value in quote.generate_quote().items():
            print(f"{key}: {value}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
```
