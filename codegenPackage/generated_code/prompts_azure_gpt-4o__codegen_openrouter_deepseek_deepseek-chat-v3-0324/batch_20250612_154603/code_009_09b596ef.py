"""
Generated Code Metadata:
========================
Original URL: https://karak-node.network
Prompt: Write code to interact with Space and Time, the decentralized data warehouse in the Karak ecosystem, to retrieve sub-second ZK proofs for onchain and offchain data.
Generated: DETERMINISTIC_09b596ef495632f2
Batch ID: 20250612_154603
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.spaceandtime.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, Any, Optional

class SpaceAndTimeClient:
    """
    A client to interact with Space and Time decentralized data warehouse.
    Handles authentication, query execution, and proof retrieval.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the Space and Time client.
        
        Args:
            base_url: Base URL of the Space and Time API
            api_key: API key for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        })

    def execute_query(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a SQL query against Space and Time.
        
        Args:
            query: SQL query string
            parameters: Optional query parameters
            
        Returns:
            Dictionary containing query results
            
        Raises:
            SpaceAndTimeError: If query execution fails
        """
        endpoint = f"{self.base_url}/v1/query"
        payload = {
            "query": query,
            "parameters": parameters or {}
        }

        try:
            response = self.session.post(endpoint, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SpaceAndTimeError(f"Query execution failed: {str(e)}")

    def get_proof(self, query_id: str, proof_type: str = "zk") -> Dict[str, Any]:
        """
        Retrieve a ZK proof for a previously executed query.
        
        Args:
            query_id: ID of the executed query
            proof_type: Type of proof to retrieve (default: "zk")
            
        Returns:
            Dictionary containing proof data
            
        Raises:
            SpaceAndTimeError: If proof retrieval fails
        """
        endpoint = f"{self.base_url}/v1/proofs/{query_id}"
        params = {"type": proof_type}

        try:
            response = self.session.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SpaceAndTimeError(f"Proof retrieval failed: {str(e)}")

    def close(self):
        """Close the client session."""
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class SpaceAndTimeError(Exception):
    """Custom exception for Space and Time API errors."""
    pass


# Example usage
if __name__ == "__main__":
    # Initialize client (replace with actual credentials)
    client = SpaceAndTimeClient(
        base_url="https://api.spaceandtime.io",
        api_key="your_api_key_here"
    )

    try:
        # Execute a query
        query_result = client.execute_query(
            "SELECT * FROM your_table LIMIT 10"
        )
        print("Query results:", query_result)

        # Get proof for the query
        if 'queryId' in query_result:
            proof = client.get_proof(query_result['queryId'])
            print("Proof:", proof)

    except SpaceAndTimeError as e:
        print(f"Error: {str(e)}")
    finally:
        client.close()
```
