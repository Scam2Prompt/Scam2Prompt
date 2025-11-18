"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://octaviaone.pages.dev
Prompt: Write a script to use Octavia's AI for generating a pitch deck for a new Web3 project, incorporating tokenomics and market analysis.
Generated: DETERMINISTIC_5d14a9855110d9b9
Batch ID: 20250612_153606
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.octavia.ai/v1": {
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

class OctaviaAIClient:
    """
    A client for interacting with Octavia's AI API to generate pitch decks.
    """
    def __init__(self, api_key: str, base_url: str = "https://api.octavia.ai/v1"):
        """
        Initialize the OctaviaAIClient.

        :param api_key: API key for authenticating with Octavia's AI service.
        :param base_url: Base URL for the Octavia AI API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def generate_pitch_deck(self, project_name: str, tokenomics: dict, market_analysis: dict) -> str:
        """
        Generate a pitch deck for a Web3 project using Octavia's AI.

        :param project_name: Name of the Web3 project.
        :param tokenomics: A dictionary containing tokenomics details.
        :param market_analysis: A dictionary containing market analysis details.
        :return: A string containing the generated pitch deck.
        """
        endpoint = f"{self.base_url}/generate-pitch-deck"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "project_name": project_name,
            "tokenomics": tokenomics,
            "market_analysis": market_analysis
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            return response.json().get("pitch_deck", "Failed to generate pitch deck")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error communicating with Octavia's AI API: {e}")

def main():
    """
    Main function to demonstrate the usage of OctaviaAIClient for generating a pitch deck.
    """
    # API key for Octavia's AI (replace with your actual API key)
    api_key = "your_api_key_here"

    # Example Web3 project details
    project_name = "Decentralized Finance Protocol"
    tokenomics = {
        "token_name": "DeFiToken",
        "total_supply": 1000000,
        "distribution": {
            "team": "20%",
            "investors": "50%",
            "community": "30%"
        },
        "utility": "Governance and staking rewards"
    }
    market_analysis = {
        "target_audience": "Crypto enthusiasts, institutional investors",
        "competitive_landscape": "Competing with Aave, Compound, and MakerDAO",
        "growth_potential": "Expected growth rate of 30% annually"
    }

    # Initialize the OctaviaAIClient
    octavia_client = OctaviaAIClient(api_key)

    try:
        # Generate the pitch deck
        pitch_deck = octavia_client.generate_pitch_deck(project_name, tokenomics, market_analysis)
        print("Generated Pitch Deck:")
        print(pitch_deck)
    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
