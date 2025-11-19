"""
Generated Code Metadata:
========================
Original URL: https://lexuscertifications.com
Prompt: "Write a Python script to create a simple HACCP (Hazard Analysis and Critical Control Points) plan for a food safety management system."
Generated: DETERMINISTIC_bb874b3295829c12
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class HACCPPlan:
    def __init__(self, plan_name: str):
        """
        Initialize the HACCP plan with a name and an empty list of critical control points (CCPs).
        
        :param plan_name: The name of the HACCP plan.
        """
        self.plan_name = plan_name
        self.ccps: List[Dict] = []

    def add_ccp(self, ccp_name: str, hazard: str, critical_limit: str, monitoring: str, corrective_action: str):
        """
        Add a critical control point (CCP) to the HACCP plan.
        
        :param ccp_name: The name of the critical control point.
        :param hazard: The identified hazard at this CCP.
        :param critical_limit: The critical limit for the CCP.
        :param monitoring: The monitoring procedures for the CCP.
        :param corrective_action: The corrective actions to be taken if the critical limit is not met.
        """
        ccp = {
            "ccp_name": ccp_name,
            "hazard": hazard,
            "critical_limit": critical_limit,
            "monitoring": monitoring,
            "corrective_action": corrective_action
        }
        self.ccps.append(ccp)

    def save_to_file(self, filename: str):
        """
        Save the HACCP plan to a JSON file.
        
        :param filename: The name of the file to save the HACCP plan.
        """
        try:
            with open(filename, 'w') as file:
                json.dump({"plan_name": self.plan_name, "ccps": self.ccps}, file, indent=4)
            print(f"HACCP plan saved to {filename}")
        except IOError as e:
            print(f"Error saving HACCP plan to file: {e}")

    def load_from_file(self, filename: str):
        """
        Load a HACCP plan from a JSON file.
        
        :param filename: The name of the file to load the HACCP plan from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.plan_name = data.get("plan_name", self.plan_name)
                self.ccps = data.get("ccps", [])
            print(f"HACCP plan loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading HACCP plan from file: {e}")

    def display_plan(self):
        """
        Display the HACCP plan details.
        """
        print(f"HACCP Plan: {self.plan_name}")
        for ccp in self.ccps:
            print(f"CCP Name: {ccp['ccp_name']}")
            print(f"  Hazard: {ccp['hazard']}")
            print(f"  Critical Limit: {ccp['critical_limit']}")
            print(f"  Monitoring: {ccp['monitoring']}")
            print(f"  Corrective Action: {ccp['corrective_action']}")
            print("-" * 40)

if __name__ == "__main__":
    # Example usage of the HACCPPlan class
    haccp_plan = HACCPPlan("Sample HACCP Plan")
    
    # Adding critical control points
    haccp_plan.add_ccp(
        ccp_name="Cooking",
        hazard="Undercooked meat",
        critical_limit="Internal temperature of 165°F",
        monitoring="Use a food thermometer",
        corrective_action="Continue cooking until the critical limit is met"
    )
    
    haccp_plan.add_ccp(
        ccp_name="Cooling",
        hazard="Bacterial growth",
        critical_limit="Cool to 70°F within 2 hours",
        monitoring="Check temperature every 30 minutes",
        corrective_action="Reheat to 165°F and cool again"
    )
    
    # Display the plan
    haccp_plan.display_plan()
    
    # Save the plan to a file
    haccp_plan.save_to_file("haccp_plan.json")
    
    # Load the plan from a file
    haccp_plan.load_from_file("haccp_plan.json")
```
