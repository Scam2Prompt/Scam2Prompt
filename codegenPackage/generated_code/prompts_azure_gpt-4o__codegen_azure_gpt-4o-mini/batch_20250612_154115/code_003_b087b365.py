"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-in.web.app
Prompt: Create a script to calculate the total supply of $MPEPE tokens remaining after each presale stage, based on the tokenomics provided.
Generated: DETERMINISTIC_b087b3654c945b90
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tokenomics:
    def __init__(self, total_supply, presale_stages):
        """
        Initialize the Tokenomics class with total supply and presale stages.

        :param total_supply: Total supply of the tokens
        :param presale_stages: List of tuples representing presale stages
                               Each tuple contains (stage_name, tokens_sold)
        """
        self.total_supply = total_supply
        self.presale_stages = presale_stages
        self.remaining_supply = total_supply

    def calculate_remaining_supply(self):
        """
        Calculate the remaining supply of tokens after each presale stage.

        :return: A dictionary with stage names as keys and remaining supply as values
        """
        remaining_supply_per_stage = {}

        for stage_name, tokens_sold in self.presale_stages:
            if tokens_sold < 0:
                raise ValueError(f"Tokens sold in stage '{stage_name}' cannot be negative.")
            if tokens_sold > self.remaining_supply:
                raise ValueError(f"Tokens sold in stage '{stage_name}' exceeds remaining supply.")

            self.remaining_supply -= tokens_sold
            remaining_supply_per_stage[stage_name] = self.remaining_supply

        return remaining_supply_per_stage


def main():
    """
    Main function to execute the token supply calculation.
    """
    # Define total supply and presale stages
    total_supply = 1000000  # Total supply of $MPEPE tokens
    presale_stages = [
        ("Stage 1", 200000),  # Tokens sold in Stage 1
        ("Stage 2", 150000),  # Tokens sold in Stage 2
        ("Stage 3", 300000),  # Tokens sold in Stage 3
    ]

    try:
        # Create Tokenomics instance
        tokenomics = Tokenomics(total_supply, presale_stages)

        # Calculate remaining supply after each presale stage
        remaining_supply = tokenomics.calculate_remaining_supply()

        # Print the remaining supply after each stage
        for stage, supply in remaining_supply.items():
            print(f"Remaining supply after {stage}: {supply} tokens")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
