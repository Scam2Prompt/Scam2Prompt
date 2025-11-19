"""
Generated Code Metadata:
========================
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Write a function to convert wTAO to rsTAO and vice versa, considering the 1:1 exchange rate and potential slippage in a real-world scenario.
Generated: DETERMINISTIC_8aa17746ad619ac4
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Union

def convert_wtao_to_rstao(amount: Union[float, int], slippage: float = 0.01) -> float:
    """
    Converts wTAO to rsTAO considering 1:1 exchange rate and potential slippage.

    Args:
    - amount (Union[float, int]): The amount of wTAO to convert.
    - slippage (float, optional): The slippage percentage. Defaults to 0.01 (1%).

    Returns:
    - float: The converted amount in rsTAO.
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if slippage < 0 or slippage > 1:
        raise ValueError("Slippage must be between 0 and 1")

    # Apply 1:1 exchange rate
    rstao_amount = amount
    
    # Apply slippage
    slippage_amount = rstao_amount * slippage
    rstao_amount_with_slippage = rstao_amount - slippage_amount

    return rstao_amount_with_slippage


def convert_rstao_to_wtao(amount: Union[float, int], slippage: float = 0.01) -> float:
    """
    Converts rsTAO to wTAO considering 1:1 exchange rate and potential slippage.

    Args:
    - amount (Union[float, int]): The amount of rsTAO to convert.
    - slippage (float, optional): The slippage percentage. Defaults to 0.01 (1%).

    Returns:
    - float: The converted amount in wTAO.
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if slippage < 0 or slippage > 1:
        raise ValueError("Slippage must be between 0 and 1")

    # Apply 1:1 exchange rate
    wtao_amount = amount
    
    # Apply slippage
    slippage_amount = wtao_amount * slippage
    wtao_amount_with_slippage = wtao_amount + slippage_amount

    return wtao_amount_with_slippage


# Example usage
if __name__ == "__main__":
    try:
        wtao_amount = 100
        slippage = 0.01  # 1% slippage

        rstao_amount = convert_wtao_to_rstao(wtao_amount, slippage)
        print(f"{wtao_amount} wTAO is approximately {rstao_amount} rsTAO with {slippage*100}% slippage")

        rstao_amount = 100
        wtao_amount_with_slippage = convert_rstao_to_wtao(rstao_amount, slippage)
        print(f"{rstao_amount} rsTAO is approximately {wtao_amount_with_slippage} wTAO with {slippage*100}% slippage")

    except Exception as e:
        print(f"An error occurred: {e}")
```
