"""
Generated Code Metadata:
========================
Original URL: https://app-chainbase.com
Prompt: Generate a code snippet to create a manuscript in Chainbase that converts blockchain data into a dataset suitable for AI training.
Generated: DETERMINISTIC_806534236b698f3b
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any
from chainbase import ChainbaseClient
from datetime import datetime

class BlockchainToAIDataset:
    """
    Converts blockchain data from Chainbase into a structured dataset for AI training.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the Chainbase client with the provided API key.
        
        Args:
            api_key (str): Chainbase API key for authentication
        """
        self.client = ChainbaseClient(api_key)
        self.dataset = []
        
    def fetch_block_data(self, chain_id: str, start_block: int, end_block: int) -> List[Dict[str, Any]]:
        """
        Fetch block data from Chainbase for a given range of blocks.
        
        Args:
            chain_id (str): Blockchain identifier (e.g., 'eth-mainnet')
            start_block (int): Starting block number
            end_block (int): Ending block number
            
        Returns:
            List[Dict[str, Any]]: List of block data dictionaries
        """
        try:
            blocks = []
            for block_num in range(start_block, end_block + 1):
                block = self.client.get_block(chain_id, block_num)
                if block:
                    blocks.append(block)
            return blocks
        except Exception as e:
            print(f"Error fetching block data: {e}")
            return []
    
    def process_transactions(self, block_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Process transactions from a block into a standardized format.
        
        Args:
            block_data (Dict[str, Any]): Raw block data from Chainbase
            
        Returns:
            List[Dict[str, Any]]: Processed transactions
        """
        processed = []
        for tx in block_data.get('transactions', []):
            processed_tx = {
                'tx_hash': tx.get('hash'),
                'from': tx.get('from'),
                'to': tx.get('to'),
                'value': tx.get('value'),
                'gas': tx.get('gas'),
                'gas_price': tx.get('gasPrice'),
                'block_number': block_data.get('number'),
                'timestamp': datetime.fromtimestamp(int(block_data.get('timestamp', 0))).isoformat(),
                'input_data': tx.get('input')
            }
            processed.append(processed_tx)
        return processed
    
    def generate_dataset(self, chain_id: str, start_block: int, end_block: int) -> List[Dict[str, Any]]:
        """
        Generate AI training dataset from blockchain data.
        
        Args:
            chain_id (str): Blockchain identifier
            start_block (int): Starting block number
            end_block (int): Ending block number
            
        Returns:
            List[Dict[str, Any]]: Generated dataset
        """
        blocks = self.fetch_block_data(chain_id, start_block, end_block)
        for block in blocks:
            self.dataset.extend(self.process_transactions(block))
        return self.dataset
    
    def save_to_json(self, file_path: str) -> bool:
        """
        Save the generated dataset to a JSON file.
        
        Args:
            file_path (str): Path to save the JSON file
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.dataset, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving dataset: {e}")
            return False

# Example usage
if __name__ == "__main__":
    API_KEY = "your_chainbase_api_key"
    converter = BlockchainToAIDataset(API_KEY)
    
    # Generate dataset for Ethereum blocks 18000000 to 18000100
    dataset = converter.generate_dataset('eth-mainnet', 18000000, 18000100)
    
    # Save to file
    converter.save_to_json('blockchain_dataset.json')
```
