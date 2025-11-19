"""
Generated Code Metadata:
========================
Original URL: https://propsfundedtrader.com
Prompt: "Write a Python script to calculate the profit split for a funded trader with a $100,000 account size and a 10% monthly return, assuming a 30% profit split rate for the service provider."
Generated: DETERMINISTIC_3df66b2da0716dab
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# profit_split_calculator.py

def calculate_profit_split(account_size: float, monthly_return: float, profit_split_rate: float) -> dict:
    """
    Calculates the profit split for a funded trader.

    Args:
    - account_size (float): The size of the trading account.
    - monthly_return (float): The monthly return as a decimal.
    - profit_split_rate (float): The profit split rate as a decimal.

    Returns:
    - dict: A dictionary containing the profit split details.
    """

    # Calculate the monthly profit
    monthly_profit = account_size * monthly_return

    # Calculate the profit share for the service provider
    service_provider_share = monthly_profit * profit_split_rate

    # Calculate the profit share for the trader
    trader_share = monthly_profit - service_provider_share

    # Create a dictionary to store the profit split details
    profit_split_details = {
        "account_size": account_size,
        "monthly_return": monthly_return * 100,  # Convert to percentage
        "monthly_profit": monthly_profit,
        "profit_split_rate": profit_split_rate * 100,  # Convert to percentage
        "service_provider_share": service_provider_share,
        "trader_share": trader_share,
    }

    return profit_split_details


def main():
    try:
        # Define the input parameters
        account_size = 100000  # $100,000
        monthly_return = 0.10  # 10% monthly return
        profit_split_rate = 0.30  # 30% profit split rate

        # Calculate the profit split
        profit_split_details = calculate_profit_split(account_size, monthly_return, profit_split_rate)

        # Print the profit split details
        print("Profit Split Details:")
        print(f"Account Size: ${profit_split_details['account_size']:.2f}")
        print(f"Monthly Return: {profit_split_details['monthly_return']}%")
        print(f"Monthly Profit: ${profit_split_details['monthly_profit']:.2f}")
        print(f"Profit Split Rate: {profit_split_details['profit_split_rate']}%")
        print(f"Service Provider Share: ${profit_split_details['service_provider_share']:.2f}")
        print(f"Trader Share: ${profit_split_details['trader_share']:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
