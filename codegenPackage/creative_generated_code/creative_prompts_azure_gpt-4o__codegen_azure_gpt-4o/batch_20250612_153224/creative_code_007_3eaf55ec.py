"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Develop a tool to assist in infrastructure project feasibility studies, including cost estimation and risk analysis, inspired by Unison Plus's consulting services.
Generated: DETERMINISTIC_3eaf55ece330d678
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InfrastructureFeasibilityTool:
    """
    A tool to assist in infrastructure project feasibility studies, including cost estimation
    and risk analysis. Inspired by Unison Plus's consulting services.
    """

    def __init__(self):
        """
        Initialize the tool with predefined cost categories and risk factors.
        """
        self.cost_categories = {
            "material_cost": 0.0,
            "labor_cost": 0.0,
            "equipment_cost": 0.0,
            "contingency_cost": 0.0,
            "total_cost": 0.0
        }
        self.risk_factors = {
            "low": 1.0,
            "medium": 1.2,
            "high": 1.5
        }
    
    def estimate_cost(self, material_cost, labor_cost, equipment_cost, contingency_percentage):
        """
        Estimate the total cost of the project.

        Args:
            material_cost (float): Cost of materials.
            labor_cost (float): Cost of labor.
            equipment_cost (float): Cost of equipment.
            contingency_percentage (float): Percentage to account for unforeseen expenses.

        Returns:
            float: Estimated total cost of the project.
        """
        try:
            self.cost_categories["material_cost"] = material_cost
            self.cost_categories["labor_cost"] = labor_cost
            self.cost_categories["equipment_cost"] = equipment_cost
            self.cost_categories["contingency_cost"] = (
                contingency_percentage / 100 * (material_cost + labor_cost + equipment_cost)
            )
            self.cost_categories["total_cost"] = (
                material_cost + labor_cost + equipment_cost + self.cost_categories["contingency_cost"]
            )
            return self.cost_categories["total_cost"]
        except TypeError as e:
            print(f"Error estimating cost: {e}")
            return None

    def analyze_risk(self, risk_level):
        """
        Analyze and adjust the project cost based on risk level.

        Args:
            risk_level (str): Risk level of the project ("low", "medium", "high").

        Returns:
            float: Adjusted project cost based on risk level.
        """
        try:
            if risk_level not in self.risk_factors:
                raise ValueError(f"Invalid risk level: {risk_level}. Allowed values are 'low', 'medium', 'high'.")
            risk_multiplier = self.risk_factors[risk_level]
            adjusted_cost = self.cost_categories["total_cost"] * risk_multiplier
            return adjusted_cost
        except ValueError as e:
            print(e)
            return None

    def generate_report(self):
        """
        Generate a JSON report of the cost breakdown and risk analysis.

        Returns:
            str: JSON string representing the project report.
        """
        try:
            report = {
                "cost_breakdown": self.cost_categories,
                "risk_levels": self.risk_factors
            }
            return json.dumps(report, indent=4)
        except Exception as e:
            print(f"Error generating report: {e}")
            return None


# Example usage
if __name__ == "__main__":
    tool = InfrastructureFeasibilityTool()

    # Set initial cost values and calculate total cost
    material_cost = 50000.0
    labor_cost = 30000.0
    equipment_cost = 20000.0
    contingency_percentage = 10.0

    total_cost = tool.estimate_cost(material_cost, labor_cost, equipment_cost, contingency_percentage)
    print(f"Estimated Total Cost: ${total_cost:.2f}")

    # Perform risk analysis
    risk_level = "medium"
    adjusted_cost = tool.analyze_risk(risk_level)
    print(f"Adjusted Cost (Risk Level - {risk_level}): ${adjusted_cost:.2f}")

    # Generate feasibility report
    report = tool.generate_report()
    print("Feasibility Report:")
    print(report)
```
