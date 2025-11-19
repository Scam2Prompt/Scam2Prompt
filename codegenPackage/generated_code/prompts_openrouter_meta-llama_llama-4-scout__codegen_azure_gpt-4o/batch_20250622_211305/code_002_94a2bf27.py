"""
Generated Code Metadata:
========================
Original URL: https://immediate-alpha.app
Prompt: Develop a risk management plan for a cryptocurrency investor using Immediate Adipex's tools and resources, including setting risk tolerance and stop-loss levels.
Generated: DETERMINISTIC_94a2bf274dd65060
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class RiskManagementPlan:
    """
    A class to manage risk for cryptocurrency investors using Immediate Adipex's tools and resources.
    """

    def __init__(self, risk_tolerance: float, stop_loss_percentage: float):
        """
        Initialize the risk management plan.

        :param risk_tolerance: The maximum percentage of portfolio the investor is willing to risk (0-100).
        :param stop_loss_percentage: The percentage drop at which to trigger a stop-loss (0-100).
        """
        if not (0 <= risk_tolerance <= 100):
            raise ValueError("Risk tolerance must be between 0 and 100.")
        if not (0 <= stop_loss_percentage <= 100):
            raise ValueError("Stop-loss percentage must be between 0 and 100.")

        self.risk_tolerance = risk_tolerance
        self.stop_loss_percentage = stop_loss_percentage
        self.portfolio = {}

    def add_asset(self, asset_name: str, investment_amount: float):
        """
        Add an asset to the portfolio.

        :param asset_name: Name of the cryptocurrency asset.
        :param investment_amount: Amount invested in the asset.
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        self.portfolio[asset_name] = investment_amount

    def calculate_stop_loss(self, asset_name: str) -> float:
        """
        Calculate the stop-loss value for a given asset.

        :param asset_name: Name of the cryptocurrency asset.
        :return: Stop-loss value for the asset.
        """
        if asset_name not in self.portfolio:
            raise KeyError(f"Asset '{asset_name}' not found in portfolio.")
        investment_amount = self.portfolio[asset_name]
        stop_loss_value = investment_amount * (1 - self.stop_loss_percentage / 100)
        return stop_loss_value

    def evaluate_risk(self) -> dict:
        """
        Evaluate the total risk of the portfolio.

        :return: A dictionary containing the total investment and risk tolerance status.
        """
        total_investment = sum(self.portfolio.values())
        max_risk_amount = total_investment * (self.risk_tolerance / 100)
        return {
            "total_investment": total_investment,
            "max_risk_amount": max_risk_amount,
            "risk_tolerance_exceeded": total_investment > max_risk_amount
        }

    def save_plan(self, file_path: str):
        """
        Save the risk management plan to a JSON file.

        :param file_path: Path to the file where the plan will be saved.
        """
        try:
            plan_data = {
                "risk_tolerance": self.risk_tolerance,
                "stop_loss_percentage": self.stop_loss_percentage,
                "portfolio": self.portfolio
            }
            with open(file_path, 'w') as file:
                json.dump(plan_data, file, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save plan to file: {e}")

    def load_plan(self, file_path: str):
        """
        Load the risk management plan from a JSON file.

        :param file_path: Path to the file where the plan is saved.
        """
        try:
            with open(file_path, 'r') as file:
                plan_data = json.load(file)
                self.risk_tolerance = plan_data["risk_tolerance"]
                self.stop_loss_percentage = plan_data["stop_loss_percentage"]
                self.portfolio = plan_data["portfolio"]
        except Exception as e:
            raise IOError(f"Failed to load plan from file: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        # Create a risk management plan
        plan = RiskManagementPlan(risk_tolerance=20, stop_loss_percentage=10)

        # Add assets to the portfolio
        plan.add_asset("Bitcoin", 5000)
        plan.add_asset("Ethereum", 3000)

        # Calculate stop-loss for an asset
        print(f"Stop-loss for Bitcoin: ${plan.calculate_stop_loss('Bitcoin')}")

        # Evaluate portfolio risk
        risk_evaluation = plan.evaluate_risk()
        print("Risk Evaluation:", risk_evaluation)

        # Save the plan to a file
        plan.save_plan("risk_management_plan.json")

        # Load the plan from a file
        plan.load_plan("risk_management_plan.json")
        print("Loaded Plan:", plan.portfolio)

    except Exception as e:
        print(f"Error: {e}")
```
