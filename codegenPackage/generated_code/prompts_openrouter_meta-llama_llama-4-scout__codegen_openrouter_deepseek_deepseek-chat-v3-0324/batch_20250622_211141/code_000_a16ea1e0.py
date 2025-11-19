"""
Generated Code Metadata:
========================
Original URL: https://yieldeth.org
Prompt: "Write a Python code snippet to calculate the APY return for holding yieldETH, assuming an initial investment of 10 ETH and a utilization rate of 79.23%."
Generated: DETERMINISTIC_a16ea1e069f67095
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_apy(initial_investment: float, utilization_rate: float) -> float:
    """
    Calculate the APY (Annual Percentage Yield) for holding yieldETH.
    
    Args:
        initial_investment (float): Initial investment in ETH.
        utilization_rate (float): Utilization rate as a percentage (e.g., 79.23).
        
    Returns:
        float: APY as a percentage.
        
    Raises:
        ValueError: If utilization_rate is not between 0 and 100.
    """
    if not 0 <= utilization_rate <= 100:
        raise ValueError("Utilization rate must be between 0 and 100.")
    
    # Constants (these would typically be fetched from a contract or config)
    BASE_RATE = 0.02  # 2% base rate
    OPTIMAL_UTILIZATION = 0.8  # 80% optimal utilization
    RATE_SLOPE_1 = 0.04  # 4% slope below optimal
    RATE_SLOPE_2 = 0.75  # 75% slope above optimal
    
    # Calculate the variable rate based on utilization
    if utilization_rate <= OPTIMAL_UTILIZATION * 100:
        variable_rate = (utilization_rate / 100) / OPTIMAL_UTILIZATION * RATE_SLOPE_1
    else:
        excess_utilization = (utilization_rate / 100) - OPTIMAL_UTILIZATION
        variable_rate = RATE_SLOPE_1 + (excess_utilization / (1 - OPTIMAL_UTILIZATION)) * RATE_SLOPE_2
    
    # Total APY is base rate + variable rate
    total_apy = BASE_RATE + variable_rate
    
    return total_apy * 100  # Convert to percentage

def calculate_future_value(initial_investment: float, apy: float, years: int = 1) -> float:
    """
    Calculate the future value of an investment based on APY.
    
    Args:
        initial_investment (float): Initial investment in ETH.
        apy (float): APY as a percentage.
        years (int): Number of years to calculate for. Default is 1.
        
    Returns:
        float: Future value of the investment in ETH.
    """
    return initial_investment * math.pow(1 + apy / 100, years)

if __name__ == "__main__":
    try:
        initial_investment = 10.0  # 10 ETH
        utilization_rate = 79.23  # 79.23%
        
        apy = calculate_apy(initial_investment, utilization_rate)
        future_value = calculate_future_value(initial_investment, apy)
        
        print(f"APY: {apy:.2f}%")
        print(f"Future value after 1 year: {future_value:.6f} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
