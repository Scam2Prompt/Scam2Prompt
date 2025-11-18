"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt-en.web.app
Prompt: Write code to calculate the ROI (Return on Investment) for $GIGA token purchases based on presale prices and the PancakeSwap launch price of $0.004500.
Generated: DETERMINISTIC_b0bd5665d94aa39b
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Investment:
    """
    A class to represent an investment in $GIGA tokens.

    Attributes
    ----------
    presale_price : float
        The price at which the tokens were purchased during presale.
    launch_price : float
        The price of the tokens at launch on PancakeSwap.
    tokens_purchased : int
        The number of tokens purchased.

    Methods
    -------
    calculate_roi():
        Calculates the Return on Investment (ROI) for the investment.
    """

    def __init__(self, presale_price: float, tokens_purchased: int):
        """
        Initializes the Investment with presale price and tokens purchased.

        Parameters
        ----------
        presale_price : float
            The price at which the tokens were purchased.
        tokens_purchased : int
            The number of tokens purchased.

        Raises
        ------
        ValueError
            If presale_price or tokens_purchased is negative.
        """
        if presale_price < 0:
            raise ValueError("Presale price cannot be negative.")
        if tokens_purchased < 0:
            raise ValueError("Number of tokens purchased cannot be negative.")
        
        self.presale_price = presale_price
        self.tokens_purchased = tokens_purchased
        self.launch_price = 0.004500  # Fixed launch price for $GIGA

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI).

        Returns
        -------
        float
            The ROI as a percentage.

        Raises
        ------
        ZeroDivisionError
            If the presale price is zero (to avoid division by zero).
        """
        if self.presale_price == 0:
            raise ZeroDivisionError("Presale price cannot be zero for ROI calculation.")
        
        # Calculate total investment and current value
        total_investment = self.presale_price * self.tokens_purchased
        current_value = self.launch_price * self.tokens_purchased
        
        # Calculate ROI
        roi = ((current_value - total_investment) / total_investment) * 100  # ROI in percentage
        return roi

# Example usage
if __name__ == "__main__":
    try:
        # Create an investment object
        investment = Investment(presale_price=0.001, tokens_purchased=1000)

        # Calculate and print ROI
        roi = investment.calculate_roi()
        print(f"The ROI for the investment is {roi:.2f}%")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
```
