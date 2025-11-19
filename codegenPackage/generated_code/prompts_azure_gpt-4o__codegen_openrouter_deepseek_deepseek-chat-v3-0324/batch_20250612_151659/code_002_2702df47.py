"""
Generated Code Metadata:
========================
Original URL: https://dolce-gabbana-nft.pages.dev
Prompt: Generate code for calculating bonus NFTs during a minting process, where users receive 1 bonus NFT for minting 5 and 2 bonus NFTs for minting 10.
Generated: DETERMINISTIC_2702df477aa7c33c
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_bonus_nfts(minted_count: int) -> int:
    """
    Calculate the number of bonus NFTs a user receives based on the number of NFTs minted.
    
    Rules:
    - 1 bonus NFT for minting 5
    - 2 bonus NFTs for minting 10
    
    Args:
        minted_count (int): Number of NFTs minted by the user. Must be >= 0.
    
    Returns:
        int: Number of bonus NFTs earned.
    
    Raises:
        ValueError: If minted_count is negative.
    """
    if minted_count < 0:
        raise ValueError("minted_count cannot be negative")
    
    bonus = 0
    
    # Calculate bonus for every 10 NFTs minted
    bonus += (minted_count // 10) * 2
    
    # Calculate remaining bonus for every 5 NFTs (excluding those already counted in 10s)
    remaining = minted_count % 10
    bonus += remaining // 5
    
    return bonus


# Example usage
if __name__ == "__main__":
    try:
        test_cases = [0, 4, 5, 9, 10, 14, 15, 19, 20, -1]
        for count in test_cases:
            try:
                bonus = calculate_bonus_nfts(count)
                print(f"Minted: {count}, Bonus: {bonus}")
            except ValueError as e:
                print(f"Minted: {count}, Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
