"""
Generated Code Metadata:
========================
Original URL: https://rocket-pool.xyz
Prompt: Design a function to calculate the commission earned by a node operator on Rocket Pool, and describe how to integrate rETH into a DeFi protocol.
Generated: DETERMINISTIC_2c6a28d6978490a9
Batch ID: 20250622_212600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_commission(dao_fee: float, rpl_stake: float, eth_pool: float, commission_rate: float) -> float:
    """
    Calculate the commission earned by a node operator on Rocket Pool.

    Args:
    - dao_fee (float): The DAO fee.
    - rpl_stake (float): The RPL stake.
    - eth_pool (float): The ETH pool.
    - commission_rate (float): The commission rate.

    Returns:
    - commission (float): The commission earned.

    Raises:
    - ValueError: If any input is negative.
    """

    # Check for negative inputs
    if dao_fee < 0 or rpl_stake < 0 or eth_pool < 0 or commission_rate < 0:
        raise ValueError("All inputs must be non-negative.")

    # Calculate the total value
    total_value = eth_pool + rpl_stake

    # Calculate the commission
    commission = (total_value * commission_rate) * (1 - dao_fee)

    return commission


def integrate_reth(defi_protocol: Dict) -> Dict:
    """
    Integrate rETH into a DeFi protocol.

    Args:
    - defi_protocol (Dict): The DeFi protocol configuration.

    Returns:
    - integrated_protocol (Dict): The updated DeFi protocol configuration.

    Raises:
    - ValueError: If the DeFi protocol configuration is invalid.
    """

    # Check if the DeFi protocol configuration is valid
    required_keys = ["name", "rETH_address", "oracle_address"]
    if not all(key in defi_protocol for key in required_keys):
        raise ValueError("Invalid DeFi protocol configuration.")

    # Initialize the integrated protocol
    integrated_protocol = defi_protocol.copy()

    # Add rETH as a collateral asset
    integrated_protocol["collateral_assets"] = integrated_protocol.get("collateral_assets", [])
    integrated_protocol["collateral_assets"].append("rETH")

    # Update the oracle address
    integrated_protocol["oracle_address"] = defi_protocol["rETH_address"]

    # Add rETH liquidity pool
    integrated_protocol["liquidity_pools"] = integrated_protocol.get("liquidity_pools", {})
    integrated_protocol["liquidity_pools"]["rETH"] = {
        "address": defi_protocol["rETH_address"],
        "oracle_address": defi_protocol["oracle_address"]
    }

    return integrated_protocol


# Example usage
if __name__ == "__main__":
    dao_fee = 0.1  # 10%
    rpl_stake = 1000.0
    eth_pool = 10000.0
    commission_rate = 0.05  # 5%

    commission = calculate_commission(dao_fee, rpl_stake, eth_pool, commission_rate)
    print(f"Commission: {commission}")

    defi_protocol = {
        "name": "Example Protocol",
        "rETH_address": "0x...rETH_address...",
        "oracle_address": "0x...oracle_address..."
    }

    integrated_protocol = integrate_reth(defi_protocol)
    print(integrated_protocol)
```
