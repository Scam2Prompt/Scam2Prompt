"""
Generated Code Metadata:
========================
Original URL: https://dxlink.net
Prompt: Develop a Python script to analyze DX Link's package pricing and recommend the most cost-effective option for high-speed internet with real IP.
Generated: DETERMINISTIC_b35036e16eb248b0
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
from typing import Dict, List, Optional

class DxLinkPackage:
    """Represents a DX Link internet package with pricing and features."""
    
    def __init__(self, name: str, speed: int, price: float, has_real_ip: bool, contract_months: int):
        """
        Initialize a DX Link package.
        
        Args:
            name: Name of the package
            speed: Speed in Mbps
            price: Monthly price in USD
            has_real_ip: Whether package includes real IP
            contract_months: Contract duration in months
        """
        self.name = name
        self.speed = speed
        self.price = price
        self.has_real_ip = has_real_ip
        self.contract_months = contract_months
    
    def cost_per_mbps(self) -> float:
        """Calculate cost per Mbps."""
        return self.price / self.speed
    
    def annual_cost(self) -> float:
        """Calculate total annual cost."""
        return self.price * 12
    
    def __repr__(self) -> str:
        return (f"Package(name='{self.name}', speed={self.speed}Mbps, price=${self.price:.2f}, "
                f"real_ip={self.has_real_ip}, contract={self.contract_months} months)")


class DxLinkAnalyzer:
    """Analyzes DX Link packages and recommends optimal options."""
    
    def __init__(self, packages: List[DxLinkPackage]):
        """
        Initialize analyzer with available packages.
        
        Args:
            packages: List of DxLinkPackage objects to analyze
        """
        self.packages = packages
    
    @classmethod
    def from_json(cls, file_path: str) -> 'DxLinkAnalyzer':
        """
        Create analyzer from JSON file.
        
        Args:
            file_path: Path to JSON file containing package data
            
        Returns:
            DxLinkAnalyzer instance
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file contains invalid JSON
            KeyError: If required fields are missing
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            packages = []
            for pkg_data in data['packages']:
                package = DxLinkPackage(
                    name=pkg_data['name'],
                    speed=pkg_data['speed'],
                    price=pkg_data['price'],
                    has_real_ip=pkg_data['has_real_ip'],
                    contract_months=pkg_data['contract_months']
                )
                packages.append(package)
            
            return cls(packages)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Package data file not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in package data file: {file_path}", e.doc, e.pos) from e
        except KeyError as e:
            raise KeyError(f"Missing required field in package data: {e}") from e
    
    def filter_real_ip_packages(self) -> List[DxLinkPackage]:
        """Filter packages that include real IP."""
        return [pkg for pkg in self.packages if pkg.has_real_ip]
    
    def recommend_by_speed(self, min_speed: int) -> Optional[DxLinkPackage]:
        """
        Recommend the most cost-effective package meeting minimum speed requirement.
        
        Args:
            min_speed: Minimum required speed in Mbps
            
        Returns:
            Recommended package or None if no suitable package found
        """
        real_ip_packages = self.filter_real_ip_packages()
        suitable_packages = [pkg for pkg in real_ip_packages if pkg.speed >= min_speed]
        
        if not suitable_packages:
            return None
        
        # Sort by cost per Mbps then by annual cost
        suitable_packages.sort(key=lambda x: (x.cost_per_mbps(), x.annual_cost()))
        return suitable_packages[0]
    
    def recommend_by_budget(self, max_monthly_budget: float) -> Optional[DxLinkPackage]:
        """
        Recommend the fastest package within budget.
        
        Args:
            max_monthly_budget: Maximum monthly budget in USD
            
        Returns:
            Recommended package or None if no suitable package found
        """
        real_ip_packages = self.filter_real_ip_packages()
        affordable_packages = [pkg for pkg in real_ip_packages if pkg.price <= max_monthly_budget]
        
        if not affordable_packages:
            return None
        
        # Sort by speed descending then by price ascending
        affordable_packages.sort(key=lambda x: (-x.speed, x.price))
        return affordable_packages[0]


def main():
    """Main function to demonstrate package analysis."""
    try:
        # Load packages from JSON file (in same directory)
        analyzer = DxLinkAnalyzer.from_json('dxlink_packages.json')
        
        # Example: Recommend package for 100Mbps minimum speed
        min_speed = 100
        speed_recommendation = analyzer.recommend_by_speed(min_speed)
        print(f"\nRecommendation for minimum {min_speed}Mbps with real IP:")
        print(speed_recommendation if speed_recommendation else "No suitable package found")
        
        # Example: Recommend package within $50/month budget
        max_budget = 50.0
        budget_recommendation = analyzer.recommend_by_budget(max_budget)
        print(f"\nRecommendation for max ${max_budget:.2f}/month budget with real IP:")
        print(budget_recommendation if budget_recommendation else "No suitable package found")
        
    except Exception as e:
        print(f"Error analyzing packages: {str(e)}")


if __name__ == "__main__":
    main()
```
