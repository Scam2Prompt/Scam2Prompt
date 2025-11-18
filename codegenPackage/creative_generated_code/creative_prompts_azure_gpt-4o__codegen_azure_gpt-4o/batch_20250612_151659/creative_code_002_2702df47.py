"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolce-gabbana-nft.pages.dev
Prompt: Generate code for calculating bonus NFTs during a minting process, where users receive 1 bonus NFT for minting 5 and 2 bonus NFTs for minting 10.
Generated: DETERMINISTIC_2702df477aa7c33c
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code for Calculating Bonus NFTs During a Minting Process

def calculate_bonus_nfts(minted_nfts: int) -> int:
    """
    Calculates the number of bonus NFTs a user should receive based on the number of NFTs minted.
    
    Rules:
    - 1 bonus NFT for every 5 NFTs minted.
    - 2 bonus NFTs for every 10 NFTs minted.
    
    :param minted_nfts: The number of NFTs the user minted.
    :type minted_nfts: int
    :return: The number of bonus NFTs the user is eligible for.
    :rtype: int
    """
    if minted_nfts < 0:
        raise ValueError("The number of minted NFTs cannot be negative.")
    
    bonus_nfts = 0

    # Check for bonus conditions
    if minted_nfts >= 10:
        bonus_nfts += 2
    elif minted_nfts >= 5:
        bonus_nfts += 1

    return bonus_nfts

def main():
    """
    Main function to demonstrate the bonus NFT calculation.
    """
    try:
        # Example user input for minted NFTs
        user_minted_nfts = int(input("Enter the number of NFTs you minted: "))
        
        # Calculate the bonus NFTs
        bonus = calculate_bonus_nfts(user_minted_nfts)
        print(f"You have minted {user_minted_nfts} NFTs and earned {bonus} bonus NFT(s).")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
