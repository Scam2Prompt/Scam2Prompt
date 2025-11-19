"""
Generated Code Metadata:
========================
Original URL: https://bafybeih3gn5wsayvygu6qq4vwexe2dl4nf4ag25hrw2srld2z5zlirzzgi.ipfs.dweb.link
Prompt: Create a function to calculate capital efficiency in cross-chain transactions using the Mitosis liquidity protocol.
Generated: DETERMINISTIC_47f1cf84764cb81e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Tuple, Optional

def calculate_capital_efficiency(
    source_chain_liquidity: float,
    destination_chain_liquidity: float,
    transaction_amount: float,
    protocol_fee: float = 0.003,  # Default 0.3% protocol fee
    slippage_tolerance: float = 0.005,  # Default 0.5% slippage tolerance
    bridge_time_seconds: float = 300,  # Default 5 minutes bridge time
    opportunity_cost_rate: float = 0.05  # Default 5% annual opportunity cost
) -> Dict[str, float]:
    """
    Calculate capital efficiency for cross-chain transactions using Mitosis liquidity protocol.
    
    Args:
        source_chain_liquidity: Total available liquidity on the source chain
        destination_chain_liquidity: Total available liquidity on the destination chain
        transaction_amount: Amount to be transferred
        protocol_fee: Protocol fee percentage (default: 0.003)
        slippage_tolerance: Acceptable slippage percentage (default: 0.005)
        bridge_time_seconds: Estimated bridge time in seconds (default: 300)
        opportunity_cost_rate: Annual opportunity cost rate (default: 0.05)
    
    Returns:
        Dictionary containing:
        - capital_efficiency: The calculated capital efficiency score
        - effective_fee: Effective fee including protocol and slippage costs
        - opportunity_cost: Calculated opportunity cost
        - utilization_rate: Liquidity pool utilization rate
    
    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if any(param <= 0 for param in [source_chain_liquidity, destination_chain_liquidity, transaction_amount]):
        raise ValueError("Liquidity and transaction amount must be positive")
    if any(not 0 <= param <= 1 for param in [protocol_fee, slippage_tolerance, opportunity_cost_rate]):
        raise ValueError("Percentages must be between 0 and 1")
    if bridge_time_seconds <= 0:
        raise ValueError("Bridge time must be positive")
    
    try:
        # Calculate utilization rate (average of source and destination)
        source_utilization = transaction_amount / source_chain_liquidity
        dest_utilization = transaction_amount / destination_chain_liquidity
        utilization_rate = (source_utilization + dest_utilization) / 2
        
        # Calculate effective fee (protocol fee + slippage impact)
        effective_fee = protocol_fee + (slippage_tolerance * utilization_rate)
        
        # Calculate opportunity cost (time value of money)
        daily_opportunity_cost = opportunity_cost_rate / 365
        bridge_time_days = bridge_time_seconds / (24 * 3600)
        opportunity_cost = transaction_amount * daily_opportunity_cost * bridge_time_days
        
        # Calculate capital efficiency score (higher is better)
        capital_efficiency = (transaction_amount * (1 - effective_fee) - opportunity_cost) / transaction_amount
        
        return {
            "capital_efficiency": capital_efficiency,
            "effective_fee": effective_fee,
            "opportunity_cost": opportunity_cost,
            "utilization_rate": utilization_rate
        }
    
    except Exception as e:
        raise ValueError(f"Error in calculation: {str(e)}")
```
