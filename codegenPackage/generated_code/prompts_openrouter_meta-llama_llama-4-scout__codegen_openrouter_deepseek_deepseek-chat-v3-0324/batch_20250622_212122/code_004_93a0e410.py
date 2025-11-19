"""
Generated Code Metadata:
========================
Original URL: https://stellarterm.org
Prompt: Compare the features of StellarTerm with other Stellar network clients and provide a recommendation on which one to use for a specific use case.
Generated: DETERMINISTIC_93a0e410746ec48d
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, List, Optional

class StellarClientComparator:
    """
    Compares features of StellarTerm with other Stellar network clients.
    Provides recommendations based on specific use cases.
    """
    
    def __init__(self):
        self.clients = {
            'StellarTerm': {
                'features': ['User-friendly interface', 'Built-in wallet', 'DEX trading', 'No KYC'],
                'best_for': ['Beginners', 'Quick trades', 'Non-custodial use'],
                'limitations': ['Limited advanced features', 'Web-only']
            },
            'StellarX': {
                'features': ['Social features', 'DEX trading', 'Portfolio tracking', 'No KYC'],
                'best_for': ['Social trading', 'Community interaction'],
                'limitations': ['Requires email']
            },
            'Lobstr': {
                'features': ['Mobile app', 'DEX trading', 'Fiat onramps', 'Multi-currency support'],
                'best_for': ['Mobile users', 'Fiat purchases'],
                'limitations': ['Custodial option only']
            },
            'SolarWallet': {
                'features': ['Mobile app', 'Secure storage', 'Multi-account support', 'Hardware wallet support'],
                'best_for': ['Security-conscious users', 'Long-term holders'],
                'limitations': ['No built-in DEX']
            }
        }
    
    def get_client_features(self, client_name: str) -> Optional[Dict[str, List[str]]]:
        """
        Retrieve features for a specific Stellar client.
        
        Args:
            client_name: Name of the Stellar client
            
        Returns:
            Dictionary containing features, best_for, and limitations if found, else None
        """
        return self.clients.get(client_name)
    
    def compare_all_clients(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Get comparison data for all supported Stellar clients.
        
        Returns:
            Dictionary containing all clients and their features
        """
        return self.clients
    
    def recommend_client(self, use_case: str) -> List[str]:
        """
        Recommend Stellar clients based on a specific use case.
        
        Args:
            use_case: The intended use case for the Stellar client
            
        Returns:
            List of recommended clients sorted by relevance
        """
        recommendations = []
        
        for client, data in self.clients.items():
            if use_case.lower() in [x.lower() for x in data['best_for']]:
                recommendations.append(client)
        
        return recommendations
    
    def get_feature_comparison(self, feature: str) -> Dict[str, bool]:
        """
        Check which clients support a specific feature.
        
        Args:
            feature: The feature to check for
            
        Returns:
            Dictionary mapping clients to whether they support the feature
        """
        comparison = {}
        
        for client, data in self.clients.items():
            comparison[client] = feature.lower() in [f.lower() for f in data['features']]
        
        return comparison


# Example usage
if __name__ == "__main__":
    comparator = StellarClientComparator()
    
    # Get features for a specific client
    print("StellarTerm features:", comparator.get_client_features("StellarTerm"))
    
    # Compare all clients
    print("All clients comparison:", comparator.compare_all_clients())
    
    # Get recommendations for a use case
    print("Recommended clients for beginners:", comparator.recommend_client("beginners"))
    
    # Check which clients support mobile apps
    print("Mobile support comparison:", comparator.get_feature_comparison("Mobile app"))
```
