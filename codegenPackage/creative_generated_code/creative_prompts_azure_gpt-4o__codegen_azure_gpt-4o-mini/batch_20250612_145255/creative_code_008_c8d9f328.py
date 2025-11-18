"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivebrokers.fo
Prompt: Generate Python code to calculate the odds and payouts for various types of bets (e.g., single, express, system) offered by 1Win.
Generated: DETERMINISTIC_c8d9f3280d043ef4
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Bet:
    """A class to represent a generic Bet."""
    
    def __init__(self, odds):
        """
        Initialize a Bet with given odds.

        :param odds: The odds associated with the bet (float).
        """
        if odds <= 0:
            raise ValueError("Odds must be greater than 0.")
        self.odds = odds


class SingleBet(Bet):
    """A class to represent a single bet."""
    
    def __init__(self, odds, stake):
        """
        Initialize a SingleBet with given odds and stake.

        :param odds: The odds associated with the bet (float).
        :param stake: The amount of money placed on the bet (float).
        """
        super().__init__(odds)
        if stake <= 0:
            raise ValueError("Stake must be greater than 0.")
        self.stake = stake

    def payout(self):
        """Calculate the payout for a single bet."""
        return self.stake * self.odds


class ExpressBet(Bet):
    """A class to represent an express (parlay) bet."""
    
    def __init__(self, bets):
        """
        Initialize an ExpressBet with a list of Bet instances.

        :param bets: A list of Bet instances.
        """
        if not bets or not all(isinstance(bet, Bet) for bet in bets):
            raise ValueError("Bets must be a non-empty list of Bet instances.")
        self.bets = bets

    def payout(self):
        """Calculate the payout for an express bet."""
        payout = 1
        for bet in self.bets:
            payout *= bet.odds
        return payout


class SystemBet:
    """A class to represent a system bet."""
    
    def __init__(self, bets, system_type):
        """
        Initialize a SystemBet with a list of Bet instances and a system type.

        :param bets: A list of Bet instances.
        :param system_type: A string indicating the system type (e.g., '2 out of 3').
        """
        if not bets or not all(isinstance(bet, Bet) for bet in bets):
            raise ValueError("Bets must be a non-empty list of Bet instances.")
        self.bets = bets
        self.system_type = system_type

    def payout(self):
        """Calculate the payout based on system type."""
        if self.system_type == '2 out of 3':
            # Example payout calculation for 2 out of 3
            if len(self.bets) < 3:
                raise ValueError("At least 3 bets are required for '2 out of 3' system.")
            odds_combination = self.bets[0].odds * self.bets[1].odds  # Example combination
            return odds_combination  # Simplified for demonstration
        else:
            raise NotImplementedError(f"System type '{self.system_type}' is not implemented.")


# Example usage
if __name__ == "__main__":
    try:
        # Create single bet
        single_bet = SingleBet(2.0, 100)
        print(f"Single Bet Payout: {single_bet.payout()}")

        # Create express bet
        express_bet = ExpressBet([single_bet, SingleBet(1.5, 50)])
        print(f"Express Bet Payout: {express_bet.payout()}")

        # Create system bet
        system_bet = SystemBet([single_bet, SingleBet(1.8, 100), SingleBet(2.5, 50)], '2 out of 3')
        print(f"System Bet Payout: {system_bet.payout()}")
    except Exception as e:
        print(f"Error: {e}")
```
