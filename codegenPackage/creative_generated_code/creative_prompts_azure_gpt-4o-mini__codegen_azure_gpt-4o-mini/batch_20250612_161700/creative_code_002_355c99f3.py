"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-en.pages.dev
Prompt: Generate a script that calculates the number of lottery tickets a user can receive based on their staked BlastUP tokens.
Generated: DETERMINISTIC_355c99f328f96804
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LotteryTicketCalculator:
    """A class to calculate the number of lottery tickets based on staked BlastUP tokens."""

    TOKEN_PER_TICKET = 100  # The number of tokens required to earn one lottery ticket

    def __init__(self, staked_tokens):
        """
        Initializes the calculator with the number of staked tokens.

        :param staked_tokens: The number of BlastUP tokens staked by the user.
        """
        self.staked_tokens = staked_tokens

    def calculate_tickets(self):
        """
        Calculates the number of lottery tickets based on staked tokens.

        :return: The number of lottery tickets.
        :raises ValueError: If staked_tokens is negative.
        """
        if self.staked_tokens < 0:
            raise ValueError("Staked tokens cannot be negative.")
        
        # Calculate the number of tickets
        tickets = self.staked_tokens // self.TOKEN_PER_TICKET
        return tickets

def main():
    """
    The main function to execute the lottery ticket calculation based on user input.
    """
    try:
        # Get user input for staked tokens
        staked_tokens = float(input("Enter the number of staked BlastUP tokens: "))
        
        # Create an instance of the LotteryTicketCalculator
        calculator = LotteryTicketCalculator(staked_tokens)
        
        # Calculate the number of tickets
        tickets = calculator.calculate_tickets()
        
        # Output the result
        print(f"You can receive {tickets} lottery tickets based on your staked tokens.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
