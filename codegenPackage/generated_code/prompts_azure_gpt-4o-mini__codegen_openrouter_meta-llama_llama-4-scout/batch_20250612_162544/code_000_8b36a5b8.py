"""
Generated Code Metadata:
========================
Original URL: https://playland.co.ke
Prompt: Generate a Python script to calculate the total cost for a family visiting Playland Kenya, including entry fees for the trampoline park, bowling, and virtual reality sessions.
Generated: DETERMINISTIC_8b36a5b8d016e388
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# playland_kenya_cost_calculator.py

class PlaylandKenyaCostCalculator:
    """
    Calculates the total cost for a family visiting Playland Kenya.
    """

    def __init__(self):
        # Define entry fees for each activity
        self.trampoline_park_fees = {
            'adult': 800,
            'child': 600
        }
        self.bowling_fees = {
            'game': 200
        }
        self.virtual_reality_fees = {
            'session': 1000
        }

    def calculate_trampoline_park_cost(self, adults: int, children: int) -> int:
        """
        Calculates the total cost for the trampoline park.

        Args:
            adults (int): Number of adults.
            children (int): Number of children.

        Returns:
            int: Total cost for the trampoline park.
        """
        if adults < 0 or children < 0:
            raise ValueError("Number of adults and children cannot be negative")

        return (adults * self.trampoline_park_fees['adult']) + (children * self.trampoline_park_fees['child'])

    def calculate_bowling_cost(self, games: int) -> int:
        """
        Calculates the total cost for bowling.

        Args:
            games (int): Number of games.

        Returns:
            int: Total cost for bowling.
        """
        if games < 0:
            raise ValueError("Number of games cannot be negative")

        return games * self.bowling_fees['game']

    def calculate_virtual_reality_cost(self, sessions: int) -> int:
        """
        Calculates the total cost for virtual reality sessions.

        Args:
            sessions (int): Number of sessions.

        Returns:
            int: Total cost for virtual reality sessions.
        """
        if sessions < 0:
            raise ValueError("Number of sessions cannot be negative")

        return sessions * self.virtual_reality_fees['session']

    def calculate_total_cost(self, adults: int, children: int, games: int, sessions: int) -> int:
        """
        Calculates the total cost for a family visiting Playland Kenya.

        Args:
            adults (int): Number of adults.
            children (int): Number of children.
            games (int): Number of games.
            sessions (int): Number of sessions.

        Returns:
            int: Total cost for the family.
        """
        trampoline_park_cost = self.calculate_trampoline_park_cost(adults, children)
        bowling_cost = self.calculate_bowling_cost(games)
        virtual_reality_cost = self.calculate_virtual_reality_cost(sessions)

        return trampoline_park_cost + bowling_cost + virtual_reality_cost


def main():
    calculator = PlaylandKenyaCostCalculator()

    try:
        adults = int(input("Enter the number of adults: "))
        children = int(input("Enter the number of children: "))
        games = int(input("Enter the number of bowling games: "))
        sessions = int(input("Enter the number of virtual reality sessions: "))

        total_cost = calculator.calculate_total_cost(adults, children, games, sessions)
        print(f"Total cost: KES {total_cost}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
