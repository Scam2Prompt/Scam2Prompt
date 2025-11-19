"""
Generated Code Metadata:
========================
Original URL: https://nansenportfolio.app
Prompt: Write a Python script to calculate the potential returns on investment for a private equity investment, considering factors such as risk aversion and timing, as described by Grade World Investment Limited.
Generated: DETERMINISTIC_32a48b0dbb6bc4e0
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Optional, Dict, Union

class PrivateEquityInvestmentCalculator:
    """
    A class to calculate potential returns on private equity investments considering risk aversion and timing.
    
    Attributes:
        initial_investment (float): The initial amount invested.
        risk_aversion_factor (float): A factor representing the investor's risk aversion (0 to 1).
        investment_horizon (int): The investment period in years.
        expected_return_rate (float): The expected annual return rate (e.g., 0.1 for 10%).
        volatility (float): The volatility of returns (standard deviation).
    """
    
    def __init__(
        self,
        initial_investment: float,
        risk_aversion_factor: float,
        investment_horizon: int,
        expected_return_rate: float,
        volatility: float
    ):
        """
        Initialize the calculator with investment parameters.
        
        Args:
            initial_investment: The initial amount invested.
            risk_aversion_factor: A factor representing the investor's risk aversion (0 to 1).
            investment_horizon: The investment period in years.
            expected_return_rate: The expected annual return rate (e.g., 0.1 for 10%).
            volatility: The volatility of returns (standard deviation).
            
        Raises:
            ValueError: If any of the parameters are invalid.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be positive.")
        if not 0 <= risk_aversion_factor <= 1:
            raise ValueError("Risk aversion factor must be between 0 and 1.")
        if investment_horizon <= 0:
            raise ValueError("Investment horizon must be positive.")
        if volatility < 0:
            raise ValueError("Volatility cannot be negative.")
            
        self.initial_investment = initial_investment
        self.risk_aversion_factor = risk_aversion_factor
        self.investment_horizon = investment_horizon
        self.expected_return_rate = expected_return_rate
        self.volatility = volatility
    
    def calculate_expected_value(self) -> float:
        """
        Calculate the expected value of the investment considering risk aversion.
        
        Returns:
            The expected value of the investment after the investment horizon.
        """
        adjusted_return = self.expected_return_rate * (1 - self.risk_aversion_factor)
        expected_value = self.initial_investment * (1 + adjusted_return) ** self.investment_horizon
        return expected_value
    
    def monte_carlo_simulation(self, num_simulations: int = 10000) -> Dict[str, Union[float, np.ndarray]]:
        """
        Perform a Monte Carlo simulation to estimate potential returns.
        
        Args:
            num_simulations: Number of simulations to run (default: 10000).
            
        Returns:
            A dictionary containing:
                - 'mean': The mean expected value.
                - 'median': The median expected value.
                - 'percentiles': The 5th, 25th, 75th, and 95th percentiles.
                - 'simulations': Array of all simulated values.
        """
        np.random.seed(42)  # For reproducibility
        returns = np.random.normal(
            loc=self.expected_return_rate * (1 - self.risk_aversion_factor),
            scale=self.volatility,
            size=(num_simulations, self.investment_horizon)
        )
        simulated_values = self.initial_investment * np.prod(1 + returns, axis=1)
        
        return {
            'mean': np.mean(simulated_values),
            'median': np.median(simulated_values),
            'percentiles': {
                '5th': np.percentile(simulated_values, 5),
                '25th': np.percentile(simulated_values, 25),
                '75th': np.percentile(simulated_values, 75),
                '95th': np.percentile(simulated_values, 95)
            },
            'simulations': simulated_values
        }
    
    def generate_report(self, num_simulations: int = 10000) -> pd.DataFrame:
        """
        Generate a comprehensive report of the investment analysis.
        
        Args:
            num_simulations: Number of simulations to run (default: 10000).
            
        Returns:
            A pandas DataFrame containing the report.
        """
        expected_value = self.calculate_expected_value()
        simulation_results = self.monte_carlo_simulation(num_simulations)
        
        report_data = {
            'Initial Investment': [self.initial_investment],
            'Risk Aversion Factor': [self.risk_aversion_factor],
            'Investment Horizon (years)': [self.investment_horizon],
            'Expected Return Rate': [self.expected_return_rate],
            'Volatility': [self.volatility],
            'Expected Value': [expected_value],
            'Mean Simulated Value': [simulation_results['mean']],
            'Median Simulated Value': [simulation_results['median']],
            '5th Percentile': [simulation_results['percentiles']['5th']],
            '25th Percentile': [simulation_results['percentiles']['25th']],
            '75th Percentile': [simulation_results['percentiles']['75th']],
            '95th Percentile': [simulation_results['percentiles']['95th']]
        }
        
        return pd.DataFrame(report_data)

# Example usage
if __name__ == "__main__":
    try:
        calculator = PrivateEquityInvestmentCalculator(
            initial_investment=100000,
            risk_aversion_factor=0.3,
            investment_horizon=5,
            expected_return_rate=0.12,
            volatility=0.15
        )
        
        report = calculator.generate_report()
        print(report)
        
    except ValueError as e:
        print(f"Error: {e}")
```
