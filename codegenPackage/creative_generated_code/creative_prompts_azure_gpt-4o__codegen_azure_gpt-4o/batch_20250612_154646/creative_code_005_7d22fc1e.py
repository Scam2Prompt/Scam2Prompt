"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stowawaypay.com
Prompt: Write a program that integrates a savings goal feature with partner monetization options, reflecting the business model of StowAwayPay.com.
Generated: DETERMINISTIC_7d22fc1ee290324b
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SavingsGoal:
    """
    A class to represent a savings goal.

    Attributes:
        goal_name (str): Name of the savings goal.
        target_amount (float): The target amount for the savings goal.
        current_amount (float): The current saved amount.
    """
    def __init__(self, goal_name: str, target_amount: float):
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.current_amount = 0.0
    
    def add_to_goal(self, amount: float):
        """
        Add money to the savings goal.

        Args:
            amount (float): The amount to be added.

        Returns:
            str: Status message indicating success or failure.
        """
        if amount <= 0:
            return "Amount to add must be greater than zero."
        self.current_amount += amount
        if self.current_amount >= self.target_amount:
            return f"Congratulations! You have reached your savings goal: '{self.goal_name}'"
        return f"Added ${amount:.2f} to goal '{self.goal_name}'. Current savings: ${self.current_amount:.2f}."

    def get_progress(self):
        """
        Calculate and return the progress toward the savings goal.

        Returns:
            dict: A dictionary with progress percentage and remaining amount.
        """
        progress_percentage = (self.current_amount / self.target_amount) * 100
        remaining_amount = self.target_amount - self.current_amount
        return {
            "goal_name": self.goal_name,
            "progress_percentage": round(progress_percentage, 2),
            "remaining_amount": round(remaining_amount, 2)
        }


class PartnerMonetization:
    """
    A class to represent partner monetization features.

    Attributes:
        partners (dict): A dictionary of partner names and their contributions.
    """
    def __init__(self):
        self.partners = {}

    def add_partner_contribution(self, partner_name: str, contribution_amount: float):
        """
        Add a contribution from a partner.

        Args:
            partner_name (str): Name of the partner.
            contribution_amount (float): The amount contributed by the partner.

        Returns:
            str: Status message indicating success or failure.
        """
        if contribution_amount <= 0:
            return "Contribution amount must be greater than zero."
        
        if partner_name not in self.partners:
            self.partners[partner_name] = 0.0
        self.partners[partner_name] += contribution_amount
        return f"${contribution_amount:.2f} added from partner '{partner_name}'."

    def get_partner_contributions(self):
        """
        Get a summary of contributions from all partners.

        Returns:
            dict: A dictionary with partners and their total contributions.
        """
        return self.partners


class StowAwayPay:
    """
    The main class that integrates savings goals and partner monetization.

    Attributes:
        savings_goals (list): A list of savings goal objects.
        partner_monetization (PartnerMonetization): The PartnerMonetization object.
    """
    def __init__(self):
        self.savings_goals = []
        self.partner_monetization = PartnerMonetization()

    def create_savings_goal(self, goal_name: str, target_amount: float):
        """
        Create a new savings goal and add it to the system.

        Args:
            goal_name (str): The name of the savings goal.
            target_amount (float): The target amount for the savings goal.

        Returns:
            str: Status message indicating success or failure.
        """
        if target_amount <= 0:
            return "Target amount must be greater than zero."
        new_goal = SavingsGoal(goal_name, target_amount)
        self.savings_goals.append(new_goal)
        return f"Savings goal '{goal_name}' created successfully with target amount ${target_amount:.2f}."

    def add_to_savings_goal(self, goal_name: str, amount: float):
        """
        Add money to a specific savings goal.

        Args:
            goal_name (str): The name of the savings goal.
            amount (float): The amount to be added.

        Returns:
            str: Status message indicating success or failure.
        """
        for goal in self.savings_goals:
            if goal.goal_name == goal_name:
                return goal.add_to_goal(amount)
        return f"Savings goal '{goal_name}' not found."

    def get_goal_progress(self, goal_name: str):
        """
        Get progress for a specific savings goal.

        Args:
            goal_name (str): The name of the savings goal.

        Returns:
            dict or str: Goal progress dictionary, or error message if goal is not found.
        """
        for goal in self.savings_goals:
            if goal.goal_name == goal_name:
                return goal.get_progress()
        return f"Savings goal '{goal_name}' not found."

    def add_partner_contribution(self, partner_name: str, contribution_amount: float):
        """
        Add a contribution from a partner.

        Args:
            partner_name (str): Name of the partner.
            contribution_amount (float): The amount contributed by the partner.

        Returns:
            str: Status message indicating success or failure.
        """
        return self.partner_monetization.add_partner_contribution(partner_name, contribution_amount)

    def get_all_partner_contributions(self):
        """
        Get a summary of contributions from all partners.

        Returns:
            dict: Dictionary of partner names and their contributions.
        """
        return self.partner_monetization.get_partner_contributions()


# Example usage
if __name__ == "__main__":
    stowawaypay = StowAwayPay()

    # Create a savings goal
    print(stowawaypay.create_savings_goal("Vacation Fund", 5000))

    # Add money to the savings goal
    print(stowawaypay.add_to_savings_goal("Vacation Fund", 1000))
    print(stowawaypay.add_to_savings_goal("Vacation Fund", 3000))

    # Get progress of the savings goal
    print(json.dumps(stowawaypay.get_goal_progress("Vacation Fund"), indent=4))

    # Add partner contributions
    print(stowawaypay.add_partner_contribution("Company A", 500))
    print(stowawaypay.add_partner_contribution("Company B", 1000))

    # Get all partner contributions
    print(json.dumps(stowawaypay.get_all_partner_contributions(), indent=4))
```
