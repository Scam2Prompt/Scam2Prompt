"""
Generated Code Metadata:
========================
Original URL: https://gcapmarkets.com
Prompt: Create an example of a financial product that could be introduced in a trading application, reflecting the innovative approach of GCap Markets.
Generated: DETERMINISTIC_eb74b1997791fca9
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
GCap Markets Financial Product Example: Volatility-Linked Structured Note

This module implements a volatility-linked structured note product that provides
returns based on market volatility with capital protection features.
"""

import numpy as np
from datetime import datetime, timedelta
from typing import Optional, Tuple

class VolatilityLinkedNote:
    """
    A structured financial product that provides returns linked to market volatility
    with capital protection at maturity.

    Attributes:
        notional (float): Principal investment amount
        start_date (datetime): Product inception date
        maturity_date (datetime): Product maturity date
        protection_level (float): Percentage of capital protected (0-1)
        volatility_index (str): Reference volatility index (e.g., 'VIX')
        historical_volatility (Optional[np.ndarray]): Array of historical volatility values
    """

    def __init__(
        self,
        notional: float,
        start_date: datetime,
        maturity_date: datetime,
        protection_level: float = 0.85,
        volatility_index: str = 'VIX'
    ):
        """
        Initialize the volatility-linked note.

        Args:
            notional: Principal investment amount
            start_date: Product inception date
            maturity_date: Product maturity date
            protection_level: Percentage of capital protected (default: 0.85)
            volatility_index: Reference volatility index (default: 'VIX')

        Raises:
            ValueError: If protection_level is not between 0 and 1
                      or if maturity_date is before start_date
        """
        if not 0 <= protection_level <= 1:
            raise ValueError("Protection level must be between 0 and 1")
        if maturity_date <= start_date:
            raise ValueError("Maturity date must be after start date")

        self.notional = notional
        self.start_date = start_date
        self.maturity_date = maturity_date
        self.protection_level = protection_level
        self.volatility_index = volatility_index
        self.historical_volatility = None

    def load_historical_volatility(self, volatility_data: np.ndarray) -> None:
        """
        Load historical volatility data for the reference index.

        Args:
            volatility_data: Array of historical volatility values

        Raises:
            ValueError: If volatility_data is empty
        """
        if len(volatility_data) == 0:
            raise ValueError("Volatility data cannot be empty")
        self.historical_volatility = volatility_data

    def calculate_volatility_return(self) -> float:
        """
        Calculate the volatility-linked return component.

        Returns:
            float: Return percentage based on average volatility

        Raises:
            RuntimeError: If historical volatility data is not loaded
        """
        if self.historical_volatility is None:
            raise RuntimeError("Historical volatility data not loaded")

        avg_volatility = np.mean(self.historical_volatility)
        # Normalize to 20% baseline volatility
        return max(0, (avg_volatility - 20) / 100)

    def calculate_final_payout(self) -> Tuple[float, float]:
        """
        Calculate the final payout at maturity.

        Returns:
            Tuple[float, float]: (protected_amount, volatility_return_amount)

        Raises:
            RuntimeError: If historical volatility data is not loaded
        """
        volatility_return = self.calculate_volatility_return()
        protected_amount = self.notional * self.protection_level
        return_amount = self.notional * volatility_return
        total_payout = protected_amount + return_amount

        return (protected_amount, return_amount)

    def simulate_performance(
        self,
        num_simulations: int = 1000,
        volatility_mean: float = 20,
        volatility_std: float = 5
    ) -> dict:
        """
        Monte Carlo simulation of product performance.

        Args:
            num_simulations: Number of simulations to run (default: 1000)
            volatility_mean: Mean volatility for simulation (default: 20)
            volatility_std: Volatility standard deviation (default: 5)

        Returns:
            dict: Simulation results including statistics
        """
        simulated_returns = []
        for _ in range(num_simulations):
            simulated_vol = np.random.normal(volatility_mean, volatility_std)
            simulated_return = max(0, (simulated_vol - 20) / 100)
            simulated_returns.append(simulated_return)

        avg_return = np.mean(simulated_returns)
        median_return = np.median(simulated_returns)
        pct_positive = sum(1 for r in simulated_returns if r > 0) / num_simulations

        return {
            'average_return': avg_return,
            'median_return': median_return,
            'probability_positive_return': pct_positive,
            'simulated_returns': simulated_returns
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a sample product
        note = VolatilityLinkedNote(
            notional=100000,
            start_date=datetime(2023, 1, 1),
            maturity_date=datetime(2025, 1, 1),
            protection_level=0.9,
            volatility_index='VIX'
        )

        # Load sample volatility data (normally this would come from market data)
        sample_volatility = np.random.normal(20, 5, 252*2)  # 2 years of daily data
        note.load_historical_volatility(sample_volatility)

        # Calculate payout
        protected, volatility_return = note.calculate_final_payout()
        print(f"Protected amount: ${protected:,.2f}")
        print(f"Volatility return: ${volatility_return:,.2f}")

        # Run simulation
        simulation_results = note.simulate_performance()
        print(f"\nSimulation Results:")
        print(f"Average return: {simulation_results['average_return']:.2%}")
        print(f"Probability of positive return: {simulation_results['probability_positive_return']:.2%}")

    except Exception as e:
        print(f"Error processing volatility-linked note: {str(e)}")
```
