"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdcprinter.xyz
Prompt: What are the tokenomics of the $UPRINT token, and how does the 5% buy/sell tax contribute to USDC rewards for holders?
Generated: DETERMINISTIC_8b7cf35774f58f64
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tokenomics of $UPRINT Token:
- $UPRINT token applies a 5% buy/sell tax on transactions.
- Tax proceeds are distributed as rewards in USDC to token holders proportionally based on their token holdings.

This script demonstrates how the 5% tax is calculated and distributed to holders as USDC rewards.
"""

class UPrintTokenomics:
    def __init__(self, total_supply, holders):
        """
        Initialize tokenomics for $UPRINT.

        :param total_supply: The total supply of $UPRINT tokens (integer).
        :param holders: A dictionary where keys are holder addresses and values are their $UPRINT balances.
        """
        self.total_supply = total_supply
        self.holders = holders
        self.buy_sell_tax_rate = 0.05  # 5% tax rate

    def calculate_tax(self, transaction_amount):
        """
        Calculate the 5% tax on buy/sell transactions.

        :param transaction_amount: Amount of $UPRINT being transacted (integer).
        :return: The tax amount (integer).
        """
        return transaction_amount * self.buy_sell_tax_rate

    def distribute_rewards(self, tax_amount):
        """
        Distribute the collected tax amount as USDC rewards to holders.

        :param tax_amount: Total tax amount collected (integer).
        :return: A dictionary representing the USDC rewards distributed to each holder.
        """
        total_holder_balance = sum(self.holders.values())
        if total_holder_balance == 0:
            raise ValueError("No holders available for distribution.")

        rewards = {}
        for holder, balance in self.holders.items():
            # Calculate proportional reward based on holder's token balance
            rewards[holder] = (balance / total_holder_balance) * tax_amount
        return rewards

    def simulate_transaction(self, transaction_amount):
        """
        Simulate a buy/sell transaction and demonstrate tax and reward distribution.

        :param transaction_amount: Amount of $UPRINT being transacted (integer).
        :return: A dictionary of USDC rewards distributed to holders.
        """
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        tax = self.calculate_tax(transaction_amount)
        rewards = self.distribute_rewards(tax)

        return {
            'transaction_amount': transaction_amount,
            'tax_collected': tax,
            'usdc_rewards': rewards
        }


# Example Usage
if __name__ == "__main__":
    # Define total supply and initial holder balances
    total_supply = 1000000  # 1,000,000 $UPRINT tokens
    holders = {
        "holder1": 50000,   # Holder1 owns 50,000 tokens
        "holder2": 100000,  # Holder2 owns 100,000 tokens
        "holder3": 150000,  # Holder3 owns 150,000 tokens
    }

    # Initialize tokenomics
    tokenomics = UPrintTokenomics(total_supply, holders)

    # Simulate a transaction
    transaction_amount = 10000  # Example: 10,000 $UPRINT tokens transacted
    try:
        result = tokenomics.simulate_transaction(transaction_amount)
        print("Transaction Results:")
        print(f"Transaction Amount: {result['transaction_amount']} $UPRINT")
        print(f"Tax Collected: {result['tax_collected']} $UPRINT (converted to USDC for rewards)")
        print("USDC Rewards Distributed:")
        for holder, reward in result['usdc_rewards'].items():
            print(f"{holder}: {reward} USDC")
    except ValueError as e:
        print(f"Error: {e}")
```
