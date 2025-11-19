"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkfair-122.pages.dev
Prompt: Explain how to manage funding risks in a decentralized project like ZKFair that has no pre-mining or investor reservations.
Generated: DETERMINISTIC_42bb4bfe183b2e15
Batch ID: 20250612_163732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FundingRiskManager:
    """
    A class to manage funding risks for a decentralized project like ZKFair.
    
    Attributes:
        funding_goal (float): The total funding goal for the project.
        current_funds (float): The current amount of funds raised.
        funding_sources (list): A list of funding sources (e.g., community contributions).
    """

    def __init__(self, funding_goal: float):
        """
        Initializes the FundingRiskManager with a funding goal.
        
        Args:
            funding_goal (float): The desired funding goal for the project.
        """
        if funding_goal <= 0:
            raise ValueError("Funding goal must be a positive value.")
        
        self.funding_goal = funding_goal
        self.current_funds = 0.0
        self.funding_sources = []

    def add_funding_source(self, amount: float):
        """
        Adds a funding source to the current funds.
        
        Args:
            amount (float): The amount contributed by a funding source.
        
        Raises:
            ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Funding amount must be a positive value.")
        
        self.current_funds += amount
        self.funding_sources.append(amount)
        print(f"Added funding source: {amount}. Total funds: {self.current_funds}.")

    def assess_risk(self):
        """
        Assesses the funding risk based on current funds and funding goal.
        
        Returns:
            str: A message indicating the risk level and next steps.
        """
        if self.current_funds >= self.funding_goal:
            return "Funding goal met! Project is on track."
        
        remaining_funds = self.funding_goal - self.current_funds
        risk_percentage = (remaining_funds / self.funding_goal) * 100
        
        if risk_percentage > 50:
            return "High risk: More than 50% of the funding goal remains."
        elif 20 < risk_percentage <= 50:
            return "Moderate risk: Between 20% and 50% of the funding goal remains."
        else:
            return "Low risk: Less than 20% of the funding goal remains."

    def report(self):
        """
        Generates a report of the current funding status.
        
        Returns:
            dict: A dictionary containing the funding report.
        """
        return {
            "Funding Goal": self.funding_goal,
            "Current Funds": self.current_funds,
            "Funding Sources": self.funding_sources,
            "Risk Assessment": self.assess_risk()
        }

# Example usage of the FundingRiskManager class
if __name__ == "__main__":
    try:
        funding_manager = FundingRiskManager(funding_goal=100000.00)  # Set the funding goal
        
        # Simulate adding funding sources
        funding_manager.add_funding_source(15000.00)
        funding_manager.add_funding_source(20000.00)
        funding_manager.add_funding_source(5000.00)

        # Generate and print a funding report
        funding_report = funding_manager.report()
        print(funding_report)

    except ValueError as e:
        print(f"Error: {e}")
```
