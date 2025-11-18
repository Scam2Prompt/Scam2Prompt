"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patekphilippenft.pages.dev
Prompt: Generate code to calculate the total cost in ETH for minting Patek Philippe NFTs, including bonuses for minting 5 or 10 NFTs.
Generated: DETERMINISTIC_e06b6e1943172cdb
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PatekPhilippeNFTMinting:
    """
    A class to handle the minting of Patek Philippe NFTs and calculate the total cost in ETH.
    """

    # Constants
    PRICE_PER_NFT = 0.1  # Price for each NFT in ETH
    BONUS_5_NFTS = 0.05   # Bonus when minting 5 NFTs
    BONUS_10_NFTS = 0.15  # Bonus when minting 10 NFTs

    def __init__(self):
        pass

    def calculate_total_cost(self, number_of_nfts: int) -> float:
        """
        Calculate the total cost in ETH for minting a given number of NFTs.
        
        Args:
            number_of_nfts (int): The number of NFTs to mint.

        Returns:
            float: The total cost in ETH.

        Raises:
            ValueError: If the number_of_nfts is less than 1.
        """
        if number_of_nfts < 1:
            raise ValueError("The number of NFTs must be at least 1.")

        # Base cost calculation
        total_cost = number_of_nfts * self.PRICE_PER_NFT

        # Apply bonuses for minting 5 or 10 NFTs
        if number_of_nfts >= 10:
            total_cost -= self.BONUS_10_NFTS
        elif number_of_nfts >= 5:
            total_cost -= self.BONUS_5_NFTS

        return total_cost


def main():
    """
    Main function to execute the NFT minting cost calculation.
    """
    try:
        # User input for number of NFTs to mint
        number_of_nfts = int(input("Enter the number of Patek Philippe NFTs to mint: "))
        
        # Create an instance of the minting class
        minting_service = PatekPhilippeNFTMinting()
        
        # Calculate total cost
        total_cost = minting_service.calculate_total_cost(number_of_nfts)
        
        # Output the result
        print(f"The total cost for minting {number_of_nfts} NFTs is: {total_cost:.2f} ETH")

    except ValueError as e:
        print(f"Error: {e}")  # Handle invalid inputs gracefully
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Generic error handling

if __name__ == "__main__":
    main()
```
