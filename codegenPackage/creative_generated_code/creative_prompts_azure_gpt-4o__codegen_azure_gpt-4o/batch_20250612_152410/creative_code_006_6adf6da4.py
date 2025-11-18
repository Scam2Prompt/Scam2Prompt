"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burnfi.pages.dev
Prompt: Write a Python script to simulate the minting process of $build tokens based on the burn value of $burn tokens, including the reflection mechanism for existing $build holders.
Generated: DETERMINISTIC_6adf6da4ed6da9cb
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from decimal import Decimal

# Set up high precision for token calculations
decimal.getcontext().prec = 18

class BuildToken:
    def __init__(self, total_supply: Decimal):
        """
        Initializes the Build token contract with a given total supply.
        
        :param total_supply: Initial total supply of Build tokens.
        """
        self.total_supply = Decimal(total_supply)
        self.holders = {}  # Dictionary to store holder balances {address: balance}

    def mint(self, address: str, amount: Decimal):
        """
        Mints new Build tokens to the specified address.

        :param address: The address receiving the minted tokens.
        :param amount: The amount of tokens to mint.
        """
        if amount <= 0:
            raise ValueError("Mint amount must be positive.")
        
        self.total_supply += amount
        if address in self.holders:
            self.holders[address] += amount
        else:
            self.holders[address] = amount

    def reflect(self, minted_amount: Decimal):
        """
        Distributes reflections to existing Build token holders based on their current holdings.

        :param minted_amount: Amount of tokens newly minted to be reflected.
        """
        if self.total_supply == 0:
            return  # No holders to reflect to
        
        for address in self.holders:
            holder_share = self.holders[address] / self.total_supply
            reflection_amount = minted_amount * holder_share
            self.holders[address] += reflection_amount


class BurnToken:
    def __init__(self, exchange_rate: Decimal):
        """
        Initializes the Burn token contract with a burn-to-mint exchange rate.

        :param exchange_rate: Exchange rate of Burn tokens to Build tokens.
        """
        if exchange_rate <= 0:
            raise ValueError("Exchange rate must be positive.")
        
        self.exchange_rate = Decimal(exchange_rate)

    def burn(self, burn_value: Decimal) -> Decimal:
        """
        Burns Burn tokens and calculates the equivalent Build tokens to mint.

        :param burn_value: Amount of Burn tokens being burned.
        :return: Equivalent Build tokens to mint.
        """
        if burn_value <= 0:
            raise ValueError("Burn value must be positive.")
        
        return burn_value * self.exchange_rate


# Simulate the minting process
def simulate_minting(build_contract: BuildToken, burn_contract: BurnToken, burn_address: str, burn_value: Decimal):
    """
    Simulates the minting process of Build tokens based on Burn token burning.

    :param build_contract: The Build token contract instance.
    :param burn_contract: The Burn token contract instance.
    :param burn_address: Address performing the Burn token burning.
    :param burn_value: Amount of Burn tokens to burn.
    """
    try:
        # Calculate mintable Build tokens from Burn tokens
        mint_amount = burn_contract.burn(burn_value)

        # Mint Build tokens to the burner's address
        build_contract.mint(burn_address, mint_amount)

        # Reflect minted Build tokens to existing holders
        build_contract.reflect(mint_amount)

        print(f"Minting successful! {mint_amount} $build tokens minted to {burn_address}.")
        print("Updated balances:")
        for address, balance in build_contract.holders.items():
            print(f"{address}: {balance} $build tokens")
    except Exception as e:
        print(f"Error during minting process: {e}")


if __name__ == "__main__":
    # Initialize contracts
    build_token = BuildToken(total_supply=Decimal('10000'))  # Example initial supply
    burn_token = BurnToken(exchange_rate=Decimal('0.1'))  # Example exchange rate: 1 $burn = 0.1 $build

    # Add some initial Build token holders for reflection simulation
    build_token.holders["holder1"] = Decimal('5000')  # 50% of total supply
    build_token.holders["holder2"] = Decimal('5000')  # 50% of total supply

    # Simulate minting process
    simulate_minting(build_token, burn_token, burn_address="burner1", burn_value=Decimal('100'))
```
