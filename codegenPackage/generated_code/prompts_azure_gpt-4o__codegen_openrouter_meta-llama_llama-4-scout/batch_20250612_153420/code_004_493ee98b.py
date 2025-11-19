"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Develop a program that calculates the cost-effectiveness of using filler masterbatches versus additive masterbatches in PVC applications, referencing the product categories on the M J Pigment & Additives website.
Generated: DETERMINISTIC_493ee98b18c9c14a
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import math

class Masterbatch:
    def __init__(self, name, price_per_kg, density):
        """
        Initialize a Masterbatch object.

        Args:
        - name (str): Name of the masterbatch.
        - price_per_kg (float): Price per kilogram of the masterbatch.
        - density (float): Density of the masterbatch in g/cm^3.
        """
        self.name = name
        self.price_per_kg = price_per_kg
        self.density = density

    def calculate_cost_per_liter(self):
        """
        Calculate the cost per liter of the masterbatch.

        Returns:
        - cost_per_liter (float): Cost per liter of the masterbatch.
        """
        # 1 kg = 1000 grams, 1 liter = 1000 cm^3
        mass_per_liter = self.density * 1000  # in grams
        mass_per_liter_kg = mass_per_liter / 1000  # convert to kg
        cost_per_liter = self.price_per_kg / mass_per_liter_kg
        return cost_per_liter


class FillerMasterbatch(Masterbatch):
    def __init__(self, name, price_per_kg, density, filler_content):
        """
        Initialize a FillerMasterbatch object.

        Args:
        - name (str): Name of the filler masterbatch.
        - price_per_kg (float): Price per kilogram of the filler masterbatch.
        - density (float): Density of the filler masterbatch in g/cm^3.
        - filler_content (float): Filler content in % by weight.
        """
        super().__init__(name, price_per_kg, density)
        self.filler_content = filler_content

    def calculate_filler_cost_per_liter(self):
        """
        Calculate the cost per liter of the filler in the masterbatch.

        Returns:
        - filler_cost_per_liter (float): Cost per liter of the filler.
        """
        cost_per_liter = self.calculate_cost_per_liter()
        filler_cost_per_liter = cost_per_liter * (self.filler_content / 100)
        return filler_cost_per_liter


class AdditiveMasterbatch(Masterbatch):
    def __init__(self, name, price_per_kg, density, additive_content):
        """
        Initialize an AdditiveMasterbatch object.

        Args:
        - name (str): Name of the additive masterbatch.
        - price_per_kg (float): Price per kilogram of the additive masterbatch.
        - density (float): Density of the additive masterbatch in g/cm^3.
        - additive_content (float): Additive content in % by weight.
        """
        super().__init__(name, price_per_kg, density)
        self.additive_content = additive_content

    def calculate_additive_cost_per_liter(self):
        """
        Calculate the cost per liter of the additive in the masterbatch.

        Returns:
        - additive_cost_per_liter (float): Cost per liter of the additive.
        """
        cost_per_liter = self.calculate_cost_per_liter()
        additive_cost_per_liter = cost_per_liter * (self.additive_content / 100)
        return additive_cost_per_liter


def calculate_cost_effectiveness(filler_masterbatch, additive_masterbatch, pvc_application):
    """
    Calculate the cost-effectiveness of using filler masterbatches versus additive masterbatches.

    Args:
    - filler_masterbatch (FillerMasterbatch): Filler masterbatch object.
    - additive_masterbatch (AdditiveMasterbatch): Additive masterbatch object.
    - pvc_application (str): PVC application.

    Returns:
    - None
    """
    try:
        filler_cost_per_liter = filler_masterbatch.calculate_filler_cost_per_liter()
        additive_cost_per_liter = additive_masterbatch.calculate_additive_cost_per_liter()

        print(f"Cost-effectiveness analysis for {pvc_application}:")
        print(f"Filler Masterbatch: {filler_masterbatch.name} - Filler cost per liter: ${filler_cost_per_liter:.2f}")
        print(f"Additive Masterbatch: {additive_masterbatch.name} - Additive cost per liter: ${additive_cost_per_liter:.2f}")

        if filler_cost_per_liter < additive_cost_per_liter:
            print(f"Using {filler_masterbatch.name} is more cost-effective for {pvc_application}.")
        elif filler_cost_per_liter > additive_cost_per_liter:
            print(f"Using {additive_masterbatch.name} is more cost-effective for {pvc_application}.")
        else:
            print(f"Both {filler_masterbatch.name} and {additive_masterbatch.name} have the same cost-effectiveness for {pvc_application}.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Product categories on the M J Pigment & Additives website
    filler_masterbatch = FillerMasterbatch("M J Filler Masterbatch", 2.50, 1.2, 60)
    additive_masterbatch = AdditiveMasterbatch("M J Additive Masterbatch", 5.00, 1.1, 20)
    pvc_application = "PVC Pipes"

    calculate_cost_effectiveness(filler_masterbatch, additive_masterbatch, pvc_application)
```
