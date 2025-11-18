"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraidex.pages.dev
Prompt: Generate code to calculate the expected output of a token swap on OraiDEX, factoring in slippage and the 0.3% tax rate.
Generated: DETERMINISTIC_93ac50475eb39898
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_token_swap_output(input_amount, exchange_rate, slippage_percentage, tax_rate_percentage):
    """
    Calculate the expected output of a token swap on OraiDEX, factoring in slippage and tax rate.
    
    Args:
        input_amount (float): The amount of token being swapped.
        exchange_rate (float): The current exchange rate (output token per input token).
        slippage_percentage (float): The slippage percentage (e.g., 0.5 for 0.5% slippage).
        tax_rate_percentage (float): The tax rate percentage (e.g., 0.3 for 0.3% tax).
    
    Returns:
        float: The expected output amount after factoring slippage and tax.
    Raises:
        ValueError: If input values are invalid (negative or zero).
    """

    # Validate input parameters
    if input_amount <= 0:
        raise ValueError("Input amount must be greater than zero.")
    if exchange_rate <= 0:
        raise ValueError("Exchange rate must be greater than zero.")
    if slippage_percentage < 0:
        raise ValueError("Slippage percentage cannot be negative.")
    if tax_rate_percentage < 0:
        raise ValueError("Tax rate percentage cannot be negative.")

    # Calculate raw output amount before slippage and tax
    raw_output = input_amount * exchange_rate

    # Calculate slippage adjustment
    slippage_adjustment = raw_output * (slippage_percentage / 100)

    # Apply slippage to the raw output
    adjusted_output = raw_output - slippage_adjustment

    # Calculate tax adjustment
    tax_adjustment = adjusted_output * (tax_rate_percentage / 100)

    # Apply tax to the adjusted output
    final_output = adjusted_output - tax_adjustment

    return final_output


def main():
    try:
        # Example inputs (replace these values with user-specific inputs)
        input_amount = float(input("Enter the input token amount: "))
        exchange_rate = float(input("Enter the exchange rate (output token per input token): "))
        slippage_percentage = float(input("Enter the slippage percentage (e.g., 0.5 for 0.5%): "))
        tax_rate_percentage = float(input("Enter the tax rate percentage (e.g., 0.3 for 0.3%): "))

        # Calculate and display the expected output
        expected_output = calculate_token_swap_output(
            input_amount, exchange_rate, slippage_percentage, tax_rate_percentage
        )

        print(f"Expected output token amount: {expected_output:.6f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
