"""
Generated Code Metadata:
========================
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Develop a script that simulates different investment scenarios in BASE and calculates the total JESSE tokens for each scenario based on the presale cap.
Generated: DETERMINISTIC_812f9a196d6926c8
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict

def calculate_jesse_tokens(
    base_invested: float,
    presale_cap: float,
    total_jesse_supply: float = 1_000_000_000  # Default total JESSE supply
) -> float:
    """
    Calculate the JESSE tokens allocated based on BASE invested and presale cap.
    
    Args:
        base_invested (float): Amount of BASE invested
        presale_cap (float): Total presale cap in BASE
        total_jesse_supply (float): Total JESSE token supply (default: 1B)
    
    Returns:
        float: JESSE tokens allocated
    """
    if presale_cap <= 0:
        raise ValueError("Presale cap must be greater than 0")
    if base_invested < 0:
        raise ValueError("BASE invested cannot be negative")
    
    allocation_ratio = base_invested / presale_cap
    jesse_tokens = allocation_ratio * total_jesse_supply
    return jesse_tokens

def simulate_investment_scenarios(
    investment_amounts: List[float],
    presale_caps: List[float],
    total_jesse_supply: float = 1_000_000_000
) -> List[Dict[str, float]]:
    """
    Simulate multiple investment scenarios and calculate JESSE tokens for each.
    
    Args:
        investment_amounts (List[float]): List of BASE investment amounts to simulate
        presale_caps (List[float]): List of presale caps to simulate
        total_jesse_supply (float): Total JESSE token supply (default: 1B)
    
    Returns:
        List[Dict[str, float]]: List of scenario results with BASE, cap, and JESSE
    """
    scenarios = []
    
    for base in investment_amounts:
        for cap in presale_caps:
            try:
                jesse = calculate_jesse_tokens(base, cap, total_jesse_supply)
                scenarios.append({
                    'base_invested': base,
                    'presale_cap': cap,
                    'jesse_tokens': jesse
                })
            except ValueError as e:
                print(f"Skipping invalid scenario (BASE: {base}, Cap: {cap}): {str(e)}")
    
    return scenarios

def format_scenario_results(scenarios: List[Dict[str, float]]) -> None:
    """
    Print formatted results of investment scenarios.
    
    Args:
        scenarios (List[Dict[str, float]]): List of scenario results to display
    """
    print("\nInvestment Scenario Results:")
    print("-" * 50)
    print(f"{'BASE Invested':<15} {'Presale Cap':<15} {'JESSE Tokens':<15}")
    print("-" * 50)
    
    for scenario in scenarios:
        print(
            f"{scenario['base_invested']:<15.2f} "
            f"{scenario['presale_cap']:<15.2f} "
            f"{scenario['jesse_tokens']:<15.2f}"
        )

if __name__ == "__main__":
    # Example usage
    try:
        # Define test scenarios
        test_investments = [100, 500, 1000, 5000, 10000]
        test_presale_caps = [1_000_000, 5_000_000, 10_000_000]
        
        # Run simulations
        results = simulate_investment_scenarios(test_investments, test_presale_caps)
        
        # Display results
        format_scenario_results(results)
        
    except Exception as e:
        print(f"An error occurred during simulation: {str(e)}")
```
