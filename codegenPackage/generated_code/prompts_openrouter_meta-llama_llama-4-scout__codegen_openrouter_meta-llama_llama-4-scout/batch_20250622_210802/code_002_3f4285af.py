"""
Generated Code Metadata:
========================
Original URL: https://dresale.pages.dev
Prompt: "Generate a Python script to calculate the amount of $DRE tokens a user can buy based on the provided FTM amounts and presale cap."
Generated: DETERMINISTIC_3f4285af1082e013
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculate the amount of $DRE tokens a user can buy based on the provided FTM amounts and presale cap.

Usage:
    python dre_token_calculator.py
"""

def calculate_dre_tokens(ftm_amount, presale_cap, ftm_per_dre):
    """
    Calculate the amount of $DRE tokens a user can buy.

    Args:
        ftm_amount (float): The amount of FTM provided by the user.
        presale_cap (float): The presale cap in FTM.
        ftm_per_dre (float): The amount of FTM required to buy one $DRE token.

    Returns:
        float: The amount of $DRE tokens the user can buy.

    Raises:
        ValueError: If the FTM amount, presale cap, or FTM per DRE is negative.
    """
    if ftm_amount < 0 or presale_cap < 0 or ftm_per_dre <= 0:
        raise ValueError("FTM amount, presale cap, and FTM per DRE must be non-negative, and FTM per DRE must be positive.")

    # Calculate the maximum amount of DRE tokens that can be bought with the presale cap
    max_dre_tokens = presale_cap / ftm_per_dre

    # Calculate the amount of DRE tokens the user can buy
    dre_tokens = min(ftm_amount / ftm_per_dre, max_dre_tokens)

    return dre_tokens


def main():
    try:
        # Define the presale cap and FTM per DRE
        presale_cap = 100000  # FTM
        ftm_per_dre = 0.1  # FTM per DRE

        # Get the FTM amount from the user
        ftm_amount = float(input("Enter the FTM amount: "))

        # Calculate the DRE tokens
        dre_tokens = calculate_dre_tokens(ftm_amount, presale_cap, ftm_per_dre)

        # Print the result
        print(f"You can buy {dre_tokens:.2f} $DRE tokens.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
