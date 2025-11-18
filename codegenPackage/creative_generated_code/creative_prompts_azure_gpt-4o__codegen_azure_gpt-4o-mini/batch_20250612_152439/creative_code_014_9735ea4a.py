"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet.pages.dev
Prompt: How can I use LavaSDK to implement a decentralized application that queries data from multiple blockchain networks? Provide a code example.
Generated: DETERMINISTIC_9735ea4abc9f396b
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from LavaSDK
from lava_sdk import LavaSDK, BlockchainNetwork

# Define a class for the decentralized application
class MultiBlockchainQueryApp:
    def __init__(self, api_key):
        """
        Initializes the MultiBlockchainQueryApp instance.

        Args:
            api_key (str): API key for authenticating with LavaSDK.
        """
        self.sdk = LavaSDK(api_key)

    def query_blockchain_data(self, networks, query):
        """
        Queries data from multiple blockchain networks.

        Args:
            networks (list): List of blockchain network names to query.
            query (str): The query string to execute on the blockchain.

        Returns:
            dict: A dictionary with network names as keys and query results as values.
        """
        results = {}
        for network in networks:
            try:
                # Create a connection to the specified blockchain network
                blockchain = BlockchainNetwork(network)
                # Execute the query and store the result
                result = self.sdk.execute_query(blockchain, query)
                results[network] = result
            except Exception as e:
                # Log the error and continue with the next network
                print(f"Error querying {network}: {str(e)}")
                results[network] = None  # Store None for failed queries
        
        return results

# Example usage of the MultiBlockchainQueryApp class
if __name__ == "__main__":
    # Define your API key here
    API_KEY = "your_api_key_here"
    
    # Initialize the application
    app = MultiBlockchainQueryApp(API_KEY)

    # Specify the networks and the query
    networks_to_query = ["Ethereum", "Polygon", "BinanceSmartChain"]
    sample_query = "SELECT block_number, transaction_count FROM blocks LIMIT 10"

    # Execute the query across specified networks
    try:
        query_results = app.query_blockchain_data(networks_to_query, sample_query)
        print("Query Results:", query_results)
    except Exception as e:
        print(f"An error occurred while querying blockchain data: {str(e)}")
```

Make sure to replace `"your_api_key_here"` with an actual API key provided by LavaSDK for authentication. This code includes basic error handling and is structured to follow best practices for clarity and maintainability.
