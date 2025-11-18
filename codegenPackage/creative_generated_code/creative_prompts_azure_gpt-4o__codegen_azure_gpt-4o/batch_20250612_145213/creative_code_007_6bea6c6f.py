"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledger-live-ledger.org
Prompt: Write a program to track and display ongoing tournaments and promotions for a betting platform, inspired by Vavada's weekly X-tournament for new users.
Generated: DETERMINISTIC_6bea6c6fda995ddc
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Tournament:
    """
    Represents a tournament with a name, start date, end date, and description.
    """
    def __init__(self, name, start_date, end_date, description):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description

    def is_active(self):
        """
        Checks if the tournament is currently active.
        """
        current_date = datetime.datetime.now()
        return self.start_date <= current_date <= self.end_date

    def __str__(self):
        """
        Returns a formatted string representation of the tournament.
        """
        status = "Active" if self.is_active() else "Inactive"
        return (f"Tournament: {self.name}\n"
                f"Start Date: {self.start_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"End Date: {self.end_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Description: {self.description}\n"
                f"Status: {status}\n")

class Promotion:
    """
    Represents a promotion with a title, details, and expiration date.
    """
    def __init__(self, title, details, expiration_date):
        self.title = title
        self.details = details
        self.expiration_date = expiration_date

    def is_active(self):
        """
        Checks if the promotion is currently active.
        """
        current_date = datetime.datetime.now()
        return current_date <= self.expiration_date

    def __str__(self):
        """
        Returns a formatted string representation of the promotion.
        """
        status = "Active" if self.is_active() else "Expired"
        return (f"Promotion: {self.title}\n"
                f"Details: {self.details}\n"
                f"Expiration Date: {self.expiration_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Status: {status}\n")

class BettingPlatform:
    """
    Represents a betting platform that tracks tournaments and promotions.
    """
    def __init__(self):
        self.tournaments = []
        self.promotions = []

    def add_tournament(self, tournament):
        """
        Adds a tournament to the platform.
        """
        if not isinstance(tournament, Tournament):
            raise ValueError("Invalid tournament object")
        self.tournaments.append(tournament)

    def add_promotion(self, promotion):
        """
        Adds a promotion to the platform.
        """
        if not isinstance(promotion, Promotion):
            raise ValueError("Invalid promotion object")
        self.promotions.append(promotion)

    def display_active_tournaments(self):
        """
        Displays all active tournaments.
        """
        print("=== Active Tournaments ===")
        for tournament in self.tournaments:
            if tournament.is_active():
                print(tournament)

    def display_active_promotions(self):
        """
        Displays all active promotions.
        """
        print("\n=== Active Promotions ===")
        for promotion in self.promotions:
            if promotion.is_active():
                print(promotion)

if __name__ == "__main__":
    # Example usage of the BettingPlatform

    # Create a betting platform instance
    platform = BettingPlatform()

    # Add sample tournaments
    platform.add_tournament(Tournament(
        name="Weekly X-Tournament",
        start_date=datetime.datetime(2023, 10, 1, 12, 0, 0),
        end_date=datetime.datetime(2023, 10, 7, 23, 59, 59),
        description="A tournament for new users with exciting rewards!"
    ))
    platform.add_tournament(Tournament(
        name="Pro Gamer Challenge",
        start_date=datetime.datetime(2023, 10, 5, 12, 0, 0),
        end_date=datetime.datetime(2023, 10, 12, 23, 59, 59),
        description="Compete for ultimate gaming glory!"
    ))

    # Add sample promotions
    platform.add_promotion(Promotion(
        title="Welcome Bonus",
        details="Get a 100% bonus on your first deposit!",
        expiration_date=datetime.datetime(2023, 12, 31, 23, 59, 59)
    ))
    platform.add_promotion(Promotion(
        title="Refer-a-Friend",
        details="Earn $50 for every friend you refer!",
        expiration_date=datetime.datetime(2023, 11, 15, 23, 59, 59)
    ))

    # Display active tournaments and promotions
    platform.display_active_tournaments()
    platform.display_active_promotions()
```
