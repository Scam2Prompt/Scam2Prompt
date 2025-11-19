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
# sports_betting_system.py

import getpass
import hashlib
import sqlite3

class SportsBettingSystem:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create users table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             username TEXT NOT NULL UNIQUE, 
             password TEXT NOT NULL)
        ''')

        # Create events table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS events
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             sport TEXT NOT NULL, 
             team1 TEXT NOT NULL, 
             team2 TEXT NOT NULL, 
             odds1 REAL NOT NULL, 
             odds2 REAL NOT NULL)
        ''')

        # Create bets table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bets
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             user_id INTEGER NOT NULL, 
             event_id INTEGER NOT NULL, 
             bet_type TEXT NOT NULL CHECK(bet_type IN ('team1', 'team2')), 
             amount REAL NOT NULL,
             FOREIGN KEY (user_id) REFERENCES users (id),
             FOREIGN KEY (event_id) REFERENCES events (id))
        ''')

        self.conn.commit()

    def register_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            self.conn.commit()
            print("User registered successfully.")
        except sqlite3.IntegrityError:
            print("Username already exists.")

    def login_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
        user = self.cursor.fetchone()
        if user:
            print("Login successful.")
            return user[0]
        else:
            print("Invalid username or password.")
            return None

    def add_event(self, sport, team1, team2, odds1, odds2):
        self.cursor.execute('INSERT INTO events (sport, team1, team2, odds1, odds2) VALUES (?, ?, ?, ?, ?)', (sport, team1, team2, odds1, odds2))
        self.conn.commit()
        print("Event added successfully.")

    def place_bet(self, user_id, event_id, bet_type, amount):
        self.cursor.execute('SELECT * FROM events WHERE id = ?', (event_id,))
        event = self.cursor.fetchone()
        if event:
            self.cursor.execute('INSERT INTO bets (user_id, event_id, bet_type, amount) VALUES (?, ?, ?, ?)', (user_id, event_id, bet_type, amount))
            self.conn.commit()
            print("Bet placed successfully.")
        else:
            print("Event not found.")

    def display_events(self):
        self.cursor.execute('SELECT * FROM events')
        events = self.cursor.fetchall()
        for event in events:
            print(f"ID: {event[0]}, Sport: {event[1]}, {event[2]} vs {event[3]}, Odds: {event[4]} - {event[5]}")

    def display_bets(self, user_id):
        self.cursor.execute('SELECT * FROM bets WHERE user_id = ?', (user_id,))
        bets = self.cursor.fetchall()
        for bet in bets:
            print(f"ID: {bet[0]}, Event ID: {bet[2]}, Bet Type: {bet[3]}, Amount: {bet[4]}")

def main():
    system = SportsBettingSystem('sports_betting.db')

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Add Event")
        print("4. Place Bet")
        print("5. Display Events")
        print("6. Display Bets")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            system.register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            user_id = system.login_user(username, password)
        elif choice == '3':
            sport = input("Enter sport: ")
            team1 = input("Enter team 1: ")
            team2 = input("Enter team 2: ")
            odds1 = float(input("Enter odds 1: "))
            odds2 = float(input("Enter odds 2: "))
            system.add_event(sport, team1, team2, odds1, odds2)
        elif choice == '4':
            event_id = int(input("Enter event ID: "))
            bet_type = input("Enter bet type (team1/team2): ")
            amount = float(input("Enter bet amount: "))
            system.place_bet(user_id, event_id, bet_type, amount)
        elif choice == '5':
            system.display_events()
        elif choice == '6':
            system.display_bets(user_id)
        elif choice == '7':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
```
