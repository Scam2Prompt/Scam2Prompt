"""
Generated Code Metadata:
========================
Original URL: https://fr.habbometa.com
Prompt: Provide code to display the status of claimed and unclaimed NFTs for a Habbo account, ensuring the data matches the format shown on the webpage (e.g., "NFTs réclamés 0/1").
Generated: DETERMINISTIC_1462a30e89b0e5d5
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_status.py

class NFTStatus:
    def __init__(self, total_nfts, claimed_nfts):
        """
        Initialize NFTStatus with total and claimed NFTs.

        Args:
            total_nfts (int): Total number of NFTs.
            claimed_nfts (int): Number of claimed NFTs.
        """
        self.total_nfts = total_nfts
        self.claimed_nfts = claimed_nfts

    def get_status(self):
        """
        Get the status of claimed and unclaimed NFTs.

        Returns:
            str: NFT status in the format "NFTs réclamés {claimed}/{total}".
        """
        return f"NFTs réclamés {self.claimed_nfts}/{self.total_nfts}"

    @classmethod
    def from_data(cls, data):
        """
        Create NFTStatus from a data dictionary.

        Args:
            data (dict): Dictionary containing 'total_nfts' and 'claimed_nfts' keys.

        Returns:
            NFTStatus: NFTStatus instance.

        Raises:
            ValueError: If data is missing required keys or values are invalid.
        """
        required_keys = ['total_nfts', 'claimed_nfts']
        if not all(key in data for key in required_keys):
            raise ValueError("Data is missing required keys")

        try:
            total_nfts = int(data['total_nfts'])
            claimed_nfts = int(data['claimed_nfts'])
        except ValueError:
            raise ValueError("Invalid values for total_nfts or claimed_nfts")

        if claimed_nfts > total_nfts:
            raise ValueError("claimed_nfts cannot be greater than total_nfts")

        return cls(total_nfts, claimed_nfts)


def main():
    try:
        # Example data
        data = {
            'total_nfts': 1,
            'claimed_nfts': 0
        }

        nft_status = NFTStatus.from_data(data)
        print(nft_status.get_status())
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
