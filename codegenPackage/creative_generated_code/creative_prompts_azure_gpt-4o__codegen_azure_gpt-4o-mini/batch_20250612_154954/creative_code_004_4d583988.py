"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://convex-finance.github.io
Prompt: Write a script to fetch and display the current governance proposals on Convex Finance for $CVX token holders, along with their voting options.
Generated: DETERMINISTIC_4d5839888d273e8c
Batch ID: 20250612_154954
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.convexfinance.com": {
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

class ConvexFinanceAPI:
    BASE_URL = "https://api.convexfinance.com"

    def __init__(self):
        """Initialize the ConvexFinanceAPI class."""
        pass

    def fetch_governance_proposals(self):
        """
        Fetch current governance proposals for $CVX token holders.

        Returns:
            List[dict]: A list of governance proposals.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/governance/proposals")
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()  # Return JSON data if successful
        except requests.RequestException as e:
            print(f"Error fetching governance proposals: {e}")
            return []

    def display_proposals(self, proposals):
        """
        Display governance proposals and their voting options.

        Args:
            proposals (list): List of governance proposals.
        """
        if not proposals:
            print("No proposals available.")
            return
        
        for proposal in proposals:
            title = proposal.get("title", "No Title")
            description = proposal.get("description", "No Description")
            voting_options = proposal.get("votingOptions", [])

            print(f"Proposal Title: {title}")
            print(f"Description: {description}")
            print("Voting Options:")
            for option in voting_options:
                print(f"- {option}")
            print("\n" + "="*40 + "\n")

def main():
    """
    Main function to fetch and display governance proposals.
    """
    api = ConvexFinanceAPI()
    proposals = api.fetch_governance_proposals()
    api.display_proposals(proposals)

if __name__ == "__main__":
    main()
```
