"""
Generated Code Metadata:
========================
Original URL: https://stader.pages.dev
Prompt: Create a function that calculates the ETHx exchange rate (1 ETHx = 1.029570 ETH) and simulates the staking rewards based on the annualized rate of 2.72%.
Generated: DETERMINISTIC_0ff37a4cc6c50ec3
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_ethx_exchange_rate(ethx_amount: float) -> float:
    """
    Calculates the ETH exchange rate for a given ETHx amount.

    Args:
    ethx_amount (float): The amount of ETHx.

    Returns:
    float: The equivalent amount of ETH.
    """
    # Define the ETHx exchange rate
    ethx_to_eth_rate = 1.029570
    
    # Calculate the ETH amount
    eth_amount = ethx_amount * ethx_to_eth_rate
    
    return eth_amount


def simulate_staking_rewards(ethx_amount: float, 
                             annualized_rate: float = 0.0272, 
                             compounding_frequency: int = 365) -> float:
    """
    Simulates the staking rewards for a given ETHx amount.

    Args:
    ethx_amount (float): The amount of ETHx.
    annualized_rate (float, optional): The annualized staking rate. Defaults to 0.0272 (2.72%).
    compounding_frequency (int, optional): The compounding frequency per year. Defaults to 365.

    Returns:
    float: The staking rewards.
    """
    try:
        # Validate inputs
        if ethx_amount < 0:
            raise ValueError("ETHx amount cannot be negative")
        if annualized_rate < 0 or annualized_rate > 1:
            raise ValueError("Annualized rate must be between 0 and 1")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be greater than 0")

        # Calculate the staking rewards
        staking_rewards = ethx_amount * (annualized_rate / compounding_frequency)
        
        return staking_rewards
    
    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    # Example usage
    ethx_amount = 100
    eth_amount = calculate_ethx_exchange_rate(ethx_amount)
    staking_rewards = simulate_staking_rewards(ethx_amount)

    print(f"1 ETHx = 1.029570 ETH")
    print(f"{ethx_amount} ETHx ≈ {eth_amount} ETH")
    print(f"Staking rewards for {ethx_amount} ETHx: {staking_rewards}")


if __name__ == "__main__":
    main()
```
