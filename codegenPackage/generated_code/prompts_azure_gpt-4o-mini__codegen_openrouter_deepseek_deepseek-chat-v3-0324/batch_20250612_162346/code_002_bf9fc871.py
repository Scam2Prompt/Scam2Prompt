"""
Generated Code Metadata:
========================
Original URL: https://realis.pages.dev
Prompt: Generate a Python function that calculates the drop rate for different rarities of Meowgon NFTs based on the provided percentages.
Generated: DETERMINISTIC_bf9fc871e874d195
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_drop_rates(total_nfts, rarity_percentages):
    """
    Calculate the number of NFTs to drop for each rarity based on given percentages.
    
    Args:
        total_nfts (int): Total number of NFTs to be dropped.
        rarity_percentages (dict): Dictionary with rarity names as keys and their percentages as values.
                                  Example: {'common': 60, 'rare': 30, 'epic': 8, 'legendary': 2}
    
    Returns:
        dict: Dictionary with rarity names as keys and the calculated count of NFTs as values.
    
    Raises:
        ValueError: If total_nfts is not positive or if percentages don't sum to 100.
    """
    # Validate input
    if not isinstance(total_nfts, int) or total_nfts <= 0:
        raise ValueError("total_nfts must be a positive integer")
    
    if not isinstance(rarity_percentages, dict):
        raise ValueError("rarity_percentages must be a dictionary")
    
    total_percentage = sum(rarity_percentages.values())
    if total_percentage != 100:
        raise ValueError("Percentages must sum to 100")
    
    # Calculate drop counts
    drop_counts = {}
    remaining_nfts = total_nfts
    
    # Sort rarities from highest to lowest percentage to handle rounding properly
    sorted_rarities = sorted(rarity_percentages.items(), key=lambda x: -x[1])
    
    for rarity, percentage in sorted_rarities[:-1]:
        count = int(round(total_nfts * percentage / 100))
        drop_counts[rarity] = count
        remaining_nfts -= count
    
    # Assign remaining NFTs to the last rarity to ensure total matches
    last_rarity = sorted_rarities[-1][0]
    drop_counts[last_rarity] = remaining_nfts
    
    return drop_counts
```
