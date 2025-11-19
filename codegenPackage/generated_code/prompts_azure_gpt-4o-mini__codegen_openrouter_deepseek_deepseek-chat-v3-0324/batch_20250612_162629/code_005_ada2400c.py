"""
Generated Code Metadata:
========================
Original URL: https://battle-barkers.com
Prompt: Write a code example that simulates the impact of inflation on investment returns over a 10-year period.
Generated: DETERMINISTIC_ada2400c6dc03cf8
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt

def calculate_inflation_adjusted_returns(
    initial_investment: float,
    annual_return_rate: float,
    inflation_rate: float,
    years: int = 10
) -> tuple[list[float], list[float], list[float]]:
    """
    Calculate nominal returns, inflation-adjusted returns, and inflation impact over time.
    
    Args:
        initial_investment: Initial investment amount
        annual_return_rate: Expected annual return rate (as decimal, e.g., 0.07 for 7%)
        inflation_rate: Expected annual inflation rate (as decimal)
        years: Number of years to project (default 10)
    
    Returns:
        Tuple containing three lists:
        - nominal_values: Investment values without inflation adjustment
        - real_values: Inflation-adjusted investment values
        - inflation_impact: Cumulative inflation impact for each year
    """
    nominal_values = [initial_investment]
    real_values = [initial_investment]
    inflation_impact = [1.0]  # Multiplier for year 0
    
    for year in range(1, years + 1):
        # Calculate nominal growth
        nominal_value = nominal_values[-1] * (1 + annual_return_rate)
        nominal_values.append(nominal_value)
        
        # Calculate inflation impact
        inflation_multiplier = inflation_impact[-1] / (1 + inflation_rate)
        inflation_impact.append(inflation_multiplier)
        
        # Calculate real (inflation-adjusted) value
        real_value = nominal_value * inflation_multiplier
        real_values.append(real_value)
    
    return nominal_values, real_values, inflation_impact

def plot_inflation_impact(
    nominal_values: list[float],
    real_values: list[float],
    inflation_impact: list[float]
) -> None:
    """Plot the comparison between nominal and real returns with inflation impact."""
    years = list(range(len(nominal_values)))
    
    plt.figure(figsize=(12, 6))
    
    # Plot nominal vs real values
    plt.subplot(1, 2, 1)
    plt.plot(years, nominal_values, label='Nominal Value', marker='o')
    plt.plot(years, real_values, label='Real Value (Inflation-adjusted)', marker='x')
    plt.title('Nominal vs Real Investment Value')
    plt.xlabel('Years')
    plt.ylabel('Value ($)')
    plt.grid(True)
    plt.legend()
    
    # Plot inflation impact
    plt.subplot(1, 2, 2)
    plt.plot(years, [1/m for m in inflation_impact], label='Inflation Impact', color='red', marker='s')
    plt.title('Cumulative Inflation Impact')
    plt.xlabel('Years')
    plt.ylabel('Purchasing Power (1 = original)')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def main():
    try:
        # Get user input with validation
        initial_investment = float(input("Enter initial investment amount: $"))
        annual_return_rate = float(input("Enter expected annual return rate (e.g., 7 for 7%): ")) / 100
        inflation_rate = float(input("Enter expected annual inflation rate (e.g., 3 for 3%): ")) / 100
        
        if initial_investment <= 0:
            raise ValueError("Investment amount must be positive")
        if annual_return_rate < 0:
            raise ValueError("Return rate cannot be negative")
        if inflation_rate < 0:
            raise ValueError("Inflation rate cannot be negative")
        
        # Calculate and display results
        nominal, real, inflation = calculate_inflation_adjusted_returns(
            initial_investment, annual_return_rate, inflation_rate
        )
        
        print("\nYear | Nominal Value | Real Value | Purchasing Power")
        print("--------------------------------------------------")
        for year in range(len(nominal)):
            print(f"{year:4} | ${nominal[year]:>12,.2f} | ${real[year]:>10,.2f} | {1/inflation[year]:>15.2f}x")
        
        # Plot results
        plot_inflation_impact(nominal, real, inflation)
        
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
