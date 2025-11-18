"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graph-networks-app.vercel.app
Prompt: Generate code to query a graph network using The Graph Networks Registry v0.0.0 and display the results in JSON format.
Generated: DETERMINISTIC_f5f2fce46179bec7
Batch ID: 20250612_154737
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name": {
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

class GraphNetworkQuery:
    """
    A class to interact with The Graph Networks Registry API to query graph networks.
    """

    BASE_URL = "https://api.thegraph.com/subgraphs/name"

    def __init__(self, subgraph_name):
        """
        Initializes the GraphNetworkQuery with a given subgraph name.
        
        Parameters:
            subgraph_name (str): The name of the subgraph to query.
        """
        self.subgraph_name = subgraph_name

    def query(self, query_string):
        """
        Executes a GraphQL query against the specified subgraph.

        Parameters:
            query_string (str): The GraphQL query string to execute.

        Returns:
            dict: The JSON response from the API if the query is successful.

        Raises:
            Exception: If the query fails or if the response is not valid.
        """
        url = f"{self.BASE_URL}/{self.subgraph_name}"
        headers = {"Content-Type": "application/json"}
        payload = {"query": query_string}

        try:
            response = requests.post(url, headers=headers, json=payload)

            # Check if the response status code is 200 (OK)
            response.raise_for_status()

            # Parse and return the JSON response
            json_response = response.json()

            # Check if there are errors in the response
            if 'errors' in json_response:
                raise Exception(f"GraphQL error: {json_response['errors']}")

            return json_response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {str(e)}")
        except json.JSONDecodeError:
            raise Exception("Failed to decode JSON response.")

# Example usage
if __name__ == "__main__":
    # Define the subgraph name and query
    subgraph_name = "example/subgraph"
    query_string = """
    {
        entities {
            id
            name
        }
    }
    """

    # Create an instance of the GraphNetworkQuery
    graph_query = GraphNetworkQuery(subgraph_name)

    try:
        # Execute the query and print the results
        results = graph_query.query(query_string)
        print(json.dumps(results, indent=2))
    except Exception as e:
        print(f"Error: {str(e)}")
```
