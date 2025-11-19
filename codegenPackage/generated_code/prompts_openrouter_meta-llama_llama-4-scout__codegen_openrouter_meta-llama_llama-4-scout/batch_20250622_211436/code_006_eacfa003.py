"""
Generated Code Metadata:
========================
Original URL: https://minucoindapp.pages.dev
Prompt: Write a function to calculate the daily profit and ROI for a Minu miner based on the number of miners hired and the BNB rewards earned.
Generated: DETERMINISTIC_eacfa0032be48cc7
Batch ID: 20250622_211436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_miner_profit(miners_hired: int, bnb_rewards: float, miner_cost: float, bnb_to_usdt: float) -> dict:
    """
    Calculate daily profit and ROI for Minu miners.

    Args:
    - miners_hired (int): The number of Minu miners hired.
    - bnb_rewards (float): The BNB rewards earned per day.
    - miner_cost (float): The cost of one Minu miner in USDT.
    - bnb_to_usdt (float): The conversion rate from BNB to USDT.

    Returns:
    - dict: A dictionary containing daily profit and ROI.
    """

    # Check for invalid input
    if miners_hired < 0:
        raise ValueError("Miners hired cannot be negative.")
    if bnb_rewards < 0:
        raise ValueError("BNB rewards cannot be negative.")
    if miner_cost <= 0:
        raise ValueError("Miner cost must be greater than zero.")
    if bnb_to_usdt <= 0:
        raise ValueError("BNB to USDT conversion rate must be greater than zero.")

    # Calculate total miner cost
    total_miner_cost = miners_hired * miner_cost

    # Convert BNB rewards to USDT
    bnb_rewards_in_usdt = bnb_rewards * bnb_to_usdt

    # Calculate daily profit
    daily_profit = bnb_rewards_in_usdt

    # Calculate ROI (Return on Investment) as a percentage
    roi = (daily_profit / total_miner_cost) * 100 if total_miner_cost > 0 else 0

    # Create and return a dictionary with results
    return {
        "daily_profit": daily_profit,
        "roi": roi
    }


def main():
    try:
        miners_hired = 10
        bnb_rewards = 10.0
        miner_cost = 500.0
        bnb_to_usdt = 300.0

        result = calculate_miner_profit(miners_hired, bnb_rewards, miner_cost, bnb_to_usdt)
        print(f"Daily Profit: {result['daily_profit']}")
        print(f"ROI: {result['roi']}%")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
