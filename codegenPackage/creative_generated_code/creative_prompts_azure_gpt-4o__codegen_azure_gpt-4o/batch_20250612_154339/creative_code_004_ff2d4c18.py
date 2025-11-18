"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hemi.host
Prompt: Write a script using Hemi’s ecosystem tools to query blockchain data via The Graph integration.
Generated: DETERMINISTIC_ff2d4c185019e69b
Batch ID: 20250612_154339
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/example/example-subgraph": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from Hemi's ecosystem tools and The Graph integration
from hemi.graph import GraphClient
from hemi.utilities import validate_query, handle_error

# Define constants for The Graph's API endpoint and the subgraph to query
GRAPH_API_ENDPOINT = "https://api.thegraph.com/subgraphs/name/example/example-subgraph"

# Initialize the GraphClient
graph_client = GraphClient(api_endpoint=GRAPH_API_ENDPOINT)

def query_blockchain_data(query_string):
    """
    Function to query blockchain data using Hemi's GraphClient.

    Args:
        query_string (str): The GraphQL query string to execute.

    Returns:
        dict: The result of the query if successful.
    """
    try:
        # Validate the query syntax before sending it
        validate_query(query_string)
        
        # Execute the query using the GraphClient
        response = graph_client.query(query_string)

        # Check if the response contains errors
        if response.get("errors"):
            error_message = response["errors"]
            handle_error(error_message)
            return None

        # Return the data from the response
        return response.get("data", {})
    
    except Exception as e:
        # Handle unexpected errors gracefully
        handle_error(f"An unexpected error occurred: {str(e)}")
        return None

# Define the GraphQL query string
query = """
{
  transactions(first: 10) {
    id
    from
    to
    value
    timestamp
  }
}
"""

if __name__ == "__main__":
    # Query the blockchain data using the defined query string
    result = query_blockchain_data(query)

    if result:
        # Print the queried data in a readable format
        print("Query Result:")
        for transaction in result.get("transactions", []):
            print(f"Transaction ID: {transaction['id']}")
            print(f"From: {transaction['from']}")
            print(f"To: {transaction['to']}")
            print(f"Value: {transaction['value']}")
            print(f"Timestamp: {transaction['timestamp']}")
            print("-" * 40)
    else:
        print("Failed to retrieve blockchain data.")
```
