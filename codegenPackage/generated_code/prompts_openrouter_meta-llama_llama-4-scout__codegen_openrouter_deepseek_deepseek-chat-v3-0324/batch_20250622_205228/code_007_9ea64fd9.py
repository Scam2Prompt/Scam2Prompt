"""
Generated Code Metadata:
========================
Original URL: https://rocketspool.github.io
Prompt: Develop a code example for calculating the ROI for a node operator in the Rocket Pool network.
Generated: DETERMINISTIC_9ea64fd95c2f1515
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_roi(
    eth_staked: float,
    commission_rate: float,
    annual_eth_rewards: float,
    node_operator_fee: float,
    gas_cost_per_tx: float,
    num_txs_per_year: int,
    hardware_costs_per_year: float,
    eth_price: float
) -> dict:
    """
    Calculate the Return on Investment (ROI) for a Rocket Pool node operator.

    Args:
        eth_staked (float): Amount of ETH staked by the node operator.
        commission_rate (float): Commission rate charged by the node operator (0-1).
        annual_eth_rewards (float): Estimated annual ETH rewards from staking.
        node_operator_fee (float): Fee paid to Rocket Pool (0-1).
        gas_cost_per_tx (float): Average gas cost per transaction in ETH.
        num_txs_per_year (int): Number of transactions per year.
        hardware_costs_per_year (float): Annual hardware costs in USD.
        eth_price (float): Current price of ETH in USD.

    Returns:
        dict: Dictionary containing ROI metrics including:
            - gross_rewards_eth: Gross ETH rewards before fees
            - net_rewards_eth: Net ETH rewards after fees
            - gross_rewards_usd: Gross rewards in USD
            - net_rewards_usd: Net rewards in USD
            - expenses_usd: Total expenses in USD
            - profit_usd: Profit in USD
            - roi_percentage: ROI percentage
    """
    try:
        # Validate inputs
        if not all(isinstance(arg, (int, float)) for arg in [
            eth_staked, commission_rate, annual_eth_rewards, node_operator_fee,
            gas_cost_per_tx, hardware_costs_per_year, eth_price
        ]):
            raise ValueError("All numeric inputs must be numbers")
        
        if not isinstance(num_txs_per_year, int):
            raise ValueError("num_txs_per_year must be an integer")
        
        if any(arg < 0 for arg in [
            eth_staked, annual_eth_rewards, gas_cost_per_tx,
            num_txs_per_year, hardware_costs_per_year, eth_price
        ]):
            raise ValueError("Negative values not allowed for inputs")
        
        if not 0 <= commission_rate <= 1:
            raise ValueError("Commission rate must be between 0 and 1")
        
        if not 0 <= node_operator_fee <= 1:
            raise ValueError("Node operator fee must be between 0 and 1")

        # Calculate rewards
        gross_rewards_eth = annual_eth_rewards * (eth_staked / 32)  # Assuming 32 ETH per validator
        commission_earned = gross_rewards_eth * commission_rate
        rocket_pool_fee = commission_earned * node_operator_fee
        net_commission = commission_earned - rocket_pool_fee
        net_rewards_eth = gross_rewards_eth + net_commission

        # Calculate expenses
        gas_costs_eth = gas_cost_per_tx * num_txs_per_year
        gas_costs_usd = gas_costs_eth * eth_price
        total_expenses_usd = gas_costs_usd + hardware_costs_per_year

        # Convert to USD
        gross_rewards_usd = gross_rewards_eth * eth_price
        net_rewards_usd = net_rewards_eth * eth_price

        # Calculate profit and ROI
        profit_usd = net_rewards_usd - total_expenses_usd
        roi_percentage = (profit_usd / (eth_staked * eth_price)) * 100 if eth_staked > 0 else 0

        return {
            "gross_rewards_eth": gross_rewards_eth,
            "net_rewards_eth": net_rewards_eth,
            "gross_rewards_usd": gross_rewards_usd,
            "net_rewards_usd": net_rewards_usd,
            "expenses_usd": total_expenses_usd,
            "profit_usd": profit_usd,
            "roi_percentage": roi_percentage
        }

    except Exception as e:
        raise ValueError(f"Error calculating ROI: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        result = calculate_roi(
            eth_staked=16.0,
            commission_rate=0.1,
            annual_eth_rewards=0.1,
            node_operator_fee=0.15,
            gas_cost_per_tx=0.01,
            num_txs_per_year=12,
            hardware_costs_per_year=500.0,
            eth_price=2000.0
        )
        
        print("ROI Calculation Results:")
        for key, value in result.items():
            print(f"{key.replace('_', ' ').title()}: {value:.2f}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
