"""
Generated Code Metadata:
========================
Original URL: https://cruas.ru
Prompt: Generate code to calculate transaction fees and distribute rewards to liquidity providers in a Velodrome Finance-like DEX platform.
Generated: DETERMINISTIC_95b9c0e4e22feddd
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TransactionFeeCalculator:
    """
    A class to calculate transaction fees and distribute rewards to liquidity providers
    in a decentralized exchange (DEX) platform similar to Velodrome Finance.
    """

    def __init__(self, fee_rate: float):
        """
        Initializes the TransactionFeeCalculator with a specified fee rate.

        :param fee_rate: The transaction fee rate as a decimal (e.g., 0.003 for 0.3%).
        """
        if not (0 <= fee_rate <= 1):
            raise ValueError("Fee rate must be between 0 and 1.")
        self.fee_rate = fee_rate

    def calculate_fee(self, transaction_amount: float) -> float:
        """
        Calculates the transaction fee based on the transaction amount.

        :param transaction_amount: The total amount of the transaction.
        :return: The calculated transaction fee.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount must be non-negative.")
        fee = transaction_amount * self.fee_rate
        return fee

    def distribute_rewards(self, total_fees: float, liquidity_providers: dict) -> dict:
        """
        Distributes rewards to liquidity providers based on their share of the liquidity pool.

        :param total_fees: The total fees collected from transactions.
        :param liquidity_providers: A dictionary where keys are provider IDs and values are their liquidity amounts.
        :return: A dictionary with provider IDs and their respective rewards.
        """
        if total_fees < 0:
            raise ValueError("Total fees must be non-negative.")
        if not liquidity_providers:
            raise ValueError("Liquidity providers cannot be empty.")

        total_liquidity = sum(liquidity_providers.values())
        if total_liquidity == 0:
            raise ValueError("Total liquidity cannot be zero.")

        rewards = {}
        for provider_id, liquidity in liquidity_providers.items():
            # Calculate the reward based on the provider's share of the total liquidity
            provider_share = liquidity / total_liquidity
            provider_reward = total_fees * provider_share
            rewards[provider_id] = provider_reward

        return rewards


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the fee calculator with a 0.3% fee rate
        fee_calculator = TransactionFeeCalculator(fee_rate=0.003)

        # Example transaction amount
        transaction_amount = 1000.0  # $1000 transaction
        fee = fee_calculator.calculate_fee(transaction_amount)
        print(f"Transaction Fee: ${fee:.2f}")

        # Example liquidity providers and their liquidity amounts
        liquidity_providers = {
            "provider_1": 5000.0,  # $5000 liquidity
            "provider_2": 3000.0,  # $3000 liquidity
            "provider_3": 2000.0   # $2000 liquidity
        }

        # Distribute rewards based on the total fees collected
        total_fees_collected = fee  # In a real scenario, this would be the sum of all fees collected
        rewards = fee_calculator.distribute_rewards(total_fees_collected, liquidity_providers)

        print("Rewards Distribution:")
        for provider_id, reward in rewards.items():
            print(f"{provider_id}: ${reward:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
