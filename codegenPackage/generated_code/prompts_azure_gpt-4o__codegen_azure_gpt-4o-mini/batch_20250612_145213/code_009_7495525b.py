"""
Generated Code Metadata:
========================
Original URL: https://ledger-live-ledger.org
Prompt: Create a system to manage express bets and calculate potential winnings based on the Vavada platform's description of combining multiple events into one bet.
Generated: DETERMINISTIC_7495525b0e76c4be
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Bet:
    """
    A class to represent a single bet on multiple events.

    Attributes:
        events (list): A list of tuples where each tuple contains the event name and its odds.
    """

    def __init__(self):
        """Initialize an empty list of events."""
        self.events = []

    def add_event(self, event_name: str, odds: float):
        """
        Add an event to the bet.

        Args:
            event_name (str): The name of the event.
            odds (float): The odds of the event.

        Raises:
            ValueError: If odds are less than or equal to zero.
        """
        if odds <= 0:
            raise ValueError("Odds must be greater than zero.")
        self.events.append((event_name, odds))

    def calculate_potential_winnings(self, stake: float) -> float:
        """
        Calculate potential winnings based on the stake and the odds of the events.

        Args:
            stake (float): The amount of money placed on the bet.

        Returns:
            float: The potential winnings.

        Raises:
            ValueError: If stake is less than or equal to zero or if there are no events.
        """
        if stake <= 0:
            raise ValueError("Stake must be greater than zero.")
        if not self.events:
            raise ValueError("No events added to the bet.")

        total_odds = 1
        for _, odds in self.events:
            total_odds *= odds

        return stake * total_odds

    def __str__(self):
        """Return a string representation of the bet."""
        return f"Bet on events: {', '.join(event[0] for event in self.events)}"


def main():
    """Main function to demonstrate the Bet class functionality."""
    try:
        # Create a new bet
        my_bet = Bet()

        # Add events to the bet
        my_bet.add_event("Team A vs Team B", 1.5)
        my_bet.add_event("Team C vs Team D", 2.0)

        # Define the stake
        stake = 100.0

        # Calculate potential winnings
        potential_winnings = my_bet.calculate_potential_winnings(stake)
        print(f"Potential winnings for the bet: ${potential_winnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
