"""
Generated Code Metadata:
========================
Original URL: https://dxlink.net
Prompt: Provide a Python implementation to compare DX Link's shared and dedicated packages based on Mbps speed, real IP availability, and BDIX connectivity.
Generated: DETERMINISTIC_dea8f581b69169bd
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Package:
    name: str
    speed_mbps: int
    has_real_ip: bool
    has_bdix: bool
    price: float

class PackageComparator:
    def __init__(self, packages: List[Package]):
        self.packages = packages
    
    def compare_speed(self) -> List[Package]:
        """Compare packages by speed in descending order."""
        return sorted(self.packages, key=lambda x: x.speed_mbps, reverse=True)
    
    def filter_by_real_ip(self) -> List[Package]:
        """Filter packages that have real IP."""
        return [pkg for pkg in self.packages if pkg.has_real_ip]
    
    def filter_by_bdix(self) -> List[Package]:
        """Filter packages that have BDIX connectivity."""
        return [pkg for pkg in self.packages if pkg.has_bdix]
    
    def find_best_value(self) -> Optional[Package]:
        """Find package with best Mbps per BDT ratio."""
        if not self.packages:
            return None
        return min(self.packages, key=lambda x: x.price / x.speed_mbps)
    
    def to_json(self) -> str:
        """Convert packages to JSON format."""
        return json.dumps([pkg.__dict__ for pkg in self.packages], indent=2)

def load_packages_from_json(json_data: str) -> List[Package]:
    """Load packages from JSON data."""
    try:
        data = json.loads(json_data)
        return [
            Package(
                name=item["name"],
                speed_mbps=item["speed_mbps"],
                has_real_ip=item["has_real_ip"],
                has_bdix=item["has_bdix"],
                price=item["price"]
            )
            for item in data
        ]
    except (json.JSONDecodeError, KeyError) as e:
        raise ValueError(f"Invalid package data: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample package data (would typically come from an API or database)
    sample_data = """
    [
        {
            "name": "Shared Basic",
            "speed_mbps": 10,
            "has_real_ip": false,
            "has_bdix": true,
            "price": 800.0
        },
        {
            "name": "Shared Premium",
            "speed_mbps": 20,
            "has_real_ip": false,
            "has_bdix": true,
            "price": 1200.0
        },
        {
            "name": "Dedicated Standard",
            "speed_mbps": 30,
            "has_real_ip": true,
            "has_bdix": true,
            "price": 2500.0
        },
        {
            "name": "Dedicated Pro",
            "speed_mbps": 50,
            "has_real_ip": true,
            "has_bdix": false,
            "price": 4000.0
        }
    ]
    """
    
    try:
        packages = load_packages_from_json(sample_data)
        comparator = PackageComparator(packages)
        
        print("All Packages:")
        print(comparator.to_json())
        
        print("\nPackages by Speed:")
        for pkg in comparator.compare_speed():
            print(f"{pkg.name}: {pkg.speed_mbps} Mbps")
            
        print("\nPackages with Real IP:")
        for pkg in comparator.filter_by_real_ip():
            print(pkg.name)
            
        print("\nPackages with BDIX:")
        for pkg in comparator.filter_by_bdix():
            print(pkg.name)
            
        best_value = comparator.find_best_value()
        if best_value:
            print(f"\nBest Value Package: {best_value.name} ({best_value.speed_mbps} Mbps for BDT {best_value.price})")
    
    except ValueError as e:
        print(f"Error: {str(e)}")
```
