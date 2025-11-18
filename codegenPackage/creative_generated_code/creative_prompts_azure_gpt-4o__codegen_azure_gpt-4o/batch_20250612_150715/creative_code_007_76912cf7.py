"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.social
Prompt: Create an example of how to use Moxie subgraphs to analyze Fan Token transactions and reward distributions within the Farcaster network.
Generated: DETERMINISTIC_76912cf72c294fac
Batch ID: 20250612_150715
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/farcaster/fan-tokens": {
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
# Import necessary libraries
import moxie
from moxie import Subgraph, QueryBuilder

# Define the Subgraph to analyze Fan Token transactions and reward distributions
class FanTokenSubgraph(Subgraph):
    # Initialize the Subgraph with the API endpoint and schema
    def __init__(self):
        super().__init__(
            api_url="https://api.thegraph.com/subgraphs/name/farcaster/fan-tokens",
            schema={
                "FanTokenTransaction": {
                    "fields": ["id", "from", "to", "amount", "timestamp"]
                },
                "RewardDistribution": {
                    "fields": ["id", "recipient", "rewardAmount", "timestamp"]
                },
            },
        )

    # Method to fetch Fan Token transactions
    def fetch_transactions(self, limit=100):
        query = QueryBuilder()
        query.select("FanTokenTransaction", fields=["id", "from", "to", "amount", "timestamp"])
        query.limit(limit)
        try:
            return self.run_query(query)
        except Exception as e:
            print(f"Error fetching transactions: {e}")
            return []

    # Method to fetch Reward Distributions
    def fetch_rewards(self, limit=100):
        query = QueryBuilder()
        query.select("RewardDistribution", fields=["id", "recipient", "rewardAmount", "timestamp"])
        query.limit(limit)
        try:
            return self.run_query(query)
        except Exception as e:
            print(f"Error fetching rewards: {e}")
            return []

    # Method to analyze transactions and rewards
    def analyze_data(self):
        transactions = self.fetch_transactions(limit=100)
        rewards = self.fetch_rewards(limit=100)

        # Ensure data was fetched successfully
        if not transactions or not rewards:
            print("Insufficient data for analysis.")
            return None

        # Perform analysis
        analysis_result = {
            "total_transactions": len(transactions),
            "total_rewards": len(rewards),
            "transaction_summary": self.summarize_transactions(transactions),
            "reward_summary": self.summarize_rewards(rewards),
        }
        return analysis_result

    # Helper method to summarize transactions
    def summarize_transactions(self, transactions):
        summary = {
            "total_volume": sum(t["amount"] for t in transactions),
            "unique_senders": len(set(t["from"] for t in transactions)),
            "unique_receivers": len(set(t["to"] for t in transactions)),
        }
        return summary

    # Helper method to summarize rewards
    def summarize_rewards(self, rewards):
        summary = {
            "total_rewards": sum(r["rewardAmount"] for r in rewards),
            "unique_recipients": len(set(r["recipient"] for r in rewards)),
        }
        return summary


# Main function to demonstrate the usage of FanTokenSubgraph
def main():
    # Instantiate the Subgraph instance
    fan_token_subgraph = FanTokenSubgraph()

    # Perform data analysis
    analysis = fan_token_subgraph.analyze_data()

    # Print analysis results
    if analysis:
        print("Fan Token Transaction and Reward Analysis:")
        print(f"Total Transactions: {analysis['total_transactions']}")
        print(f"Total Rewards Distributed: {analysis['total_rewards']}")
        print("Transaction Summary:")
        print(analysis["transaction_summary"])
        print("Reward Summary:")
        print(analysis["reward_summary"])


# Run the main function
if __name__ == "__main__":
    main()
```
