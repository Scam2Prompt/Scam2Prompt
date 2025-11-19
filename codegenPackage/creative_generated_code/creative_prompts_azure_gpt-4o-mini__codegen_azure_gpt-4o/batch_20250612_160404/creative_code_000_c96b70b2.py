"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arweave.ar
Prompt: How can I generate a wallet using the Arweave API, specifically with the wallet ID format seen in the content?
Generated: DETERMINISTIC_c96b70b2773bfbc8
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from arweave import Wallet

def generate_wallet(output_dir: str) -> str:
    """
    Generates a new Arweave wallet and saves the key file to a specified directory.
    
    Args:
        output_dir (str): The directory where the wallet key file will be saved.

    Returns:
        str: The wallet address (ID) of the generated wallet.

    Raises:
        FileNotFoundError: If the specified output directory does not exist.
        PermissionError: If the program does not have write permissions for the directory.
    """
    # Check if the output directory exists
    if not os.path.exists(output_dir):
        raise FileNotFoundError(f"Output directory '{output_dir}' does not exist.")

    # Check if the directory is writable
    if not os.access(output_dir, os.W_OK):
        raise PermissionError(f"Write permissions are required for the directory '{output_dir}'.")

    # Generate a new wallet
    wallet = Wallet.create_wallet()

    # Extract the wallet address (ID)
    wallet_address = wallet.address

    # Define the key file path
    key_file_path = os.path.join(output_dir, f"{wallet_address}_keyfile.json")

    # Save the wallet key to the specified directory
    with open(key_file_path, "w") as key_file:
        json.dump(wallet.key, key_file, indent=4)

    return wallet_address

if __name__ == "__main__":
    try:
        # Specify the directory where the wallet key file will be saved
        output_directory = "./wallets"

        # Create the directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        # Generate the wallet and retrieve the wallet address
        wallet_id = generate_wallet(output_directory)

        print(f"Wallet generated successfully with address: {wallet_id}")
        print(f"Key file saved to: {output_directory}")

    except Exception as e:
        print(f"Error: {e}")
```
