"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetasite.web.app
Prompt: Create a script that calculates the potential APY for staking $EMT tokens based on the current presale stage bonuses.
Generated: DETERMINISTIC_f18e95a921da6fc9
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_apy(base_apy, bonus_percentage):
    """
    Calculate the potential APY (Annual Percentage Yield) for staking EMT tokens.

    Args:
        base_apy (float): The base APY rate (e.g., 10.0 for 10%).
        bonus_percentage (float): Bonus percentage provided during the presale stage (e.g., 20.0 for 20% bonus).

    Returns:
        float: The total APY including the presale bonus.
    """
    try:
        # Validate input types
        if not isinstance(base_apy, (float, int)) or not isinstance(bonus_percentage, (float, int)):
            raise ValueError("Base APY and bonus percentage must be numeric values.")

        # Ensure values are positive
        if base_apy < 0 or bonus_percentage < 0:
            raise ValueError("Base APY and bonus percentage must be non-negative values.")

        # Calculate total APY
        total_apy = base_apy * (1 + bonus_percentage / 100)
        return total_apy
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    """
    Main function to calculate and display the potential APY for staking EMT tokens.
    """
    try:
        # Example: User input for base APY and bonus percentage
        base_apy = float(input("Enter the base APY (e.g., 10.0 for 10%): "))
        bonus_percentage = float(input("Enter the bonus percentage during presale (e.g., 20.0 for 20%): "))

        # Calculate potential APY
        potential_apy = calculate_apy(base_apy, bonus_percentage)

        # Display results
        print(f"Base APY: {base_apy}%")
        print(f"Presale Bonus: {bonus_percentage}%")
        print(f"Potential APY: {potential_apy:.2f}%")
    except ValueError:
        print("Invalid input. Please enter numeric values for both base APY and bonus percentage.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
