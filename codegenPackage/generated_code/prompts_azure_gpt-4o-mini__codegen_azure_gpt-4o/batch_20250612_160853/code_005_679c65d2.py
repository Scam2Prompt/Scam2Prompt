"""
Generated Code Metadata:
========================
Original URL: https://cvex.pages.dev
Prompt: Write a program to simulate futures trading scenarios on CVEX, incorporating the unique cross-margin capabilities and collateral adjustments.
Generated: DETERMINISTIC_679c65d2380e1e1b
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import random

class FuturesContract:
    """
    Represents a futures contract in the CVEX trading system.
    """
    def __init__(self, symbol, expiry_date, initial_margin, maintenance_margin):
        self.symbol = symbol
        self.expiry_date = expiry_date
        self.initial_margin = initial_margin
        self.maintenance_margin = maintenance_margin
        self.price = random.uniform(50, 150)  # Simulated initial price

    def update_price(self):
        """
        Simulates price updates for the futures contract.
        """
        self.price += random.uniform(-5, 5)  # Random price fluctuation


class TraderAccount:
    """
    Represents a trader's account with cross-margin capabilities.
    """
    def __init__(self, trader_id, collateral):
        self.trader_id = trader_id
        self.collateral = collateral
        self.positions = {}  # Dictionary to store positions in futures contracts

    def add_position(self, contract, quantity):
        """
        Adds a position in a futures contract to the trader's account.
        """
        if contract.symbol in self.positions:
            self.positions[contract.symbol]['quantity'] += quantity
        else:
            self.positions[contract.symbol] = {
                'contract': contract,
                'quantity': quantity
            }

    def calculate_margin_requirement(self):
        """
        Calculates the total margin requirement for the trader's account.
        """
        total_margin = 0
        for position in self.positions.values():
            contract = position['contract']
            quantity = position['quantity']
            total_margin += contract.initial_margin * abs(quantity)
        return total_margin

    def check_margin(self):
        """
        Checks if the trader's collateral meets the margin requirements.
        """
        margin_requirement = self.calculate_margin_requirement()
        if self.collateral < margin_requirement:
            raise ValueError("Insufficient collateral to meet margin requirements.")

    def adjust_collateral(self, amount):
        """
        Adjusts the trader's collateral balance.
        """
        self.collateral += amount


class CVEXSimulator:
    """
    Simulates futures trading scenarios on CVEX.
    """
    def __init__(self):
        self.contracts = []
        self.trader_accounts = {}

    def create_contract(self, symbol, expiry_date, initial_margin, maintenance_margin):
        """
        Creates a new futures contract and adds it to the simulator.
        """
        contract = FuturesContract(symbol, expiry_date, initial_margin, maintenance_margin)
        self.contracts.append(contract)
        return contract

    def register_trader(self, trader_id, initial_collateral):
        """
        Registers a new trader in the simulator.
        """
        if trader_id in self.trader_accounts:
            raise ValueError(f"Trader ID {trader_id} is already registered.")
        self.trader_accounts[trader_id] = TraderAccount(trader_id, initial_collateral)

    def simulate_trading(self):
        """
        Simulates trading scenarios, including price updates and margin checks.
        """
        for contract in self.contracts:
            contract.update_price()

        for trader in self.trader_accounts.values():
            try:
                trader.check_margin()
            except ValueError as e:
                print(f"Margin call for trader {trader.trader_id}: {e}")

    def display_status(self):
        """
        Displays the current status of contracts and trader accounts.
        """
        print("Futures Contracts:")
        for contract in self.contracts:
            print(f"Symbol: {contract.symbol}, Price: {contract.price:.2f}, Expiry: {contract.expiry_date}")

        print("\nTrader Accounts:")
        for trader in self.trader_accounts.values():
            print(f"Trader ID: {trader.trader_id}, Collateral: {trader.collateral:.2f}")
            for position in trader.positions.values():
                contract = position['contract']
                quantity = position['quantity']
                print(f"  Position: {contract.symbol}, Quantity: {quantity}, Price: {contract.price:.2f}")


# Example usage
if __name__ == "__main__":
    simulator = CVEXSimulator()

    # Create futures contracts
    contract1 = simulator.create_contract("AAPL", datetime.date(2024, 6, 30), initial_margin=1000, maintenance_margin=800)
    contract2 = simulator.create_contract("TSLA", datetime.date(2024, 7, 15), initial_margin=1500, maintenance_margin=1200)

    # Register traders
    simulator.register_trader("Trader1", initial_collateral=5000)
    simulator.register_trader("Trader2", initial_collateral=10000)

    # Add positions
    simulator.trader_accounts["Trader1"].add_position(contract1, quantity=3)
    simulator.trader_accounts["Trader2"].add_position(contract2, quantity=-2)

    # Simulate trading scenarios
    simulator.simulate_trading()

    # Display current status
    simulator.display_status()
```
