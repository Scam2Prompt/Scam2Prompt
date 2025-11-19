"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: Compare the features of LiteSpeed Web Server with other popular web servers.
Generated: DETERMINISTIC_e47c87e9cc788179
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A script to compare LiteSpeed Web Server features with other popular web servers.
"""

import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class WebServerFeature:
    """Dataclass to represent a web server feature."""
    name: str
    description: str
    supported: bool

@dataclass
class WebServerComparison:
    """Dataclass to represent web server comparison data."""
    server_name: str
    features: List[WebServerFeature]

def load_comparison_data() -> Dict[str, WebServerComparison]:
    """Load web server comparison data from a JSON file."""
    try:
        with open('web_server_comparison.json', 'r') as file:
            data = json.load(file)
            return {
                server: WebServerComparison(
                    server_name=server,
                    features=[
                        WebServerFeature(
                            name=feature['name'],
                            description=feature['description'],
                            supported=feature['supported']
                        ) for feature in features
                    ]
                )
                for server, features in data.items()
            }
    except FileNotFoundError:
        raise FileNotFoundError("Comparison data file not found.")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in comparison data file.")

def compare_servers(server1: str, server2: str, comparison_data: Dict[str, WebServerComparison]) -> None:
    """Compare features between two web servers."""
    try:
        server1_data = comparison_data[server1]
        server2_data = comparison_data[server2]
        
        print(f"\nComparing {server1} vs {server2}:\n")
        print(f"{'Feature':<30} {server1:<15} {server2:<15}")
        print("-" * 60)
        
        # Get all unique feature names
        all_features = set()
        for feature in server1_data.features:
            all_features.add(feature.name)
        for feature in server2_data.features:
            all_features.add(feature.name)
            
        for feature_name in sorted(all_features):
            # Find feature in each server
            server1_feature = next((f for f in server1_data.features if f.name == feature_name), None)
            server2_feature = next((f for f in server2_data.features if f.name == feature_name), None)
            
            # Get support status
            server1_support = "Yes" if server1_feature and server1_feature.supported else "No"
            server2_support = "Yes" if server2_feature and server2_feature.supported else "No"
            
            print(f"{feature_name:<30} {server1_support:<15} {server2_support:<15}")
            
    except KeyError as e:
        raise ValueError(f"Server {e} not found in comparison data.")

def main():
    """Main function to execute the comparison."""
    try:
        comparison_data = load_comparison_data()
        
        # Example comparison
        compare_servers("LiteSpeed", "Apache", comparison_data)
        compare_servers("LiteSpeed", "Nginx", comparison_data)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Note: This code expects a JSON file named `web_server_comparison.json` with the following structure:
```json
{
    "LiteSpeed": [
        {"name": "HTTP/3 Support", "description": "Supports HTTP/3 protocol", "supported": true},
        {"name": "Apache Compatibility", "description": "Compatible with Apache configurations", "supported": true}
    ],
    "Apache": [
        {"name": "HTTP/3 Support", "description": "Supports HTTP/3 protocol", "supported": false},
        {"name": "Apache Compatibility", "description": "Compatible with Apache configurations", "supported": true}
    ],
    "Nginx": [
        {"name": "HTTP/3 Support", "description": "Supports HTTP/3 protocol", "supported": true},
        {"name": "Apache Compatibility", "description": "Compatible with Apache configurations", "supported": false}
    ]
}
```
