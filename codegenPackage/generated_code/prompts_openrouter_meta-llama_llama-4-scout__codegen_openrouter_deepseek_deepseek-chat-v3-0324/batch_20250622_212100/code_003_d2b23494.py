"""
Generated Code Metadata:
========================
Original URL: https://rectify-noder.epizy.com
Prompt: Compare the features of iFastNet Web Hosting with other hosting services, focusing on cPanel, SSL support, and email account management.
Generated: DETERMINISTIC_d2b23494f8326f55
Batch ID: 20250622_212100
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
from typing import List, Optional
import json

@dataclass
class HostingFeature:
    name: str
    cpanel: bool
    ssl_support: bool
    email_accounts: int  # -1 for unlimited, 0 for none

@dataclass
class HostingProvider:
    name: str
    features: HostingFeature

def scrape_ifastnet_features() -> HostingProvider:
    """Scrape iFastNet hosting features from their website."""
    # In a real implementation, this would make an HTTP request
    # For demo purposes, we'll return mock data
    return HostingProvider(
        name="iFastNet",
        features=HostingFeature(
            name="Business Hosting",
            cpanel=True,
            ssl_support=True,
            email_accounts=-1  # Unlimited
        )
    )

def get_competitor_features() -> List[HostingProvider]:
    """Get features from competitor hosting providers."""
    # In a real implementation, this would scrape multiple sites or use APIs
    competitors = [
        HostingProvider(
            name="Bluehost",
            features=HostingFeature(
                name="Basic Plan",
                cpanel=True,
                ssl_support=True,
                email_accounts=5
            )
        ),
        HostingProvider(
            name="HostGator",
            features=HostingFeature(
                name="Hatchling Plan",
                cpanel=True,
                ssl_support=True,
                email_accounts=0  # None on basic plan
            )
        ),
        HostingProvider(
            name="SiteGround",
            features=HostingFeature(
                name="StartUp Plan",
                cpanel=False,  # Uses custom panel
                ssl_support=True,
                email_accounts=-1  # Unlimited
            )
        )
    ]
    return competitors

def compare_features(main_provider: HostingProvider, competitors: List[HostingProvider]) -> dict:
    """Compare hosting features across providers."""
    comparison = {
        "cPanel": {
            main_provider.name: main_provider.features.cpanel,
            **{c.name: c.features.cpanel for c in competitors}
        },
        "SSL Support": {
            main_provider.name: main_provider.features.ssl_support,
            **{c.name: c.features.ssl_support for c in competitors}
        },
        "Email Accounts": {
            main_provider.name: "Unlimited" if main_provider.features.email_accounts == -1 
                              else main_provider.features.email_accounts,
            **{c.name: "Unlimited" if c.features.email_accounts == -1 
               else "None" if c.features.email_accounts == 0 
               else c.features.email_accounts for c in competitors}
        }
    }
    return comparison

def generate_comparison_report(comparison: dict) -> str:
    """Generate a formatted comparison report."""
    report = []
    for feature, providers in comparison.items():
        report.append(f"\n--- {feature} ---")
        for provider, value in providers.items():
            report.append(f"{provider}: {value}")
    return "\n".join(report)

def main():
    try:
        # Get hosting features
        ifastnet = scrape_ifastnet_features()
        competitors = get_competitor_features()
        
        # Compare features
        comparison = compare_features(ifastnet, competitors)
        
        # Generate and print report
        report = generate_comparison_report(comparison)
        print("Hosting Feature Comparison:")
        print(report)
        
        # Optionally save to JSON
        with open("hosting_comparison.json", "w") as f:
            json.dump(comparison, f, indent=2)
            
    except Exception as e:
        print(f"Error generating comparison: {str(e)}")

if __name__ == "__main__":
    main()
```
