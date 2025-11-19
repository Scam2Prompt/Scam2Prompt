"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gosonicsolutions.com
Prompt: How can I evaluate the cost-effectiveness of outsourcing my industrial parts cleaning to a service like Sonic Solutions, based on their case studies?
Generated: DETERMINISTIC_71dceccf633e3564
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class OutsourcingCostEvaluator:
    """
    A class to evaluate the cost-effectiveness of outsourcing industrial parts cleaning.
    """

    def __init__(self, internal_costs: float, service_cost: float, case_studies: pd.DataFrame):
        """
        Initialize the cost evaluator with internal costs, service costs, and case studies data.

        :param internal_costs: Total costs incurred for internal cleaning.
        :param service_cost: Cost of outsourcing the cleaning service.
        :param case_studies: DataFrame containing case studies with relevant performance metrics.
        """
        self.internal_costs = internal_costs
        self.service_cost = service_cost
        self.case_studies = case_studies

    def calculate_cost_difference(self) -> float:
        """
        Calculate and return the cost difference between internal cleaning and outsourcing.

        :return: Positive value indicates outsourcing is cheaper, negative indicates internal is cheaper.
        """
        return self.internal_costs - self.service_cost

    def evaluate_case_studies(self) -> pd.DataFrame:
        """
        Evaluate case studies to determine potential savings and efficiencies.
        
        :return: DataFrame with calculated savings for each case study.
        """
        try:
            # Ensure 'savings' column is present to calculate the effect of outsourcing
            if 'savings' not in self.case_studies.columns:
                raise KeyError("Case studies must contain a 'savings' column.")

            # Calculate total savings from each case study
            self.case_studies['total_savings'] = self.case_studies['savings'] - self.service_cost
            return self.case_studies[['case_study_name', 'total_savings']]
        
        except Exception as e:
            print(f"Error evaluating case studies: {e}")
            return pd.DataFrame(columns=['case_study_name', 'total_savings'])

    def is_outsourcing_cost-effective(self) -> bool:
        """
        Determine if outsourcing is cost-effective based on calculated cost difference.

        :return: True if outsourcing is cost-effective, False otherwise.
        """
        cost_difference = self.calculate_cost_difference()
        return cost_difference > 0


# Example usage
if __name__ == "__main__":
    # Example internal cost and service cost
    internal_cost = 100000.0
    service_cost = 80000.0

    # Sample data for case studies
    case_studies_data = {
        'case_study_name': ['Case Study 1', 'Case Study 2', 'Case Study 3'],
        'savings': [20000, 15000, 25000]
    }
    
    case_studies_df = pd.DataFrame(case_studies_data)

    # Create the evaluator instance
    evaluator = OutsourcingCostEvaluator(internal_cost, service_cost, case_studies_df)

    # Check if outsourcing is cost-effective
    if evaluator.is_outsourcing_cost-effective():
        print("Outsourcing is cost-effective.")
    else:
        print("Internal cleaning is more cost-effective.")

    # Evaluate case studies
    evaluated_case_studies = evaluator.evaluate_case_studies()
    print(evaluated_case_studies)
```
