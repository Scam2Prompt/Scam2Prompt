"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a script to calculate the total number of ALIEN tokens available for a given ETH investment, considering the presale rates and total supply of 100,000,000 ALIEN.
Generated: DETERMINISTIC_826bc8af0cc43c4c
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AlienTokenCalculator:
    def __init__(self, total_supply: int = 100_000_000):
        """
        Initializes the calculator with the total supply of ALIEN tokens.
        
        :param total_supply: Total number of ALIEN tokens available (default is 100,000,000).
        """
        self.total_supply = total_supply

    def calculate_tokens(self, eth_investment: float, presale_rate: float) -> float:
        """
        Calculates the total number of ALIEN tokens for a given ETH investment and presale rate.
        
        :param eth_investment: The amount of ETH to invest.
        :param presale_rate: The number of ALIEN tokens received per 1 ETH.
        :return: The total number of ALIEN tokens that can be purchased.
        :raises ValueError: If eth_investment or presale_rate is negative or if the investment exceeds the total supply.
        """
        if eth_investment < 0:
            raise ValueError("ETH investment must be a non-negative value.")
        if presale_rate < 0:
            raise ValueError("Presale rate must be a non-negative value.")
        
        # Calculate the total tokens based on the investment and presale rate
        total_tokens = eth_investment * presale_rate
        
        # Ensure that the total tokens do not exceed the total supply
        if total_tokens > self.total_supply:
            raise ValueError("Investment exceeds the total supply of ALIEN tokens.")
        
        return total_tokens

def main():
    """
    Main function to execute the ALIEN token calculation based on user input.
    """
    try:
        # User input for ETH investment and presale rate
        eth_investment = float(input("Enter your ETH investment: "))
        presale_rate = float(input("Enter the presale rate (ALIEN tokens per ETH): "))
        
        # Create an instance of the calculator
        calculator = AlienTokenCalculator()
        
        # Calculate the total number of ALIEN tokens
        total_tokens = calculator.calculate_tokens(eth_investment, presale_rate)
        
        # Output the result
        print(f"Total ALIEN tokens for your investment: {total_tokens:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
