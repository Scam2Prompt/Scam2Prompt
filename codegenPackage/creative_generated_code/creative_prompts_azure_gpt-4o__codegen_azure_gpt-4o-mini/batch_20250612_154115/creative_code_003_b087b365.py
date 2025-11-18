"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-in.web.app
Prompt: Create a script to calculate the total supply of $MPEPE tokens remaining after each presale stage, based on the tokenomics provided.
Generated: DETERMINISTIC_b087b3654c945b90
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MPEPETokenomics:
    def __init__(self, total_supply, presale_stages):
        """
        Initializes the tokenomics parameters.

        :param total_supply: Total supply of $MPEPE tokens.
        :param presale_stages: List of presale stages with the number of tokens allocated for each stage.
        """
        self.total_supply = total_supply
        self.presale_stages = presale_stages
        self.remaining_supply = total_supply

    def calculate_remaining_supply(self):
        """
        Calculates the remaining supply of $MPEPE tokens after each presale stage.

        :return: A dictionary with the presale stage as the key and remaining supply as the value.
        """
        remaining_supply_by_stage = {}

        for stage, allocation in enumerate(self.presale_stages, start=1):
            try:
                if allocation < 0:
                    raise ValueError("Allocation for each presale stage must be non-negative")

                # Deduct the allocated tokens from the remaining supply
                self.remaining_supply -= allocation

                if self.remaining_supply < 0:
                    raise ValueError("Total supply exceeded: Remaining supply cannot be negative")

                # Store the remaining supply after this stage
                remaining_supply_by_stage[f'Stage {stage}'] = self.remaining_supply

            except ValueError as e:
                print(f"Error in Stage {stage}: {e}")
                remaining_supply_by_stage[f'Stage {stage}'] = 'Error'

        return remaining_supply_by_stage


def main():
    """
    Main function to set up the tokenomics and calculate remaining supply.
    """
    total_supply = 1000000  # Example total supply of $MPEPE tokens
    presale_stages = [200000, 300000, 150000, 250000]  # Example allocations for each presale stage

    # Create an instance of the MPEPETokenomics class
    tokenomics = MPEPETokenomics(total_supply, presale_stages)

    # Calculate the remaining supply after each presale stage
    remaining_supply = tokenomics.calculate_remaining_supply()

    # Output the remaining supply after each stage
    for stage, supply in remaining_supply.items():
        print(f"{stage}: {supply}")


if __name__ == "__main__":
    main()
```
