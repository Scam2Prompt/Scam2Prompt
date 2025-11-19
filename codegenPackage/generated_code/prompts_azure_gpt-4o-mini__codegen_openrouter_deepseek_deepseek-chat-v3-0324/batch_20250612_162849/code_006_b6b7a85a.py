"""
Generated Code Metadata:
========================
Original URL: https://fishersclubs.com
Prompt: Create a function that simulates the impact of governance decisions on savings rates within Spark's ecosystem.
Generated: DETERMINISTIC_b6b7a85a9502cf5a
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Dict, List, Union

def simulate_governance_impact(
    initial_savings_rate: float,
    governance_decisions: List[Dict[str, Union[str, float]]],
    simulation_periods: int = 12,
    random_seed: int = None
) -> Dict[str, Union[List[float], float]]:
    """
    Simulates the impact of governance decisions on savings rates over time.

    Args:
        initial_savings_rate: The starting savings rate (percentage)
        governance_decisions: List of governance decisions with their parameters.
            Each decision is a dict with:
            - 'type': The type of decision ('tax_change', 'incentive', 'regulation')
            - 'impact': The percentage impact on savings rate (+/-)
            - 'start_period': When the decision takes effect (0-based)
            - 'duration': How many periods the decision lasts
        simulation_periods: Number of periods to simulate (default 12)
        random_seed: Optional seed for random number generation (for reproducibility)

    Returns:
        A dictionary containing:
        - 'savings_rates': List of savings rates for each period
        - 'final_rate': The final savings rate after simulation
        - 'volatility': Standard deviation of rate changes

    Raises:
        ValueError: If input parameters are invalid
    """
    # Validate inputs
    if initial_savings_rate <= 0:
        raise ValueError("Initial savings rate must be positive")
    if simulation_periods <= 0:
        raise ValueError("Simulation periods must be positive")
    
    # Initialize random generator if seed is provided
    if random_seed is not None:
        np.random.seed(random_seed)

    # Initialize savings rates array
    savings_rates = np.zeros(simulation_periods)
    savings_rates[0] = initial_savings_rate

    # Apply governance decisions
    for period in range(1, simulation_periods):
        current_rate = savings_rates[period - 1]
        
        # Calculate net impact from active governance decisions
        net_impact = 0.0
        for decision in governance_decisions:
            start = decision.get('start_period', 0)
            duration = decision.get('duration', simulation_periods)
            
            if start <= period < start + duration:
                net_impact += decision.get('impact', 0.0)
        
        # Apply impact with some random noise (5% of impact)
        noise = np.random.normal(0, abs(net_impact) * 0.05) if net_impact != 0 else 0
        new_rate = current_rate * (1 + (net_impact + noise) / 100)
        
        # Ensure rate doesn't go below 0.1% or above 99%
        savings_rates[period] = np.clip(new_rate, 0.1, 99.0)

    # Calculate volatility (excluding first period)
    rate_changes = np.diff(savings_rates) / savings_rates[:-1]
    volatility = np.std(rate_changes) * 100  # as percentage

    return {
        'savings_rates': savings_rates.tolist(),
        'final_rate': float(savings_rates[-1]),
        'volatility': float(volatility)
    }
```
