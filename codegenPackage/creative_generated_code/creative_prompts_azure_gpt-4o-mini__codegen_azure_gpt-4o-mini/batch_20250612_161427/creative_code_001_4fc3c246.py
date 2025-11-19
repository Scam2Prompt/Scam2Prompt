"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-9y3.pages.dev
Prompt: Write a function that takes an amount in BASE and returns the equivalent amount in JESSE tokens, considering the presale rate of 0.1 BASE for 99,500 JESSE.
Generated: DETERMINISTIC_4fc3c24631ba1dea
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
    """A class to convert BASE amounts into JESSE tokens based on the presale rate."""
    
    PRESALE_RATE = 0.1  # Amount of BASE needed for 99,500 JESSE tokens
    JESSE_TOKENS_PER_BASE = 99500 / PRESALE_RATE  # JESSE tokens per BASE unit

    @staticmethod
    def convert_base_to_jesse(base_amount: float) -> float:
        """Converts a given amount in BASE to JESSE tokens.
        
        Args:
            base_amount (float): The amount in BASE to convert.
        
        Returns:
            float: The equivalent amount in JESSE tokens.
        
        Raises:
            ValueError: If the base_amount is negative or not a number.
        """
        if not isinstance(base_amount, (int, float)):
            raise ValueError("The base_amount must be a number.")
        if base_amount < 0:
            raise ValueError("The base_amount cannot be negative.")
        
        # Calculate the amount of JESSE tokens
        jesse_tokens = base_amount * TokenConverter.JESSE_TOKENS_PER_BASE
        
        return jesse_tokens


# Example usage
if __name__ == "__main__":
    try:
        base_amount = 1.0  # Example BASE amount
        jesse_amount = TokenConverter.convert_base_to_jesse(base_amount)
        print(f"{base_amount} BASE is equivalent to {jesse_amount:.2f} JESSE tokens.")
    except ValueError as e:
        print(f"Error: {e}")
```
