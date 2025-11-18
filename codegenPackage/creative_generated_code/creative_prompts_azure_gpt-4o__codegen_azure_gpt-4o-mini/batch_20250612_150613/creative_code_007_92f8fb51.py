"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-zielchain.vercel.app
Prompt: Create a script to handle NFT ownership rights for non-commercial use, such as profile pictures on social media, in accordance with ZIELCHAIN's terms.
Generated: DETERMINISTIC_92f8fb51f8b9451c
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Any

class NFTOwnershipManager:
    """
    A class to handle NFT ownership rights for non-commercial use according to ZIELCHAIN's terms.
    """

    def __init__(self, nft_data_file: str):
        """
        Initializes the NFTOwnershipManager with the NFT data file.

        Args:
            nft_data_file (str): The path to the JSON file containing NFT data.
        """
        self.nft_data_file = nft_data_file
        self.nft_data = self.load_nft_data()

    def load_nft_data(self) -> Dict[str, Any]:
        """
        Loads NFT data from the specified JSON file.

        Returns:
            Dict[str, Any]: The loaded NFT data.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file is not a valid JSON.
        """
        try:
            with open(self.nft_data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error: The file {self.nft_data_file} was not found.") from e
        except json.JSONDecodeError as e:
            raise ValueError("Error: The file is not a valid JSON.") from e

    def check_ownership(self, nft_id: str, owner_address: str) -> bool:
        """
        Checks if a given address owns a specific NFT.

        Args:
            nft_id (str): The unique identifier of the NFT.
            owner_address (str): The address of the user.

        Returns:
            bool: True if the user owns the NFT, False otherwise.
        """
        nft_info = self.nft_data.get(nft_id)
        if nft_info:
            return nft_info.get('owner') == owner_address
        return False

    def get_usage_rights(self, nft_id: str) -> str:
        """
        Retrieves the usage rights associated with an NFT.

        Args:
            nft_id (str): The unique identifier of the NFT.

        Returns:
            str: Description of the usage rights for the NFT.
        """
        nft_info = self.nft_data.get(nft_id)
        if nft_info:
            return nft_info.get('usage_rights', 'No usage rights information available.')
        return 'NFT not found.'

    def update_usage_rights(self, nft_id: str, new_rights: str) -> None:
        """
        Updates the usage rights for a specific NFT.

        Args:
            nft_id (str): The unique identifier of the NFT.
            new_rights (str): The new usage rights to be assigned.

        Raises:
            ValueError: If the NFT is not found.
        """
        nft_info = self.nft_data.get(nft_id)
        if nft_info:
            nft_info['usage_rights'] = new_rights
            self.save_nft_data()
        else:
            raise ValueError('NFT not found.')

    def save_nft_data(self) -> None:
        """
        Saves the current NFT data back to the JSON file.
        """
        with open(self.nft_data_file, 'w') as file:
            json.dump(self.nft_data, file, indent=4)

# Example usage:
if __name__ == "__main__":
    nft_manager = NFTOwnershipManager('nft_data.json')

    # Check ownership of an NFT
    nft_id = 'nft123'
    user_address = '0xabc123'
    if nft_manager.check_ownership(nft_id, user_address):
        print(f"User {user_address} owns NFT {nft_id}.")
        print("Usage rights:", nft_manager.get_usage_rights(nft_id))
    else:
        print(f"User {user_address} does not own NFT {nft_id}.")

    # Update usage rights
    try:
        nft_manager.update_usage_rights(nft_id, 'Profile picture usage only')
        print("Usage rights updated successfully.")
    except ValueError as e:
        print(e)
```
