"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dclinvest-sa.com
Prompt: Generate code to simulate venture capital funding rounds for startups, incorporating DCL Invest SA's approach to providing financing for businesses with long-term growth potential.
Generated: DETERMINISTIC_f10081f256602e9d
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from decimal import Decimal

class Startup:
    """
    Represents a startup company seeking venture capital funding.
    """
    def __init__(self, name: str, growth_potential: float, funding_needed: Decimal):
        self.name = name
        self.growth_potential = growth_potential  # Scale from 0 to 1
        self.funding_needed = funding_needed
        self.funding_received = Decimal('0.00')

    def receive_funding(self, amount: Decimal):
        """
        Updates the funding received by the startup.
        
        :param amount: The amount of funding received.
        """
        if amount <= 0:
            raise ValueError("Funding amount must be greater than zero.")
        if self.funding_received + amount > self.funding_needed:
            raise ValueError("Funding exceeds the amount needed.")
        self.funding_received += amount

    def is_funded(self) -> bool:
        """
        Checks if the startup has received the required funding.
        
        :return: True if fully funded, False otherwise.
        """
        return self.funding_received >= self.funding_needed

class FundingRound:
    """
    Represents a funding round in which multiple startups can receive funding.
    """
    def __init__(self, round_name: str, total_funds: Decimal):
        self.round_name = round_name
        self.total_funds = total_funds
        self.startups = []

    def add_startup(self, startup: Startup):
        """
        Adds a startup to the funding round.
        
        :param startup: The startup to be added.
        """
        self.startups.append(startup)

    def simulate_funding(self):
        """
        Simulates the funding process for all startups in the round.
        Each startup receives a random amount of funding based on its growth potential.
        """
        for startup in self.startups:
            if startup.is_funded():
                print(f"{startup.name} is already fully funded.")
                continue

            # Calculate funding amount based on growth potential
            funding_amount = (self.total_funds * Decimal(startup.growth_potential)).quantize(Decimal('0.01'))

            # Ensure we do not exceed total available funds
            if funding_amount > self.total_funds:
                funding_amount = self.total_funds
            
            try:
                startup.receive_funding(funding_amount)
                self.total_funds -= funding_amount
                print(f"{startup.name} received funding of {funding_amount:.2f}. Total funded: {startup.funding_received:.2f}.")
            except ValueError as e:
                print(f"Error funding {startup.name}: {e}")

def main():
    """
    Main function to simulate venture capital funding rounds.
    """
    # Initialize startups with names, growth potential, and funding needed
    startups = [
        Startup("Tech Innovations Inc.", 0.8, Decimal('1000000.00')),
        Startup("Green Energy Solutions", 0.6, Decimal('500000.00')),
        Startup("HealthTech Revolution", 0.9, Decimal('2000000.00')),
        Startup("EduTech Dynamics", 0.5, Decimal('300000.00'))
    ]

    # Create a funding round
    funding_round = FundingRound("Series A", Decimal('2500000.00'))

    # Add startups to the funding round
    for startup in startups:
        funding_round.add_startup(startup)

    # Simulate the funding process
    funding_round.simulate_funding()

if __name__ == "__main__":
    main()
```
