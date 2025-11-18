"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Develop a Python script to simulate the lottery prize draw for consórcio participants, ensuring compliance with the rules and tax deductions outlined on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_e0639b6472d47204
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ConsorcioLottery:
    def __init__(self, participants, prize_amount, tax_rate):
        """
        Initializes the ConsorcioLottery with participants, prize amount, and tax rate.
        
        :param participants: List of participant names.
        :param prize_amount: Total prize amount before tax deduction.
        :param tax_rate: Tax rate to apply on the prize.
        """
        self.participants = participants
        self.prize_amount = prize_amount
        self.tax_rate = tax_rate

    def draw_winner(self):
        """
        Randomly selects a winner from the participants and calculates the net prize amount after tax.
        
        :return: Tuple containing the winner's name and the net prize amount.
        """
        if not self.participants:
            raise ValueError("No participants available for the lottery.")

        winner = random.choice(self.participants)
        net_prize = self.calculate_net_prize(self.prize_amount, self.tax_rate)
        return winner, net_prize

    @staticmethod
    def calculate_net_prize(prize_amount, tax_rate):
        """
        Calculates the net prize amount after applying the tax rate.
        
        :param prize_amount: The total prize amount before tax.
        :param tax_rate: The tax rate to apply.
        :return: The net prize amount after tax deduction.
        """
        if prize_amount < 0:
            raise ValueError("Prize amount must be non-negative.")
        if not (0 <= tax_rate <= 1):
            raise ValueError("Tax rate must be between 0 and 1.")

        tax_deduction = prize_amount * tax_rate
        return prize_amount - tax_deduction

def main():
    """
    Main function to simulate the lottery prize draw.
    """
    # Example participants
    participants = ["Alice", "Bob", "Charlie", "Diana"]
    
    # Prize amount and tax rate as per Consórcio Chevrolet guidelines
    prize_amount = 10000.00  # Example prize amount
    tax_rate = 0.15  # 15% tax rate

    try:
        lottery = ConsorcioLottery(participants, prize_amount, tax_rate)
        winner, net_prize = lottery.draw_winner()
        print(f"The winner is: {winner}")
        print(f"The net prize amount after tax is: {net_prize:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
