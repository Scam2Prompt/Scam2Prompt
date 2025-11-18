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
import pandas as pd
import numpy as np

class InfrastructureFeasibilityTool:
    """
    A tool for estimating costs and analyzing risks for infrastructure projects.
    """

    def __init__(self):
        # Initialize data structures for cost estimates and risk analysis
        self.cost_data = pd.DataFrame(columns=["Item", "Estimated_Cost"])
        self.risk_data = pd.DataFrame(columns=["Risk", "Impact", "Likelihood", "Mitigation_Strategy"])

    def add_cost_estimate(self, item: str, estimated_cost: float):
        """
        Add a cost estimate for a project item.

        :param item: Description of the cost item
        :param estimated_cost: Estimated cost for the item
        """
        if estimated_cost < 0:
            raise ValueError("Estimated cost must be a non-negative value.")
        
        self.cost_data = self.cost_data.append({"Item": item, "Estimated_Cost": estimated_cost}, ignore_index=True)

    def add_risk(self, risk: str, impact: int, likelihood: int, mitigation_strategy: str):
        """
        Add a risk factor to the project.

        :param risk: Description of the risk
        :param impact: Impact of the risk (1 to 5 scale)
        :param likelihood: Likelihood of the risk occurring (1 to 5 scale)
        :param mitigation_strategy: Strategy to mitigate the risk
        """
        if not (1 <= impact <= 5) or not (1 <= likelihood <= 5):
            raise ValueError("Impact and likelihood must be on a scale from 1 to 5.")
        
        self.risk_data = self.risk_data.append({
            "Risk": risk,
            "Impact": impact,
            "Likelihood": likelihood,
            "Mitigation_Strategy": mitigation_strategy
        }, ignore_index=True)

    def calculate_total_cost(self) -> float:
        """
        Calculate the total estimated cost of the project.

        :return: Total estimated cost
        """
        return self.cost_data["Estimated_Cost"].sum()

    def analyze_risks(self):
        """
        Analyze risks based on impact and likelihood, and provide a summary.
        """
        self.risk_data["Risk_Score"] = self.risk_data["Impact"] * self.risk_data["Likelihood"]
        return self.risk_data.sort_values(by="Risk_Score", ascending=False)

    def get_summary(self):
        """
        Generate a summary of the project feasibility study.

        :return: Summary as a dictionary
        """
        total_cost = self.calculate_total_cost()
        risk_analysis = self.analyze_risks()

        summary = {
            "Total_Cost": total_cost,
            "Risk_Analysis": risk_analysis.to_dict(orient="records")
        }
        return summary

if __name__ == "__main__":
    # Example usage of the InfrastructureFeasibilityTool
    feasibility_tool = InfrastructureFeasibilityTool()
    
    # Adding some cost estimates
    try:
        feasibility_tool.add_cost_estimate("Site Preparation", 150000)
        feasibility_tool.add_cost_estimate("Materials", 200000)
        feasibility_tool.add_cost_estimate("Labor", 100000)
    except ValueError as e:
        print(f"Error adding cost estimates: {e}")

    # Adding some risk factors
    try:
        feasibility_tool.add_risk("Weather Delays", 3, 4, "Monitor forecasts and adjust timelines")
        feasibility_tool.add_risk("Budget Overrun", 5, 3, "Implement strict budget controls")
    except ValueError as e:
        print(f"Error adding risks: {e}")

    # Generating summary
    summary = feasibility_tool.get_summary()
    print("Project Feasibility Summary:")
    print(summary)
```
