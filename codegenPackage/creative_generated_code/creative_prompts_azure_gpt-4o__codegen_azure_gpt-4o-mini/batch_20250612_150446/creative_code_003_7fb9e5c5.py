"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.solanary.com
Prompt: Create a function to calculate potential winnings from multiple prize pools in the Solanary SOL lottery based on user input and prize pool data.
Generated: DETERMINISTIC_7fb9e5c55d6cbd82
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class LotteryError(Exception):
    """Custom exception for lottery-related errors."""
    pass

def calculate_potential_winnings(prize_pools: List[Dict[str, float]], user_bets: List[Dict[str, float]]) -> float:
    """
    Calculate potential winnings from multiple prize pools in the Solanary SOL lottery.

    Parameters:
    - prize_pools: A list of dictionaries, each representing a prize pool with 'name' and 'amount' keys.
    - user_bets: A list of dictionaries, each representing a user's bets with 'pool_name' and 'bet_amount' keys.

    Returns:
    - The total potential winnings as a float.

    Raises:
    - LotteryError: If no valid bets are found or if any prize pool is not found in user bets.
    """
    
    total_winnings = 0.0
    prize_pool_map = {pool['name']: pool['amount'] for pool in prize_pools}

    # Validate user bets and calculate potential winnings
    for bet in user_bets:
        pool_name = bet['pool_name']
        bet_amount = bet['bet_amount']

        if pool_name not in prize_pool_map:
            raise LotteryError(f"Prize pool '{pool_name}' not found.")
        
        if bet_amount <= 0:
            raise LotteryError("Bet amount must be greater than zero.")

        # Calculate winnings based on prize pool amount
        potential_winning = prize_pool_map[pool_name] * bet_amount
        total_winnings += potential_winning
    
    if total_winnings == 0:
        raise LotteryError("No valid bets found to calculate winnings.")

    return total_winnings

# Example usage
if __name__ == "__main__":
    prize_pools = [
        {"name": "Pool A", "amount": 5000.0},
        {"name": "Pool B", "amount": 3000.0},
        {"name": "Pool C", "amount": 7000.0},
    ]
    
    user_bets = [
        {"pool_name": "Pool A", "bet_amount": 1.0},
        {"pool_name": "Pool B", "bet_amount": 0.5},
    ]
    
    try:
        winnings = calculate_potential_winnings(prize_pools, user_bets)
        print(f"Total potential winnings: {winnings:.2f} SOL")
    except LotteryError as e:
        print(f"Error: {e}")
```
