"""
Generated Code Metadata:
========================
Original URL: https://curve.fr
Prompt: Develop a simple program to compare the costs of buying and renewing domain names through different registrars (e.g., GoDaddy, OVH, IONOS, Gandi) and a marketplace like Boischaut, considering factors like transfer fees and annual renewal costs.
Generated: DETERMINISTIC_3809d73937f4ef99
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List, Dict, Optional
import json
import sys

@dataclass
class DomainPrice:
    registrar: str
    domain: str
    initial_price: float
    renewal_price: float
    transfer_price: float
    currency: str = "USD"

class DomainComparator:
    """
    A class to compare domain prices across different registrars and marketplaces.
    """
    
    def __init__(self):
        self.registrars = {
            "GoDaddy": self._scrape_godaddy,
            "OVH": self._scrape_ovh,
            "IONOS": self._scrape_ionos,
            "Gandi": self._scrape_gandi,
            "Boischaut": self._scrape_boischaut
        }
    
    def compare_prices(self, domain: str) -> List[DomainPrice]:
        """
        Compare prices for a given domain across all registrars.
        
        Args:
            domain: The domain name to compare prices for (e.g., "example.com")
            
        Returns:
            List of DomainPrice objects containing pricing information
        """
        results = []
        
        for registrar_name, scraper_func in self.registrars.items():
            try:
                price_info = scraper_func(domain)
                if price_info:
                    results.append(price_info)
            except Exception as e:
                print(f"Error scraping {registrar_name}: {str(e)}", file=sys.stderr)
        
        return results
    
    def _scrape_godaddy(self, domain: str) -> Optional[DomainPrice]:
        """Scrape GoDaddy pricing information."""
        # Note: This is a mock implementation. In production, you'd need to:
        # 1. Handle actual API calls or web scraping
        # 2. Respect robots.txt and terms of service
        # 3. Implement proper rate limiting
        
        # Mock data - replace with actual scraping logic
        return DomainPrice(
            registrar="GoDaddy",
            domain=domain,
            initial_price=11.99,
            renewal_price=19.99,
            transfer_price=9.99
        )
    
    def _scrape_ovh(self, domain: str) -> Optional[DomainPrice]:
        """Scrape OVH pricing information."""
        # Mock data
        return DomainPrice(
            registrar="OVH",
            domain=domain,
            initial_price=12.99,
            renewal_price=15.99,
            transfer_price=8.99
        )
    
    def _scrape_ionos(self, domain: str) -> Optional[DomainPrice]:
        """Scrape IONOS pricing information."""
        # Mock data
        return DomainPrice(
            registrar="IONOS",
            domain=domain,
            initial_price=1.00,
            renewal_price=17.00,
            transfer_price=10.00
        )
    
    def _scrape_gandi(self, domain: str) -> Optional[DomainPrice]:
        """Scrape Gandi pricing information."""
        # Mock data
        return DomainPrice(
            registrar="Gandi",
            domain=domain,
            initial_price=15.00,
            renewal_price=15.00,
            transfer_price=10.50
        )
    
    def _scrape_boischaut(self, domain: str) -> Optional[DomainPrice]:
        """Scrape Boischaut marketplace pricing information."""
        # Mock data
        return DomainPrice(
            registrar="Boischaut",
            domain=domain,
            initial_price=50.00,  # Marketplace purchase price
            renewal_price=15.00,  # Assuming renewal through registrar
            transfer_price=0.00   # Transfer fee might be included in purchase
        )

def display_results(results: List[DomainPrice]):
    """Display comparison results in a readable format."""
    if not results:
        print("No pricing information available.")
        return
    
    print("\nDomain Price Comparison Results:")
    print("-" * 60)
    print(f"{'Registrar':<15} {'Initial':>10} {'Renewal':>10} {'Transfer':>10} {'Total 1st Year':>15}")
    print("-" * 60)
    
    for price in results:
        total_first_year = price.initial_price + price.transfer_price
        print(f"{price.registrar:<15} {price.initial_price:>10.2f} {price.renewal_price:>10.2f} "
              f"{price.transfer_price:>10.2f} {total_first_year:>15.2f} {price.currency}")
    
    print("-" * 60)

def main():
    """Main function to handle user input and display results."""
    if len(sys.argv) != 2:
        print("Usage: python domain_comparator.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    comparator = DomainComparator()
    
    try:
        results = comparator.compare_prices(domain)
        display_results(results)
        
        # Optionally save results to JSON
        with open(f"domain_prices_{domain}.json", "w") as f:
            json.dump([r.__dict__ for r in results], f, indent=2)
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
