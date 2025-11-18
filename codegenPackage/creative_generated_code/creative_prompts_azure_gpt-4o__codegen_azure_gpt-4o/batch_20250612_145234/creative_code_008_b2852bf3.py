"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://districtchronicles.com
Prompt: Develop a Python script to simulate a slot game with adjustable volatility settings, inspired by Pixxie928's advice on choosing games based on volatility.
Generated: DETERMINISTIC_b2852bf3f757bed2
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class SlotMachine:
    def __init__(self, volatility="medium"):
        """
        Initialize the slot machine with a given volatility level.
        :param volatility: str - "low", "medium", or "high"
        """
        self.volatility = volatility.lower()
        self.validate_volatility()
        # Define payout probabilities and amounts based on volatility
        self.payouts = {
            "low": [(0.6, 1), (0.3, 2), (0.1, 5)],  # Higher chance of small payouts
            "medium": [(0.7, 0), (0.2, 3), (0.1, 10)],  # Balanced payouts
            "high": [(0.85, 0), (0.1, 5), (0.05, 20)],  # Rare, larger payouts
        }

    def validate_volatility(self):
        """
        Validate that the selected volatility level is correct.
        Raise ValueError if the level is invalid.
        """
        if self.volatility not in self.payouts:
            raise ValueError("Invalid volatility level. Choose 'low', 'medium', or 'high'.")

    def spin(self):
        """
        Simulate a single spin of the slot machine.
        :return: int - The payout amount for this spin.
        """
        outcomes = self.payouts[self.volatility]
        rand = random.random()
        cumulative_probability = 0
        for probability, payout in outcomes:
            cumulative_probability += probability
            if rand <= cumulative_probability:
                return payout
        return 0  # Default to no payout if no condition met

    def play(self, spins=1):
        """
        Play the slot machine for a given number of spins.
        :param spins: int - Number of spins to simulate.
        :return: dict - Total spins, total payouts, and net results.
        """
        if spins <= 0:
            raise ValueError("Number of spins must be greater than 0.")

        total_payout = 0
        for spin_number in range(spins):
            payout = self.spin()
            total_payout += payout
            print(f"Spin {spin_number + 1}: Payout = {payout}")

        # Assume the cost per spin is 1 unit
        total_cost = spins
        net_result = total_payout - total_cost

        return {
            "total_spins": spins,
            "total_payout": total_payout,
            "net_result": net_result,
        }


def main():
    """
    Main function to run the slot game simulation.
    """
    print("Welcome to the Slot Machine Simulator!")
    print("Choose your volatility: low, medium, or high.")

    # Get user input for volatility and number of spins
    while True:
        try:
            user_volatility = input("Enter volatility level: ").strip().lower()
            slot_machine = SlotMachine(volatility=user_volatility)
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            spins = int(input("Enter the number of spins: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Play the slot machine
    results = slot_machine.play(spins=spins)

    # Display results
    print("\n--- Game Results ---")
    print(f"Total Spins: {results['total_spins']}")
    print(f"Total Payout: {results['total_payout']}")
    print(f"Net Result: {results['net_result']} (negative means loss, positive means profit)")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
```
