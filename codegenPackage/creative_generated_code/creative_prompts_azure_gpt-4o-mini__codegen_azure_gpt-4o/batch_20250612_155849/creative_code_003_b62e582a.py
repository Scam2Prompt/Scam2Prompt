"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betlahze.vip
Prompt: Develop a function to implement a cashback system for losses in a betting application, taking cues from the loyalty rewards described by BaxBet.
Generated: DETERMINISTIC_b62e582ab62595d2
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code for implementing a cashback system for losses in a betting application

# Import necessary modules
from typing import List

# Define constants
CASHBACK_PERCENTAGE = 0.10  # 10% cashback rate
MINIMUM_LOSS_FOR_CASHBACK = 100  # Minimum loss amount required to qualify for cashback

# Custom exception for invalid input data
class CashbackSystemError(Exception):
    pass

def calculate_cashback(user_id: int, bet_history: List[dict]) -> float:
    """
    Function to calculate cashback based on losses in a betting application.

    Args:
        user_id (int): The ID of the user for whom cashback is being calculated.
        bet_history (List[dict]): A list of dictionaries representing bets. Each dictionary contains:
            - 'bet_id' (int): Unique ID for the bet
            - 'amount' (float): Amount of the bet
            - 'result' (str): 'win' or 'loss'
            - 'payout' (float): Amount returned to the user in case of a win
            
    Returns:
        float: The cashback amount calculated.
        
    Raises:
        CashbackSystemError: If invalid bet history data is provided.
    """
    # Validate inputs
    if not isinstance(user_id, int) or user_id <= 0:
        raise CashbackSystemError("Invalid user ID. Must be a positive integer.")
    
    if not isinstance(bet_history, list):
        raise CashbackSystemError("Invalid bet history format. Must be a list of dictionaries.")
    
    # Initialize total losses
    total_loss = 0.0
    
    # Process each bet in the betting history
    for bet in bet_history:
        # Validate individual bet structure
        if not isinstance(bet, dict) or not all(key in bet for key in ('bet_id', 'amount', 'result', 'payout')):
            raise CashbackSystemError("Invalid bet data format. Each bet must contain 'bet_id', 'amount', 'result', and 'payout'.")
        
        # Calculate losses for bets with result 'loss'
        if bet['result'] == 'loss':
            loss = bet.get('amount', 0.0) - bet.get('payout', 0.0)
            if loss > 0:
                total_loss += loss
    
    # Check if total loss meets the minimum threshold for cashback
    if total_loss >= MINIMUM_LOSS_FOR_CASHBACK:
        cashback = total_loss * CASHBACK_PERCENTAGE
    else:
        cashback = 0.0  # No cashback if losses are below the threshold
    
    return cashback

# Example usage
if __name__ == "__main__":
    try:
        user_id = 12345
        bet_history = [
            {'bet_id': 1, 'amount': 200, 'result': 'loss', 'payout': 0},
            {'bet_id': 2, 'amount': 150, 'result': 'win', 'payout': 300},
            {'bet_id': 3, 'amount': 100, 'result': 'loss', 'payout': 0},
        ]
        
        cashback_amount = calculate_cashback(user_id, bet_history)
        print(f"Cashback for user {user_id}: ${cashback_amount:.2f}")
    except CashbackSystemError as e:
        print(f"Error calculating cashback: {e}")
```
