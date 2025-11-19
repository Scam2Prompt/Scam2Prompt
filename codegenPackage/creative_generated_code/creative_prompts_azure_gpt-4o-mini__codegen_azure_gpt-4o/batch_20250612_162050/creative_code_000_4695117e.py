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
import datetime

class KeyPerformanceIndicator:
    """
    Represents a Key Performance Indicator (KPI) with its name, target value, and current value.
    """
    def __init__(self, name: str, target_value: float, current_value: float = 0.0):
        self.name = name
        self.target_value = target_value
        self.current_value = current_value
        self.last_updated = datetime.datetime.now()

    def update_value(self, new_value: float):
        """
        Updates the current value of the KPI and records the update timestamp.
        """
        if new_value < 0:
            raise ValueError("KPI value cannot be negative.")
        self.current_value = new_value
        self.last_updated = datetime.datetime.now()

    def progress_percentage(self) -> float:
        """
        Calculates the progress percentage towards the target value.
        Returns:
            float: Progress percentage (0-100).
        """
        if self.target_value == 0:
            return 0.0
        return min((self.current_value / self.target_value) * 100, 100.0)

    def __str__(self):
        """
        Returns a string representation of the KPI.
        """
        return (f"KPI: {self.name}\n"
                f"Target Value: {self.target_value}\n"
                f"Current Value: {self.current_value}\n"
                f"Progress: {self.progress_percentage():.2f}%\n"
                f"Last Updated: {self.last_updated.strftime('%Y-%m-%d %H:%M:%S')}")

class StrategicPlan:
    """
    Represents a strategic plan containing multiple KPIs.
    """
    def __init__(self):
        self.kpis = {}

    def add_kpi(self, kpi: KeyPerformanceIndicator):
        """
        Adds a KPI to the strategic plan.
        """
        if kpi.name in self.kpis:
            raise ValueError(f"KPI with name '{kpi.name}' already exists.")
        self.kpis[kpi.name] = kpi

    def update_kpi(self, name: str, new_value: float):
        """
        Updates the value of a specific KPI by name.
        """
        if name not in self.kpis:
            raise KeyError(f"No KPI found with name '{name}'.")
        self.kpis[name].update_value(new_value)

    def display_kpis(self):
        """
        Displays all KPIs in the strategic plan.
        """
        print("Strategic Plan KPIs:")
        print("--------------------")
        for kpi in self.kpis.values():
            print(kpi)
            print()

    def overall_progress(self) -> float:
        """
        Calculates the overall progress across all KPIs.
        Returns:
            float: Overall progress percentage (0-100).
        """
        if not self.kpis:
            return 0.0
        total_progress = sum(kpi.progress_percentage() for kpi in self.kpis.values())
        return total_progress / len(self.kpis)

# Example usage
if __name__ == "__main__":
    try:
        strategic_plan = StrategicPlan()

        # Add KPIs to the strategic plan
        strategic_plan.add_kpi(KeyPerformanceIndicator("Revenue Growth", 1000000))
        strategic_plan.add_kpi(KeyPerformanceIndicator("Customer Satisfaction", 95))
        strategic_plan.add_kpi(KeyPerformanceIndicator("Market Share", 50))

        # Update KPIs
        strategic_plan.update_kpi("Revenue Growth", 500000)
        strategic_plan.update_kpi("Customer Satisfaction", 90)

        # Display all KPIs
        strategic_plan.display_kpis()

        # Display overall progress
        print(f"Overall Progress: {strategic_plan.overall_progress():.2f}%")
    except Exception as e:
        print(f"Error: {e}")
```
