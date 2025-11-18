"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Create a guide for builders to interact with Moxie subgraphs and explore contract data to track Fan Token activity and reward distributions.
Generated: DETERMINISTIC_8986f1bb1d4c1f94
Batch ID: 20250612_150715
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/moxie/moxie-subgraph": {
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

class MoxieSubgraph:
    """A class to interact with Moxie's subgraph API for fetching Fan Token activities and reward distributions."""
    
    def __init__(self, subgraph_url):
        """
        Initializes the MoxieSubgraph with the specified subgraph URL.

        Args:
            subgraph_url (str): The URL for the Moxie subgraph API.
        """
        self.subgraph_url = subgraph_url

    def query(self, query_string):
        """
        Executes a GraphQL query against the Moxie subgraph.

        Args:
            query_string (str): The GraphQL query string to execute.

        Returns:
            dict: The JSON response from the subgraph API.

        Raises:
            Exception: If the API call fails or returns an error.
        """
        try:
            response = requests.post(
                self.subgraph_url,
                json={'query': query_string},
                headers={'Content-Type': 'application/json'}
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the parsed JSON response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error querying the subgraph: {e}")

    def get_fan_token_activity(self, token_id):
        """
        Fetches the activity data for a specific fan token.

        Args:
            token_id (str): The ID of the fan token.

        Returns:
            dict: The fan token activity data.

        Raises:
            Exception: If the query fails.
        """
        query = f"""
        {{
            fanToken(id: "{token_id}") {{
                id
                name
                totalSupply
                transactions {{
                    id
                    timestamp
                    from
                    to
                    value
                }}
            }}
        }}
        """
        data = self.query(query)
        return data.get('data', {}).get('fanToken', {})

    def get_reward_distributions(self, token_id):
        """
        Fetches the reward distribution data for a specific fan token.

        Args:
            token_id (str): The ID of the fan token.

        Returns:
            dict: The reward distribution data.

        Raises:
            Exception: If the query fails.
        """
        query = f"""
        {{
            fanToken(id: "{token_id}") {{
                id
                rewards {{
                    id
                    amount
                    recipient
                    distributionDate
                }}
            }}
        }}
        """
        data = self.query(query)
        return data.get('data', {}).get('fanToken', {}).get('rewards', [])

# Example usage
if __name__ == "__main__":
    SUBGRAPH_URL = "https://api.thegraph.com/subgraphs/name/moxie/moxie-subgraph"  # Replace with actual subgraph URL
    moxie = MoxieSubgraph(SUBGRAPH_URL)
    
    token_id = "your_fan_token_id_here"  # Replace with actual fan token ID

    try:
        activity = moxie.get_fan_token_activity(token_id)
        print("Fan Token Activity:", json.dumps(activity, indent=2))

        rewards = moxie.get_reward_distributions(token_id)
        print("Reward Distributions:", json.dumps(rewards, indent=2))
    except Exception as e:
        print("An error occurred:", e)
```
