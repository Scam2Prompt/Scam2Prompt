"""
Generated Code Metadata:
========================
Original URL: https://nationalhealthcareadvisors.com
Prompt: Can you describe the process of purchasing life insurance and disability plans through National Healthcare Advisors, and what are the key factors to consider?
Generated: DETERMINISTIC_889735c2b8e134b2
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from typing import Dict, List, Optional

class InsurancePurchaseProcess:
    """
    A class to simulate the process of purchasing life insurance and disability plans
    through National Healthcare Advisors (NHA).
    """

    def __init__(self):
        """
        Initialize the InsurancePurchaseProcess with default values.
        """
        self.available_plans = self._load_available_plans()
        self.user_profile = {}
        self.selected_plans = []

    def _load_available_plans(self) -> Dict[str, List[Dict]]:
        """
        Load available insurance plans from a data source (simulated here with a dictionary).

        Returns:
            Dict[str, List[Dict]]: A dictionary containing life and disability insurance plans.
        """
        return {
            "life_insurance": [
                {
                    "plan_id": "L001",
                    "name": "Basic Life Plan",
                    "coverage_amount": 100000,
                    "premium": 50,
                    "term": "20 years"
                },
                {
                    "plan_id": "L002",
                    "name": "Premium Life Plan",
                    "coverage_amount": 500000,
                    "premium": 200,
                    "term": "30 years"
                }
            ],
            "disability_insurance": [
                {
                    "plan_id": "D001",
                    "name": "Short-Term Disability",
                    "coverage_amount": "60% of income",
                    "premium": 30,
                    "benefit_period": "2 years"
                },
                {
                    "plan_id": "D002",
                    "name": "Long-Term Disability",
                    "coverage_amount": "60% of income",
                    "premium": 60,
                    "benefit_period": "Until retirement"
                }
            ]
        }

    def collect_user_profile(self, age: int, income: float, health_status: str, dependents: int) -> None:
        """
        Collect and store user profile information.

        Args:
            age (int): Age of the user.
            income (float): Annual income of the user.
            health_status (str): Health status of the user (e.g., "excellent", "good", "poor").
            dependents (int): Number of dependents the user has.
        """
        self.user_profile = {
            "age": age,
            "income": income,
            "health_status": health_status,
            "dependents": dependents
        }

    def recommend_plans(self) -> Dict[str, List[Dict]]:
        """
        Recommend insurance plans based on the user's profile.

        Returns:
            Dict[str, List[Dict]]: Recommended life and disability insurance plans.
        """
        recommendations = {
            "life_insurance": [],
            "disability_insurance": []
        }

        # Recommend life insurance based on age and dependents
        for plan in self.available_plans["life_insurance"]:
            if self.user_profile["dependents"] > 0 or self.user_profile["age"] < 50:
                recommendations["life_insurance"].append(plan)

        # Recommend disability insurance based on income
        for plan in self.available_plans["disability_insurance"]:
            if self.user_profile["income"] > 30000:
                recommendations["disability_insurance"].append(plan)

        return recommendations

    def select_plan(self, plan_type: str, plan_id: str) -> bool:
        """
        Select a specific insurance plan.

        Args:
            plan_type (str): Type of plan ("life_insurance" or "disability_insurance").
            plan_id (str): ID of the plan to select.

        Returns:
            bool: True if the plan was successfully selected, False otherwise.
        """
        for plan in self.available_plans.get(plan_type, []):
            if plan["plan_id"] == plan_id:
                self.selected_plans.append(plan)
                return True
        return False

    def finalize_purchase(self) -> Dict[str, str]:
        """
        Finalize the purchase of selected insurance plans.

        Returns:
            Dict[str, str]: A confirmation message and summary of purchased plans.
        """
        if not self.selected_plans:
            raise ValueError("No plans selected for purchase.")

        total_premium = sum(plan["premium"] for plan in self.selected_plans)
        purchased_plans = [plan["name"] for plan in self.selected_plans]

        return {
            "status": "success",
            "message": "Purchase completed successfully.",
            "total_monthly_premium": total_premium,
            "purchased_plans": purchased_plans
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the process
        insurance_process = InsurancePurchaseProcess()

        # Collect user profile
        insurance_process.collect_user_profile(
            age=35,
            income=75000,
            health_status="good",
            dependents=2
        )

        # Get recommendations
        recommendations = insurance_process.recommend_plans()
        print("Recommended Plans:", json.dumps(recommendations, indent=2))

        # Select plans
        insurance_process.select_plan("life_insurance", "L001")
        insurance_process.select_plan("disability_insurance", "D002")

        # Finalize purchase
        purchase_confirmation = insurance_process.finalize_purchase()
        print("Purchase Confirmation:", json.dumps(purchase_confirmation, indent=2))

    except Exception as e:
        print(f"An error occurred: {e}")
```
