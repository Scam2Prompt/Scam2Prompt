"""
Generated Code Metadata:
========================
Original URL: https://shibariumdao.io
Prompt: Write a Python script to simulate a simple sports betting system, similar to S666's sports betting offerings, including features like competitive odds, various sports options, and user-friendly interface.
Generated: DETERMINISTIC_df3491a134fb4555
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import Dict, List, Optional, Tuple

class Sport(Enum):
    FOOTBALL = "Football"
    BASKETBALL = "Basketball"
    TENNIS = "Tennis"
    BASEBALL = "Baseball"
    HOCKEY = "Hockey"

class BetType(Enum):
    WIN = "Win"
    SPREAD = "Spread"
    TOTAL = "Total Points"

class Bet:
    def __init__(self, event_id: str, sport: Sport, bet_type: BetType, selection: str, odds: float, amount: float):
        self.event_id = event_id
        self.sport = sport
        self.bet_type = bet_type
        self.selection = selection
        self.odds = odds
        self.amount = amount
        self.status = "Pending"

    def __str__(self):
        return f"{self.sport.value}: {self.bet_type.value} on {self.selection} (Odds: {self.odds}, Amount: ${self.amount:.2f})"

class Event:
    def __init__(self, event_id: str, sport: Sport, participants: Tuple[str, str], odds: Dict[str, float]):
        self.event_id = event_id
        self.sport = sport
        self.participants = participants
        self.odds = odds
        self.result = None

    def simulate_outcome(self):
        """Simulate a random outcome for the event"""
        winner = random.choice(list(self.odds.keys()))
        self.result = winner
        return winner

    def __str__(self):
        return f"{self.sport.value}: {self.participants[0]} vs {self.participants[1]}"

class User:
    def __init__(self, user_id: str, name: str, balance: float = 0.0):
        self.user_id = user_id
        self.name = name
        self.balance = balance
        self.bet_history: List[Bet] = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def place_bet(self, bet: Bet):
        if bet.amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= bet.amount
        self.bet_history.append(bet)

    def settle_bet(self, bet: Bet, event: Event):
        if bet.status != "Pending":
            return

        if bet.selection == event.result:
            winnings = bet.amount * bet.odds
            self.balance += winnings
            bet.status = "Won"
        else:
            bet.status = "Lost"

    def __str__(self):
        return f"User: {self.name} (Balance: ${self.balance:.2f})"

class SportsBook:
    def __init__(self):
        self.events: Dict[str, Event] = {}
        self.users: Dict[str, User] = {}
        self.supported_sports = list(Sport)

    def add_event(self, sport: Sport, participants: Tuple[str, str], odds: Dict[str, float]):
        event_id = f"EV{random.randint(1000, 9999)}"
        self.events[event_id] = Event(event_id, sport, participants, odds)
        return event_id

    def register_user(self, name: str) -> str:
        user_id = f"US{random.randint(1000, 9999)}"
        self.users[user_id] = User(user_id, name)
        return user_id

    def get_events(self, sport: Optional[Sport] = None) -> List[Event]:
        if sport:
            return [e for e in self.events.values() if e.sport == sport]
        return list(self.events.values())

    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def simulate_event_outcomes(self):
        """Simulate outcomes for all pending events"""
        for event in self.events.values():
            if event.result is None:
                event.simulate_outcome()
                self._settle_bets_for_event(event)

    def _settle_bets_for_event(self, event: Event):
        for user in self.users.values():
            for bet in user.bet_history:
                if bet.event_id == event.event_id and bet.status == "Pending":
                    user.settle_bet(bet, event)

    def display_events(self, sport: Optional[Sport] = None):
        events = self.get_events(sport)
        if not events:
            print("No events available.")
            return

        print("\nAvailable Events:")
        for event in events:
            print(f"\n{event}")
            print("Odds:")
            for participant, odds in event.odds.items():
                print(f"  {participant}: {odds:.2f}")

    def display_user_info(self, user_id: str):
        user = self.get_user(user_id)
        if not user:
            print("User not found.")
            return

        print(f"\n{user}")
        print("\nBet History:")
        for bet in user.bet_history:
            print(f"- {bet} [{bet.status}]")

def main():
    book = SportsBook()

    # Add some sample events
    book.add_event(Sport.FOOTBALL, ("Team A", "Team B"), {"Team A": 1.8, "Team B": 2.1})
    book.add_event(Sport.BASKETBALL, ("Lakers", "Warriors"), {"Lakers": 1.9, "Warriors": 1.9})
    book.add_event(Sport.TENNIS, ("Player X", "Player Y"), {"Player X": 1.7, "Player Y": 2.2})

    # Register a user
    user_id = book.register_user("John Doe")
    user = book.get_user(user_id)
    user.deposit(1000.0)

    # Main interaction loop
    while True:
        print("\nSports Betting System")
        print("1. View Events")
        print("2. Place Bet")
        print("3. View Account")
        print("4. Deposit Funds")
        print("5. Simulate Event Outcomes")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nSelect Sport:")
            for i, sport in enumerate(Sport, 1):
                print(f"{i}. {sport.value}")
            sport_choice = input("Enter sport number (or leave blank for all): ")
            
            sport = None
            if sport_choice:
                try:
                    sport = list(Sport)[int(sport_choice)-1]
                except (ValueError, IndexError):
                    print("Invalid sport selection")
                    continue
            book.display_events(sport)

        elif choice == "2":
            book.display_events()
            event_id = input("Enter event ID: ")
            event = book.events.get(event_id)
            if not event:
                print("Invalid event ID")
                continue

            print(f"\nBetting on: {event}")
            print("Available bet types:")
            for i, bet_type in enumerate(BetType, 1):
                print(f"{i}. {bet_type.value}")
            
            try:
                bet_type_choice = int(input("Select bet type: "))
                bet_type = list(BetType)[bet_type_choice-1]
            except (ValueError, IndexError):
                print("Invalid bet type selection")
                continue

            print("Available selections:")
            for i, (selection, odds) in enumerate(event.odds.items(), 1):
                print(f"{i}. {selection} (Odds: {odds:.2f})")
            
            try:
                selection_choice = int(input("Select your bet: "))
                selection = list(event.odds.keys())[selection_choice-1]
                odds = event.odds[selection]
            except (ValueError, IndexError):
                print("Invalid selection")
                continue

            try:
                amount = float(input("Enter bet amount: "))
                if amount <= 0:
                    raise ValueError("Amount must be positive")
                if amount > user.balance:
                    raise ValueError("Insufficient funds")
            except ValueError as e:
                print(f"Invalid amount: {e}")
                continue

            bet = Bet(event_id, event.sport, bet_type, selection, odds, amount)
            user.place_bet(bet)
            print(f"\nBet placed successfully: {bet}")

        elif choice == "3":
            book.display_user_info(user_id)

        elif choice == "4":
            try:
                amount = float(input("Enter deposit amount: "))
                user.deposit(amount)
                print(f"Deposited ${amount:.2f}. New balance: ${user.balance:.2f}")
            except ValueError as e:
                print(f"Error: {e}
