"""
Generated Code Metadata:
========================
Original URL: https://sharp-2vj.pages.dev
Prompt: Generate code to calculate Sharpe Points earned by interacting with Sharpe AI products, such as trading perpetual swaps or bridging funds.
Generated: DETERMINISTIC_a16d683450e7d352
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sharpe_points_calculator.py

from typing import Dict
from enum import Enum
from dataclasses import dataclass

class InteractionType(str, Enum):
    """Type of interaction with Sharpe AI products."""
    TRADE_PERPETUAL_SWAP = "trade_perpetual_swap"
    BRIDGE_FUNDS = "bridge_funds"

@dataclass
class Interaction:
    """Represents an interaction with Sharpe AI products."""
    interaction_type: InteractionType
    amount: float  # in USD
    leverage: float  # for trade_perpetual_swap

class SharpePointsCalculator:
    """Calculates Sharpe Points earned by interacting with Sharpe AI products."""

    def __init__(self, config: Dict[str, float]):
        """
        Initializes the calculator with configuration.

        Args:
        - config: A dictionary containing configuration parameters.
            - trade_perpetual_swap_multiplier: Multiplier for trading perpetual swaps.
            - bridge_funds_multiplier: Multiplier for bridging funds.
        """
        self.config = config

    def calculate_sharpe_points(self, interaction: Interaction) -> float:
        """
        Calculates Sharpe Points earned for a given interaction.

        Args:
        - interaction: The interaction to calculate Sharpe Points for.

        Returns:
        - The Sharpe Points earned.

        Raises:
        - ValueError: If interaction type is not supported.
        """
        if interaction.interaction_type == InteractionType.TRADE_PERPETUAL_SWAP:
            return self._calculate_trade_perpetual_swap_sharpe_points(interaction)
        elif interaction.interaction_type == InteractionType.BRIDGE_FUNDS:
            return self._calculate_bridge_funds_sharpe_points(interaction)
        else:
            raise ValueError("Unsupported interaction type")

    def _calculate_trade_perpetual_swap_sharpe_points(self, interaction: Interaction) -> float:
        """
        Calculates Sharpe Points earned for trading perpetual swaps.

        Args:
        - interaction: The interaction to calculate Sharpe Points for.

        Returns:
        - The Sharpe Points earned.
        """
        multiplier = self.config.get("trade_perpetual_swap_multiplier", 0.1)
        sharpe_points = interaction.amount * interaction.leverage * multiplier
        return sharpe_points

    def _calculate_bridge_funds_sharpe_points(self, interaction: Interaction) -> float:
        """
        Calculates Sharpe Points earned for bridging funds.

        Args:
        - interaction: The interaction to calculate Sharpe Points for.

        Returns:
        - The Sharpe Points earned.
        """
        multiplier = self.config.get("bridge_funds_multiplier", 0.05)
        sharpe_points = interaction.amount * multiplier
        return sharpe_points

def main():
    config = {
        "trade_perpetual_swap_multiplier": 0.1,
        "bridge_funds_multiplier": 0.05
    }
    calculator = SharpePointsCalculator(config)

    # Example usage:
    interaction1 = Interaction(InteractionType.TRADE_PERPETUAL_SWAP, 1000, 5)
    interaction2 = Interaction(InteractionType.BRIDGE_FUNDS, 500, 1)

    try:
        sharpe_points1 = calculator.calculate_sharpe_points(interaction1)
        sharpe_points2 = calculator.calculate_sharpe_points(interaction2)

        print(f"Sharpe Points for trading perpetual swaps: {sharpe_points1}")
        print(f"Sharpe Points for bridging funds: {sharpe_points2}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
