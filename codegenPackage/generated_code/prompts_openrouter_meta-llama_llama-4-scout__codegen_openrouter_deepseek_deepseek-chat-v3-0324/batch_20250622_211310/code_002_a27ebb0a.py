"""
Generated Code Metadata:
========================
Original URL: https://immediategenesis.co
Prompt: Generate a list of 5 key topics in investment education that a beginner should learn, based on the content provided by Beraventex, and write a short Python script to simulate a simple investment strategy for one of these topics.
Generated: DETERMINISTIC_a27ebb0ae8105550
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Investment Education Topics for Beginners (Based on Beraventex Content):
1. Understanding Risk and Return
2. Diversification Strategies
3. Compound Interest and Time Value of Money
4. Asset Allocation Basics
5. Fundamental vs. Technical Analysis

This script demonstrates a simple dollar-cost averaging (DCA) investment strategy,
which is a key concept under Diversification Strategies.
"""

import random
from typing import List, Tuple

def simulate_dca_investment(
    initial_investment: float,
    monthly_contribution: float,
    months: int,
    mean_return: float,
    volatility: float
) -> Tuple[List[float], List[float]]:
    """
    Simulate a dollar-cost averaging investment strategy with random market fluctuations.
    
    Args:
        initial_investment: Starting investment amount
        monthly_contribution: Fixed amount added each month
        months: Duration of investment in months
        mean_return: Average monthly return (decimal)
        volatility: Standard deviation of returns (decimal)
    
    Returns:
        Tuple containing:
        - List of portfolio values each month
        - List of monthly returns
    """
    if not all(isinstance(x, (int, float)) for x in [initial_investment, monthly_contribution, months, mean_return, volatility]):
        raise ValueError("All numeric parameters must be numbers")
    if months <= 0:
        raise ValueError("Investment period must be positive")
    
    portfolio_value = [initial_investment]
    monthly_returns = []
    
    for _ in range(months - 1):
        # Generate random monthly return with normal distribution
        monthly_return = random.gauss(mean_return, volatility)
        monthly_returns.append(monthly_return)
        
        # Calculate new portfolio value
        new_value = portfolio_value[-1] * (1 + monthly_return) + monthly_contribution
        portfolio_value.append(new_value)
    
    return portfolio_value, monthly_returns

def print_simulation_results(portfolio_values: List[float], monthly_returns: List[float]) -> None:
    """Print formatted simulation results."""
    print("\nDollar-Cost Averaging Simulation Results")
    print("=" * 40)
    print(f"{'Month':<10}{'Portfolio Value':<20}{'Monthly Return':<15}")
    print("-" * 40)
    
    for i, (value, ret) in enumerate(zip(portfolio_values, [0.0] + monthly_returns)):
        print(f"{i + 1:<10}${value:,.2f}{'':<10}{ret * 100:.2f}%")

if __name__ == "__main__":
    try:
        # Simulation parameters
        INITIAL_INVESTMENT = 1000.00  # $1,000 starting capital
        MONTHLY_CONTRIBUTION = 100.00  # $100 monthly contribution
        DURATION_MONTHS = 12           # 1 year simulation
        AVG_MONTHLY_RETURN = 0.005     # 0.5% average monthly return
        VOLATILITY = 0.02              # 2% standard deviation
        
        # Run simulation
        portfolio_values, monthly_returns = simulate_dca_investment(
            INITIAL_INVESTMENT,
            MONTHLY_CONTRIBUTION,
            DURATION_MONTHS,
            AVG_MONTHLY_RETURN,
            VOLATILITY
        )
        
        # Display results
        print_simulation_results(portfolio_values, monthly_returns)
        
        # Print summary
        total_contributions = INITIAL_INVESTMENT + (MONTHLY_CONTRIBUTION * (DURATION_MONTHS - 1))
        final_value = portfolio_values[-1]
        total_return = (final_value - total_contributions) / total_contributions * 100
        print("\nSummary:")
        print(f"Total Contributions: ${total_contributions:,.2f}")
        print(f"Final Portfolio Value: ${final_value:,.2f}")
        print(f"Total Return: {total_return:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
