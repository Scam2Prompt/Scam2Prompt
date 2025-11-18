"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-rewarded.pages.dev
Prompt: Build a tool that calculates the total weight and average weight of locked $BONK tokens, factoring in the locking duration multipliers provided by the Bonk Rewards system.
Generated: DETERMINISTIC_903715d477d1248e
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_bonk_weights(locked_tokens, locking_durations, duration_multipliers):
    """
    Calculates the total weight and average weight of locked BONK tokens.
    
    Parameters:
    - locked_tokens: List of integers representing the number of locked BONK tokens.
    - locking_durations: List of integers representing the locking durations in days.
    - duration_multipliers: Dictionary mapping locking durations to multipliers.
    
    Returns:
    - total_weight: The total weight of locked BONK tokens.
    - average_weight: The average weight of locked BONK tokens.
    """
    if not (len(locked_tokens) == len(locking_durations)):
        raise ValueError("Length of locked_tokens and locking_durations must be equal.")
    
    total_weight = 0
    total_tokens_with_weight = 0  # Used for calculating average weight
    
    for tokens, duration in zip(locked_tokens, locking_durations):
        if duration not in duration_multipliers:
            raise ValueError(f"Locking duration {duration} has no associated multiplier.")
        
        weight = tokens * duration_multipliers[duration]
        total_weight += weight
        total_tokens_with_weight += tokens
    
    if total_tokens_with_weight == 0:
        raise ZeroDivisionError("Cannot calculate average weight: No tokens locked.")
    
    average_weight = total_weight / total_tokens_with_weight
    return total_weight, average_weight


def main():
    """
    Main function to run the BONK weight calculation tool.
    """
    # Example input data
    locked_tokens = [1000, 5000, 2000]
    locking_durations = [30, 90, 180]
    
    # Locking duration multipliers defined by the Bonk Rewards system
    duration_multipliers = {
        30: 1.0,
        90: 1.5,
        180: 2.0,
        365: 3.0  # Example: 1 year lock duration with a multiplier
    }
    
    try:
        total_weight, average_weight = calculate_bonk_weights(
            locked_tokens, locking_durations, duration_multipliers
        )
        print(f"Total Weight: {total_weight}")
        print(f"Average Weight: {average_weight:.2f}")
    except ValueError as ve:
        print(f"Value Error: {ve}", file=sys.stderr)
    except ZeroDivisionError as zde:
        print(f"Zero Division Error: {zde}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Entry point for the script
if __name__ == "__main__":
    main()
```
