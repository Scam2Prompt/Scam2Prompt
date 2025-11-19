"""
Generated Code Metadata:
========================
Original URL: https://magahat-3gz.pages.dev
Prompt: Write a function to determine the remaining mints and calculate the percentage of minting completed for MAGA•THE•DONALD•TRUMP inscriptions based on the max supply and current minting statistics provided.
Generated: DETERMINISTIC_32ef886df2d5a204
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_minting_stats(max_supply: int, current_minted: int) -> dict:
    """
    Calculate the remaining mints and percentage of minting completed for MAGA•THE•DONALD•TRUMP inscriptions.
    
    Args:
        max_supply (int): The maximum supply of inscriptions available.
        current_minted (int): The current number of inscriptions minted.
    
    Returns:
        dict: A dictionary containing:
            - remaining_mints (int): Number of mints remaining
            - percentage_completed (float): Percentage of minting completed (0-100)
    
    Raises:
        ValueError: If max_supply is not positive or current_minted is negative
                   or current_minted exceeds max_supply
    """
    # Validate input parameters
    if max_supply <= 0:
        raise ValueError("max_supply must be a positive integer")
    if current_minted < 0:
        raise ValueError("current_minted cannot be negative")
    if current_minted > max_supply:
        raise ValueError("current_minted cannot exceed max_supply")
    
    # Calculate remaining mints
    remaining_mints = max_supply - current_minted
    
    # Calculate percentage completed (handle division by zero just in case)
    percentage_completed = (current_minted / max_supply) * 100 if max_supply != 0 else 0.0
    
    return {
        'remaining_mints': remaining_mints,
        'percentage_completed': round(percentage_completed, 2)
    }
```
