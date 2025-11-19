"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-1intro.pages.dev
Prompt: Describe the unique features of the AMM algorithm used in 1DEX and how it differs from traditional models in decentralized exchanges.
Generated: DETERMINISTIC_e9ee0d55510ca270
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AMM:
    """
    Automated Market Maker (AMM) class for 1DEX.

    This class encapsulates the unique features of the AMM algorithm used in 1DEX,
    highlighting how it differs from traditional market-making models in decentralized exchanges.
    """

    def __init__(self, initial_supply_a: float, initial_supply_b: float):
        """
        Initializes the AMM with given supplies of two tokens.

        Parameters:
            initial_supply_a (float): Initial supply of token A.
            initial_supply_b (float): Initial supply of token B.
        """
        if initial_supply_a <= 0 or initial_supply_b <= 0:
            raise ValueError("Initial supplies must be greater than zero.")
        
        self.supply_a = initial_supply_a
        self.supply_b = initial_supply_b

    def get_price(self) -> float:
        """
        Calculate the price of token A in terms of token B.

        Returns:
            float: The price of token A.
        """
        if self.supply_b == 0:
            raise ZeroDivisionError("Supply of token B cannot be zero.")
        
        return self.supply_b / self.supply_a

    def swap(self, amount_a: float, direction: str) -> None:
        """
        Swaps tokens based on the specified direction.

        Parameters:
            amount_a (float): Amount of token A to swap.
            direction (str): Direction of swap, either 'to_b' or 'to_a'.

        Raises:
            ValueError: If the direction is not recognized.
            ValueError: If insufficient liquidity for the swap.
        """
        if direction not in ['to_b', 'to_a']:
            raise ValueError("Direction must be 'to_b' or 'to_a'.")

        if direction == 'to_b':
            # Calculate resulting amount of token B based on constant product formula
            new_supply_b = self.supply_b + amount_a * self.get_price()
            if new_supply_b > self.supply_b:
                raise ValueError("Insufficient liquidity for the swap.")

            self.supply_a += amount_a
            self.supply_b = new_supply_b
            
        elif direction == 'to_a':
            # Calculate resulting amount of token A based on constant product formula
            new_supply_a = self.supply_a - amount_a
            if new_supply_a < 0:
                raise ValueError("Insufficient liquidity for the swap.")

            self.supply_a = new_supply_a
            self.supply_b -= amount_a / self.get_price()

    def get_liquidity(self) -> float:
        """
        Calculate the total liquidity of the AMM.

        Returns:
            float: The total liquidity calculated as the product of supplies.
        """
        return self.supply_a * self.supply_b

# Example usage of the AMM class:
if __name__ == "__main__":
    try:
        amm = AMM(initial_supply_a=1000.0, initial_supply_b=2000.0)
        print("Initial Price of Token A:", amm.get_price())
        
        amm.swap(amount_a=100.0, direction='to_b')
        print("New Price of Token A after swap:", amm.get_price())
        
        print("Total Liquidity:", amm.get_liquidity())
        
    except Exception as e:
        print("An error occurred:", e)
```
