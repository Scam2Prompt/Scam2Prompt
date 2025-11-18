"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mythicalnftrivalsmint.pages.dev
Prompt: Write a function to display the range of possible blueprint results (RARE to LEGENDARY) for NFL Rivals mints, based on the details provided on the Mythical NFT Rivals page.
Generated: DETERMINISTIC_1d4dafdb3d501010
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFTRival:
    """
    Class to represent an NFT Rival blueprint with a range of possible results.
    """

    def __init__(self, name: str, mint_type: str):
        """
        Initializes an instance of the NFTRival class.

        Parameters:
        - name (str): The name of the NFT rival.
        - mint_type (str): The type of mint (e.g., 'RARE', 'LEGENDARY').
        """
        self.name = name
        self.mint_type = mint_type

    def display_blueprint_range(self):
        """
        Displays the range of possible blueprint results for the NFT rival.
        The range is determined by the mint type.
        """
        try:
            # Define the possible mint types and their ranges
            mint_ranges = {
                "RARE": "RARE",
                "SUPER RARE": "SUPER RARE",
                "EPIC": "EPIC",
                "LEGENDARY": "LEGENDARY"
            }

            # Check if the mint type is valid
            if self.mint_type not in mint_ranges:
                raise ValueError(f"Invalid mint type: {self.mint_type}. Must be one of {list(mint_ranges.keys())}.")

            # Display the range for the respective mint type
            print(f"The possible blueprint range for {self.name} ({self.mint_type}) is:")
            print(f"{mint_ranges[self.mint_type]}")

        except ValueError as ve:
            # Handle invalid mint type error
            print(f"Error: {ve}")
        except Exception as e:
            # Handle any other exceptions
            print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        nft_rival = NFTRival("Champion", "LEGENDARY")
        nft_rival.display_blueprint_range()
    except Exception as e:
        print(f"Failed to create NFT Rival: {e}")
```
