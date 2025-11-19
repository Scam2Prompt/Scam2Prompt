"""
Generated Code Metadata:
========================
Original URL: https://story-docs.vercel.app
Prompt: What are the benefits of converting static IPs to programmable IPs using Story Protocol?
Generated: DETERMINISTIC_147cb772c39ea693
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates the benefits of converting static IPs to programmable IPs using Story Protocol
# through a simulated example of managing IP assets.

from typing import Dict, List, Optional
from dataclasses import dataclass
import json

@dataclass
class IPAsset:
    """Represents an intellectual property asset."""
    id: str
    name: str
    type: str
    metadata: Dict[str, str]
    is_programmable: bool = False
    license_terms: Optional[Dict[str, str]] = None

class StoryProtocolManager:
    """Manages IP assets with Story Protocol capabilities."""
    
    def __init__(self):
        self.assets: Dict[str, IPAsset] = {}
    
    def add_static_ip(self, asset_id: str, name: str, asset_type: str, metadata: Dict[str, str]) -> IPAsset:
        """Add a static IP asset to the manager."""
        asset = IPAsset(
            id=asset_id,
            name=name,
            type=asset_type,
            metadata=metadata
        )
        self.assets[asset_id] = asset
        return asset
    
    def convert_to_programmable(self, asset_id: str, license_terms: Dict[str, str]) -> IPAsset:
        """Convert a static IP to programmable using Story Protocol."""
        if asset_id not in self.assets:
            raise ValueError(f"Asset with ID {asset_id} not found")
        
        asset = self.assets[asset_id]
        asset.is_programmable = True
        asset.license_terms = license_terms
        return asset
    
    def create_derivative_work(self, original_id: str, new_id: str, new_name: str, modifications: Dict[str, str]) -> IPAsset:
        """Create a derivative work from a programmable IP asset."""
        if original_id not in self.assets:
            raise ValueError(f"Original asset with ID {original_id} not found")
        
        original = self.assets[original_id]
        if not original.is_programmable:
            raise ValueError("Original asset must be programmable to create derivatives")
        
        new_metadata = {**original.metadata, **modifications}
        derivative = IPAsset(
            id=new_id,
            name=new_name,
            type=original.type,
            metadata=new_metadata,
            is_programmable=True,
            license_terms=original.license_terms
        )
        self.assets[new_id] = derivative
        return derivative
    
    def get_royalty_info(self, asset_id: str) -> Dict[str, str]:
        """Get royalty information for a programmable IP asset."""
        if asset_id not in self.assets:
            raise ValueError(f"Asset with ID {asset_id} not found")
        
        asset = self.assets[asset_id]
        if not asset.is_programmable:
            raise ValueError("Asset must be programmable to have royalty information")
        
        return asset.license_terms or {}
    
    def list_assets(self) -> List[IPAsset]:
        """List all managed IP assets."""
        return list(self.assets.values())

# Example usage demonstrating the benefits
if __name__ == "__main__":
    manager = StoryProtocolManager()
    
    # Add a static IP
    static_ip = manager.add_static_ip(
        asset_id="ip1",
        name="Original Story",
        asset_type="literary",
        metadata={"author": "Jane Doe", "year": "2023"}
    )
    
    # Convert to programmable IP
    programmable_ip = manager.convert_to_programmable(
        asset_id="ip1",
        license_terms={
            "royalty_rate": "5%",
            "allowed_uses": "derivatives, commercial",
            "attribution_required": "yes"
        }
    )
    
    # Create derivative work
    derivative = manager.create_derivative_work(
        original_id="ip1",
        new_id="ip2",
        new_name="Movie Adaptation",
        modifications={"director": "John Smith", "year": "2024"}
    )
    
    # Get royalty information
    royalty_info = manager.get_royalty_info("ip2")
    
    # Output results
    print("Original IP:", static_ip)
    print("Programmable IP:", programmable_ip)
    print("Derivative Work:", derivative)
    print("Royalty Info:", royalty_info)
```
