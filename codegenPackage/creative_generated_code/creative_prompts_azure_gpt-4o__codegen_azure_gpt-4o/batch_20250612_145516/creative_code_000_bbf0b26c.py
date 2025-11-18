"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Write a Python script to simulate the investment strategy timeline described on the SUI Strategies website, including the percentage allocations for SUI, APT, SOL, BTC, and USD across different quarters from 2024 to 2026.
Generated: DETERMINISTIC_bbf0b26ce389b095
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd


class InvestmentStrategySimulator:
    """
    Simulates an investment strategy timeline with percentage allocations across assets.

    Attributes:
        strategy_data (list): List of dictionaries containing quarter and percentage allocations.
    """

    def __init__(self):
        """
        Initializes the InvestmentStrategySimulator with the predefined allocation strategy.
        """
        self.strategy_data = [
            # Each entry represents allocation percentages for a specific quarter
            {"Quarter": "Q1 2024", "SUI": 40, "APT": 20, "SOL": 20, "BTC": 10, "USD": 10},
            {"Quarter": "Q2 2024", "SUI": 35, "APT": 25, "SOL": 20, "BTC": 10, "USD": 10},
            {"Quarter": "Q3 2024", "SUI": 30, "APT": 25, "SOL": 25, "BTC": 10, "USD": 10},
            {"Quarter": "Q4 2024", "SUI": 25, "APT": 25, "SOL": 30, "BTC": 10, "USD": 10},
            {"Quarter": "Q1 2025", "SUI": 20, "APT": 30, "SOL": 30, "BTC": 10, "USD": 10},
            {"Quarter": "Q2 2025", "SUI": 15, "APT": 30, "SOL": 35, "BTC": 10, "USD": 10},
            {"Quarter": "Q3 2025", "SUI": 10, "APT": 35, "SOL": 35, "BTC": 10, "USD": 10},
            {"Quarter": "Q4 2025", "SUI": 10, "APT": 30, "SOL": 40, "BTC": 10, "USD": 10},
            {"Quarter": "Q1 2026", "SUI": 5, "APT": 30, "SOL": 45, "BTC": 10, "USD": 10},
            {"Quarter": "Q2 2026", "SUI": 5, "APT": 25, "SOL": 50, "BTC": 10, "USD": 10},
            {"Quarter": "Q3 2026", "SUI": 5, "APT": 20, "SOL": 55, "BTC": 10, "USD": 10},
            {"Quarter": "Q4 2026", "SUI": 5, "APT": 15, "SOL": 60, "BTC": 10, "USD": 10},
        ]

    def generate_strategy_dataframe(self):
        """
        Generates a Pandas DataFrame representing the investment strategy timeline.

        Returns:
            pd.DataFrame: DataFrame with allocation data for each quarter.
        """
        try:
            # Convert strategy data to a DataFrame
            df = pd.DataFrame(self.strategy_data)
            return df
        except Exception as e:
            print(f"Error generating strategy DataFrame: {e}")
            raise

    def save_to_csv(self, filename="investment_strategy_timeline.csv"):
        """
        Saves the investment strategy timeline to a CSV file.

        Args:
            filename (str, optional): The name of the CSV file. Defaults to 'investment_strategy_timeline.csv'.
        """
        try:
            df = self.generate_strategy_dataframe()
            df.to_csv(filename, index=False)
            print(f"Investment strategy timeline saved to {filename}")
        except Exception as e:
            print(f"Error saving strategy to CSV: {e}")
            raise


if __name__ == "__main__":
    # Instantiate the simulator and run the simulation
    simulator = InvestmentStrategySimulator()

    # Generate the DataFrame and print it for verification
    strategy_df = simulator.generate_strategy_dataframe()
    print(strategy_df)

    # Save the DataFrame to a CSV file
    simulator.save_to_csv()
```
