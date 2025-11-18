"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-presale-dogcoin.pages.dev
Prompt: Write a function to calculate the total DOG tokens a user can purchase based on the presale cap of 1000 ETH and the current ETH deposit amount.
Generated: DETERMINISTIC_cf46ce06b413be2a
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_dog_tokens(eth_deposit: float, eth_to_dog_rate: float = 0.1, presale_cap: float = 1000.0) -> float:
    """
    Calculate the total DOG tokens a user can purchase based on their ETH deposit.
    
    Args:
        eth_deposit (float): The amount of ETH the user wants to deposit.
        eth_to_dog_rate (float): The conversion rate from ETH to DOG tokens (default is 0.1).
        presale_cap (float): The maximum cap for the presale in ETH (default is 1000.0).
    
    Returns:
        float: The total DOG tokens the user can purchase.
    
    Raises:
        ValueError: If eth_deposit is negative or exceeds the presale cap.
    """
    # Validate the ETH deposit amount
    if eth_deposit < 0:
        raise ValueError("ETH deposit cannot be negative.")
    if eth_deposit > presale_cap:
        raise ValueError(f"ETH deposit exceeds the presale cap of {presale_cap} ETH.")
    
    # Calculate the total DOG tokens based on the ETH deposit
    dog_tokens = eth_deposit / eth_to_dog_rate
    return dog_tokens

# Example usage:
if __name__ == "__main__":
    try:
        user_eth_deposit = 200.0  # Example ETH deposit
        total_dog_tokens = calculate_dog_tokens(user_eth_deposit)
        print(f"Total DOG tokens purchased: {total_dog_tokens}")
    except ValueError as e:
        print(f"Error: {e}")
```
