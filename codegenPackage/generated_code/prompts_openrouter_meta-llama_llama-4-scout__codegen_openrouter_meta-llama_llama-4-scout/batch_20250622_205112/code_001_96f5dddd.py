"""
Generated Code Metadata:
========================
Original URL: https://bafybeiavwskgiww3elpabxoxlcv3n46mhlr4fohrwq3gyojtkwmivmo2bu.ipfs.dweb.link
Prompt: "Write a function to calculate the amount of $BCKR tokens received for a given ETH deposit in a presale, considering a presale cap of 1000 ETH and a total supply of 100,000,000 BCKR."
Generated: DETERMINISTIC_96f5dddd310729d8
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_bckr_tokens(eth_deposit: float, presale_cap: float = 1000, total_bckr_supply: int = 100000000) -> float:
    """
    Calculate the amount of BCKR tokens received for a given ETH deposit in a presale.

    Args:
    - eth_deposit (float): The amount of ETH deposited.
    - presale_cap (float): The presale cap in ETH. Defaults to 1000.
    - total_bckr_supply (int): The total supply of BCKR tokens. Defaults to 100,000,000.

    Returns:
    - float: The amount of BCKR tokens received.

    Raises:
    - ValueError: If the ETH deposit or presale cap is negative.
    - ZeroDivisionError: If the presale cap is zero.
    """

    # Check for invalid input values
    if eth_deposit < 0:
        raise ValueError("ETH deposit cannot be negative.")
    if presale_cap <= 0:
        if presale_cap == 0:
            raise ZeroDivisionError("Presale cap cannot be zero.")
        else:
            raise ValueError("Presale cap must be greater than zero.")

    # Calculate the token price in BCKR per ETH
    # Assuming a simple linear distribution of tokens
    bckr_per_eth = total_bckr_supply / presale_cap

    # Calculate the BCKR tokens received for the given ETH deposit
    bckr_tokens = eth_deposit * bckr_per_eth

    return bckr_tokens


def main():
    try:
        eth_deposit = 1.0  # example ETH deposit
        bckr_tokens_received = calculate_bckr_tokens(eth_deposit)
        print(f"For an ETH deposit of {eth_deposit} ETH, you receive {bckr_tokens_received} BCKR tokens.")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
