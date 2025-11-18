"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethtokens.pages.dev
Prompt: Create a script to calculate the percentage of ENA tokens that need to be locked or staked to maintain unvested grants, referencing Ethena's platform rules.
Generated: DETERMINISTIC_64ef96522d7abf08
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_staking_percentage(total_tokens, unvested_grants, staking_rules_percentage):
    """
    Calculate the percentage of ENA tokens required to be staked/locked.

    Args:
        total_tokens (float): Total number of ENA tokens held by the user.
        unvested_grants (float): Total unvested grants in ENA tokens.
        staking_rules_percentage (float): Platform-required percentage for staking.

    Returns:
        float: Percentage of ENA tokens that need to be locked/staked.
    """
    try:
        # Validate inputs
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")
        if unvested_grants < 0:
            raise ValueError("Unvested grants cannot be negative.")
        if staking_rules_percentage < 0 or staking_rules_percentage > 100:
            raise ValueError("Staking rules percentage must be between 0 and 100.")

        # Calculate staking requirement
        required_staking_tokens = unvested_grants * (staking_rules_percentage / 100)
        staking_percentage_of_total = (required_staking_tokens / total_tokens) * 100

        return round(staking_percentage_of_total, 2)
    except ValueError as e:
        # Handle input validation errors
        print(f"Input Error: {e}")
        sys.exit(1)
    except ZeroDivisionError:
        # Handle division by zero error
        print("Calculation Error: Total tokens cannot be zero.")
        sys.exit(1)
    except Exception as e:
        # Handle other unforeseen errors
        print(f"Unexpected Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example Inputs (Replace these with dynamic inputs in production)
    try:
        # Read user inputs (for production, use input() or integrations like API calls)
        total_tokens = float(input("Enter total ENA tokens: "))
        unvested_grants = float(input("Enter unvested grants in ENA tokens: "))
        staking_rules_percentage = float(input("Enter staking rules percentage: "))

        # Calculate required staking percentage
        staking_percentage = calculate_staking_percentage(
            total_tokens, unvested_grants, staking_rules_percentage
        )

        # Display the result
        print(
            f"To maintain unvested grants, you need to stake approximately {staking_percentage}% of your total ENA tokens."
        )
    except ValueError:
        print("Please enter valid numerical values for the inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
