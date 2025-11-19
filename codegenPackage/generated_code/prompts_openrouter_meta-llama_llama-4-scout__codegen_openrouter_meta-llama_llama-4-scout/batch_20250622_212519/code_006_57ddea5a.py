"""
Generated Code Metadata:
========================
Original URL: https://superaivip.com
Prompt: Recommend a suitable Super AI plan for a digital marketing agency, considering factors such as team size, project requirements, and budget constraints.
Generated: DETERMINISTIC_57ddea5a81f25749
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# super_ai_plan_recommender.py

class SuperAIPlanRecommender:
    """
    Recommends a suitable Super AI plan for a digital marketing agency.

    Attributes:
        team_sizes (list): List of supported team sizes.
        project_requirements (list): List of supported project requirements.
        budgets (list): List of supported budgets.
        plans (dict): Dictionary of available Super AI plans.
    """

    def __init__(self):
        self.team_sizes = ["small", "medium", "large"]
        self.project_requirements = ["simple", "complex", "enterprise"]
        self.budgets = ["low", "medium", "high"]
        self.plans = {
            "basic": {"team_size": "small", "project_requirement": "simple", "budget": "low", "price": 1000},
            "premium": {"team_size": "medium", "project_requirement": "complex", "budget": "medium", "price": 5000},
            "enterprise": {"team_size": "large", "project_requirement": "enterprise", "budget": "high", "price": 10000},
        }

    def validate_input(self, team_size, project_requirement, budget):
        """
        Validates user input.

        Args:
            team_size (str): Team size.
            project_requirement (str): Project requirement.
            budget (str): Budget.

        Raises:
            ValueError: If input is invalid.
        """
        if team_size not in self.team_sizes:
            raise ValueError("Invalid team size. Supported team sizes: {}".format(self.team_sizes))
        if project_requirement not in self.project_requirements:
            raise ValueError("Invalid project requirement. Supported project requirements: {}".format(self.project_requirements))
        if budget not in self.budgets:
            raise ValueError("Invalid budget. Supported budgets: {}".format(self.budgets))

    def recommend_plan(self, team_size, project_requirement, budget):
        """
        Recommends a suitable Super AI plan.

        Args:
            team_size (str): Team size.
            project_requirement (str): Project requirement.
            budget (str): Budget.

        Returns:
            dict: Recommended Super AI plan.

        Raises:
            ValueError: If no plan is found.
        """
        self.validate_input(team_size, project_requirement, budget)

        recommended_plan = None
        for plan, details in self.plans.items():
            if (details["team_size"] == team_size and 
                details["project_requirement"] == project_requirement and 
                details["budget"] == budget):
                recommended_plan = {"plan": plan, "price": details["price"]}
                break

        if recommended_plan is None:
            raise ValueError("No plan found for the given criteria.")

        return recommended_plan


def main():
    try:
        recommender = SuperAIPlanRecommender()
        team_size = input("Enter team size (small, medium, large): ")
        project_requirement = input("Enter project requirement (simple, complex, enterprise): ")
        budget = input("Enter budget (low, medium, high): ")

        recommended_plan = recommender.recommend_plan(team_size, project_requirement, budget)
        print("Recommended Super AI Plan:")
        print("Plan: {}".format(recommended_plan["plan"]))
        print("Price: {}".format(recommended_plan["price"]))
    except ValueError as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    main()
```
