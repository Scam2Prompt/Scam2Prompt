"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Write Python code to analyze grant funding opportunities, applying methods from PDMA's Grant Writing Professional course.
Generated: DETERMINISTIC_661558765b5ccca8
Batch ID: 20250612_145730
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/grants": {
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
from typing import List, Dict

class GrantFundingAnalyzer:
    """
    A class to analyze grant funding opportunities and apply methods from PDMA's Grant Writing Professional course.
    """
    
    def __init__(self, api_url: str, keywords: List[str]):
        """
        Initializes the GrantFundingAnalyzer.

        :param api_url: The URL of the grant funding opportunities API.
        :param keywords: A list of keywords to filter grant opportunities.
        """
        self.api_url = api_url
        self.keywords = keywords

    def fetch_grant_opportunities(self) -> List[Dict]:
        """
        Fetches grant opportunities from the API.

        :return: A list of grant opportunities.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            grants = response.json()
            return grants
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error fetching grant opportunities: {e}")
        except json.JSONDecodeError:
            raise RuntimeError("Failed to decode response as JSON.")

    def filter_grants_by_keywords(self, grants: List[Dict]) -> List[Dict]:
        """
        Filters grant opportunities based on the provided keywords.

        :param grants: A list of grant opportunities.
        :return: A list of filtered grant opportunities.
        """
        filtered_grants = [
            grant for grant in grants
            if any(keyword.lower() in (grant.get("description", "").lower() + grant.get("title", "").lower())
                   for keyword in self.keywords)
        ]
        return filtered_grants

    def rank_grants_by_funding_amount(self, grants: List[Dict]) -> List[Dict]:
        """
        Ranks grant opportunities by funding amount in descending order.

        :param grants: A list of grant opportunities.
        :return: A list of grant opportunities ranked by funding amount.
        """
        return sorted(grants, key=lambda grant: grant.get("funding_amount", 0), reverse=True)

    def analyze_grants(self) -> List[Dict]:
        """
        Fetches, filters, and ranks grant opportunities.

        :return: A list of ranked grant opportunities.
        """
        grants = self.fetch_grant_opportunities()
        filtered_grants = self.filter_grants_by_keywords(grants)
        ranked_grants = self.rank_grants_by_funding_amount(filtered_grants)
        return ranked_grants


def main():
    """
    Main function to execute the GrantFundingAnalyzer workflow.
    """
    # Replace with the actual API URL
    api_url = "https://api.example.com/grants"
    
    # Keywords for filtering grants
    keywords = ["education", "technology", "health"]
    
    # Initialize the analyzer
    analyzer = GrantFundingAnalyzer(api_url, keywords)
    
    try:
        # Analyze grant opportunities
        ranked_grants = analyzer.analyze_grants()
        
        # Output the analysis results
        print("Top grant opportunities:")
        for i, grant in enumerate(ranked_grants[:5], 1):  # Show top 5 grants
            print(f"{i}. Title: {grant.get('title', 'N/A')}, Funding Amount: ${grant.get('funding_amount', 'N/A')}")
    except RuntimeError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
