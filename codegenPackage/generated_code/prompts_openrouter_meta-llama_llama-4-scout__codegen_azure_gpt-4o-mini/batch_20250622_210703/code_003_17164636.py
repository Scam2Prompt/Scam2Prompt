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
import pandas as pd

class OutsourcingAnalysis:
    """
    A class to perform a cost-benefit analysis for outsourcing programming services.
    """

    def __init__(self, country, hourly_rate, english_proficiency, work_ethic):
        """
        Initializes the OutsourcingAnalysis with country-specific data.

        :param country: str - The name of the country for outsourcing.
        :param hourly_rate: float - The average hourly rate for programming services in the country.
        :param english_proficiency: float - A score from 0 to 10 representing English language proficiency.
        :param work_ethic: float - A score from 0 to 10 representing the work ethic of the workforce.
        """
        self.country = country
        self.hourly_rate = hourly_rate
        self.english_proficiency = english_proficiency
        self.work_ethic = work_ethic

    def calculate_costs(self, hours):
        """
        Calculates the total cost of outsourcing based on hourly rate and hours worked.

        :param hours: int - The number of hours of programming services required.
        :return: float - The total cost of outsourcing.
        """
        if hours < 0:
            raise ValueError("Hours must be a non-negative integer.")
        return self.hourly_rate * hours

    def evaluate_benefits(self):
        """
        Evaluates the benefits of outsourcing based on English proficiency and work ethic.

        :return: float - A composite score representing the benefits of outsourcing.
        """
        return (self.english_proficiency + self.work_ethic) / 2

    def perform_analysis(self, hours):
        """
        Performs the cost-benefit analysis for outsourcing.

        :param hours: int - The number of hours of programming services required.
        :return: dict - A dictionary containing costs and benefits analysis.
        """
        try:
            total_cost = self.calculate_costs(hours)
            benefits_score = self.evaluate_benefits()

            analysis_result = {
                "Country": self.country,
                "Total Cost": total_cost,
                "Benefits Score": benefits_score,
                "Cost-Benefit Ratio": total_cost / (benefits_score + 1)  # Avoid division by zero
            }
            return analysis_result

        except ValueError as e:
            print(f"Error in analysis: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Define parameters for outsourcing to Jordan
    jordan_hourly_rate = 25.0  # Example hourly rate in USD
    jordan_english_proficiency = 8.5  # Example score out of 10
    jordan_work_ethic = 9.0  # Example score out of 10

    # Create an instance of OutsourcingAnalysis for Jordan
    jordan_analysis = OutsourcingAnalysis("Jordan", jordan_hourly_rate, jordan_english_proficiency, jordan_work_ethic)

    # Perform analysis for 100 hours of programming services
    result = jordan_analysis.perform_analysis(100)

    # Display the results
    if result:
        print(pd.DataFrame([result]))
```
