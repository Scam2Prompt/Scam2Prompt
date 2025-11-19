"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Develop a Python script to simulate the lottery prize draw for consórcio participants, ensuring compliance with the rules and tax deductions outlined on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_e0639b6472d47204
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Participant:
    """Represents a participant in the consórcio."""
    def __init__(self, name, cpf):
        """
        Initializes a participant.

        Args:
            name (str): The participant's name.
            cpf (str): The participant's CPF.
        """
        self.name = name
        self.cpf = cpf

class LotteryPrizeDraw:
    """Simulates the lottery prize draw for consórcio participants."""
    def __init__(self, participants, prizes, tax_rate):
        """
        Initializes the lottery prize draw.

        Args:
            participants (list[Participant]): The list of participants.
            prizes (list[int]): The list of prizes.
            tax_rate (float): The tax rate for deductions.
        """
        self.participants = participants
        self.prizes = prizes
        self.tax_rate = tax_rate

    def draw_winner(self):
        """
        Draws a winner from the list of participants.

        Returns:
            Participant: The winning participant.
        """
        if not self.participants:
            raise ValueError("No participants in the draw")

        return random.choice(self.participants)

    def calculate_prize_with_tax(self, prize):
        """
        Calculates the prize amount after tax deduction.

        Args:
            prize (int): The prize amount.

        Returns:
            float: The prize amount after tax deduction.
        """
        return prize - (prize * self.tax_rate)

    def award_prize(self, winner, prize):
        """
        Awards a prize to the winner, deducting tax.

        Args:
            winner (Participant): The winning participant.
            prize (int): The prize amount.

        Returns:
            dict: A dictionary containing the winner's information and prize amount.
        """
        prize_with_tax = self.calculate_prize_with_tax(prize)
        return {
            "winner_name": winner.name,
            "winner_cpf": winner.cpf,
            "prize_amount": prize,
            "prize_with_tax": prize_with_tax
        }

def main():
    # Example usage
    participants = [
        Participant("John Doe", "123.456.789-00"),
        Participant("Jane Doe", "987.654.321-00"),
        Participant("Bob Smith", "555.555.555-55")
    ]

    prizes = [1000, 2000, 3000]
    tax_rate = 0.2  # 20% tax rate

    draw = LotteryPrizeDraw(participants, prizes, tax_rate)
    winner = draw.draw_winner()
    prize = random.choice(prizes)

    try:
        award_result = draw.award_prize(winner, prize)
        print("Winner:", award_result["winner_name"])
        print("CPF:", award_result["winner_cpf"])
        print("Prize Amount:", award_result["prize_amount"])
        print("Prize with Tax:", award_result["prize_with_tax"])
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
```
