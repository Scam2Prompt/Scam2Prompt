"""
Generated Code Metadata:
========================
Original URL: https://jellybabiesnft.web.app
Prompt: How can I develop a lottery system for NFTs akin to the Jellotto feature from the Jelly Babies NFT project?
Generated: DETERMINISTIC_1b7fca685e3785e7
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from datetime import datetime

class NFTLottery:
    """
    A class to represent an NFT lottery system.
    """

    def __init__(self, ticket_price, prize_pool, max_tickets):
        """
        Initialize the lottery system.

        :param ticket_price: Price of a single ticket (in cryptocurrency or fiat).
        :param prize_pool: Total prize pool for the lottery.
        :param max_tickets: Maximum number of tickets available for the lottery.
        """
        self.ticket_price = ticket_price
        self.prize_pool = prize_pool
        self.max_tickets = max_tickets
        self.tickets = {}  # Dictionary to store ticket holders
        self.winner = None
        self.lottery_active = True

    def buy_ticket(self, user_id):
        """
        Allows a user to buy a ticket for the lottery.

        :param user_id: Unique identifier for the user buying the ticket.
        :return: Confirmation message or error message.
        """
        if not self.lottery_active:
            return "Lottery is closed. No more tickets can be purchased."

        if len(self.tickets) >= self.max_tickets:
            return "All tickets have been sold."

        if user_id in self.tickets:
            return "User has already purchased a ticket."

        # Assign a ticket number to the user
        ticket_number = len(self.tickets) + 1
        self.tickets[user_id] = ticket_number
        return f"Ticket purchased successfully! Your ticket number is {ticket_number}."

    def draw_winner(self):
        """
        Draws a random winner from the pool of ticket holders.

        :return: The winner's user ID and ticket number.
        """
        if not self.lottery_active:
            return "Lottery is already closed."

        if len(self.tickets) == 0:
            return "No tickets sold. Cannot draw a winner."

        # Randomly select a winner
        self.winner = random.choice(list(self.tickets.items()))
        self.lottery_active = False  # Close the lottery
        return f"Winner drawn! User ID: {self.winner[0]}, Ticket Number: {self.winner[1]}"

    def get_lottery_status(self):
        """
        Returns the current status of the lottery.

        :return: Status message.
        """
        if self.lottery_active:
            return f"Lottery is active. {self.max_tickets - len(self.tickets)} tickets remaining."
        else:
            return f"Lottery is closed. Winner: User ID {self.winner[0]}, Ticket Number {self.winner[1]}"

    def save_lottery_data(self, file_path):
        """
        Saves the lottery data to a JSON file.

        :param file_path: Path to the file where data will be saved.
        :return: Confirmation message or error message.
        """
        try:
            data = {
                "ticket_price": self.ticket_price,
                "prize_pool": self.prize_pool,
                "max_tickets": self.max_tickets,
                "tickets": self.tickets,
                "winner": self.winner,
                "lottery_active": self.lottery_active,
                "timestamp": datetime.now().isoformat()
            }
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            return "Lottery data saved successfully."
        except Exception as e:
            return f"Error saving lottery data: {e}"

    def load_lottery_data(self, file_path):
        """
        Loads lottery data from a JSON file.

        :param file_path: Path to the file where data is stored.
        :return: Confirmation message or error message.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.ticket_price = data["ticket_price"]
                self.prize_pool = data["prize_pool"]
                self.max_tickets = data["max_tickets"]
                self.tickets = data["tickets"]
                self.winner = data["winner"]
                self.lottery_active = data["lottery_active"]
            return "Lottery data loaded successfully."
        except Exception as e:
            return f"Error loading lottery data: {e}"


# Example usage
if __name__ == "__main__":
    # Initialize the lottery system
    lottery = NFTLottery(ticket_price=0.01, prize_pool=10, max_tickets=100)

    # Users buy tickets
    print(lottery.buy_ticket("user1"))
    print(lottery.buy_ticket("user2"))
    print(lottery.buy_ticket("user3"))

    # Check lottery status
    print(lottery.get_lottery_status())

    # Draw a winner
    print(lottery.draw_winner())

    # Save lottery data
    print(lottery.save_lottery_data("lottery_data.json"))

    # Load lottery data
    print(lottery.load_lottery_data("lottery_data.json"))

    # Check lottery status again
    print(lottery.get_lottery_status())
```
