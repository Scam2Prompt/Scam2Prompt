"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthcareventure.nl
Prompt: Write Python code to simulate a buy-and-build strategy for acquiring and consolidating youth mental healthcare companies, ensuring scalability and profitability analysis based on the goals outlined by HealthCare Venture.
Generated: DETERMINISTIC_f5a07f56c91ca46e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import logging

# Configure logging for monitoring and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class YouthMentalHealthConsolidation:
    """
    A class to simulate the buy-and-build strategy for acquiring and consolidating
    youth mental healthcare companies.
    """

    def __init__(self):
        """
        Initializes the consolidation strategy.
        Stores data for acquired companies and profitability projections.
        """
        self.acquired_companies = pd.DataFrame(columns=['Company Name', 'Annual Revenue', 'Profit Margin'])
        self.total_investment = 0
        self.total_revenue = 0
        self.total_profit = 0

    def acquire_company(self, company_name, annual_revenue, profit_margin, acquisition_cost):
        """
        Acquires a new company and updates the portfolio.

        Args:
            company_name (str): Name of the company being acquired.
            annual_revenue (float): Annual revenue of the company.
            profit_margin (float): Profit margin of the company (percent as decimal).
            acquisition_cost (float): Cost to acquire the company.

        Returns:
            None
        """
        try:
            # Validate inputs
            if annual_revenue < 0 or profit_margin < 0 or acquisition_cost < 0:
                raise ValueError("Revenue, profit margin, and acquisition cost must be non-negative.")

            # Add company to the portfolio
            self.acquired_companies = pd.concat(
                [self.acquired_companies, pd.DataFrame([{
                    'Company Name': company_name,
                    'Annual Revenue': annual_revenue,
                    'Profit Margin': profit_margin
                }])],
                ignore_index=True
            )

            # Update profitability and investment totals
            self.total_investment += acquisition_cost
            self.total_revenue += annual_revenue
            self.total_profit += annual_revenue * profit_margin

            logging.info(f"Successfully acquired {company_name}. Updated portfolio.")

        except ValueError as ve:
            logging.error(f"Invalid input: {ve}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

    def analyze_profitability(self):
        """
        Analyzes overall profitability of the consolidated portfolio.

        Returns:
            dict: A dictionary containing profitability metrics.
        """
        try:
            # Calculate ROI (Return on Investment)
            if self.total_investment == 0:
                roi = 0  # Avoid division by zero
            else:
                roi = (self.total_profit / self.total_investment) * 100

            # Compile profitability metrics
            metrics = {
                "Total Investment": self.total_investment,
                "Total Revenue": self.total_revenue,
                "Total Profit": self.total_profit,
                "ROI (%)": roi
            }

            # Log metrics for monitoring
            logging.info(f"Profitability analysis completed. Metrics: {metrics}")
            return metrics

        except Exception as e:
            logging.error(f"An error occurred during profitability analysis: {e}")
            return {}

    def is_scalable(self, target_roi):
        """
        Determines if the strategy is scalable based on a target ROI.

        Args:
            target_roi (float): Target ROI percentage.

        Returns:
            bool: True if the strategy is scalable, False otherwise.
        """
        try:
            # Validate input
            if target_roi < 0:
                raise ValueError("Target ROI must be non-negative.")

            # Analyze current ROI
            metrics = self.analyze_profitability()
            current_roi = metrics.get("ROI (%)", 0)

            # Determine scalability
            scalable = current_roi >= target_roi
            logging.info(f"Scalability analysis completed. Scalable: {scalable}")
            return scalable

        except ValueError as ve:
            logging.error(f"Invalid input: {ve}")
        except Exception as e:
            logging.error(f"An error occurred during scalability analysis: {e}")
            return False


# Example usage (commented out for production readiness)
# Uncomment the following section to test the simulation

# if __name__ == "__main__":
#     strategy = YouthMentalHealthConsolidation()
#     
#     # Acquire sample companies
#     strategy.acquire_company("Therapy Co.", 500000, 0.15, 200000)
#     strategy.acquire_company("Counseling Inc.", 800000, 0.20, 300000)
#     
#     # Analyze profitability
#     metrics = strategy.analyze_profitability()
#     print("Profitability Metrics:", metrics)
#     
#     # Check scalability
#     is_scalable = strategy.is_scalable(target_roi=20)
#     print("Is the strategy scalable?", is_scalable)
```
