"""
Generated Code Metadata:
========================
Original URL: https://foodandwine.one
Prompt: Write a Python script to simulate a simple sports betting system, including user registration, login, and placing bets on various sports events, inspired by Hi88's sportsbook offerings.
Generated: DETERMINISTIC_b11d61a2d0856ace
Batch ID: 20250622_204755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
import random
from datetime import datetime
from getpass import getpass
from typing import Dict, List, Optional, Tuple

# Constants
USER_DATA_FILE = "users.json"
EVENTS_DATA_FILE = "events.json"
BETS_DATA_FILE = "bets.json"
MIN_BET_AMOUNT = 1
MAX_BET_AMOUNT = 1000
SPORTS = ["Football", "Basketball", "Tennis", "Baseball", "Hockey"]
ODDS_RANGE = (1.1, 10.0)

class SportsBettingSystem:
    def __init__(self):
        self.current_user: Optional[Dict] = None
        self.load_data()

    def load_data(self) -> None:
        """Load user, event, and bet data from JSON files."""
        self.users = self._load_json_file(USER_DATA_FILE, default=[])
        self.events = self._load_json_file(EVENTS_DATA_FILE, default=[])
        self.bets = self._load_json_file(BETS_DATA_FILE, default=[])

    def _load_json_file(self, filename: str, default=None) -> Dict:
        """Helper method to load JSON data from file."""
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    return json.load(f)
            return default if default is not None else {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading {filename}: {e}")
            return default if default is not None else {}

    def _save_json_file(self, filename: str, data: Dict) -> None:
        """Helper method to save data to JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving {filename}: {e}")

    def register_user(self) -> bool:
        """Register a new user."""
        print("\n=== User Registration ===")
        username = input("Enter username: ").strip()
        
        if any(user['username'] == username for user in self.users):
            print("Username already exists. Please choose another.")
            return False

        password = getpass("Enter password: ").strip()
        if len(password) < 6:
            print("Password must be at least 6 characters.")
            return False

        initial_balance = 100.0  # Starting balance for new users
        new_user = {
            "username": username,
            "password": password,  # Note: In production, use proper password hashing
            "balance": initial_balance,
            "registration_date": datetime.now().isoformat()
        }

        self.users.append(new_user)
        self._save_json_file(USER_DATA_FILE, self.users)
        print(f"Registration successful! Your starting balance is ${initial_balance:.2f}")
        return True

    def login(self) -> bool:
        """Authenticate user."""
        print("\n=== User Login ===")
        username = input("Username: ").strip()
        password = getpass("Password: ").strip()

        for user in self.users:
            if user['username'] == username and user['password'] == password:
                self.current_user = user
                print(f"Welcome back, {username}!")
                print(f"Your current balance: ${user['balance']:.2f}")
                return True

        print("Invalid username or password.")
        return False

    def logout(self) -> None:
        """Log out current user."""
        if self.current_user:
            print(f"Goodbye, {self.current_user['username']}!")
            self.current_user = None
        else:
            print("No user is currently logged in.")

    def generate_events(self) -> None:
        """Generate random sports events for betting."""
        if not self.events:
            events = []
            for _ in range(10):
                sport = random.choice(SPORTS)
                team1 = f"Team {random.randint(1, 10)}"
                team2 = f"Team {random.randint(1, 10)}"
                while team2 == team1:
                    team2 = f"Team {random.randint(1, 10)}"
                
                event = {
                    "id": len(events) + 1,
                    "sport": sport,
                    "team1": team1,
                    "team2": team2,
                    "odds1": round(random.uniform(*ODDS_RANGE), 2),
                    "odds2": round(random.uniform(*ODDS_RANGE), 2),
                    "draw_odds": round(random.uniform(*ODDS_RANGE), 2) if sport != "Basketball" else None,
                    "start_time": (datetime.now() + random.timedelta(hours=random.randint(1, 72))).isoformat(),
                    "completed": False,
                    "winner": None
                }
                events.append(event)
            
            self.events = events
            self._save_json_file(EVENTS_DATA_FILE, self.events)

    def display_events(self) -> None:
        """Display available events for betting."""
        print("\n=== Available Events ===")
        for event in self.events:
            if not event['completed']:
                print(f"\nEvent ID: {event['id']}")
                print(f"Sport: {event['sport']}")
                print(f"Match: {event['team1']} vs {event['team2']}")
                print(f"Odds: {event['team1']} ({event['odds1']:.2f}) - Draw ({event['draw_odds']:.2f if event['draw_odds'] else 'N/A'}) - {event['team2']} ({event['odds2']:.2f})")
                print(f"Start Time: {datetime.fromisoformat(event['start_time']).strftime('%Y-%m-%d %H:%M')}")

    def place_bet(self) -> None:
        """Place a bet on an event."""
        if not self.current_user:
            print("Please login first.")
            return

        self.display_events()
        try:
            event_id = int(input("\nEnter Event ID to bet on: "))
            selected_event = next((e for e in self.events if e['id'] == event_id and not e['completed']), None)
            
            if not selected_event:
                print("Invalid Event ID or event already completed.")
                return

            print(f"\nBetting on: {selected_event['team1']} vs {selected_event['team2']}")
            print("1. Home Win")
            print("2. Away Win")
            if selected_event['draw_odds']:
                print("3. Draw")

            choice = input("Select outcome (1-3): ").strip()
            if choice not in ['1', '2', '3'] or (choice == '3' and not selected_event['draw_odds']):
                print("Invalid choice.")
                return

            try:
                amount = float(input(f"Enter bet amount (${MIN_BET_AMOUNT}-${MAX_BET_AMOUNT}): "))
                if amount < MIN_BET_AMOUNT or amount > MAX_BET_AMOUNT:
                    print(f"Amount must be between ${MIN_BET_AMOUNT} and ${MAX_BET_AMOUNT}.")
                    return
                
                if amount > self.current_user['balance']:
                    print("Insufficient balance.")
                    return

                outcome = "home" if choice == '1' else "away" if choice == '2' else "draw"
                odds = selected_event['odds1'] if choice == '1' else selected_event['odds2'] if choice == '2' else selected_event['draw_odds']

                bet = {
                    "id": len(self.bets) + 1,
                    "user_id": self.current_user['username'],
                    "event_id": event_id,
                    "outcome": outcome,
                    "amount": amount,
                    "odds": odds,
                    "placed_at": datetime.now().isoformat(),
                    "settled": False,
                    "won": None
                }

                self.current_user['balance'] -= amount
                self.bets.append(bet)
                
                # Update user in users list
                for i, user in enumerate(self.users):
                    if user['username'] == self.current_user['username']:
                        self.users[i] = self.current_user
                        break
                
                self._save_json_file(USER_DATA_FILE, self.users)
                self._save_json_file(BETS_DATA_FILE, self.bets)
                print(f"Bet placed successfully! Potential winnings: ${amount * odds:.2f}")

            except ValueError:
                print("Invalid amount entered.")
        except ValueError:
            print("Invalid Event ID.")

    def view_bets(self) -> None:
        """View user's betting history."""
        if not self.current_user:
            print("Please login first.")
            return

        user_bets = [bet for bet in self.bets if bet['user_id'] == self.current_user['username']]
        if not user_bets:
            print("You have no bets placed.")
            return

        print("\n=== Your Betting History ===")
        for bet
