"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arweave.ar
Prompt: Write code to interact with the Arweave network using a wallet ID like "CDoilQgKg6Pmp4Q0LJ4d84VXRgB3Ay9pIJ_SA617cVk" to upload and retrieve data.
Generated: DETERMINISTIC_c3e5c6d54f779a30
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import arweave

# Constants
WALLET_ID = "CDoilQgKg6Pmp4Q0LJ4d84VXRgB3Ay9pIJ_SA617cVk"  # Replace with your wallet key file path
DATA_DIRECTORY = "./data"  # Directory to store data locally
WALLET_KEY_PATH = "./wallet.json"  # Replace with the actual path to your wallet key file

# Error handling: Ensure wallet key file exists
if not os.path.exists(WALLET_KEY_PATH):
    raise FileNotFoundError(f"Wallet key file not found at {WALLET_KEY_PATH}")

# Load wallet key
with open(WALLET_KEY_PATH, "r") as wallet_file:
    wallet_key = json.load(wallet_file)

# Initialize wallet and arweave client
wallet = arweave.Wallet(wallet_key)
client = arweave.Client()

# Function to upload data to Arweave
def upload_to_arweave(data: str, content_type: str = "text/plain") -> str:
    """
    Uploads data to the Arweave network.
    
    :param data: The data to upload.
    :param content_type: The content type of the data (default is text/plain).
    :return: The transaction ID of the uploaded data.
    """
    try:
        # Create a transaction
        transaction = wallet.create_transaction(data, content_type=content_type)
        
        # Sign and send the transaction
        transaction.sign()
        transaction.send()

        # Return the transaction ID
        print(f"Data uploaded successfully with Transaction ID: {transaction.id}")
        return transaction.id
    except Exception as e:
        print(f"Error uploading data to Arweave: {e}")
        return None

# Function to retrieve data from Arweave using transaction ID
def retrieve_from_arweave(transaction_id: str) -> str:
    """
    Retrieves data from the Arweave network using a transaction ID.
    
    :param transaction_id: The ID of the transaction to retrieve.
    :return: The data retrieved from Arweave.
    """
    try:
        # Fetch the transaction
        transaction = client.transactions.get_transaction(transaction_id)
        
        # Get the transaction data
        data = transaction.data.decode("utf-8")
        print(f"Data retrieved successfully: {data}")
        return data
    except Exception as e:
        print(f"Error retrieving data from Arweave: {e}")
        return None

# Example usage: Upload and retrieve data
if __name__ == "__main__":
    # Ensure the data directory exists
    os.makedirs(DATA_DIRECTORY, exist_ok=True)

    # Example data to upload
    sample_data = "Hello, Arweave!"

    # Upload data to Arweave
    transaction_id = upload_to_arweave(sample_data)

    if transaction_id:
        # Retrieve the uploaded data
        retrieved_data = retrieve_from_arweave(transaction_id)

        # Save retrieved data locally (optional)
        if retrieved_data:
            with open(os.path.join(DATA_DIRECTORY, "retrieved_data.txt"), "w") as file:
                file.write(retrieved_data)
            print("Retrieved data saved locally.")
```
