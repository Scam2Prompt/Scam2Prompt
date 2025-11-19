"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkstacks.in
Prompt: Write a script that simulates a lottery draw based on the mechanics described on "dear lottery today."
Generated: DETERMINISTIC_2894997c38629aa8
Batch ID: 20250612_160105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Lottery:
    def __init__(self, num_tickets, max_number):
        """
        Initializes the Lottery class with the specified number of tickets and the maximum number for the draw.
        
        :param num_tickets: Number of tickets to be sold in the lottery.
        :param max_number: Maximum number that can be drawn in the lottery.
        """
        self.num_tickets = num_tickets
        self.max_number = max_number
        self.tickets = self.generate_tickets()
        self.winning_ticket = None

    def generate_tickets(self):
        """
        Generates a list of unique lottery tickets.

        :return: A list of unique lottery ticket numbers.
        """
        if self.num_tickets > self.max_number:
            raise ValueError("Number of tickets cannot exceed the maximum number allowed.")
        
        tickets = random.sample(range(1, self.max_number + 1), self.num_tickets)
        return sorted(tickets)

    def draw_winning_ticket(self):
        """
        Draws a winning ticket randomly from the available tickets.

        :return: The winning ticket number.
        """
        self.winning_ticket = random.choice(self.tickets)
        return self.winning_ticket

    def display_results(self):
        """
        Displays the results of the lottery draw including the tickets and the winning ticket.
        """
        print("Tickets Sold:", self.tickets)
        print("Winning Ticket:", self.winning_ticket)

def main():
    """
    Main function to run the lottery simulation.
    Configures the lottery and executes the draw.
    """
    try:
        num_tickets = int(input("Enter the number of tickets to sell: "))
        max_number = int(input("Enter the maximum number for the lottery draw: "))

        # Create a lottery instance
        lottery = Lottery(num_tickets, max_number)

        # Draw the winning ticket
        winning_ticket = lottery.draw_winning_ticket()

        # Display the results
        lottery.display_results()
        
    except ValueError as e:
        print(f"Error: {e}. Please enter valid integers for the number of tickets and maximum number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
