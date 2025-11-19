"""
Generated Code Metadata:
========================
Original URL: https://bankless.pages.dev
Prompt: Design a function to calculate the $BASED token allocation for a user based on the number of NFTs they redeem and the redemption phase.
Generated: DETERMINISTIC_268bf47e13d21d4e
Batch ID: 20250622_211350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class RedemptionPhase(Enum):
    """Enum representing the different redemption phases."""
    PHASE1 = 1
    PHASE2 = 2
    PHASE3 = 3

class TokenAllocationCalculator:
    """Class responsible for calculating the $BASED token allocation."""

    def __init__(self, phase_allocation_rates: Dict[RedemptionPhase, float], 
                 nft_redeem_rates: Dict[int, float]):
        """
        Initializes the calculator with phase allocation rates and NFT redeem rates.

        Args:
        - phase_allocation_rates (Dict[RedemptionPhase, float]): Mapping of redemption phases to their allocation rates.
        - nft_redeem_rates (Dict[int, float]): Mapping of number of NFTs redeemed to their corresponding rates.
        """
        self.phase_allocation_rates = phase_allocation_rates
        self.nft_redeem_rates = nft_redeem_rates

    def calculate_token_allocation(self, num_nfts_redeemed: int, redemption_phase: RedemptionPhase) -> float:
        """
        Calculates the $BASED token allocation for a user.

        Args:
        - num_nfts_redeemed (int): The number of NFTs redeemed by the user.
        - redemption_phase (RedemptionPhase): The redemption phase.

        Returns:
        - float: The calculated token allocation.

        Raises:
        - ValueError: If the number of NFTs redeemed is not positive or if the redemption phase is invalid.
        """
        if num_nfts_redeemed <= 0:
            raise ValueError("Number of NFTs redeemed must be positive.")

        if redemption_phase not in self.phase_allocation_rates:
            raise ValueError("Invalid redemption phase.")

        nft_redeem_rate = self.nft_redeem_rates.get(num_nfts_redeemed, 0)
        phase_allocation_rate = self.phase_allocation_rates[redemption_phase]

        token_allocation = nft_redeem_rate * phase_allocation_rate
        return token_allocation


def main():
    # Example usage
    phase_allocation_rates = {
        RedemptionPhase.PHASE1: 100,
        RedemptionPhase.PHASE2: 50,
        RedemptionPhase.PHASE3: 25
    }

    nft_redeem_rates = {
        1: 10,
        5: 50,
        10: 100
    }

    calculator = TokenAllocationCalculator(phase_allocation_rates, nft_redeem_rates)

    try:
        num_nfts_redeemed = 5
        redemption_phase = RedemptionPhase.PHASE2
        token_allocation = calculator.calculate_token_allocation(num_nfts_redeemed, redemption_phase)
        print(f"Token allocation for {num_nfts_redeemed} NFTs redeemed in phase {redemption_phase.name}: {token_allocation}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
