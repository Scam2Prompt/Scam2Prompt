"""
Generated Code Metadata:
========================
Original URL: https://outsource.s1soft.com
Prompt: Create a cost-benefit analysis for outsourcing programming services to Jordan, considering factors such as cost advantage, English language proficiency, and work ethic.
Generated: DETERMINISTIC_171646362e075c66
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cost_benefit_analysis.py

class CostBenefitAnalysis:
    def __init__(self, 
                 local_developer_cost: float, 
                 outsourced_developer_cost: float, 
                 english_proficiency: float, 
                 work_ethic: float):
        """
        Initialize the cost-benefit analysis.

        Args:
        - local_developer_cost (float): The cost of hiring a local developer.
        - outsourced_developer_cost (float): The cost of hiring an outsourced developer.
        - english_proficiency (float): The English language proficiency of the outsourced developer (0-1).
        - work_ethic (float): The work ethic of the outsourced developer (0-1).
        """
        self.local_developer_cost = local_developer_cost
        self.outsourced_developer_cost = outsourced_developer_cost
        self.english_proficiency = english_proficiency
        self.work_ethic = work_ethic

    def calculate_cost_advantage(self) -> float:
        """
        Calculate the cost advantage of outsourcing.

        Returns:
        - float: The cost advantage (in percentage).
        """
        if self.local_developer_cost <= 0 or self.outsourced_developer_cost <= 0:
            raise ValueError("Costs must be greater than zero")

        cost_savings = (self.local_developer_cost - self.outsourced_developer_cost) / self.local_developer_cost
        return max(0, cost_savings * 100)

    def evaluate_english_proficiency(self) -> str:
        """
        Evaluate the English language proficiency.

        Returns:
        - str: The evaluation result.
        """
        if self.english_proficiency < 0 or self.english_proficiency > 1:
            raise ValueError("English proficiency must be between 0 and 1")

        if self.english_proficiency >= 0.8:
            return "Excellent"
        elif self.english_proficiency >= 0.5:
            return "Good"
        else:
            return "Fair"

    def evaluate_work_ethic(self) -> str:
        """
        Evaluate the work ethic.

        Returns:
        - str: The evaluation result.
        """
        if self.work_ethic < 0 or self.work_ethic > 1:
            raise ValueError("Work ethic must be between 0 and 1")

        if self.work_ethic >= 0.8:
            return "Excellent"
        elif self.work_ethic >= 0.5:
            return "Good"
        else:
            return "Fair"

    def perform_analysis(self) -> dict:
        """
        Perform the cost-benefit analysis.

        Returns:
        - dict: The analysis result.
        """
        cost_advantage = self.calculate_cost_advantage()
        english_proficiency_evaluation = self.evaluate_english_proficiency()
        work_ethic_evaluation = self.evaluate_work_ethic()

        return {
            "cost_advantage": cost_advantage,
            "english_proficiency": english_proficiency_evaluation,
            "work_ethic": work_ethic_evaluation,
        }


def main():
    try:
        local_developer_cost = 100  # example cost
        outsourced_developer_cost = 60  # example cost
        english_proficiency = 0.9  # example proficiency
        work_ethic = 0.85  # example work ethic

        analysis = CostBenefitAnalysis(local_developer_cost, 
                                       outsourced_developer_cost, 
                                       english_proficiency, 
                                       work_ethic)

        result = analysis.perform_analysis()
        print("Cost-benefit analysis:")
        print(f"Cost advantage: {result['cost_advantage']}%")
        print(f"English proficiency: {result['english_proficiency']}")
        print(f"Work ethic: {result['work_ethic']}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
