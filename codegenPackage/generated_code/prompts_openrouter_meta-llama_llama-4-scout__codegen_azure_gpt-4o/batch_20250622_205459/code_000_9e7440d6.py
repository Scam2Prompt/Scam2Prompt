"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: What is the investment model of Carolina Capital, a private equity real estate firm specializing in land acquisition and development in the Southeast?
Generated: DETERMINISTIC_9e7440d66515e696
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a simple representation of the investment model for Carolina Capital,
a private equity real estate firm specializing in land acquisition and development in the Southeast.

Note: This is a simulated model based on general private equity real estate practices.
It does not represent the actual investment model of Carolina Capital.
"""

class InvestmentModel:
    """
    A class to represent the investment model of Carolina Capital.
    """

    def __init__(self, fund_size, target_roi, risk_tolerance):
        """
        Initialize the investment model.

        :param fund_size: Total fund size in USD (float).
        :param target_roi: Target return on investment as a percentage (float).
        :param risk_tolerance: Risk tolerance level (string: 'low', 'medium', 'high').
        """
        self.fund_size = fund_size
        self.target_roi = target_roi
        self.risk_tolerance = risk_tolerance
        self.portfolio = []

    def add_project(self, project_name, location, cost, expected_roi, risk_level):
        """
        Add a project to the investment portfolio.

        :param project_name: Name of the project (string).
        :param location: Location of the project (string).
        :param cost: Cost of the project in USD (float).
        :param expected_roi: Expected ROI of the project as a percentage (float).
        :param risk_level: Risk level of the project (string: 'low', 'medium', 'high').
        :return: None
        """
        if cost > self.fund_size:
            raise ValueError("Project cost exceeds available fund size.")
        if risk_level not in ['low', 'medium', 'high']:
            raise ValueError("Invalid risk level. Choose from 'low', 'medium', or 'high'.")
        
        project = {
            "project_name": project_name,
            "location": location,
            "cost": cost,
            "expected_roi": expected_roi,
            "risk_level": risk_level
        }
        self.portfolio.append(project)
        self.fund_size -= cost  # Deduct project cost from available fund size

    def evaluate_portfolio(self):
        """
        Evaluate the portfolio to ensure it aligns with the firm's investment goals.

        :return: Dictionary containing portfolio summary.
        """
        total_invested = sum(project['cost'] for project in self.portfolio)
        average_roi = (
            sum(project['expected_roi'] for project in self.portfolio) / len(self.portfolio)
            if self.portfolio else 0
        )
        risk_distribution = {
            "low": sum(1 for project in self.portfolio if project['risk_level'] == 'low'),
            "medium": sum(1 for project in self.portfolio if project['risk_level'] == 'medium'),
            "high": sum(1 for project in self.portfolio if project['risk_level'] == 'high')
        }

        return {
            "total_invested": total_invested,
            "remaining_fund_size": self.fund_size,
            "average_roi": average_roi,
            "risk_distribution": risk_distribution
        }

    def display_portfolio(self):
        """
        Display the details of the investment portfolio.

        :return: None
        """
        if not self.portfolio:
            print("Portfolio is empty.")
            return

        print("Investment Portfolio:")
        for project in self.portfolio:
            print(f"Project Name: {project['project_name']}")
            print(f"Location: {project['location']}")
            print(f"Cost: ${project['cost']:.2f}")
            print(f"Expected ROI: {project['expected_roi']}%")
            print(f"Risk Level: {project['risk_level']}")
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the investment model
        carolina_capital = InvestmentModel(fund_size=10000000, target_roi=15, risk_tolerance='medium')

        # Add projects to the portfolio
        carolina_capital.add_project("Project A", "Charleston, SC", 2000000, 18, "medium")
        carolina_capital.add_project("Project B", "Atlanta, GA", 3000000, 20, "high")
        carolina_capital.add_project("Project C", "Charlotte, NC", 1500000, 12, "low")

        # Display portfolio details
        carolina_capital.display_portfolio()

        # Evaluate portfolio
        portfolio_summary = carolina_capital.evaluate_portfolio()
        print("\nPortfolio Summary:")
        print(f"Total Invested: ${portfolio_summary['total_invested']:.2f}")
        print(f"Remaining Fund Size: ${portfolio_summary['remaining_fund_size']:.2f}")
        print(f"Average ROI: {portfolio_summary['average_roi']:.2f}%")
        print(f"Risk Distribution: {portfolio_summary['risk_distribution']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
