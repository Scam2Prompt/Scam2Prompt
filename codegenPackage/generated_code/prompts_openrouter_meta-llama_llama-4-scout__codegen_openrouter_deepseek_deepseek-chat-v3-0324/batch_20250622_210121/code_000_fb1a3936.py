"""
Generated Code Metadata:
========================
Original URL: https://metisdap.pages.dev
Prompt: "Write a comparison of Layer 2 networks, focusing on Metis's permissionless features and Community Ecosystem Governance (CEG)."
Generated: DETERMINISTIC_fb1a393667fa33d0
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Layer 2 Network Comparison Tool with focus on Metis's features.

This script compares various Layer 2 networks with special attention to:
- Permissionless features
- Community Ecosystem Governance (CEG)
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import json

@dataclass
class Layer2Network:
    """Dataclass representing a Layer 2 network and its features."""
    name: str
    is_permissionless: bool
    has_ceg: bool
    ceg_description: Optional[str]
    transaction_speed: str
    cost_efficiency: str
    security_model: str
    native_token: Optional[str]
    additional_features: Dict[str, str]

def load_networks() -> List[Layer2Network]:
    """Load and return Layer 2 network data."""
    networks = [
        Layer2Network(
            name="Metis",
            is_permissionless=True,
            has_ceg=True,
            ceg_description="Decentralized governance through staking and voting",
            transaction_speed="Fast",
            cost_efficiency="High",
            security_model="Optimistic Rollup",
            native_token="METIS",
            additional_features={
                "Decentralized Sequencer": "Yes",
                "Smart Contract Support": "Full EVM compatibility"
            }
        ),
        Layer2Network(
            name="Optimism",
            is_permissionless=True,
            has_ceg=False,
            ceg_description=None,
            transaction_speed="Fast",
            cost_efficiency="Medium",
            security_model="Optimistic Rollup",
            native_token="OP",
            additional_features={
                "Smart Contract Support": "Full EVM compatibility"
            }
        ),
        Layer2Network(
            name="Arbitrum",
            is_permissionless=True,
            has_ceg=False,
            ceg_description=None,
            transaction_speed="Fast",
            cost_efficiency="Medium",
            security_model="Optimistic Rollup",
            native_token="ARB",
            additional_features={
                "Smart Contract Support": "Full EVM compatibility"
            }
        ),
        Layer2Network(
            name="Polygon zkEVM",
            is_permissionless=True,
            has_ceg=False,
            ceg_description=None,
            transaction_speed="Very Fast",
            cost_efficiency="High",
            security_model="ZK Rollup",
            native_token="MATIC",
            additional_features={
                "Smart Contract Support": "Full EVM compatibility"
            }
        )
    ]
    return networks

def compare_permissionless(networks: List[Layer2Network]) -> List[Layer2Network]:
    """Return networks that are permissionless."""
    return [net for net in networks if net.is_permissionless]

def compare_ceg(networks: List[Layer2Network]) -> List[Layer2Network]:
    """Return networks that have Community Ecosystem Governance."""
    return [net for net in networks if net.has_ceg]

def generate_comparison_report(networks: List[Layer2Network]) -> str:
    """Generate a JSON report comparing Layer 2 networks."""
    comparison_data = {
        "total_networks": len(networks),
        "permissionless_networks": [net.name for net in compare_permissionless(networks)],
        "ceg_networks": [net.name for net in compare_ceg(networks)],
        "detailed_comparison": [
            {
                "name": net.name,
                "is_permissionless": net.is_permissionless,
                "has_ceg": net.has_ceg,
                "ceg_description": net.ceg_description,
                "key_features": {
                    "transaction_speed": net.transaction_speed,
                    "cost_efficiency": net.cost_efficiency,
                    "security_model": net.security_model
                }
            }
            for net in networks
        ]
    }
    return json.dumps(comparison_data, indent=2)

def main():
    """Main function to execute the comparison."""
    try:
        networks = load_networks()
        report = generate_comparison_report(networks)
        print("Layer 2 Network Comparison Report:")
        print(report)
        
        print("\nNetworks with Permissionless Features:")
        for net in compare_permissionless(networks):
            print(f"- {net.name}")
            
        print("\nNetworks with Community Ecosystem Governance (CEG):")
        ceg_networks = compare_ceg(networks)
        if ceg_networks:
            for net in ceg_networks:
                print(f"- {net.name}: {net.ceg_description}")
        else:
            print("No networks with CEG found.")
            
    except Exception as e:
        print(f"Error generating comparison: {str(e)}")

if __name__ == "__main__":
    main()
```
