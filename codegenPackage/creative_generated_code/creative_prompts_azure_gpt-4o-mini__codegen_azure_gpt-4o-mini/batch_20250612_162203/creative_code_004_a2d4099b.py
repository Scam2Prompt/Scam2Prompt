"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flash-stakes.pages.dev
Prompt: What are the key tokenomics of the FLASH token, and how does it relate to the yield generated in the Flashstake protocol?
Generated: DETERMINISTIC_a2d4099b555170c2
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    """
    A class to represent the tokenomics of the FLASH token.
    """

    def __init__(self, total_supply: float, circulating_supply: float, yield_rate: float):
        """
        Initializes the Tokenomics class with total supply, circulating supply, and yield rate.

        Parameters:
            total_supply (float): The total supply of FLASH tokens.
            circulating_supply (float): The current circulating supply of FLASH tokens.
            yield_rate (float): The yield rate for the FLASH token.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if circulating_supply < 0 or circulating_supply > total_supply:
            raise ValueError("Circulating supply must be between 0 and total supply.")
        if yield_rate < 0:
            raise ValueError("Yield rate must be non-negative.")
        
        self.total_supply = total_supply
        self.circulating_supply = circulating_supply
        self.yield_rate = yield_rate

    def calculate_yield(self, amount_staked: float) -> float:
        """
        Calculates the yield generated from staking a specific amount of FLASH tokens.

        Parameters:
            amount_staked (float): The amount of FLASH tokens staked.

        Returns:
            float: The yield generated.
        
        Raises:
            ValueError: If amount_staked is negative or greater than the circulating supply.
        """
        if amount_staked < 0:
            raise ValueError("Amount staked must be non-negative.")
        if amount_staked > self.circulating_supply:
            raise ValueError("Amount staked cannot exceed the circulating supply.")

        yield_generated = amount_staked * self.yield_rate
        return yield_generated

    def get_tokenomics_summary(self) -> dict:
        """
        Provides a summary of the tokenomics.

        Returns:
            dict: A summary containing total supply, circulating supply, and yield rate.
        """
        return {
            "Total Supply": self.total_supply,
            "Circulating Supply": self.circulating_supply,
            "Yield Rate": self.yield_rate,
        }

# Example usage
if __name__ == "__main__":
    try:
        # Creating an instance of Tokenomics with sample values
        flash_token = Tokenomics(total_supply=1000000, circulating_supply=500000, yield_rate=0.05)

        # Calculating yield for a certain amount staked
        yield_generated = flash_token.calculate_yield(10000)
        print(f"Yield generated from staking 10,000 FLASH: {yield_generated}")

        # Getting tokenomics summary
        summary = flash_token.get_tokenomics_summary()
        print("Tokenomics Summary:", summary)

    except ValueError as e:
        print(f"Error: {e}")
```
