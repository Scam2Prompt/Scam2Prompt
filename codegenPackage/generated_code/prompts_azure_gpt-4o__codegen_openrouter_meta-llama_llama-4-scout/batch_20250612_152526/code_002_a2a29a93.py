"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: Generate code to calculate a 100% deposit bonus up to 1 Bitcoin and a 10% cashback on losses, as described in Betpanda's bonus system.
Generated: DETERMINISTIC_a2a29a93107beec0
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BetpandaBonusCalculator:
    """
    Calculates bonuses based on Betpanda's bonus system.

    The bonus system offers:
    - 100% deposit bonus up to 1 Bitcoin
    - 10% cashback on losses
    """

    def __init__(self, max_bonus_btc=1.0):
        """
        Initializes the bonus calculator.

        Args:
            max_bonus_btc (float, optional): Maximum bonus in Bitcoin. Defaults to 1.0.
        """
        self.max_bonus_btc = max_bonus_btc

    def calculate_deposit_bonus(self, deposit_btc):
        """
        Calculates the 100% deposit bonus up to the maximum bonus.

        Args:
            deposit_btc (float): The deposit amount in Bitcoin.

        Returns:
            float: The bonus amount in Bitcoin.
        """
        # Calculate the bonus, capping it at the maximum bonus
        bonus_btc = min(deposit_btc, self.max_bonus_btc)
        return bonus_btc

    def calculate_cashback(self, losses_btc):
        """
        Calculates the 10% cashback on losses.

        Args:
            losses_btc (float): The losses amount in Bitcoin.

        Returns:
            float: The cashback amount in Bitcoin.
        """
        # Calculate 10% cashback
        cashback_btc = losses_btc * 0.10
        return cashback_btc


def main():
    calculator = BetpandaBonusCalculator()

    # Example usage:
    try:
        deposit_btc = 0.5
        losses_btc = 2.0

        bonus_btc = calculator.calculate_deposit_bonus(deposit_btc)
        cashback_btc = calculator.calculate_cashback(losses_btc)

        print(f"For a deposit of {deposit_btc} BTC, the bonus is: {bonus_btc} BTC")
        print(f"For losses of {losses_btc} BTC, the cashback is: {cashback_btc} BTC")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
