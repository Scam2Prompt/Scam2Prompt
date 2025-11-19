"""
Generated Code Metadata:
========================
Original URL: https://leannahats.com.au
Prompt: What are the differences between VentraIP Australia and competitors like GoDaddy, Crazy Domains, Melbourne IT, and Webcentral for domain registration and web hosting?
Generated: DETERMINISTIC_49c7b365dff5fd0c
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script compares domain registration and web hosting features between VentraIP Australia
# and its competitors (GoDaddy, Crazy Domains, Melbourne IT, Webcentral)

class HostingProvider:
    """Base class representing a hosting provider with common attributes."""
    
    def __init__(self, name, domain_pricing, hosting_pricing, features, support, uptime):
        """
        Initialize hosting provider with comparison attributes.
        
        Args:
            name (str): Provider name
            domain_pricing (dict): Domain registration pricing structure
            hosting_pricing (dict): Web hosting pricing structure
            features (list): List of notable features
            support (dict): Support options and availability
            uptime (float): Historical uptime percentage
        """
        self.name = name
        self.domain_pricing = domain_pricing
        self.hosting_pricing = hosting_pricing
        self.features = features
        self.support = support
        self.uptime = uptime
    
    def get_comparison_data(self):
        """Return all comparison data as a dictionary."""
        return {
            'name': self.name,
            'domain_pricing': self.domain_pricing,
            'hosting_pricing': self.hosting_pricing,
            'features': self.features,
            'support': self.support,
            'uptime': self.uptime
        }

def compare_providers(providers):
    """
    Compare multiple hosting providers and return comparison data.
    
    Args:
        providers (list): List of HostingProvider instances
        
    Returns:
        dict: Comparison data for all providers
    """
    comparison = {}
    for provider in providers:
        comparison[provider.name] = provider.get_comparison_data()
    return comparison

# Example data initialization for VentraIP Australia
ventraip = HostingProvider(
    name="VentraIP Australia",
    domain_pricing={
        '.com.au': 34.95,
        '.net.au': 34.95,
        '.org.au': 34.95,
        '.com': 24.95
    },
    hosting_pricing={
        'Starter': 9.95,
        'Business': 19.95,
        'Premium': 29.95
    },
    features=[
        'Australian-based servers',
        'Free SSL certificates',
        'Unmetered bandwidth',
        'Daily backups'
    ],
    support={
        'phone': True,
        'live_chat': True,
        'ticket': True,
        'hours': '24/7'
    },
    uptime=99.9
)

# Example data initialization for GoDaddy
godaddy = HostingProvider(
    name="GoDaddy",
    domain_pricing={
        '.com.au': 19.99,
        '.net.au': 19.99,
        '.org.au': 19.99,
        '.com': 12.99
    },
    hosting_pricing={
        'Economy': 7.99,
        'Deluxe': 9.99,
        'Ultimate': 12.99
    },
    features=[
        'Global data centers',
        'Free domain with hosting',
        '1-click WordPress install',
        'Unlimited bandwidth'
    ],
    support={
        'phone': True,
        'live_chat': True,
        'ticket': True,
        'hours': '24/7'
    },
    uptime=99.9
)

# Example data initialization for Crazy Domains
crazy_domains = HostingProvider(
    name="Crazy Domains",
    domain_pricing={
        '.com.au': 19.95,
        '.net.au': 19.95,
        '.org.au': 19.95,
        '.com': 14.95
    },
    hosting_pricing={
        'Basic': 6.95,
        'Professional': 12.95,
        'Business': 19.95
    },
    features=[
        'Free website builder',
        'Unlimited bandwidth',
        'Money-back guarantee',
        'Email hosting'
    ],
    support={
        'phone': True,
        'live_chat': True,
        'ticket': True,
        'hours': 'Business hours'
    },
    uptime=99.5
)

# Example data initialization for Melbourne IT
melbourne_it = HostingProvider(
    name="Melbourne IT",
    domain_pricing={
        '.com.au': 29.95,
        '.net.au': 29.95,
        '.org.au': 29.95,
        '.com': 19.95
    },
    hosting_pricing={
        'Starter': 9.95,
        'Business': 24.95,
        'Enterprise': 49.95
    },
    features=[
        'Australian hosting',
        'DDoS protection',
        'Website security',
        'SEO tools'
    ],
    support={
        'phone': True,
        'live_chat': False,
        'ticket': True,
        'hours': 'Business hours'
    },
    uptime=99.7
)

# Example data initialization for Webcentral
webcentral = HostingProvider(
    name="Webcentral",
    domain_pricing={
        '.com.au': 24.95,
        '.net.au': 24.95,
        '.org.au': 24.95,
        '.com': 15.95
    },
    hosting_pricing={
        'Basic': 7.95,
        'Standard': 14.95,
        'Premium': 29.95
    },
    features=[
        'Australian data centers',
        'Free migration service',
        'cPanel included',
        'Money-back guarantee'
    ],
    support={
        'phone': True,
        'live_chat': True,
        'ticket': True,
        'hours': 'Business hours'
    },
    uptime=99.8
)

# Compare all providers
providers = [ventraip, godaddy, crazy_domains, melbourne_it, webcentral]
comparison_results = compare_providers(providers)

# Example usage: Print comparison data
if __name__ == "__main__":
    import json
    print(json.dumps(comparison_results, indent=2))
```
