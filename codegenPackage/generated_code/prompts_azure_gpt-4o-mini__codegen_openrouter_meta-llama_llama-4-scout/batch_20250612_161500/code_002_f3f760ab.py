"""
Generated Code Metadata:
========================
Original URL: https://dre-8x7.pages.dev
Prompt: Create a script that simulates the purchase of DRE tokens at different FTM amounts (250, 500, 1000, 2000, 3000 FTM) and outputs the corresponding DRE tokens received.
Generated: DETERMINISTIC_f3f760abb7ca1223
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dre_token_purchase_simulator.py

def calculate_dre_tokens(ftm_amount, dre_price):
    """
    Calculates the DRE tokens received for a given FTM amount.

    Args:
        ftm_amount (float): The amount of FTM to spend.
        dre_price (float): The price of one DRE token in FTM.

    Returns:
        float: The number of DRE tokens received.
    """
    if dre_price <= 0:
        raise ValueError("DRE token price must be greater than zero")

    dre_tokens = ftm_amount / dre_price
    return dre_tokens


def simulate_purchases(ftm_amounts, dre_price):
    """
    Simulates the purchase of DRE tokens at different FTM amounts.

    Args:
        ftm_amounts (list[float]): A list of FTM amounts to spend.
        dre_price (float): The price of one DRE token in FTM.

    Returns:
        dict[float, float]: A dictionary mapping FTM amounts to DRE tokens received.
    """
    purchases = {}
    for ftm_amount in ftm_amounts:
        try:
            dre_tokens = calculate_dre_tokens(ftm_amount, dre_price)
            purchases[ftm_amount] = dre_tokens
        except Exception as e:
            print(f"Error simulating purchase of {ftm_amount} FTM: {str(e)}")

    return purchases


def main():
    # Define the FTM amounts to simulate
    ftm_amounts = [250, 500, 1000, 2000, 3000]

    # Define the price of one DRE token in FTM
    dre_price = 0.1  # example price

    # Simulate the purchases
    purchases = simulate_purchases(ftm_amounts, dre_price)

    # Print the results
    print("FTM Amount\tDRE Tokens Received")
    for ftm_amount, dre_tokens in purchases.items():
        print(f"{ftm_amount:.2f}\t\t{dre_tokens:.4f}")


if __name__ == "__main__":
    main()
```
