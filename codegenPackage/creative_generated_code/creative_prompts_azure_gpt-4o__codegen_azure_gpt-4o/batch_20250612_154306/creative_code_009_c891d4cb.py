"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Create a script to analyze and visualize the impact of different risk levels on savings returns, as described in the "Sur-Mesure" formula on pipelinefinanceconseil.com. Include graphs to illustrate high-risk versus low-risk scenarios.
Generated: DETERMINISTIC_c891d4cbff7cb179
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants for risk level impact on savings returns
LOW_RISK_RETURN_RATE = 0.03  # Average annual return for low-risk investments (e.g., bonds)
HIGH_RISK_RETURN_RATE = 0.08  # Average annual return for high-risk investments (e.g., stocks)
RISK_VOLATILITY = 0.15  # Standard deviation for high-risk investments
YEARS_TO_PROJECT = 30  # Number of years to project savings
INITIAL_SAVINGS = 10000  # Initial savings amount
ANNUAL_CONTRIBUTION = 6000  # Annual contribution to savings

def simulate_savings_growth(initial_savings, annual_contribution, years, return_rate, volatility=0):
    """
    Simulates the growth of savings over time based on return rate and volatility.

    Parameters:
        initial_savings (float): Initial amount of savings.
        annual_contribution (float): Annual contribution to savings.
        years (int): Number of years to simulate.
        return_rate (float): Average annual return rate.
        volatility (float): Standard deviation for return rate (default: 0 for no volatility).

    Returns:
        np.ndarray: Array of savings amounts over the years.
    """
    savings = [initial_savings]
    for year in range(1, years + 1):
        # Calculate the return for the current year, including random volatility if applicable
        yearly_return = np.random.normal(return_rate, volatility) if volatility > 0 else return_rate
        new_balance = savings[-1] * (1 + yearly_return) + annual_contribution
        savings.append(new_balance)
    return np.array(savings)

def visualize_savings_growth(low_risk_savings, high_risk_savings, years):
    """
    Visualizes the growth of savings for low-risk and high-risk scenarios over time.

    Parameters:
        low_risk_savings (np.ndarray): Savings growth for low-risk investments.
        high_risk_savings (np.ndarray): Savings growth for high-risk investments.
        years (int): Number of years simulated.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(years + 1), low_risk_savings, label="Low Risk (3% annual return)", color="blue")
    plt.plot(np.arange(years + 1), high_risk_savings, label="High Risk (8% annual return, 15% volatility)", color="red")
    
    plt.title("Impact of Risk Levels on Savings Growth")
    plt.xlabel("Year")
    plt.ylabel("Savings ($)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to simulate and visualize savings growth under different risk scenarios.
    """
    try:
        # Simulate savings growth for low-risk and high-risk scenarios
        low_risk_savings = simulate_savings_growth(
            INITIAL_SAVINGS, ANNUAL_CONTRIBUTION, YEARS_TO_PROJECT, LOW_RISK_RETURN_RATE
        )
        high_risk_savings = simulate_savings_growth(
            INITIAL_SAVINGS, ANNUAL_CONTRIBUTION, YEARS_TO_PROJECT, HIGH_RISK_RETURN_RATE, RISK_VOLATILITY
        )

        # Visualize the savings growth results
        visualize_savings_growth(low_risk_savings, high_risk_savings, YEARS_TO_PROJECT)

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred during simulation: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
