"""
Generated Code Metadata:
========================
Original URL: https://bitsmix.biz
Prompt: Write a Python code snippet to track and analyze the funding rounds of Web3 startups, similar to the ones featured on STARTUP LOG, using APIs from Crunchbase or PitchBook.
Generated: DETERMINISTIC_609a4a8b98b5ff5e
Batch ID: 20250622_204855
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.crunchbase.com/api/v4/": {
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
import pandas as pd
from typing import Dict, List, Optional
from datetime import datetime
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Web3StartupTracker:
    """
    A class to track and analyze funding rounds of Web3 startups using Crunchbase API.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the tracker with API key.
        
        Args:
            api_key (str): Crunchbase API key
        """
        self.api_key = api_key
        self.base_url = "https://api.crunchbase.com/api/v4/"
        self.headers = {
            "X-cb-user-key": self.api_key,
            "accept": "application/json"
        }
        
    def _make_api_request(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Dict]:
        """
        Make a request to the Crunchbase API.
        
        Args:
            endpoint (str): API endpoint
            params (Dict, optional): Query parameters. Defaults to None.
            
        Returns:
            Optional[Dict]: JSON response if successful, None otherwise
        """
        try:
            response = requests.get(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            return None
    
    def get_web3_startups(self, limit: int = 100) -> Optional[List[Dict]]:
        """
        Get a list of Web3 startups from Crunchbase.
        
        Args:
            limit (int, optional): Number of results to return. Defaults to 100.
            
        Returns:
            Optional[List[Dict]]: List of startup data if successful, None otherwise
        """
        params = {
            "query": {
                "field_ids": ["category_groups"],
                "operator_id": "includes",
                "type": "predicate",
                "values": ["blockchain"]  # Using blockchain as proxy for Web3
            },
            "limit": limit,
            "field_ids": [
                "identifier",
                "short_description",
                "funding_stage",
                "funding_total",
                "num_funding_rounds",
                "founded_on"
            ]
        }
        
        response = self._make_api_request("searches/organizations", params)
        if response and "entities" in response:
            return response["entities"]
        return None
    
    def get_funding_rounds(self, organization_id: str) -> Optional[List[Dict]]:
        """
        Get funding rounds for a specific organization.
        
        Args:
            organization_id (str): Crunchbase organization ID
            
        Returns:
            Optional[List[Dict]]: List of funding rounds if successful, None otherwise
        """
        endpoint = f"entities/organizations/{organization_id}/cards/funding_rounds"
        response = self._make_api_request(endpoint)
        if response and "cards" in response:
            return response["cards"]
        return None
    
    def analyze_funding_rounds(self, funding_rounds: List[Dict]) -> Dict:
        """
        Analyze funding rounds data.
        
        Args:
            funding_rounds (List[Dict]): List of funding rounds
            
        Returns:
            Dict: Analysis results including total funding, average round, etc.
        """
        if not funding_rounds:
            return {}
            
        df = pd.DataFrame(funding_rounds)
        
        # Convert money to numeric values
        df['money_raised'] = df['money_raised'].apply(
            lambda x: float(x['value_usd']) if x and 'value_usd' in x else 0.0
        )
        
        analysis = {
            "total_funding": df['money_raised'].sum(),
            "average_round": df['money_raised'].mean(),
            "max_round": df['money_raised'].max(),
            "min_round": df['money_raised'].min(),
            "round_count": len(funding_rounds),
            "round_types": df['announced_on'].value_counts().to_dict(),
            "recent_round": df.sort_values('announced_on', ascending=False).iloc[0].to_dict()
        }
        
        return analysis
    
    def generate_report(self, startups: List[Dict], output_dir: str = "reports") -> str:
        """
        Generate a report of Web3 startup funding analysis.
        
        Args:
            startups (List[Dict]): List of startup data
            output_dir (str, optional): Directory to save report. Defaults to "reports".
            
        Returns:
            str: Path to the generated report
        """
        if not startups:
            logger.warning("No startup data to generate report")
            return ""
            
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(output_dir, f"web3_funding_report_{timestamp}.csv")
        
        report_data = []
        
        for startup in startups:
            org_id = startup.get('identifier', {}).get('uuid', '')
            funding_rounds = self.get_funding_rounds(org_id)
            analysis = self.analyze_funding_rounds(funding_rounds)
            
            report_data.append({
                "name": startup.get('identifier', {}).get('value', ''),
                "description": startup.get('short_description', ''),
                "founded_on": startup.get('founded_on', ''),
                "funding_stage": startup.get('funding_stage', ''),
                "total_funding": analysis.get('total_funding', 0),
                "round_count": analysis.get('round_count', 0),
                "average_round": analysis.get('average_round', 0),
                "recent_round_date": analysis.get('recent_round', {}).get('announced_on', ''),
                "recent_round_amount": analysis.get('recent_round', {}).get('money_raised', 0)
            })
            
        df = pd.DataFrame(report_data)
        df.to_csv(report_path, index=False)
        
        logger.info(f"Report generated at: {report_path}")
        return report_path

# Example usage
if __name__ == "__main__":
    API_KEY = "your_crunchbase_api_key_here"  # Replace with actual API key
    
    tracker = Web3StartupTracker(API_KEY)
    
    # Get Web3 startups
    web3_startups = tracker.get_web3_startups(limit=50)
    
    if web3_startups:
        # Generate and save report
        report_path = tracker.generate_report(web3_startups)
        
        if report_path:
            print(f"Successfully generated report at: {report_path}")
        else:
            print("Failed to generate report")
    else:
        print("No Web3 startups found or API request failed")
```
