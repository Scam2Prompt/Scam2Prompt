"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: Write a code snippet that implements a strategic planning tool for organizations, focusing on identifying and monitoring key performance indicators as described by Matter's approach to strategic planning.
Generated: DETERMINISTIC_4695117e5720ae93
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class KPI:
    """
    A class to represent a Key Performance Indicator (KPI).
    """

    def __init__(self, name: str, target: float, current_value: float):
        """
        Initializes a KPI instance.

        :param name: The name of the KPI.
        :param target: The target value for the KPI.
        :param current_value: The current value of the KPI.
        """
        self.name = name
        self.target = target
        self.current_value = current_value

    def is_on_target(self) -> bool:
        """
        Checks if the current value meets or exceeds the target.

        :return: True if on target, False otherwise.
        """
        return self.current_value >= self.target

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the KPI instance to a dictionary.

        :return: A dictionary representation of the KPI.
        """
        return {
            "name": self.name,
            "target": self.target,
            "current_value": self.current_value,
            "on_target": self.is_on_target()
        }


class StrategicPlanningTool:
    """
    A class to manage strategic planning and KPI monitoring.
    """

    def __init__(self):
        """
        Initializes the Strategic Planning Tool with an empty KPI list.
        """
        self.kpis: List[KPI] = []

    def add_kpi(self, name: str, target: float, current_value: float):
        """
        Adds a new KPI to the tool.

        :param name: The name of the KPI.
        :param target: The target value for the KPI.
        :param current_value: The current value of the KPI.
        """
        kpi = KPI(name, target, current_value)
        self.kpis.append(kpi)

    def get_kpis(self) -> List[Dict[str, Any]]:
        """
        Retrieves all KPIs in a dictionary format.

        :return: A list of dictionaries representing the KPIs.
        """
        return [kpi.to_dict() for kpi in self.kpis]

    def save_to_file(self, filename: str):
        """
        Saves the current KPIs to a JSON file.

        :param filename: The name of the file to save the KPIs.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_kpis(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str):
        """
        Loads KPIs from a JSON file.

        :param filename: The name of the file to load the KPIs from.
        """
        try:
            with open(filename, 'r') as file:
                kpi_data = json.load(file)
                for item in kpi_data:
                    self.add_kpi(item['name'], item['target'], item['current_value'])
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")


# Example usage
if __name__ == "__main__":
    tool = StrategicPlanningTool()
    tool.add_kpi("Customer Satisfaction", 90.0, 85.0)
    tool.add_kpi("Revenue Growth", 10.0, 12.0)

    print("Current KPIs:")
    print(tool.get_kpis())

    # Save KPIs to a file
    tool.save_to_file("kpis.json")

    # Load KPIs from a file
    new_tool = StrategicPlanningTool()
    new_tool.load_from_file("kpis.json")
    print("Loaded KPIs:")
    print(new_tool.get_kpis())
```
