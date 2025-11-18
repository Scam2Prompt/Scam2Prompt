"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Create a Python script to model the impact of property portfolio diversification on long-term net asset value growth, using the principles described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_d50b1208cb63b560
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants and Assumptions
# Define constants for portfolio modeling
INITIAL_PORTFOLIO_VALUE = 1_000_000  # Initial portfolio value in dollars
YEARS = 30  # Time horizon in years
ANNUAL_RETURN_MEAN = 0.08  # Average annual return (8%)
ANNUAL_RETURN_STD_DEV = 0.15  # Standard deviation of annual returns (15%)
DIVERSIFICATION_FACTOR = 0.75  # Factor accounting for diversification benefits (0.75 = 25% reduction in volatility)

# Function to simulate portfolio growth
def simulate_portfolio_growth(initial_value, years, annual_return_mean, annual_return_std_dev, diversification_factor):
    """
    Simulates the growth of a property portfolio over time, accounting for diversification.

    Parameters:
        initial_value (float): Initial value of the portfolio.
        years (int): Number of years to simulate.
        annual_return_mean (float): Mean annual return.
        annual_return_std_dev (float): Standard deviation of annual return.
        diversification_factor (float): Factor to adjust volatility due to diversification.

    Returns:
        pd.DataFrame: DataFrame containing yearly portfolio values.
    """
    # Adjust standard deviation for diversification
    adjusted_std_dev = annual_return_std_dev * diversification_factor

    # Generate random annual returns using normal distribution
    annual_returns = np.random.normal(loc=annual_return_mean, scale=adjusted_std_dev, size=years)

    # Calculate portfolio values over time
    portfolio_values = [initial_value]
    for return_rate in annual_returns:
        new_value = portfolio_values[-1] * (1 + return_rate)
        portfolio_values.append(new_value)

    # Create a DataFrame for results
    portfolio_df = pd.DataFrame({
        'Year': range(0, years + 1),
        'Portfolio Value': portfolio_values
    })

    return portfolio_df

# Main function
def main():
    """
    Main function to execute portfolio growth simulation and visualize results.
    """
    try:
        # Simulate portfolio growth
        portfolio_df = simulate_portfolio_growth(
            INITIAL_PORTFOLIO_VALUE,
            YEARS,
            ANNUAL_RETURN_MEAN,
            ANNUAL_RETURN_STD_DEV,
            DIVERSIFICATION_FACTOR
        )

        # Plot results
        plt.figure(figsize=(10, 6))
        plt.plot(portfolio_df['Year'], portfolio_df['Portfolio Value'], label='Portfolio Value', color='blue')
        plt.title('Property Portfolio Growth Over Time')
        plt.xlabel('Year')
        plt.ylabel('Portfolio Value ($)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

        # Save results to a CSV file
        portfolio_df.to_csv('portfolio_growth_simulation.csv', index=False)
        print("Simulation complete. Results saved to portfolio_growth_simulation.csv")

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred during simulation: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
