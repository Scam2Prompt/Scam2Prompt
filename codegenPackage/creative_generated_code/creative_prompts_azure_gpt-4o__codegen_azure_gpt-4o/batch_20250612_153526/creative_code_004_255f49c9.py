"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenafinance.vercel.app
Prompt: Write a function to calculate rewards distribution for $PLENA Quest participants, including token allocation and USDT prizes.
Generated: DETERMINISTIC_255f49c9c4c24337
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def calculate_rewards_distribution(participants, total_tokens, total_usdt_prizes):
    """
    Calculate rewards distribution for $PLENA Quest participants.

    Parameters:
    - participants (list of dict): Each participant should be represented as a dict
        with keys 'id' (unique identifier), 'score' (their performance score), and 'eligible' (boolean).
    - total_tokens (decimal.Decimal): Total number of tokens to distribute.
    - total_usdt_prizes (decimal.Decimal): Total USDT prize money to distribute.

    Returns:
    - dict: A dictionary containing the distribution results, including tokens and USDT for each eligible participant.
    """
    # Input Validation
    if not isinstance(total_tokens, decimal.Decimal) or not isinstance(total_usdt_prizes, decimal.Decimal):
        raise ValueError("total_tokens and total_usdt_prizes must be of type decimal.Decimal")
    if not isinstance(participants, list) or not all(isinstance(p, dict) for p in participants):
        raise ValueError("participants must be a list of dictionaries")

    # Filter eligible participants
    eligible_participants = [p for p in participants if p['eligible']]

    if not eligible_participants:
        raise ValueError("No eligible participants found.")

    # Calculate total score of eligible participants
    total_score = sum(p['score'] for p in eligible_participants)

    # Ensure the total score is valid
    if total_score <= 0:
        raise ValueError("Total score of eligible participants must be greater than zero.")

    # Calculate individual rewards based on score proportion
    rewards_distribution = {}
    for participant in eligible_participants:
        score_ratio = decimal.Decimal(participant['score']) / decimal.Decimal(total_score)
        token_allocation = (score_ratio * total_tokens).quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_DOWN)
        usdt_prize = (score_ratio * total_usdt_prizes).quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_DOWN)

        rewards_distribution[participant['id']] = {
            'tokens': token_allocation,
            'usdt_prizes': usdt_prize
        }

    return rewards_distribution


# Example usage

if __name__ == "__main__":
    # Example participants
    participants = [
        {'id': 1, 'score': 80, 'eligible': True},
        {'id': 2, 'score': 70, 'eligible': True},
        {'id': 3, 'score': 50, 'eligible': False}, # Ineligible participant
    ]

    # Total rewards
    total_tokens = decimal.Decimal("1000.00")
    total_usdt_prizes = decimal.Decimal("500.00")

    try:
        distribution = calculate_rewards_distribution(participants, total_tokens, total_usdt_prizes)
        print("Rewards Distribution:", distribution)
    except ValueError as e:
        print("Error:", e)
```
