"""
Generated Code Metadata:
========================
Original URL: https://saga-whitelisting.pages.dev
Prompt: Based on the Saga Protocol's litepaper, write a function to calculate token incentives for developers creating chains in the multiverse. Include relevant parameters from the token mechanism.
Generated: DETERMINISTIC_fbd6003235c894fa
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_developer_incentives(
    base_incentive: float,
    chain_complexity: float,
    adoption_factor: float,
    uptime_percentage: float,
    validator_penalty_factor: float = 0.9,
    max_incentive: float = 1000000.0
) -> float:
    """
    Calculate token incentives for developers creating chains in the Saga multiverse.
    
    Args:
        base_incentive: Base incentive amount in tokens
        chain_complexity: Complexity factor of the chain (1.0-5.0 scale)
        adoption_factor: Factor based on chain adoption (0.0-1.0)
        uptime_percentage: Percentage of time chain is operational (0.0-1.0)
        validator_penalty_factor: Penalty factor for validator issues (default 0.9)
        max_incentive: Maximum allowable incentive (default 1,000,000)
        
    Returns:
        float: Calculated incentive amount in tokens
        
    Raises:
        ValueError: If any parameter is outside valid range
    """
    # Validate input parameters
    if not (0 <= base_incentive <= max_incentive):
        raise ValueError(f"Base incentive must be between 0 and {max_incentive}")
    if not (1.0 <= chain_complexity <= 5.0):
        raise ValueError("Chain complexity must be between 1.0 and 5.0")
    if not (0.0 <= adoption_factor <= 1.0):
        raise ValueError("Adoption factor must be between 0.0 and 1.0")
    if not (0.0 <= uptime_percentage <= 1.0):
        raise ValueError("Uptime percentage must be between 0.0 and 1.0")
    if not (0.0 < validator_penalty_factor <= 1.0):
        raise ValueError("Validator penalty factor must be between 0.0 and 1.0")
    
    # Calculate incentive components
    complexity_bonus = 1 + (chain_complexity - 1) * 0.2
    adoption_bonus = 1 + (adoption_factor * 0.5)
    uptime_bonus = uptime_percentage ** 0.7  # Diminishing returns on perfect uptime
    
    # Calculate final incentive with validator penalty
    calculated_incentive = (
        base_incentive * 
        complexity_bonus * 
        adoption_bonus * 
        uptime_bonus * 
        validator_penalty_factor
    )
    
    # Cap the incentive at maximum allowed
    return min(calculated_incentive, max_incentive)
```
