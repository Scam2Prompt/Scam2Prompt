"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokentransact.net
Prompt: Develop a code example for a project investment tracker that includes features for crypto mining and energy investments as highlighted on Token Transact.
Generated: DETERMINISTIC_f2e36a4ebcabcdeb
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Investment:
    """
    Base class for investments.
    Represents a generic investment with basic properties like name, amount, and date.
    """
    def __init__(self, name, amount, date=None):
        self.name = name
        self.amount = amount
        self.date = date or datetime.date.today()

    def __str__(self):
        return f"{self.name}: ${self.amount} (Date: {self.date})"


class CryptoMiningInvestment(Investment):
    """
    Represents a crypto mining investment.
    Inherits from the Investment class and adds specific attributes like hash_rate and power_cost.
    """
    def __init__(self, name, amount, hash_rate, power_cost, date=None):
        super().__init__(name, amount, date)
        self.hash_rate = hash_rate  # Hash rate in TH/s
        self.power_cost = power_cost  # Power cost in $ per day

    def calculate_potential_profit(self, daily_mining_revenue):
        """
        Calculates potential profit based on daily revenue and power cost.

        Args:
            daily_mining_revenue (float): Estimated daily earnings from mining.

        Returns:
            float: Net daily profit.
        """
        return daily_mining_revenue - self.power_cost

    def __str__(self):
        return (super().__str__() + 
                f", Hash Rate: {self.hash_rate} TH/s, Power Cost: ${self.power_cost}/day")


class EnergyInvestment(Investment):
    """
    Represents an energy sector investment.
    Inherits from the Investment class and adds attributes like energy_type and annual_yield.
    """
    def __init__(self, name, amount, energy_type, annual_yield, date=None):
        super().__init__(name, amount, date)
        self.energy_type = energy_type  # Type of energy (e.g., solar, wind, hydro)
        self.annual_yield = annual_yield  # Annual yield percentage

    def calculate_annual_return(self):
        """
        Calculates the annual return on investment.

        Returns:
            float: Annual return in dollars.
        """
        return self.amount * (self.annual_yield / 100)

    def __str__(self):
        return (super().__str__() + 
                f", Energy Type: {self.energy_type}, Annual Yield: {self.annual_yield}%")


class InvestmentTracker:
    """
    Tracks multiple investments and provides aggregated information.

    Features:
    - Add investments
    - List all investments
    - Calculate total invested amount
    """
    def __init__(self):
        self.investments = []

    def add_investment(self, investment):
        """
        Adds an investment to the tracker.

        Args:
            investment (Investment): An instance of Investment or its subclasses.
        """
        if not isinstance(investment, Investment):
            raise TypeError("Investment must be an instance of the Investment class.")
        self.investments.append(investment)

    def list_investments(self):
        """
        Lists all investments in the tracker.

        Returns:
            list: A list of investment descriptions.
        """
        return [str(investment) for investment in self.investments]

    def calculate_total_invested(self):
        """
        Calculates the total amount invested across all investments.

        Returns:
            float: Total invested amount.
        """
        return sum(investment.amount for investment in self.investments)


# Example usage:
if __name__ == "__main__":
    try:
        tracker = InvestmentTracker()

        # Adding a crypto mining investment
        crypto_investment = CryptoMiningInvestment(
            name="Bitcoin Mining Rig",
            amount=5000,
            hash_rate=100,
            power_cost=10
        )
        tracker.add_investment(crypto_investment)

        # Adding an energy investment
        energy_investment = EnergyInvestment(
            name="Solar Farm",
            amount=20000,
            energy_type="Solar",
            annual_yield=8
        )
        tracker.add_investment(energy_investment)

        # Listing investments
        print("Investments:")
        for investment_description in tracker.list_investments():
            print(investment_description)

        # Calculating total invested amount
        print("\nTotal Invested Amount: $", tracker.calculate_total_invested())

        # Example calculations for specific investments
        daily_mining_revenue = 25  # Example revenue
        print("\nDaily Profit for Crypto Mining:", 
              crypto_investment.calculate_potential_profit(daily_mining_revenue))

        print("Annual Return for Energy Investment: $", 
              energy_investment.calculate_annual_return())

    except Exception as e:
        print(f"An error occurred: {e}")
```
