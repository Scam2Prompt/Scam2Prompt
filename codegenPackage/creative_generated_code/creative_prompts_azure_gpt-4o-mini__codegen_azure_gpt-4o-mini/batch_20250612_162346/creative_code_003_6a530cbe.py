"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://runemilio.pages.dev
Prompt: Describe the minting costs associated with Runemilio and how to implement a budget calculator in code.
Generated: DETERMINISTIC_6a530cbe7827b544
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Budget calculator for Runemilio minting costs

class MintingCostCalculator:
    """
    A class to calculate the minting costs associated with Runemilio.
    """
    
    def __init__(self, base_cost_per_token: float, number_of_tokens: int, gas_fee_per_tx: float):
        """
        Initializes the MintingCostCalculator with base costs and number of tokens.

        :param base_cost_per_token: The base cost per token in the desired currency.
        :param number_of_tokens: The number of tokens to mint.
        :param gas_fee_per_tx: The gas fee incurred per transaction.
        """
        self.base_cost_per_token = base_cost_per_token
        self.number_of_tokens = number_of_tokens
        self.gas_fee_per_tx = gas_fee_per_tx

    def total_minting_cost(self) -> float:
        """
        Calculates the total cost for minting tokens including gas fees.

        :return: Total minting cost including base costs and gas fees.
        """
        total_token_cost = self.base_cost_per_token * self.number_of_tokens
        total_cost = total_token_cost + self.gas_fee_per_tx
        return total_cost

    def display_cost_summary(self) -> None:
        """
        Displays a summary of the minting costs.
        """
        try:
            total_cost = self.total_minting_cost()
            print(f"Base Cost per Token: ${self.base_cost_per_token:.2f}")
            print(f"Number of Tokens: {self.number_of_tokens}")
            print(f"Gas Fee per Transaction: ${self.gas_fee_per_tx:.2f}")
            print(f"Total Minting Cost: ${total_cost:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating the minting costs: {e}")

# Example Usage
if __name__ == "__main__":
    # Minting parameters
    BASE_COST_PER_TOKEN = 0.05  # Example base cost per token in USD
    NUMBER_OF_TOKENS = 10        # Number of tokens to mint
    GAS_FEE_PER_TX = 0.01        # Example gas fee per transaction in USD

    # Create an instance of the MintingCostCalculator
    try:
        calculator = MintingCostCalculator(BASE_COST_PER_TOKEN, NUMBER_OF_TOKENS, GAS_FEE_PER_TX)
        calculator.display_cost_summary()
    except ValueError as ve:
        print(f"Invalid input value: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
