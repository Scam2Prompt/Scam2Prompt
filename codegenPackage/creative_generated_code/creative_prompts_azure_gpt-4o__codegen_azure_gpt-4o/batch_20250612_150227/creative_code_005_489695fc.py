"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.hu
Prompt: Write code to simulate investment scenarios for Initia Capital, focusing on the transformation of industries through innovation and technology in the CEE region.
Generated: DETERMINISTIC_489695fcf2a5d8d3
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import sys

class InvestmentSimulation:
    """
    Class to simulate investment scenarios for Initia Capital.
    Focused on transforming industries through innovation and technology
    in the CEE region.
    """

    def __init__(self, initial_fund):
        """
        Initialize the simulation with an initial fund amount.

        :param initial_fund: The initial amount of money for investments.
        """
        if initial_fund <= 0:
            raise ValueError("Initial fund must be greater than 0.")
        self.initial_fund = initial_fund
        self.remaining_fund = initial_fund
        self.portfolio = {}

    def evaluate_industry(self, industry_name):
        """
        Simulate the evaluation of an industry for investment potential.
        
        :param industry_name: Name of the industry to evaluate.
        :return: A score representing the potential of the industry (0-1).
        """
        if not industry_name:
            raise ValueError("Industry name cannot be empty.")
        # Randomly generate a score to simulate evaluation potential (higher is better)
        return round(random.uniform(0.1, 1.0), 2)

    def invest_in_industry(self, industry_name, amount):
        """
        Invest a specific amount in a given industry.

        :param industry_name: Name of the industry to invest in.
        :param amount: The amount to invest in the industry.
        """
        if industry_name in self.portfolio:
            raise ValueError(f"Already invested in {industry_name}.")
        if amount <= 0:
            raise ValueError("Investment amount must be greater than 0.")
        if amount > self.remaining_fund:
            raise ValueError("Insufficient funds for this investment.")

        potential_score = self.evaluate_industry(industry_name)
        self.portfolio[industry_name] = {
            "investment_amount": amount,
            "potential_score": potential_score,
        }
        self.remaining_fund -= amount
        print(f"Invested ${amount} in {industry_name} with a potential score of {potential_score}.")

    def simulate_return(self, industry_name):
        """
        Simulate the return on investment for a given industry.

        :param industry_name: Name of the industry to simulate returns for.
        :return: The profit or loss from the investment.
        """
        if industry_name not in self.portfolio:
            raise ValueError(f"No investment found for {industry_name}.")

        industry_data = self.portfolio[industry_name]
        base_return = industry_data["investment_amount"]
        # Simulating returns based on the potential score (higher scores yield better results)
        multiplier = random.uniform(0.5, 3.0) * industry_data["potential_score"]
        return_amount = round(base_return * multiplier, 2)
        profit_loss = return_amount - base_return
        self.portfolio[industry_name]["return_amount"] = return_amount
        self.portfolio[industry_name]["profit_loss"] = profit_loss

        print(f"Industry: {industry_name}, Return: ${return_amount}, Profit/Loss: ${profit_loss}.")
        return profit_loss

    def get_portfolio_report(self):
        """
        Generate a report of all investments and their results.

        :return: A dictionary containing the portfolio report.
        """
        report = {
            "initial_fund": self.initial_fund,
            "remaining_fund": self.remaining_fund,
            "investments": self.portfolio,
        }
        for industry, data in self.portfolio.items():
            investment = data["investment_amount"]
            return_amount = data.get("return_amount", "N/A")
            profit_loss = data.get("profit_loss", "N/A")
            print(f"Industry: {industry}, Investment: ${investment}, Return: ${return_amount}, Profit/Loss: ${profit_loss}.")
        return report


def main():
    """
    Main function to run the investment simulation.
    """
    try:
        # Initialize the investment simulation with a fund of $1,000,000
        simulation = InvestmentSimulation(initial_fund=1_000_000)

        # Invest in various industries
        simulation.invest_in_industry("FinTech", 200_000)
        simulation.invest_in_industry("Healthcare Tech", 300_000)
        simulation.invest_in_industry("Green Energy", 250_000)

        # Simulate returns for each industry
        simulation.simulate_return("FinTech")
        simulation.simulate_return("Healthcare Tech")
        simulation.simulate_return("Green Energy")

        # Generate and display the portfolio report
        simulation.get_portfolio_report()

    except ValueError as e:
        print(f"ValueError: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Run the simulation
    main()
```
