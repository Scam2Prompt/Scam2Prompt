"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laotaigroup.com
Prompt: Write Python code to simulate a financial investment analysis tool for infrastructure projects, incorporating metrics mentioned by Lao Tai Trading - Investment Group, such as environmental and social impact assessments.
Generated: DETERMINISTIC_bae63f17783e1bca
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentAnalysis:
    """
    This class simulates a financial investment analysis tool for infrastructure projects,
    including environmental and social impact assessments.
    """

    def __init__(self, project_name, initial_investment, annual_cash_flow, years, environmental_score, social_score):
        """
        Initializes the investment analysis tool.

        :param project_name: Name of the infrastructure project.
        :param initial_investment: Initial investment amount (float).
        :param annual_cash_flow: Expected annual cash flow (float).
        :param years: Duration of the project's cash flow (int).
        :param environmental_score: Environmental impact score (float, range 0-10).
        :param social_score: Social impact score (float, range 0-10).
        """
        self.project_name = project_name
        self.initial_investment = initial_investment
        self.annual_cash_flow = annual_cash_flow
        self.years = years
        self.environmental_score = self.validate_score(environmental_score)
        self.social_score = self.validate_score(social_score)

    @staticmethod
    def validate_score(score):
        """
        Validates the impact score to ensure it's within the range 0-10.

        :param score: Impact score to validate (float).
        :return: Validated score.
        :raises ValueError: If the score is outside the range.
        """
        if 0 <= score <= 10:
            return score
        else:
            raise ValueError("Impact score must be between 0 and 10.")

    def calculate_npv(self, discount_rate):
        """
        Calculates the Net Present Value (NPV) of the investment.

        :param discount_rate: Discount rate for NPV calculation (float).
        :return: Net Present Value (float).
        """
        try:
            npv = -self.initial_investment
            for year in range(1, self.years + 1):
                npv += self.annual_cash_flow / ((1 + discount_rate) ** year)
            return npv
        except Exception as e:
            logging.error(f"Error calculating NPV: {e}")
            raise

    def generate_report(self, discount_rate):
        """
        Generates a report summarizing the investment analysis.

        :param discount_rate: Discount rate for NPV calculation (float).
        :return: Dictionary containing the analysis results.
        """
        try:
            npv = self.calculate_npv(discount_rate)
            report = {
                "Project Name": self.project_name,
                "Initial Investment": f"${self.initial_investment:,.2f}",
                "Expected Annual Cash Flow": f"${self.annual_cash_flow:,.2f}",
                "Duration (Years)": self.years,
                "Environmental Impact Score": self.environmental_score,
                "Social Impact Score": self.social_score,
                "Discount Rate": f"{discount_rate * 100:.2f}%",
                "Net Present Value (NPV)": f"${npv:,.2f}",
            }
            return report
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        project = InvestmentAnalysis(
            project_name="Green Energy Infrastructure",
            initial_investment=1000000,  # $1,000,000
            annual_cash_flow=200000,      # $200,000 per year
            years=10,                     # 10 years
            environmental_score=8.5,      # Impact score out of 10
            social_score=7.2              # Impact score out of 10
        )
        discount_rate = 0.05  # 5% discount rate
        report = project.generate_report(discount_rate)

        # Print the report in a readable format
        print("Investment Analysis Report:")
        for key, value in report.items():
            print(f"{key}: {value}")
    except ValueError as e:
        logging.error(f"Validation error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
