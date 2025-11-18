"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-wienerdogs.pages.dev
Prompt: Generate a Python script to calculate the percentage of $WAI tokens staked and total rewards earned based on the data provided by WienerAI.
Generated: DETERMINISTIC_feccf3e437386b43
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the percentage of $WAI tokens staked and total rewards earned
based on data provided by WienerAI.

Author: Expert Programmer
Date: YYYY-MM-DD

Requirements:
- Python 3.x
"""

import json

def calculate_staking_metrics(data):
    """
    Calculates the percentage of $WAI tokens staked and total rewards earned.

    Args:
        data (dict): A dictionary containing staking and reward information.

    Returns:
        dict: A dictionary with staking percentage and total rewards.
    """
    try:
        # Extract total tokens and staked tokens
        total_tokens = data.get("total_tokens", 0)
        staked_tokens = data.get("staked_tokens", 0)
        rewards = data.get("rewards", [])

        if total_tokens <= 0:
            raise ValueError("Invalid total token amount. Total tokens must be greater than 0.")

        # Calculate staking percentage
        staking_percentage = (staked_tokens / total_tokens) * 100

        # Calculate total rewards earned
        total_rewards = sum(rewards)

        return {
            "staking_percentage": staking_percentage,
            "total_rewards": total_rewards
        }
    except (TypeError, ValueError) as e:
        # Handle errors and provide user-friendly feedback
        return {"error": str(e)}

def main():
    """
    Main function to load data and calculate staking metrics.
    """
    try:
        # Sample data from WienerAI (replace with actual data source if needed)
        sample_data = """
        {
            "total_tokens": 100000,
            "staked_tokens": 75000,
            "rewards": [100, 250, 500, 300]
        }
        """
        
        # Parse JSON data
        data = json.loads(sample_data)

        # Calculate staking metrics
        metrics = calculate_staking_metrics(data)

        # Handle calculation errors
        if "error" in metrics:
            print(f"Error: {metrics['error']}")
        else:
            # Print results
            print(f"Percentage of $WAI Tokens Staked: {metrics['staking_percentage']:.2f}%")
            print(f"Total Rewards Earned: {metrics['total_rewards']} $WAI")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data. Please check the data format.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
