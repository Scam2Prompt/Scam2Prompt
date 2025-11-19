"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burnfi.pages.dev
Prompt: Write a code snippet to calculate the BNB reward based on $build holdings and proofs as described on BurnedFi.
Generated: DETERMINISTIC_f02010c6935bbdbe
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_bnb_reward(build_holdings, proofs, total_proof_value, total_bnb_pool):
    """
    Calculate the BNB reward for a user based on $build holdings and proofs.

    Args:
        build_holdings (float): The amount of $build tokens the user holds.
        proofs (float): The user's contribution in proofs (e.g., burned tokens, staked tokens, etc.).
        total_proof_value (float): The total contribution in proofs across all users.
        total_bnb_pool (float): The total BNB reward pool available.

    Returns:
        float: The calculated BNB reward for the user.
    """
    try:
        # Validate inputs
        if build_holdings < 0 or proofs < 0 or total_proof_value <= 0 or total_bnb_pool <= 0:
            raise ValueError("All input values must be positive, and total_proof_value/total_bnb_pool must be greater than zero.")

        # Calculate the user's proof contribution ratio
        proof_ratio = proofs / total_proof_value

        # Calculate reward based on $build holdings and proofs
        bnb_reward = total_bnb_pool * proof_ratio * (build_holdings / (build_holdings + 1))

        return round(bnb_reward, 8)  # Return reward rounded to 8 decimal places

    except ZeroDivisionError:
        print("Error: Division by zero. Please ensure total_proof_value and build_holdings are valid.", file=sys.stderr)
        return 0.0
    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return 0.0
    except Exception as e:
        print(f"Unexpected error occurred: {e}", file=sys.stderr)
        return 0.0

# Example usage
if __name__ == "__main__":
    # Example inputs
    user_build_holdings = 1000.0
    user_proofs = 50.0
    global_total_proof_value = 1000.0
    global_total_bnb_pool = 10.0

    # Calculate user's BNB reward
    reward = calculate_bnb_reward(user_build_holdings, user_proofs, global_total_proof_value, global_total_bnb_pool)
    print(f"Calculated BNB Reward: {reward} BNB")
```
