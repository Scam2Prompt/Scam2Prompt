"""
Generated Code Metadata:
========================
Original URL: https://defillama-app.github.io
Prompt: Write a function that retrieves and analyzes hack/exploit history data from DefiLlama for security audits.
Generated: DETERMINISTIC_b7454edfb0bce18c
Batch ID: 20250612_155650
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi": {
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

class DefiLlamaHackAnalyzer:
    """
    A class to retrieve and analyze hack/exploit history data from DefiLlama.
    """
    
    def __init__(self):
        self.base_url = "https://api.llama.fi"
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "DefiLlamaHackAnalyzer/1.0",
            "Accept": "application/json"
        })
    
    def _make_request(self, endpoint: str) -> Dict:
        """
        Internal method to make API requests to DefiLlama.
        
        Args:
            endpoint: API endpoint to request
            
        Returns:
            JSON response as dictionary
            
        Raises:
            requests.exceptions.RequestException: If request fails
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def get_hack_history(self) -> List[Dict]:
        """
        Retrieves historical hack/exploit data from DefiLlama.
        
        Returns:
            List of hack events with details
        """
        endpoint = "/hacks"
        data = self._make_request(endpoint)
        return data.get("hacks", [])
    
    def analyze_hacks(self, hacks: List[Dict]) -> Dict[str, float]:
        """
        Analyzes hack data to calculate key statistics.
        
        Args:
            hacks: List of hack events
            
        Returns:
            Dictionary with analysis results
        """
        if not hacks:
            return {}
        
        df = pd.DataFrame(hacks)
        
        # Convert amounts to numeric and dates to datetime
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        
        # Calculate statistics
        analysis = {
            'total_hacks': len(df),
            'total_amount_lost': df['amount'].sum(),
            'avg_amount_per_hack': df['amount'].mean(),
            'median_amount': df['amount'].median(),
            'max_single_hack': df['amount'].max(),
            'min_single_hack': df['amount'].min(),
            'hacks_last_year': len(df[df['date'] > (datetime.now() - pd.DateOffset(years=1))]),
            'top_protocols': df['protocol'].value_counts().head(5).to_dict()
        }
        
        return analysis
    
    def get_protocol_hacks(self, protocol: str) -> Optional[List[Dict]]:
        """
        Retrieves hack history for a specific protocol.
        
        Args:
            protocol: Protocol name to search for
            
        Returns:
            List of hack events for the protocol or None if not found
        """
        hacks = self.get_hack_history()
        protocol_hacks = [h for h in hacks if h.get('protocol', '').lower() == protocol.lower()]
        return protocol_hacks if protocol_hacks else None
    
    def generate_report(self, analysis: Dict) -> str:
        """
        Generates a human-readable security report from analysis data.
        
        Args:
            analysis: Analysis dictionary from analyze_hacks()
            
        Returns:
            Formatted report string
        """
        report = []
        report.append("=== DeFi Security Audit Report ===")
        report.append(f"Total hacks analyzed: {analysis.get('total_hacks', 0):,}")
        report.append(f"Total amount lost: ${analysis.get('total_amount_lost', 0):,.2f}")
        report.append(f"Average amount per hack: ${analysis.get('avg_amount_per_hack', 0):,.2f}")
        report.append(f"Median hack amount: ${analysis.get('median_amount', 0):,.2f}")
        report.append(f"Largest single hack: ${analysis.get('max_single_hack', 0):,.2f}")
        report.append(f"Smallest single hack: ${analysis.get('min_single_hack', 0):,.2f}")
        report.append(f"Hacks in last year: {analysis.get('hacks_last_year', 0):,}")
        
        report.append("\nTop 5 most hacked protocols:")
        for protocol, count in analysis.get('top_protocols', {}).items():
            report.append(f"- {protocol}: {count} hacks")
            
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    analyzer = DefiLlamaHackAnalyzer()
    try:
        hacks = analyzer.get_hack_history()
        analysis = analyzer.analyze_hacks(hacks)
        report = analyzer.generate_report(analysis)
        print(report)
        
        # Example protocol lookup
        eth_hacks = analyzer.get_protocol_hacks("ethereum")
        if eth_hacks:
            print(f"\nFound {len(eth_hacks)} hacks on Ethereum")
    except Exception as e:
        print(f"Error: {str(e)}")
```
