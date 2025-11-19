"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.madoniaoli.it
Prompt: Develop a function that calculates the health benefits of using Madonia's extra virgin olive oil in daily cooking, referencing its properties and characteristics.
Generated: DETERMINISTIC_7433287471ec25e9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OliveOil:
    """
    A class to represent an extra virgin olive oil and its health benefits.
    """

    def __init__(self, name, polyphenols, monounsaturated_fats, antioxidants):
        """
        Initializes the OliveOil object with its properties.

        Args:
            name (str): The name of the olive oil.
            polyphenols (float): The amount of polyphenols in mg per 100ml.
            monounsaturated_fats (float): The amount of monounsaturated fats in g per 100ml.
            antioxidants (float): The amount of antioxidants in mg per 100ml.
        """
        self.name = name
        self.polyphenols = polyphenols
        self.monounsaturated_fats = monounsaturated_fats
        self.antioxidants = antioxidants

    def calculate_health_benefits(self):
        """
        Calculates the health benefits of using this olive oil in daily cooking.

        Returns:
            dict: A dictionary containing the health benefits associated with the olive oil.
        """
        try:
            benefits = {
                "Heart Health": self._heart_health_benefits(),
                "Inflammation Reduction": self._inflammation_reduction_benefits(),
                "Antioxidant Support": self._antioxidant_support_benefits(),
                "Weight Management": self._weight_management_benefits()
            }
            return benefits
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating health benefits: {str(e)}")

    def _heart_health_benefits(self):
        """
        Evaluates the heart health benefits based on monounsaturated fats.

        Returns:
            str: A statement about heart health benefits.
        """
        if self.monounsaturated_fats >= 70:
            return "High in monounsaturated fats, promoting heart health."
        return "Contains healthy fats but may not be optimal for heart health."

    def _inflammation_reduction_benefits(self):
        """
        Evaluates the benefits related to inflammation reduction based on polyphenols.

        Returns:
            str: A statement about inflammation reduction benefits.
        """
        if self.polyphenols > 100:
            return "High in polyphenols, known for their anti-inflammatory properties."
        return "Contains some polyphenols, but may have limited anti-inflammatory effects."

    def _antioxidant_support_benefits(self):
        """
        Evaluates the antioxidant support based on antioxidant content.

        Returns:
            str: A statement about antioxidant support benefits.
        """
        if self.antioxidants > 100:
            return "Rich in antioxidants that help combat oxidative stress."
        return "Contains antioxidants but may not provide significant support."

    def _weight_management_benefits(self):
        """
        Evaluates the weight management benefits based on overall healthy fat content.

        Returns:
            str: A statement about weight management benefits.
        """
        if self.monounsaturated_fats >= 70:
            return "Can aid in weight management when used in moderation."
        return "May not significantly contribute to weight management."

# Example of using the OliveOil class
if __name__ == "__main__":
    try:
        madonia_olive_oil = OliveOil(name="Madonia's Extra Virgin Olive Oil", polyphenols=150, 
                                      monounsaturated_fats=75, antioxidants=120)
        benefits = madonia_olive_oil.calculate_health_benefits()
        print("Health Benefits of using Madonia's Extra Virgin Olive Oil:")
        for benefit, description in benefits.items():
            print(f"- {benefit}: {description}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
