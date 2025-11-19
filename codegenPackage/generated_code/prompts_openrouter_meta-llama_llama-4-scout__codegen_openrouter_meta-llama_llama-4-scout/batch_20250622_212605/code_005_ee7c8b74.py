"""
Generated Code Metadata:
========================
Original URL: https://lifonex.com
Prompt: Create a function to convert Lifonex market probabilities into potential profit/loss calculations, taking into account the 4.05% APY on cash and positions.
Generated: DETERMINISTIC_ee7c8b7485df92d7
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_potential_profit_loss(market_probabilities, stake_amount, apy=0.0405):
    """
    Calculate potential profit/loss based on Lifonex market probabilities.

    Args:
    - market_probabilities (dict): Dictionary containing market probabilities.
        Example: {'win': 0.6, 'loss': 0.4}
    - stake_amount (float): The amount staked on the market.
    - apy (float, optional): The annual percentage yield. Defaults to 0.0405 (4.05%).

    Returns:
    - dict: Dictionary containing potential profit/loss calculations.

    Raises:
    - ValueError: If market probabilities do not add up to 1.
    """

    # Validate market probabilities
    if abs(sum(market_probabilities.values()) - 1) > 1e-6:
        raise ValueError("Market probabilities must add up to 1")

    # Calculate potential profit/loss
    potential_profit_loss = {}

    for outcome, probability in market_probabilities.items():
        # Calculate potential profit/loss without APY
        if outcome == 'win':
            potential_profit = stake_amount * (1 / probability - 1)
            potential_loss = 0
        elif outcome == 'loss':
            potential_profit = 0
            potential_loss = stake_amount

        # Apply APY to stake amount
        apy_factor = 1 + (apy / 365)  # assume 365-day year for simplicity
        adjusted_stake_amount = stake_amount * apy_factor

        # Store results
        if outcome not in potential_profit_loss:
            potential_profit_loss[outcome] = {}
        potential_profit_loss[outcome]['potential_profit'] = potential_profit
        potential_profit_loss[outcome]['potential_loss'] = potential_loss
        potential_profit_loss[outcome]['adjusted_stake_amount'] = adjusted_stake_amount

    return potential_profit_loss


def main():
    market_probabilities = {'win': 0.6, 'loss': 0.4}
    stake_amount = 100.0

    try:
        result = calculate_potential_profit_loss(market_probabilities, stake_amount)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
