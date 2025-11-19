"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Illustrate how to implement a product comparison feature for Shelter's Electric Fireplaces using LED 3D technology versus traditional models.
Generated: DETERMINISTIC_60bf7f436c5cb425
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# product_comparison.py

class ElectricFireplace:
    """
    Represents an electric fireplace with certain features.
    """
    
    def __init__(self, model_name, led_3d: bool, price: float, heat_output: int):
        """
        Initializes an instance of ElectricFireplace.

        :param model_name: str - The name of the fireplace model
        :param led_3d: bool - Indicates if the model uses LED 3D technology
        :param price: float - The price of the fireplace
        :param heat_output: int - The heat output of the fireplace in BTUs
        """
        self.model_name = model_name
        self.led_3d = led_3d
        self.price = price
        self.heat_output = heat_output

    def __str__(self):
        """
        Returns a string representation of the electric fireplace.
        """
        return f"{self.model_name} - LED 3D: {self.led_3d}, Price: ${self.price:.2f}, Heat Output: {self.heat_output} BTUs"

def compare_fireplaces(fireplace1: ElectricFireplace, fireplace2: ElectricFireplace):
    """
    Compares two electric fireplaces and returns a comparison summary.

    :param fireplace1: ElectricFireplace - The first fireplace to compare
    :param fireplace2: ElectricFireplace - The second fireplace to compare
    :return: str - A summary of the comparison
    """
    comparison_summary = f"Comparing {fireplace1.model_name} and {fireplace2.model_name}:\n"
    
    # Compare price
    if fireplace1.price < fireplace2.price:
        comparison_summary += f"{fireplace1.model_name} is cheaper than {fireplace2.model_name}.\n"
    elif fireplace1.price > fireplace2.price:
        comparison_summary += f"{fireplace2.model_name} is cheaper than {fireplace1.model_name}.\n"
    else:
        comparison_summary += f"Both models have the same price.\n"

    # Compare heat output
    if fireplace1.heat_output > fireplace2.heat_output:
        comparison_summary += f"{fireplace1.model_name} has higher heat output.\n"
    elif fireplace1.heat_output < fireplace2.heat_output:
        comparison_summary += f"{fireplace2.model_name} has higher heat output.\n"
    else:
        comparison_summary += "Both models have the same heat output.\n"

    # Compare technology
    if fireplace1.led_3d and not fireplace2.led_3d:
        comparison_summary += f"{fireplace1.model_name} features LED 3D technology, while {fireplace2.model_name} does not.\n"
    elif not fireplace1.led_3d and fireplace2.led_3d:
        comparison_summary += f"{fireplace2.model_name} features LED 3D technology, while {fireplace1.model_name} does not.\n"
    else:
        comparison_summary += "Both models use the same LED technology.\n"

    return comparison_summary

def main():
    """
    Main function to create fireplace instances and compare them.
    """
    try:
        # Example electric fireplaces
        fireplace_1 = ElectricFireplace("Shelter LED 3D Model A", True, 899.99, 5000)
        fireplace_2 = ElectricFireplace("Shelter Traditional Model B", False, 699.99, 4500)

        # Perform comparison
        result = compare_fireplaces(fireplace_1, fireplace_2)
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
