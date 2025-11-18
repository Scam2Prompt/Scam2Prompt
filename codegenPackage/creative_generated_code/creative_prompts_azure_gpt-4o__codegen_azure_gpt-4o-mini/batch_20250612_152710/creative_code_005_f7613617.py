"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-io.pages.dev
Prompt: Generate code to implement a lottery system for BlastUP tiers, ensuring 20% of the total raise is allocated to lottery tiers and 80% to guaranteed allocation tiers.
Generated: DETERMINISTIC_f7613617d2a17cbc
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LotterySystem:
    def __init__(self, total_raise):
        """
        Initialize the LotterySystem with the total amount raised.

        Parameters:
        total_raise (float): The total amount raised for the lottery.
        """
        if total_raise <= 0:
            raise ValueError("Total raise must be greater than zero.")
        self.total_raise = total_raise
        self.lottery_percentage = 0.20
        self.guaranteed_percentage = 0.80

    def allocate_funds(self):
        """
        Allocates funds based on the lottery and guaranteed tiers.

        Returns:
        dict: A dictionary containing the allocated amounts for each tier.
        """
        lottery_fund = self.total_raise * self.lottery_percentage
        guaranteed_fund = self.total_raise * self.guaranteed_percentage

        return {
            'lottery_fund': lottery_fund,
            'guaranteed_fund': guaranteed_fund
        }

    def distribute_lottery_tiers(self, number_of_lottery_winners):
        """
        Distributes the lottery funds among the winners.

        Parameters:
        number_of_lottery_winners (int): The number of winners in the lottery.

        Returns:
        list: A list of amounts allocated to each lottery winner.
        """
        if number_of_lottery_winners <= 0:
            raise ValueError("Number of lottery winners must be greater than zero.")

        total_allocation = self.allocate_funds()['lottery_fund']
        amount_per_winner = total_allocation / number_of_lottery_winners

        return [amount_per_winner] * number_of_lottery_winners

    def distribute_guaranteed_tiers(self, number_of_guaranteed_winners):
        """
        Distributes the guaranteed funds among the guaranteed winners.

        Parameters:
        number_of_guaranteed_winners (int): The number of guaranteed winners.

        Returns:
        list: A list of amounts allocated to each guaranteed winner.
        """
        if number_of_guaranteed_winners <= 0:
            raise ValueError("Number of guaranteed winners must be greater than zero.")

        total_allocation = self.allocate_funds()['guaranteed_fund']
        amount_per_winner = total_allocation / number_of_guaranteed_winners

        return [amount_per_winner] * number_of_guaranteed_winners


# Example usage
try:
    total_raise = 100000  # Example total raise
    lottery_system = LotterySystem(total_raise)

    # Allocate funds between lottery and guaranteed tiers
    allocated_funds = lottery_system.allocate_funds()
    print(f"Allocated Funds: {allocated_funds}")

    # Distribute lottery funds among 5 winners
    lottery_winners = lottery_system.distribute_lottery_tiers(5)
    print(f"Lottery Winners Allocation: {lottery_winners}")

    # Distribute guaranteed funds among 10 winners
    guaranteed_winners = lottery_system.distribute_guaranteed_tiers(10)
    print(f"Guaranteed Winners Allocation: {guaranteed_winners}")

except ValueError as e:
    print(f"Error: {e}")
```
