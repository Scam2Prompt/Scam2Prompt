"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-nova.com
Prompt: Write a Python script that utilizes the principles of dollar-cost averaging, as taught by Immediate Nova V5, to simulate investment growth over time.
Generated: DETERMINISTIC_06a41e5503a3a0ee
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random
import matplotlib.pyplot as plt


class DollarCostAveragingSimulator:
    """
    A simulator for investment growth using the dollar-cost averaging method.
    """

    def __init__(self, monthly_investment, start_date, end_date, initial_price, volatility):
        """
        Initialize the simulator.

        :param monthly_investment: Amount invested each month (float).
        :param start_date: Start date of the investment (datetime.date).
        :param end_date: End date of the investment (datetime.date).
        :param initial_price: Initial price of the asset (float).
        :param volatility: Simulates price fluctuations (float between 0 and 1).
        """
        self.monthly_investment = monthly_investment
        self.start_date = start_date
        self.end_date = end_date
        self.initial_price = initial_price
        self.volatility = volatility
        self.historic_prices = []
        self.total_invested = 0
        self.total_shares = 0

    def simulate_price(self, current_price):
        """
        Simulate the price movement of the asset based on volatility.

        :param current_price: Current price of the asset (float).
        :return: Simulated new price of the asset (float).
        """
        change_factor = random.uniform(1 - self.volatility, 1 + self.volatility)
        return max(current_price * change_factor, 0.01)  # Ensure price doesn't go below 0.01

    def simulate_investment(self):
        """
        Simulates the dollar-cost averaging investment over the specified time period.
        """
        current_price = self.initial_price
        current_date = self.start_date

        while current_date <= self.end_date:
            # Simulate buying shares with the monthly investment amount
            shares_bought = self.monthly_investment / current_price
            self.total_shares += shares_bought
            self.total_invested += self.monthly_investment
            self.historic_prices.append(current_price)

            # Simulate price movements
            current_price = self.simulate_price(current_price)

            # Move to the next month
            current_date = self._get_next_month(current_date)

    def _get_next_month(self, date):
        """
        Increment the date by one month.

        :param date: Current date (datetime.date).
        :return: Next month's date (datetime.date).
        """
        month = date.month + 1
        year = date.year
        if month > 12:
            month = 1
            year += 1
        return datetime.date(year, month, date.day)

    def calculate_total_value(self):
        """
        Calculate the total value of the investment at the end of the simulation.

        :return: Total value of the investment (float).
        """
        final_price = self.historic_prices[-1]
        return self.total_shares * final_price

    def plot_investment_growth(self):
        """
        Plot the historic price of the asset over the investment period.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.historic_prices, label="Historic Asset Prices")
        plt.title("Investment Growth Using Dollar-Cost Averaging")
        plt.xlabel("Months")
        plt.ylabel("Asset Price ($)")
        plt.legend()
        plt.grid(True)
        plt.show()


def main():
    """
    Main function to run the Dollar-Cost Averaging Simulator.
    """
    # Define simulation parameters
    monthly_investment = 500  # $500 invested each month
    start_date = datetime.date(2020, 1, 1)  # Start date of the investment
    end_date = datetime.date(2025, 1, 1)  # End date of the investment
    initial_price = 100  # Initial asset price ($)
    volatility = 0.05  # 5% monthly volatility

    try:
        # Create and run simulator
        simulator = DollarCostAveragingSimulator(
            monthly_investment, start_date, end_date, initial_price, volatility
        )
        simulator.simulate_investment()

        # Calculate and display results
        total_value = simulator.calculate_total_value()
        print(f"Total Invested: ${simulator.total_invested:.2f}")
        print(f"Total Value of Investment: ${total_value:.2f}")
        print(f"Total Shares Owned: {simulator.total_shares:.2f}")

        # Plot investment growth
        simulator.plot_investment_growth()

    except Exception as e:
        print(f"An error occurred during simulation: {e}")


if __name__ == "__main__":
    main()
```
