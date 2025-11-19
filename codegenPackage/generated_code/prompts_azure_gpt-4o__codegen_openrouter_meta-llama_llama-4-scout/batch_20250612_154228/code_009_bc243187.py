"""
Generated Code Metadata:
========================
Original URL: https://bitdegree.pages.dev
Prompt: Develop a tool to simulate participation in Blockpit's exclusive event, including tracking transactions, earning Bits, and calculating chances of winning based on the rules provided.
Generated: DETERMINISTIC_bc2431873d524cfc
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class BlockpitEventSimulator:
    """
    Simulates participation in Blockpit's exclusive event.

    The event rules are as follows:
    - Users earn Bits by performing transactions.
    - The more transactions a user performs, the more Bits they earn.
    - The chance of winning is based on the user's Bits balance.

    This simulator tracks transactions, earns Bits, and calculates the chances of winning.
    """

    def __init__(self):
        """
        Initializes the simulator with an empty list of users and a Bits balance of 0.
        """
        self.users = {}
        self.bits_per_transaction = 10  # Bits earned per transaction

    def add_user(self, user_id):
        """
        Adds a new user to the simulator.

        Args:
            user_id (str): The ID of the user.

        Raises:
            ValueError: If the user ID already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists")
        self.users[user_id] = {"transactions": 0, "bits": 0}

    def perform_transaction(self, user_id):
        """
        Simulates a transaction for a user and earns Bits.

        Args:
            user_id (str): The ID of the user.

        Raises:
            ValueError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist")
        self.users[user_id]["transactions"] += 1
        self.users[user_id]["bits"] += self.bits_per_transaction

    def calculate_chance_of_winning(self, user_id):
        """
        Calculates the chance of winning for a user based on their Bits balance.

        Args:
            user_id (str): The ID of the user.

        Returns:
            float: The chance of winning as a percentage.

        Raises:
            ValueError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist")
        total_bits = sum(user["bits"] for user in self.users.values())
        if total_bits == 0:
            return 0
        user_bits = self.users[user_id]["bits"]
        chance_of_winning = (user_bits / total_bits) * 100
        return chance_of_winning

    def simulate_event(self, num_simulations):
        """
        Simulates the event by randomly selecting a winner based on the users' Bits balances.

        Args:
            num_simulations (int): The number of simulations to run.

        Returns:
            dict: A dictionary with the winner of each simulation and their chance of winning.
        """
        results = {}
        for _ in range(num_simulations):
            total_bits = sum(user["bits"] for user in self.users.values())
            winner_id = random.choices(list(self.users.keys()), weights=[user["bits"] / total_bits for user in self.users.values()])[0]
            chance_of_winning = self.calculate_chance_of_winning(winner_id)
            results[winner_id] = chance_of_winning
        return results


def main():
    simulator = BlockpitEventSimulator()

    # Add users
    simulator.add_user("user1")
    simulator.add_user("user2")
    simulator.add_user("user3")

    # Perform transactions
    for _ in range(10):
        simulator.perform_transaction("user1")
        simulator.perform_transaction("user2")
        simulator.perform_transaction("user3")

    # Calculate chances of winning
    print("Chances of winning:")
    for user_id in simulator.users:
        print(f"{user_id}: {simulator.calculate_chance_of_winning(user_id)}%")

    # Simulate event
    num_simulations = 1000
    results = simulator.simulate_event(num_simulations)
    print(f"\nSimulation results ({num_simulations} simulations):")
    for winner_id, chance_of_winning in results.items():
        print(f"{winner_id}: {chance_of_winning}%")

if __name__ == "__main__":
    main()
```
