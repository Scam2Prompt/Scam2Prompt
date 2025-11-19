"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-chainbase.com
Prompt: Provide an example of how to programmatically access omnichain data using Chainbase's SDK in Python.
Generated: DETERMINISTIC_07ca220934f05e62
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import chainbase

class OmnichainDataFetcher:
    """
    A class to fetch omnichain data using Chainbase's SDK.
    """

    def __init__(self, api_key: str):
        """
        Initializes the OmnichainDataFetcher with the provided API key.

        Args:
            api_key (str): The API key for accessing Chainbase's services.
        """
        self.api_key = api_key
        self.client = self.initialize_chainbase_client()

    def initialize_chainbase_client(self):
        """
        Initializes the Chainbase client with the API key.

        Returns:
            chainbase.Client: An instance of the Chainbase client.
        """
        try:
            client = chainbase.Client(api_key=self.api_key)
            return client
        except Exception as e:
            raise RuntimeError("Failed to initialize Chainbase client") from e

    def get_omnichain_data(self, query: str):
        """
        Fetches omnichain data using a specified query.

        Args:
            query (str): The query to fetch data from Chainbase.

        Returns:
            dict: The response data from Chainbase.

        Raises:
            ValueError: If the query is invalid or empty.
            RuntimeError: If there is an error while fetching data.
        """
        if not query:
            raise ValueError("Query must not be empty")

        try:
            response = self.client.fetch_data(query)
            return response
        except Exception as e:
            raise RuntimeError("Error fetching omnichain data") from e

if __name__ == "__main__":
    # Example usage of the OmnichainDataFetcher class
    API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    query = '{"someQueryParameter": "value"}'  # Replace with your actual query

    try:
        fetcher = OmnichainDataFetcher(api_key=API_KEY)
        data = fetcher.get_omnichain_data(query)
        print("Fetched omnichain data:", data)
    except Exception as e:
        print(f"An error occurred: {e}")
```
