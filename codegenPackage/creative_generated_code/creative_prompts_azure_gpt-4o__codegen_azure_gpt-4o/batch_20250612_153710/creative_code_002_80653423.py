"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-chainbase.com
Prompt: Generate a code snippet to create a manuscript in Chainbase that converts blockchain data into a dataset suitable for AI training.
Generated: DETERMINISTIC_806534236b698f3b
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import chainbase
import json
import os

def connect_to_chainbase(api_key: str):
    """
    Connect to the Chainbase API using the provided API key.
    
    :param api_key: Chainbase API key
    :return: Chainbase client instance
    """
    try:
        client = chainbase.Client(api_key)
        return client
    except Exception as e:
        print(f"Error connecting to Chainbase: {e}")
        return None

def fetch_blockchain_data(client, blockchain: str, start_block: int, end_block: int):
    """
    Retrieve blockchain data from Chainbase for a specific range of blocks.
    
    :param client: Chainbase client instance
    :param blockchain: Name of the blockchain to query (e.g., 'ethereum')
    :param start_block: Starting block number
    :param end_block: Ending block number
    :return: Blockchain data as a list of dictionaries
    """
    try:
        data = client.get_blocks(blockchain, start=start_block, end=end_block)
        return data
    except Exception as e:
        print(f"Error fetching blockchain data: {e}")
        return []

def parse_data_for_ai_training(blockchain_data):
    """
    Parse blockchain data into a format suitable for AI training.
    
    :param blockchain_data: Raw blockchain data as a list of dictionaries
    :return: Parsed dataset for AI training
    """
    dataset = []
    try:
        for block in blockchain_data:
            # Extract relevant data fields from the block
            parsed_block = {
                "block_number": block.get("number"),
                "timestamp": block.get("timestamp"),
                "transactions": [
                    {
                        "tx_hash": tx.get("hash"),
                        "from": tx.get("from"),
                        "to": tx.get("to"),
                        "value": tx.get("value"),
                        "gas": tx.get("gas"),
                    }
                    for tx in block.get("transactions", [])
                ],
            }
            dataset.append(parsed_block)
        return dataset
    except Exception as e:
        print(f"Error parsing blockchain data: {e}")
        return []

def save_dataset_to_file(dataset, file_path: str):
    """
    Save the AI training dataset to a file in JSON format.
    
    :param dataset: Parsed dataset for AI training
    :param file_path: Path to the output file
    """
    try:
        with open(file_path, "w") as file:
            json.dump(dataset, file, indent=4)
        print(f"Dataset saved successfully to {file_path}")
    except Exception as e:
        print(f"Error saving dataset to file: {e}")

def main():
    """
    Main function to execute the manuscript logic.
    """
    # User-provided inputs
    api_key = os.getenv("CHAINBASE_API_KEY", "your_api_key_here")
    blockchain = "ethereum"
    start_block = 1000000
    end_block = 1000100
    output_file = "ai_training_dataset.json"

    # Step 1: Connect to Chainbase
    client = connect_to_chainbase(api_key)
    if not client:
        return

    # Step 2: Fetch blockchain data
    blockchain_data = fetch_blockchain_data(client, blockchain, start_block, end_block)
    if not blockchain_data:
        return

    # Step 3: Parse the data for AI training
    ai_dataset = parse_data_for_ai_training(blockchain_data)
    if not ai_dataset:
        return

    # Step 4: Save the parsed dataset to a file
    save_dataset_to_file(ai_dataset, output_file)

if __name__ == "__main__":
    main()
```
