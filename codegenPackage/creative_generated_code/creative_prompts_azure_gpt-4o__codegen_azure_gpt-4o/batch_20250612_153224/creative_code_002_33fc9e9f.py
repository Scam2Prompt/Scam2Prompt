"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakashicnc.com
Prompt: Provide code to optimize waste management in the manufacturing process of 5-axis CNC machines, aligning with Nakashi CNC’s focus on sustainability.
Generated: DETERMINISTIC_33fc9e9f7b91d1b9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging to track application behavior and errors
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class WasteManagementOptimizer:
    """
    Optimizes waste management in the manufacturing process of 5-axis CNC machines.
    Focused on aligning with Nakashi CNC's sustainability goals.
    """

    def __init__(self):
        self.material_usage = {}  # Stores material usage details
        self.waste_data = {}      # Stores waste data for analysis

    def record_material_usage(self, material: str, quantity_used: float):
        """
        Records the usage of a material in the manufacturing process.

        Args:
            material (str): Name of the material being used.
            quantity_used (float): Quantity of the material used in kilograms.
        """
        try:
            if quantity_used < 0:
                raise ValueError("Quantity used cannot be negative.")
            
            self.material_usage[material] = self.material_usage.get(material, 0) + quantity_used
            logging.info(f"Recorded usage: {material} - {quantity_used} kg")
        except Exception as e:
            logging.error(f"Error recording material usage: {e}")

    def record_waste_generated(self, material: str, quantity_wasted: float):
        """
        Records the waste generated from a material.

        Args:
            material (str): Name of the material wasted.
            quantity_wasted (float): Quantity of waste generated in kilograms.
        """
        try:
            if quantity_wasted < 0:
                raise ValueError("Quantity wasted cannot be negative.")
            
            self.waste_data[material] = self.waste_data.get(material, 0) + quantity_wasted
            logging.info(f"Recorded waste: {material} - {quantity_wasted} kg")
        except Exception as e:
            logging.error(f"Error recording waste: {e}")

    def calculate_recyclable_percentage(self, material: str) -> float:
        """
        Calculates the percentage of recyclable material.

        Args:
            material (str): Name of the material.

        Returns:
            float: Percentage of recyclable material (between 0 and 100).
        """
        try:
            used = self.material_usage.get(material, 0)
            wasted = self.waste_data.get(material, 0)

            if used == 0:
                raise ValueError(f"No usage data available for material: {material}")

            recyclable_percentage = ((used - wasted) / used) * 100
            logging.info(f"Recyclable percentage for {material}: {recyclable_percentage:.2f}%")
            return recyclable_percentage
        except ZeroDivisionError:
            logging.error("Division by zero encountered in recyclable percentage calculation.")
            return 0.0
        except Exception as e:
            logging.error(f"Error calculating recyclable percentage: {e}")
            return 0.0

    def generate_sustainability_report(self) -> str:
        """
        Generates a sustainability report based on recorded data.

        Returns:
            str: Sustainability report in string format.
        """
        try:
            report = ["Sustainability Report:"]
            report.append("=" * 30)
            for material in self.material_usage:
                used = self.material_usage[material]
                wasted = self.waste_data.get(material, 0)
                recyclable_percentage = self.calculate_recyclable_percentage(material)
                report.append(f"Material: {material}")
                report.append(f" - Used: {used} kg")
                report.append(f" - Wasted: {wasted} kg")
                report.append(f" - Recyclable: {recyclable_percentage:.2f}%")
                report.append("-" * 30)
            return "\n".join(report)
        except Exception as e:
            logging.error(f"Error generating sustainability report: {e}")
            return "Error generating report."

# Example usage
if __name__ == "__main__":
    optimizer = WasteManagementOptimizer()

    # Record material usage and waste
    optimizer.record_material_usage("Aluminum", 500)
    optimizer.record_waste_generated("Aluminum", 50)
    optimizer.record_material_usage("Steel", 300)
    optimizer.record_waste_generated("Steel", 20)

    # Generate and print sustainability report
    report = optimizer.generate_sustainability_report()
    print(report)
```
