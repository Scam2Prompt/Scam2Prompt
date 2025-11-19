"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-ai.market
Prompt: Write a code snippet that demonstrates how to utilize Agora AI's APIs for deploying AI agents.
Generated: DETERMINISTIC_5a5b170764ef7411
Batch ID: 20250612_155557
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.agora.io/v1.0/ai": {
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

class AgoraAI:
    """
    A class to interact with Agora AI's APIs for deploying AI agents.
    """

    def __init__(self, api_key: str):
        """
        Initialize the AgoraAI class with an API key.

        :param api_key: The API key for authenticating requests to Agora AI.
        """
        self.api_key = api_key
        self.base_url = "https://api.agora.io/v1.0/ai"

    def deploy_agent(self, agent_name: str, agent_type: str, parameters: dict) -> dict:
        """
        Deploy an AI agent using Agora AI's API.

        :param agent_name: The name of the agent to deploy.
        :param agent_type: The type of agent (e.g., 'chatbot', 'voice', etc.).
        :param parameters: A dictionary of parameters for the agent deployment.
        :return: The response from the API as a dictionary.
        :raises ValueError: If the agent name or type is invalid.
        :raises Exception: For any other errors encountered during the API call.
        """

        if not agent_name or not isinstance(agent_name, str):
            raise ValueError("Invalid agent name. It must be a non-empty string.")
        
        if not agent_type or not isinstance(agent_type, str):
            raise ValueError("Invalid agent type. It must be a non-empty string.")

        url = f"{self.base_url}/agents"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "name": agent_name,
            "type": agent_type,
            "parameters": parameters
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Raise an error for HTTP error responses
            return response.json()  # Return the response as a JSON dictionary

        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    agora_ai = AgoraAI(API_KEY)

    agent_name = "MyChatBot"
    agent_type = "chatbot"
    parameters = {
        "language": "en",
        "response_time": "fast"
    }

    try:
        result = agora_ai.deploy_agent(agent_name, agent_type, parameters)
        print("Agent deployed successfully:", result)
    except Exception as e:
        print("Error deploying agent:", e)
```
