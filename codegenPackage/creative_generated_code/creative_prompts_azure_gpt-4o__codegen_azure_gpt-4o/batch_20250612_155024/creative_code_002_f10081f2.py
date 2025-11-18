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

class Startup:
    """
    Represents a startup seeking venture capital funding.
    """
    def __init__(self, name, industry, growth_potential):
        """
        Initialize a Startup object.
        
        :param name: Name of the startup.
        :param industry: Industry in which the startup operates.
        :param growth_potential: Growth potential score (0 - 100) of the startup.
        """
        self.name = name
        self.industry = industry
        self.growth_potential = growth_potential
        self.funding_received = 0

    def receive_funding(self, amount):
        """
        Adds funding to the startup.
        
        :param amount: Amount of funding received.
        """
        self.funding_received += amount


class VentureCapitalFirm:
    """
    Represents a venture capital firm (e.g., DCL Invest SA).
    """
    def __init__(self, name, total_funds, min_growth_threshold):
        """
        Initialize a VentureCapitalFirm object.
        
        :param name: Name of the venture capital firm.
        :param total_funds: Total funds available for investment.
        :param min_growth_threshold: Minimum growth potential required to invest in a startup.
        """
        self.name = name
        self.total_funds = total_funds
        self.min_growth_threshold = min_growth_threshold

    def evaluate_startup(self, startup):
        """
        Evaluate whether the firm should invest in the startup.
        
        :param startup: Startup object to evaluate.
        :return: Boolean indicating whether the firm will invest in the startup.
        """
        if startup.growth_potential >= self.min_growth_threshold:
            return True
        return False

    def invest(self, startup, round_number):
        """
        Simulate an investment round for the startup.
        
        :param startup: Startup object to invest in.
        :param round_number: Current funding round number.
        :return: Investment amount if successful, or None if the firm does not invest.
        """
        try:
            # Check if the firm has sufficient funds and the startup qualifies for investment
            if self.total_funds <= 0:
                raise ValueError(f"{self.name} has no remaining funds to invest.")
            if not self.evaluate_startup(startup):
                print(f"{self.name} declined to invest in {startup.name} due to insufficient growth potential.")
                return None
            
            # Determine the amount to invest in this funding round (randomized for simulation purposes)
            investment_amount = min(random.randint(50000, 200000), self.total_funds)
            
            # Update firm's available funds and startup's funding received
            self.total_funds -= investment_amount
            startup.receive_funding(investment_amount)
            
            print(f"Round {round_number}: {self.name} invested ${investment_amount:,} in {startup.name}.")
            return investment_amount
        except Exception as e:
            print(f"Error during investment process: {e}")
            return None


def simulate_funding_rounds():
    """
    Simulates venture capital funding rounds for startups.
    """
    try:
        # Create venture capital firm (DCL Invest SA)
        dcl_invest = VentureCapitalFirm(name="DCL Invest SA", total_funds=1000000, min_growth_threshold=70)
        
        # Create sample startups
        startups = [
            Startup(name="TechNova", industry="Technology", growth_potential=85),
            Startup(name="GreenFuture", industry="Renewable Energy", growth_potential=75),
            Startup(name="MediCare+", industry="Healthcare", growth_potential=65),
            Startup(name="EduSmart", industry="Education", growth_potential=90)
        ]
        
        # Simulate funding rounds for each startup
        for round_number in range(1, 4):  # Simulate 3 rounds
            print(f"\n--- Funding Round {round_number} ---")
            for startup in startups:
                dcl_invest.invest(startup, round_number)
        
        # Display final funding results for each startup
        print("\n--- Final Funding Results ---")
        for startup in startups:
            print(f"{startup.name} received a total of ${startup.funding_received:,} in funding.")
    except Exception as e:
        print(f"Simulation error: {e}")


if __name__ == "__main__":
    # Run the funding simulation
    simulate_funding_rounds()
```
