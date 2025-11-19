"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: Write Python code to calculate the cost of installing raised access flooring in a data center, using specifications for calcium sulphate panels and accessories like panel lifters and airflow panels.
Generated: DETERMINISTIC_87217e4c6552ca2a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# raised_access_flooring_calculator.py

class RaisedAccessFlooringCalculator:
    def __init__(self, 
                 panel_cost_per_sqm, 
                 panel_lifter_cost, 
                 airflow_panel_cost, 
                 installation_labor_cost_per_sqm, 
                 area_sqm):
        """
        Initialize the calculator with costs and area.

        Args:
        - panel_cost_per_sqm (float): Cost of calcium sulphate panel per square meter.
        - panel_lifter_cost (float): Cost of panel lifter.
        - airflow_panel_cost (float): Cost of airflow panel.
        - installation_labor_cost_per_sqm (float): Installation labor cost per square meter.
        - area_sqm (float): Area of the data center in square meters.
        """
        self.panel_cost_per_sqm = panel_cost_per_sqm
        self.panel_lifter_cost = panel_lifter_cost
        self.airflow_panel_cost = airflow_panel_cost
        self.installation_labor_cost_per_sqm = installation_labor_cost_per_sqm
        self.area_sqm = area_sqm

    def calculate_panel_cost(self):
        """
        Calculate the total cost of calcium sulphate panels.

        Returns:
        - float: Total cost of panels.
        """
        return self.panel_cost_per_sqm * self.area_sqm

    def calculate_accessories_cost(self, num_panel_lifters, num_airflow_panels):
        """
        Calculate the total cost of accessories.

        Args:
        - num_panel_lifters (int): Number of panel lifters.
        - num_airflow_panels (int): Number of airflow panels.

        Returns:
        - float: Total cost of accessories.
        """
        return (self.panel_lifter_cost * num_panel_lifters) + (self.airflow_panel_cost * num_airflow_panels)

    def calculate_installation_labor_cost(self):
        """
        Calculate the total installation labor cost.

        Returns:
        - float: Total installation labor cost.
        """
        return self.installation_labor_cost_per_sqm * self.area_sqm

    def calculate_total_cost(self, num_panel_lifters, num_airflow_panels):
        """
        Calculate the total cost of installing raised access flooring.

        Args:
        - num_panel_lifters (int): Number of panel lifters.
        - num_airflow_panels (int): Number of airflow panels.

        Returns:
        - float: Total cost of installation.
        """
        panel_cost = self.calculate_panel_cost()
        accessories_cost = self.calculate_accessories_cost(num_panel_lifters, num_airflow_panels)
        installation_labor_cost = self.calculate_installation_labor_cost()
        return panel_cost + accessories_cost + installation_labor_cost


def main():
    try:
        # Example usage
        calculator = RaisedAccessFlooringCalculator(
            panel_cost_per_sqm=100.0,
            panel_lifter_cost=5000.0,
            airflow_panel_cost=200.0,
            installation_labor_cost_per_sqm=50.0,
            area_sqm=1000.0
        )

        num_panel_lifters = 2
        num_airflow_panels = 10

        total_cost = calculator.calculate_total_cost(num_panel_lifters, num_airflow_panels)

        print(f"Total cost of installation: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
