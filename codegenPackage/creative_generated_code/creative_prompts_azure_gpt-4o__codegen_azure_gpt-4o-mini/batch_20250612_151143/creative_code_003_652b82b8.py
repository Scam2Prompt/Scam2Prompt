"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecy.pages.dev
Prompt: Write a function to validate a Testnet Voyage NFT recipient's attestation, ensuring the recipient is Tier 1 to 4, as outlined in the Linea PoH requirements.
Generated: DETERMINISTIC_652b82b826a2deed
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TierValidationError(Exception):
    """Custom exception for tier validation errors."""
    pass

def validate_tier(nft_recipient_tier):
    """
    Validate the tier of a Testnet Voyage NFT recipient.

    Args:
        nft_recipient_tier (int): The tier level of the NFT recipient (1-4).

    Raises:
        TierValidationError: If the tier is out of the acceptable range (1-4).
    
    Returns:
        bool: True if the tier is valid, False otherwise.
    """
    # Define the acceptable tiers
    min_tier = 1
    max_tier = 4
    
    # Check if the given tier is within the acceptable range
    if nft_recipient_tier < min_tier or nft_recipient_tier > max_tier:
        raise TierValidationError(f"Invalid tier: {nft_recipient_tier}. Must be between {min_tier} and {max_tier}.")
    
    return True

# Example usage
if __name__ == "__main__":
    try:
        recipient_tier = int(input("Enter the NFT recipient's tier (1-4): "))
        if validate_tier(recipient_tier):
            print(f"Recipient's tier {recipient_tier} is valid for NFT attestation.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except TierValidationError as e:
        print(e)
```
