"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-venus-protocol.vercel.app
Prompt: Generate code to simulate borrowing scenarios on Venus Protocol, including varying collateral and interest rate conditions.
Generated: DETERMINISTIC_a46dfd3acc8128f4
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

# Define a class to simulate borrowing scenarios on the Venus Protocol
class VenusProtocolSimulator:
    def __init__(self):
        """
        Initializes the simulator with default values.
        """
        self.collateral_assets = {}
        self.borrowed_assets = {}
        self.collateral_factor = 0.75  # Collateral factor (e.g., 75%)
        self.base_interest_rate = 0.02  # Base annual interest rate (2%)
        self.rate_multiplier = 0.005  # Multiplier for simulated utilization rate

    def add_collateral(self, asset, amount, price):
        """
        Adds collateral for the user.
        
        :param asset: Name of the collateral asset
        :param amount: Amount of the asset deposited
        :param price: Current price of the asset
        """
        if amount <= 0 or price <= 0:
            raise ValueError("Amount and price must be greater than zero.")
        
        if asset in self.collateral_assets:
            self.collateral_assets[asset]['amount'] += amount
        else:
            self.collateral_assets[asset] = {'amount': amount, 'price': price}

    def borrow(self, asset, amount, price):
        """
        Simulates borrowing an asset.
        
        :param asset: Name of the asset to borrow
        :param amount: Amount of the asset to borrow
        :param price: Current price of the asset
        """
        if amount <= 0 or price <= 0:
            raise ValueError("Amount and price must be greater than zero.")
        
        max_borrow_value = self.get_max_borrow_value()
        borrow_value = amount * price
        
        if borrow_value > max_borrow_value:
            raise ValueError("Borrow amount exceeds the maximum allowable limit.")

        if asset in self.borrowed_assets:
            self.borrowed_assets[asset]['amount'] += amount
        else:
            self.borrowed_assets[asset] = {'amount': amount, 'price': price}

    def get_max_borrow_value(self):
        """
        Calculates the maximum allowable borrow value based on collateral.

        :return: Maximum borrow value
        """
        total_collateral_value = sum(
            asset['amount'] * asset['price'] for asset in self.collateral_assets.values()
        )
        return total_collateral_value * self.collateral_factor

    def calculate_interest_rate(self, utilization_rate):
        """
        Calculates the interest rate based on the utilization rate.
        
        :param utilization_rate: Utilization rate of the protocol
        :return: Annual interest rate
        """
        if utilization_rate < 0 or utilization_rate > 1:
            raise ValueError("Utilization rate must be between 0 and 1.")
        
        return self.base_interest_rate + self.rate_multiplier * utilization_rate

    def simulate_utilization_rate(self):
        """
        Simulates the utilization rate based on borrowed and available funds.

        :return: Utilization rate
        """
        total_borrowed_value = sum(
            asset['amount'] * asset['price'] for asset in self.borrowed_assets.values()
        )
        total_collateral_value = sum(
            asset['amount'] * asset['price'] for asset in self.collateral_assets.values()
        )
        
        if total_collateral_value == 0:
            return 0  # Avoid division by zero
        
        return total_borrowed_value / total_collateral_value

    def display_portfolio(self):
        """
        Displays the user's portfolio including collateral and borrowed assets.
        """
        print("----- Collateral Assets -----")
        for asset, data in self.collateral_assets.items():
            print(f"{asset}: {data['amount']} units @ ${data['price']} each")
        
        print("\n----- Borrowed Assets -----")
        for asset, data in self.borrowed_assets.items():
            print(f"{asset}: {data['amount']} units @ ${data['price']} each")

# Example Usage
if __name__ == "__main__":
    simulator = VenusProtocolSimulator()
    
    try:
        # Add collateral
        simulator.add_collateral("BTC", 1.5, 20000)  # 1.5 BTC @ $20,000 each
        simulator.add_collateral("ETH", 10, 1500)    # 10 ETH @ $1,500 each

        # Attempt to borrow
        simulator.borrow("USDT", 10000, 1)          # $10,000 worth of USDT @ $1 each

        # Display the portfolio
        simulator.display_portfolio()

        # Simulate and display utilization rate
        utilization_rate = simulator.simulate_utilization_rate()
        print(f"\nUtilization Rate: {utilization_rate:.2%}")

        # Calculate and display interest rate
        interest_rate = simulator.calculate_interest_rate(utilization_rate)
        print(f"Annual Interest Rate: {interest_rate:.2%}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
