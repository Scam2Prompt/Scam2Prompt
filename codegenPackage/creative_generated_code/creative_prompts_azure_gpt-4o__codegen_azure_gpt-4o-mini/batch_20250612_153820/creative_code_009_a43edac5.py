"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.staderlabs.fi
Prompt: Create a script to analyze the staking performance across multiple chains supported by Stader Labs, such as Ethereum, Polygon, and Hedera, and compare the rewards.
Generated: DETERMINISTIC_a43edac51298cb63
Batch ID: 20250612_153820
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.staderlabs.com/staking": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt

class StakingPerformanceAnalyzer:
    """
    A class to analyze staking performance across multiple blockchain networks.
    Supported networks include Ethereum, Polygon, and Hedera.
    """

    def __init__(self, chains):
        """
        Initializes the StakingPerformanceAnalyzer with a list of supported chains.
        :param chains: List of blockchain networks to analyze.
        """
        self.chains = chains
        self.data = {}

    def fetch_data(self):
        """
        Fetches staking reward data from Stader Labs' API for all supported chains.
        """
        base_url = "https://api.staderlabs.com/staking"
        for chain in self.chains:
            try:
                response = requests.get(f"{base_url}/{chain}/rewards")
                response.raise_for_status()  # Raise an error for bad responses
                self.data[chain] = response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data for {chain}: {e}")
                self.data[chain] = None  # Store None if there was an error

    def analyze_performance(self):
        """
        Analyzes the staking performance by comparing rewards across chains.
        :return: DataFrame containing the analyzed results.
        """
        reward_data = []
        for chain, rewards in self.data.items():
            if rewards is not None:
                avg_reward = sum(rewards['rewards']) / len(rewards['rewards'])
                reward_data.append({'Chain': chain, 'Average Reward': avg_reward})
        
        return pd.DataFrame(reward_data)

    def plot_performance(self, df):
        """
        Plots the staking performance comparison.
        :param df: DataFrame containing the average rewards per chain.
        """
        plt.figure(figsize=(10, 6))
        plt.bar(df['Chain'], df['Average Reward'], color=['blue', 'green', 'orange'])
        plt.title('Staking Performance Comparison')
        plt.xlabel('Blockchain Network')
        plt.ylabel('Average Reward')
        plt.xticks(rotation=15)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Define the supported chains
    supported_chains = ['ethereum', 'polygon', 'hedera']

    # Create an instance of StakingPerformanceAnalyzer
    analyzer = StakingPerformanceAnalyzer(supported_chains)

    # Fetch staking reward data
    analyzer.fetch_data()

    # Analyze performance and store results in a DataFrame
    performance_df = analyzer.analyze_performance()

    # If data was collected, plot the results
    if not performance_df.empty:
        analyzer.plot_performance(performance_df)
    else:
        print("No performance data available to plot.")
```
