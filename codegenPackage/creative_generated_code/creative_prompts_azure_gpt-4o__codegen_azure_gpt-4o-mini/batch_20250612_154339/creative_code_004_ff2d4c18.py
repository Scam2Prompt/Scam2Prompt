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
  "https://api.thegraph.com/subgraphs/name/your-subgraph-name": {
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
import requests
import json

class GraphQLClient:
    """
    A simple GraphQL client to interact with The Graph API.
    """

    def __init__(self, url):
        """
        Initializes the GraphQL client with the given URL.
        
        Args:
            url (str): The URL of the GraphQL endpoint.
        """
        self.url = url

    def execute_query(self, query, variables=None):
        """
        Executes a GraphQL query against the specified endpoint.
        
        Args:
            query (str): The GraphQL query string.
            variables (dict, optional): A dictionary of variables for the query.
        
        Returns:
            dict: The response from the GraphQL API.
        
        Raises:
            Exception: If the API request fails or returns an error.
        """
        headers = {'Content-Type': 'application/json'}
        payload = {
            'query': query,
            'variables': variables or {}
        }
        
        try:
            response = requests.post(self.url, headers=headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            response_data = response.json()

            # Check if there are errors in the response
            if 'errors' in response_data:
                raise Exception(f"GraphQL error: {response_data['errors']}")
            
            return response_data['data']

        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {e}")

def main():
    """
    Main function to query blockchain data from The Graph.
    """
    # The Graph API endpoint
    graph_url = "https://api.thegraph.com/subgraphs/name/your-subgraph-name"

    # Create a GraphQL client
    graphql_client = GraphQLClient(graph_url)
    
    # Define the GraphQL query
    query = """
    {
        yourQuery {
            field1
            field2
            field3
        }
    }
    """

    try:
        # Execute the query and get the data
        data = graphql_client.execute_query(query)
        
        # Process the returned data
        print("Query Data:", json.dumps(data, indent=4))
    
    except Exception as e:
        # Handle any errors that occur during the query execution
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
