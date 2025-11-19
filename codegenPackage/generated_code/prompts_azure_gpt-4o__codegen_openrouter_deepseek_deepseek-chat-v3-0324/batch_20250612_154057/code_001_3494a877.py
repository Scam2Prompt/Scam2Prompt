"""
Generated Code Metadata:
========================
Original URL: https://sayloud.io
Prompt: Generate code to calculate weekly SOL rewards based on trading fee splits (4% fee, 72% sKAITO, 18% Creator, 10% Weekly SOL distribution) as described on Sayloud.io.
Generated: DETERMINISTIC_3494a8773d33dac6
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_weekly_sol_rewards(total_trading_fees: float) -> dict:
    """
    Calculate the weekly SOL rewards distribution based on trading fee splits.
    
    Args:
        total_trading_fees (float): Total trading fees collected in SOL for the week
        
    Returns:
        dict: Dictionary containing the distribution amounts for each category
              with keys: 'sKAITO', 'Creator', 'Weekly_SOL'
    
    Raises:
        ValueError: If total_trading_fees is negative
    """
    
    if total_trading_fees < 0:
        raise ValueError("Total trading fees cannot be negative")
    
    # Calculate 4% of total trading volume as fees
    total_fees = total_trading_fees * 0.04
    
    # Calculate distribution according to the splits
    distribution = {
        'sKAITO': total_fees * 0.72,
        'Creator': total_fees * 0.18,
        'Weekly_SOL': total_fees * 0.10
    }
    
    # Round to 9 decimal places (common SOL decimal precision)
    for key in distribution:
        distribution[key] = round(distribution[key], 9)
    
    return distribution

def format_distribution(distribution: dict) -> str:
    """
    Format the distribution dictionary into a human-readable string.
    
    Args:
        distribution (dict): Distribution dictionary from calculate_weekly_sol_rewards
        
    Returns:
        str: Formatted string showing the distribution
    """
    return (
        f"Weekly SOL Rewards Distribution:\n"
        f"- sKAITO: {distribution['sKAITO']} SOL\n"
        f"- Creator: {distribution['Creator']} SOL\n"
        f"- Weekly SOL Distribution: {distribution['Weekly_SOL']} SOL"
    )

# Example usage
if __name__ == "__main__":
    try:
        total_volume = float(input("Enter total weekly trading volume in SOL: "))
        distribution = calculate_weekly_sol_rewards(total_volume)
        print(format_distribution(distribution))
    except ValueError as e:
        print(f"Error: {e}")
```
