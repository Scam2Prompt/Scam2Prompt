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
from datetime import datetime
from typing import List, Dict, Optional

class HACCPPlan:
    """
    A class to represent a HACCP (Hazard Analysis and Critical Control Points) plan.
    This plan helps in identifying, evaluating, and controlling hazards in food production.
    """

    def __init__(self, product_name: str, company_name: str, version: str = "1.0"):
        """
        Initialize the HACCP plan with basic information.

        Args:
            product_name (str): Name of the product.
            company_name (str): Name of the company.
            version (str, optional): Version of the HACCP plan. Defaults to "1.0".
        """
        self.product_name = product_name
        self.company_name = company_name
        self.version = version
        self.creation_date = datetime.now().strftime("%Y-%m-%d")
        self.hazards: List[Dict] = []
        self.ccps: List[Dict] = []

    def add_hazard(self, process_step: str, hazard: str, control_measure: str) -> None:
        """
        Add a hazard to the HACCP plan.

        Args:
            process_step (str): The step in the process where the hazard occurs.
            hazard (str): Description of the hazard.
            control_measure (str): Measure to control the hazard.
        """
        if not all([process_step, hazard, control_measure]):
            raise ValueError("Process step, hazard, and control measure must be provided.")

        self.hazards.append({
            "process_step": process_step,
            "hazard": hazard,
            "control_measure": control_measure
        })

    def add_ccp(self, process_step: str, critical_limit: str, monitoring_procedure: str, corrective_action: str) -> None:
        """
        Add a Critical Control Point (CCP) to the HACCP plan.

        Args:
            process_step (str): The step in the process identified as a CCP.
            critical_limit (str): The critical limit for the CCP.
            monitoring_procedure (str): Procedure to monitor the CCP.
            corrective_action (str): Action to take if the limit is exceeded.
        """
        if not all([process_step, critical_limit, monitoring_procedure, corrective_action]):
            raise ValueError("All CCP fields must be provided.")

        self.ccps.append({
            "process_step": process_step,
            "critical_limit": critical_limit,
            "monitoring_procedure": monitoring_procedure,
            "corrective_action": corrective_action
        })

    def to_json(self, file_path: Optional[str] = None) -> str:
        """
        Convert the HACCP plan to a JSON string or save it to a file.

        Args:
            file_path (str, optional): Path to save the JSON file. If None, returns the JSON string.

        Returns:
            str: JSON string if file_path is None, otherwise None.
        """
        plan_data = {
            "product_name": self.product_name,
            "company_name": self.company_name,
            "version": self.version,
            "creation_date": self.creation_date,
            "hazards": self.hazards,
            "critical_control_points": self.ccps
        }

        json_data = json.dumps(plan_data, indent=4)

        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write(json_data)
            except IOError as e:
                raise IOError(f"Failed to save HACCP plan to file: {e}")
        else:
            return json_data

    @classmethod
    def from_json(cls, file_path: str) -> 'HACCPPlan':
        """
        Load a HACCP plan from a JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            HACCPPlan: An instance of HACCPPlan loaded from the file.
        """
        try:
            with open(file_path, 'r') as f:
                plan_data = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load HACCP plan from file: {e}")

        plan = cls(
            product_name=plan_data["product_name"],
            company_name=plan_data["company_name"],
            version=plan_data.get("version", "1.0")
        )
        plan.creation_date = plan_data.get("creation_date", datetime.now().strftime("%Y-%m-%d"))
        plan.hazards = plan_data.get("hazards", [])
        plan.ccps = plan_data.get("critical_control_points", [])

        return plan

# Example usage
if __name__ == "__main__":
    try:
        # Create a new HACCP plan
        plan = HACCPPlan(
            product_name="Frozen Pizza",
            company_name="FoodSafe Inc.",
            version="1.0"
        )

        # Add hazards
        plan.add_hazard(
            process_step="Dough Preparation",
            hazard="Microbial contamination",
            control_measure="Use sanitized equipment and ingredients"
        )

        plan.add_hazard(
            process_step="Baking",
            hazard="Insufficient temperature",
            control_measure="Monitor oven temperature"
        )

        # Add CCPs
        plan.add_ccp(
            process_step="Baking",
            critical_limit="Minimum 165°F internal temperature",
            monitoring_procedure="Use calibrated thermometer",
            corrective_action="Extend baking time or adjust temperature"
        )

        # Save to file
        plan.to_json("haccp_plan.json")
        print("HACCP plan created and saved successfully.")

        # Load from file (example)
        # loaded_plan = HACCPPlan.from_json("haccp_plan.json")
        # print(loaded_plan.to_json())

    except Exception as e:
        print(f"Error: {e}")
```
