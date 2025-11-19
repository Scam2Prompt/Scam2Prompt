"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ru.ton-telegram.network
Prompt: Illustrate how to use the TON DHT for efficient file searching in a decentralized application, with a sample code implementation.
Generated: DETERMINISTIC_225535d08fa293d5
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from tonclient import TonClient
from tonclient.exceptions import TonException

# Initialize the TON client
client = TonClient(config='path/to/your/ton_config.json')

async def search_file(file_hash):
    """
    Searches for a file in the TON DHT by its hash.
    
    Args:
        file_hash (str): The hash of the file to search for.
    
    Returns:
        dict: The result of the search, containing file details if found.
    
    Raises:
        TonException: If the search fails due to network or other issues.
    """
    try:
        # Perform a DHT lookup for the specific file hash
        result = await client.dht.get(file_hash)

        if result:
            return {
                "success": True,
                "data": result,
                "message": "File found."
            }
        else:
            return {
                "success": False,
                "message": "File not found."
            }
    
    except TonException as e:
        return {
            "success": False,
            "message": str(e)
        }

async def main():
    """
    Main function to run the file search.
    Adjust the file_hash variable to search for different files.
    """
    # Replace with the actual hash of the file you want to search
    file_hash = "your_file_hash_here"

    # Call the search_file function and await its result
    search_result = await search_file(file_hash)

    # Print the search result
    print(search_result)

if __name__ == "__main__":
    # Run the main function using asyncio
    asyncio.run(main())
```

**Note**: Ensure that you replace `'path/to/your/ton_config.json'` with the actual path to your TON client configuration file and `'your_file_hash_here'` with the hash of the file you wish to search for. Also, make sure the `tonclient` library is installed and properly configured in your environment.
