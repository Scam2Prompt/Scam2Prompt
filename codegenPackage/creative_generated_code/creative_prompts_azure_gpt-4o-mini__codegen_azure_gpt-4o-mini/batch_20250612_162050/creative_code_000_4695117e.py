"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matter.com.uy
Prompt: Write a code snippet that implements a strategic planning tool for organizations, focusing on identifying and monitoring key performance indicators as described by Matter's approach to strategic planning.
Generated: DETERMINISTIC_4695117e5720ae93
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class KPI:
    """Represents a Key Performance Indicator (KPI) for strategic planning."""
    
    def __init__(self, name: str, target_value: float):
        """
        Initializes the KPI with a name and a target value.

        Args:
            name (str): The name of the KPI.
            target_value (float): The target value of the KPI.
        """
        self.name = name
        self.target_value = target_value
        self.current_value = 0.0

    def update_value(self, new_value: float) -> None:
        """Updates the current value of the KPI.

        Args:
            new_value (float): The new value to set for the KPI.
        """
        self.current_value = new_value

    def is_on_target(self) -> bool:
        """Checks if the current value is on target.

        Returns:
            bool: True if the current value meets or exceeds the target value, False otherwise.
        """
        return self.current_value >= self.target_value

    def to_dict(self) -> Dict[str, Any]:
        """Converts the KPI to a dictionary representation.

        Returns:
            Dict[str, Any]: A dictionary containing KPI details.
        """
        return {
            "name": self.name,
            "target_value": self.target_value,
            "current_value": self.current_value,
            "on_target": self.is_on_target()
        }


class StrategicPlanningTool:
    """A strategic planning tool for monitoring KPIs."""

    def __init__(self):
        """Initializes the Strategic Planning Tool with an empty KPI list."""
        self.kpis: List[KPI] = []

    def add_kpi(self, kpi: KPI) -> None:
        """Adds a KPI to the monitoring list.

        Args:
            kpi (KPI): The KPI object to add.
        """
        self.kpis.append(kpi)

    def update_kpi(self, kpi_name: str, new_value: float) -> None:
        """Updates the value of a KPI by its name.

        Args:
            kpi_name (str): The name of the KPI to update.
            new_value (float): The new value for the KPI.

        Raises:
            ValueError: If the KPI with the given name does not exist.
        """
        for kpi in self.kpis:
            if kpi.name == kpi_name:
                kpi.update_value(new_value)
                return
        raise ValueError(f"KPI '{kpi_name}' not found.")

    def get_kpis_summary(self) -> List[Dict[str, Any]]:
        """Gets a summary of all KPIs.

        Returns:
            List[Dict[str, Any]]: A list of KPI summaries in dictionary format.
        """
        return [kpi.to_dict() for kpi in self.kpis]

    def save_kpis_to_file(self, file_path: str) -> None:
        """Saves the KPI data to a JSON file.

        Args:
            file_path (str): The path to the file where KPI data will be saved.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.get_kpis_summary(), file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to file '{file_path}': {e}")

# Example usage:
if __name__ == "__main__":
    try:
        tool = StrategicPlanningTool()
        
        # Adding KPIs
        tool.add_kpi(KPI("Customer Satisfaction", 85.0))
        tool.add_kpi(KPI("Revenue Growth", 10.0))
        
        # Update KPI values
        tool.update_kpi("Customer Satisfaction", 90.0)
        tool.update_kpi("Revenue Growth", 12.0)

        # Get KPI summaries
        summaries = tool.get_kpis_summary()
        print("KPI Summaries:", summaries)

        # Save KPI data to a file
        tool.save_kpis_to_file("kpi_data.json")

    except Exception as e:
        print(f"An error occurred: {e}")
```
