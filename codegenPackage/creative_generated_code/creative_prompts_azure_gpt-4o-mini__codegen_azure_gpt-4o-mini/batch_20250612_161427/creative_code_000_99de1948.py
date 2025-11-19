"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-9y3.pages.dev
Prompt: Generate a code snippet to calculate the conversion rate from BASE to JESSE tokens based on a presale cap of 1000 BASE.
Generated: DETERMINISTIC_99de1948face5ced
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenConverter:
    def __init__(self, presale_cap: float):
        """
        Initializes the TokenConverter with a presale cap.
        
        Args:
            presale_cap (float): The maximum amount of BASE tokens available for conversion.
        """
        if presale_cap <= 0:
            raise ValueError("Presale cap must be a positive number.")
        self.presale_cap = presale_cap

    def convert_base_to_jesse(self, base_amount: float, conversion_rate: float) -> float:
        """
        Converts BASE tokens to JESSE tokens based on the set conversion rate.

        Args:
            base_amount (float): The amount of BASE tokens to convert.
            conversion_rate (float): The rate at which BASE tokens convert to JESSE tokens.

        Returns:
            float: The equivalent amount of JESSE tokens.

        Raises:
            ValueError: If base_amount is negative or if conversion_rate is less than or equal to zero.
            RuntimeError: If the base_amount exceeds the presale cap.
        """
        if base_amount < 0:
            raise ValueError("Base amount cannot be negative.")
        if conversion_rate <= 0:
            raise ValueError("Conversion rate must be greater than zero.")
        if base_amount > self.presale_cap:
            raise RuntimeError("Base amount exceeds the presale cap.")

        # Calculate the conversion
        jesse_amount = base_amount * conversion_rate
        return jesse_amount


if __name__ == "__main__":
    # Example usage of the TokenConverter class
    presale_cap = 1000.0  # Set the presale cap
    conversion_rate = 2.5  # Assume each BASE converts to 2.5 JESSE tokens

    converter = TokenConverter(presale_cap)

    try:
        base_to_convert = 800.0  # Amount of BASE tokens to convert
        jesse_tokens = converter.convert_base_to_jesse(base_to_convert, conversion_rate)
        print(f"Converted {base_to_convert} BASE to {jesse_tokens} JESSE tokens.")
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
