"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lyast.org
Prompt: Develop a script that evaluates the volatility of online slots as explained in "Apa yang Harus Anda Ketahui tentang Varians dalam Slot Online" on lyast.org.
Generated: DETERMINISTIC_58825f763ca7a754
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


def simulate_slot_spin(paytable, bet_amount):
    """
    Simulates a single spin of the slot machine.

    Args:
        paytable (list of tuples): Each tuple contains (symbol, probability, payout).
        bet_amount (float): Amount wagered per spin.

    Returns:
        float: Payout for the spin (can be 0 if no winning occurs).
    """
    # Generate a random number between 0 and 1
    spin_result = random.random()

    # Check if spin matches any payout in the paytable
    for symbol, probability, payout in paytable:
        if spin_result <= probability:
            return payout * bet_amount

    # If no match, return 0
    return 0


def calculate_volatility(paytable, bet_amount, num_spins):
    """
    Calculates the volatility for a slot machine based on a paytable.

    Args:
        paytable (list of tuples): Each tuple contains (symbol, probability, payout).
        bet_amount (float): Amount wagered per spin.
        num_spins (int): Number of spins to simulate.

    Returns:
        float: Volatility (standard deviation of payouts).
    """
    # Track payouts from all spins
    payouts = []
    try:
        for _ in range(num_spins):
            payout = simulate_slot_spin(paytable, bet_amount)
            payouts.append(payout)

        # Calculate average payout
        average_payout = sum(payouts) / num_spins

        # Calculate variance
        variance = sum(
            (payout - average_payout) ** 2 for payout in payouts
        ) / num_spins

        # Standard deviation (volatility)
        volatility = variance ** 0.5

        return volatility
    except Exception as e:
        print("Error occurred while calculating volatility:", e)
        return None


def main():
    """
    Main function to simulate slot machine volatility.
    """
    # Define paytable: (symbol, probability, payout)
    paytable = [
        ("Cherry", 0.05, 10),
        ("Lemon", 0.10, 5),
        ("Bell", 0.02, 20),
        ("Seven", 0.01, 50),
    ]

    # Inputs
    bet_amount = 1.0  # Bet amount per spin
    num_spins = 1000  # Number of spins to simulate

    # Validate inputs
    if bet_amount <= 0 or num_spins <= 0:
        print("Bet amount and number of spins must be positive values.")
        return

    print("Calculating volatility...")
    volatility = calculate_volatility(paytable, bet_amount, num_spins)

    if volatility is not None:
        print(f"Volatility of the slot machine: {volatility:.2f}")
    else:
        print("Could not calculate volatility due to an error.")


# Entry point for the script
if __name__ == "__main__":
    main()
```
