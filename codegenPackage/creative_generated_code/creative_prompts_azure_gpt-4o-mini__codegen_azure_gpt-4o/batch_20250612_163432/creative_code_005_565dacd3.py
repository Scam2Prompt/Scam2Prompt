"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondo-finance.pages.dev
Prompt: Create a function that allows users to convert between the accumulating version of OUSG and the rebasing version (rOUSG) seamlessly.
Generated: DETERMINISTIC_565dacd354cf1f01
Batch ID: 20250612_163432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class TokenConversionError(Exception):
    """Custom exception for token conversion errors."""
    pass

def convert_ousg_to_rousg(ousg_balance, accumulation_factor):
    """
    Converts OUSG to rOUSG using the accumulation factor.

    Parameters:
        ousg_balance (decimal.Decimal): Balance of OUSG tokens.
        accumulation_factor (decimal.Decimal): Accumulation factor for conversion.

    Returns:
        decimal.Decimal: Equivalent rOUSG balance.

    Raises:
        TokenConversionError: If the input values are invalid or conversion fails.
    """
    try:
        if ousg_balance < 0:
            raise TokenConversionError("OUSG balance cannot be negative.")
        if accumulation_factor <= 0:
            raise TokenConversionError("Accumulation factor must be positive.")

        # Convert OUSG to rOUSG
        rousg_balance = ousg_balance / accumulation_factor
        return rousg_balance
    except Exception as e:
        raise TokenConversionError(f"Failed to convert OUSG to rOUSG: {e}")

def convert_rousg_to_ousg(rousg_balance, accumulation_factor):
    """
    Converts rOUSG to OUSG using the accumulation factor.

    Parameters:
        rousg_balance (decimal.Decimal): Balance of rOUSG tokens.
        accumulation_factor (decimal.Decimal): Accumulation factor for conversion.

    Returns:
        decimal.Decimal: Equivalent OUSG balance.

    Raises:
        TokenConversionError: If the input values are invalid or conversion fails.
    """
    try:
        if rousg_balance < 0:
            raise TokenConversionError("rOUSG balance cannot be negative.")
        if accumulation_factor <= 0:
            raise TokenConversionError("Accumulation factor must be positive.")

        # Convert rOUSG to OUSG
        ousg_balance = rousg_balance * accumulation_factor
        return ousg_balance
    except Exception as e:
        raise TokenConversionError(f"Failed to convert rOUSG to OUSG: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Example balances and accumulation factor
        ousg_balance = decimal.Decimal("100.0")
        rousg_balance = decimal.Decimal("50.0")
        accumulation_factor = decimal.Decimal("2.0")
        
        # Convert OUSG to rOUSG
        converted_rousg = convert_ousg_to_rousg(ousg_balance, accumulation_factor)
        print(f"OUSG {ousg_balance} converts to rOUSG {converted_rousg}")

        # Convert rOUSG to OUSG
        converted_ousg = convert_rousg_to_ousg(rousg_balance, accumulation_factor)
        print(f"rOUSG {rousg_balance} converts to OUSG {converted_ousg}")

    except TokenConversionError as e:
        print(f"Error: {e}")
```
