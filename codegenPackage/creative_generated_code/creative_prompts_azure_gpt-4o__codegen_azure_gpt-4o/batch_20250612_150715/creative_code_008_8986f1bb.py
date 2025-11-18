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
  "https://api.thegraph.com/subgraphs/name/moxie/example": {
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
# Guide for interacting with Moxie subgraphs and exploring contract data
# to track Fan Token activity and reward distributions.

import requests

class MoxieSubgraphClient:
    """
    A client for interacting with Moxie subgraphs to fetch contract data 
    and analyze Fan Token activity and reward distributions.
    """

    def __init__(self, endpoint_url: str):
        """
        Initializes the client with a specific subgraph endpoint URL.

        :param endpoint_url: The URL of the subgraph API endpoint.
        """
        if not endpoint_url.startswith("http"):
            raise ValueError("Invalid endpoint URL")
        self.endpoint_url = endpoint_url

    def query_subgraph(self, query: str) -> dict:
        """
        Sends a GraphQL query to the subgraph and retrieves the response.

        :param query: The GraphQL query string.
        :return: The JSON response from the subgraph as a Python dictionary.
        """
        try:
            response = requests.post(
                self.endpoint_url, 
                json={"query": query}
            )
            response.raise_for_status()
            data = response.json()
            if "errors" in data:
                raise Exception(f"Subgraph query error: {data['errors']}")
            return data.get("data", {})
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {e}")
        except Exception as e:
            raise Exception(f"Failed to query subgraph: {e}")

    def get_fan_token_activity(self, token_id: str) -> dict:
        """
        Fetches Fan Token activity for a given token ID from the subgraph.

        :param token_id: The ID of the Fan Token to analyze.
        :return: A dictionary containing the Fan Token activity data.
        """
        query = f"""
        {{
            fanToken(id: "{token_id}") {{
                id
                name
                symbol
                transactions {{
                    id
                    from
                    to
                    value
                    timestamp
                }}
                rewardDistributions {{
                    id
                    amount
                    recipient
                    timestamp
                }}
            }}
        }}
        """
        return self.query_subgraph(query)

    def get_all_fan_tokens(self) -> dict:
        """
        Fetches all Fan Tokens tracked by the subgraph.

        :return: A dictionary containing all Fan Token data.
        """
        query = """
        {
            fanTokens {
                id
                name
                symbol
            }
        }
        """
        return self.query_subgraph(query)

# Usage example:
if __name__ == "__main__":
    # Replace with the actual Moxie subgraph API endpoint URL
    endpoint_url = "https://api.thegraph.com/subgraphs/name/moxie/example"

    try:
        client = MoxieSubgraphClient(endpoint_url)
        
        # Fetch and print all Fan Tokens
        all_tokens = client.get_all_fan_tokens()
        print("All Fan Tokens:", all_tokens)

        # Example: Fetch activity for a specific Fan Token by ID
        token_id = "0x123456789abcdef"
        token_activity = client.get_fan_token_activity(token_id)
        print(f"Activity for token {token_id}:", token_activity)
    except Exception as e:
        print(f"Error: {e}")
```
