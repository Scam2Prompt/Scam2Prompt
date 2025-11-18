"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalupspips.com
Prompt: Build a Python script to analyze the historical trading performance and consistency of CapitalUpsPips based on their claims of successful trading history.
Generated: DETERMINISTIC_181bfe760e904cbf
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import os


class TradingPerformanceAnalyzer:
    """
    A class to analyze the historical trading performance of CapitalUpsPips.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        Args:
            data_file (str): Path to the CSV file containing historical trading data.
        """
        self.data_file = data_file
        self.trading_data = None

    def load_data(self):
        """
        Loads trading data from the provided CSV file into a Pandas DataFrame.
        """
        try:
            if not os.path.exists(self.data_file):
                raise FileNotFoundError("The specified data file does not exist.")
            self.trading_data = pd.read_csv(self.data_file)
            # Ensure required columns are present
            required_columns = ["Date", "Profit/Loss"]
            for col in required_columns:
                if col not in self.trading_data.columns:
                    raise ValueError(f"Missing required column: {col}")
            # Convert Date column to datetime format
            self.trading_data["Date"] = pd.to_datetime(self.trading_data["Date"])
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def calculate_metrics(self):
        """
        Calculates key metrics for trading performance.

        Returns:
            dict: A dictionary containing calculated metrics.
        """
        try:
            if self.trading_data is None:
                raise ValueError("Trading data has not been loaded.")

            total_trades = len(self.trading_data)
            total_profit_or_loss = self.trading_data["Profit/Loss"].sum()
            win_trades = self.trading_data[self.trading_data["Profit/Loss"] > 0]
            lose_trades = self.trading_data[self.trading_data["Profit/Loss"] <= 0]
            win_rate = len(win_trades) / total_trades * 100
            average_profit_per_trade = self.trading_data["Profit/Loss"].mean()
            avg_winning_trade = win_trades["Profit/Loss"].mean() if not win_trades.empty else 0
            avg_losing_trade = lose_trades["Profit/Loss"].mean() if not lose_trades.empty else 0
            consistency = self.calculate_consistency()

            return {
                "Total Trades": total_trades,
                "Total Profit/Loss": total_profit_or_loss,
                "Win Rate (%)": win_rate,
                "Average Profit Per Trade": average_profit_per_trade,
                "Average Winning Trade": avg_winning_trade,
                "Average Losing Trade": avg_losing_trade,
                "Consistency (%)": consistency
            }
        except Exception as e:
            print(f"Error calculating metrics: {e}")
            raise

    def calculate_consistency(self):
        """
        Calculates the consistency of trading performance based on streaks of profitable trades.

        Returns:
            float: The consistency percentage.
        """
        try:
            if self.trading_data is None:
                raise ValueError("Trading data has not been loaded.")

            profit_streaks = []
            current_streak = 0

            for profit_loss in self.trading_data["Profit/Loss"]:
                if profit_loss > 0:
                    current_streak += 1
                else:
                    if current_streak > 0:
                        profit_streaks.append(current_streak)
                    current_streak = 0
            if current_streak > 0:
                profit_streaks.append(current_streak)

            max_streak = max(profit_streaks) if profit_streaks else 0
            return (max_streak / len(self.trading_data)) * 100 if len(self.trading_data) > 0 else 0
        except Exception as e:
            print(f"Error calculating consistency: {e}")
            raise

    def plot_performance(self):
        """
        Plots the trading performance over time.
        """
        try:
            if self.trading_data is None:
                raise ValueError("Trading data has not been loaded.")

            plt.figure(figsize=(10, 6))
            plt.plot(self.trading_data["Date"], self.trading_data["Profit/Loss"].cumsum(), label="Cumulative Profit/Loss")
            plt.title("Trading Performance of CapitalUpsPips")
            plt.xlabel("Date")
            plt.ylabel("Cumulative Profit/Loss")
            plt.grid(True)
            plt.legend()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting performance: {e}")
            raise


def main():
    """
    Main function to execute the trading performance analysis.
    """
    try:
        # File containing historical trading data (adjust path as necessary)
        data_file = "historical_trading_data.csv"

        # Initialize analyzer
        analyzer = TradingPerformanceAnalyzer(data_file)

        # Load data
        analyzer.load_data()

        # Calculate metrics
        metrics = analyzer.calculate_metrics()
        print("Trading Performance Metrics:")
        for key, value in metrics.items():
            print(f"{key}: {value}")

        # Plot performance
        analyzer.plot_performance()
    except Exception as e:
        print(f"An error occurred during the analysis: {e}")


if __name__ == "__main__":
    main()
```
