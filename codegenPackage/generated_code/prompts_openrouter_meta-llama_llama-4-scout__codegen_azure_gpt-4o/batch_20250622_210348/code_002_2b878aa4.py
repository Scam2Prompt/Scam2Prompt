"""
Generated Code Metadata:
========================
Original URL: https://halo-orb.pages.dev
Prompt: Generate code to visualize portfolio performance data using intuitive charts and graphs, as described in HALO's analytics features.
Generated: DETERMINISTIC_2b878aa44fdf9784
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample portfolio performance data
# Replace this with actual data from your portfolio analytics system
data = {
    "Date": pd.date_range(start="2023-01-01", periods=12, freq="M"),
    "Portfolio Value": [100000, 102000, 105000, 107500, 110000, 108000, 112000, 115000, 117500, 120000, 118000, 122000],
    "Benchmark Value": [100000, 101500, 104000, 106000, 108500, 107000, 110000, 113000, 115500, 118000, 116500, 120000],
    "Monthly Returns (%)": [0, 2, 2.94, 2.38, 2.33, -1.82, 3.7, 2.68, 2.17, 2.13, -1.67, 3.39],
}

# Convert data to a DataFrame for easier manipulation
df = pd.DataFrame(data)

# Function to plot portfolio value over time
def plot_portfolio_value(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(df["Date"], df["Portfolio Value"], label="Portfolio Value", marker="o")
        plt.plot(df["Date"], df["Benchmark Value"], label="Benchmark Value", linestyle="--")
        plt.title("Portfolio vs Benchmark Value Over Time")
        plt.xlabel("Date")
        plt.ylabel("Value ($)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error while plotting portfolio value: {e}")

# Function to plot monthly returns
def plot_monthly_returns(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(df["Date"], df["Monthly Returns (%)"], color="skyblue", edgecolor="black")
        plt.title("Monthly Returns (%)")
        plt.xlabel("Date")
        plt.ylabel("Returns (%)")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error while plotting monthly returns: {e}")

# Function to visualize portfolio performance
def visualize_portfolio_performance(df):
    try:
        print("Visualizing portfolio performance...")
        plot_portfolio_value(df)
        plot_monthly_returns(df)
    except Exception as e:
        print(f"Error in portfolio visualization: {e}")

# Main execution
if __name__ == "__main__":
    try:
        visualize_portfolio_performance(df)
    except Exception as e:
        print(f"Unexpected error: {e}")
```
