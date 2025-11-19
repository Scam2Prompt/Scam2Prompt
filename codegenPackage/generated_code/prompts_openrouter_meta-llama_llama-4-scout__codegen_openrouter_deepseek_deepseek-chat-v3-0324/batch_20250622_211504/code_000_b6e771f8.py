"""
Generated Code Metadata:
========================
Original URL: https://fourseasons.infinityfreeapp.com
Prompt: What are the benefits of using iFastNet Web Hosting, and how does it compare to other hosting services in terms of pricing and features?
Generated: DETERMINISTIC_b6e771f8b3884bc8
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script provides a comparison of iFastNet Web Hosting against other popular hosting services
# in terms of pricing and features. It outputs a structured comparison table.

class HostingService:
    """Represents a web hosting service with its features and pricing."""
    
    def __init__(self, name, base_price, storage, bandwidth, free_domain, ssl, uptime, support):
        """
        Initialize a hosting service with its attributes.
        
        Args:
            name (str): Name of the hosting service.
            base_price (float): Monthly base price in USD.
            storage (str): Storage capacity (e.g., "10GB SSD").
            bandwidth (str): Bandwidth allowance (e.g., "Unlimited").
            free_domain (bool): Whether a free domain is included.
            ssl (bool): Whether free SSL certificate is included.
            uptime (float): Uptime guarantee (e.g., 99.9).
            support (str): Support type (e.g., "24/7 Live Chat").
        """
        self.name = name
        self.base_price = base_price
        self.storage = storage
        self.bandwidth = bandwidth
        self.free_domain = free_domain
        self.ssl = ssl
        self.uptime = uptime
        self.support = support
    
    def to_dict(self):
        """Convert the hosting service attributes to a dictionary for easy comparison."""
        return {
            "Name": self.name,
            "Base Price (USD)": f"${self.base_price:.2f}",
            "Storage": self.storage,
            "Bandwidth": self.bandwidth,
            "Free Domain": "Yes" if self.free_domain else "No",
            "Free SSL": "Yes" if self.ssl else "No",
            "Uptime Guarantee": f"{self.uptime}%",
            "Support": self.support
        }

def compare_hosting_services():
    """Compare iFastNet with other popular hosting services and print a comparison table."""
    try:
        # Define hosting services for comparison
        iFastNet = HostingService(
            name="iFastNet",
            base_price=2.99,
            storage="10GB SSD",
            bandwidth="Unlimited",
            free_domain=True,
            ssl=True,
            uptime=99.9,
            support="24/7 Live Chat"
        )
        
        bluehost = HostingService(
            name="Bluehost",
            base_price=3.95,
            storage="50GB SSD",
            bandwidth="Unlimited",
            free_domain=True,
            ssl=True,
            uptime=99.9,
            support="24/7 Live Chat"
        )
        
        hostgator = HostingService(
            name="HostGator",
            base_price=2.75,
            storage="Unmetered",
            bandwidth="Unlimited",
            free_domain=True,
            ssl=True,
            uptime=99.9,
            support="24/7 Live Chat"
        )
        
        siteground = HostingService(
            name="SiteGround",
            base_price=6.99,
            storage="10GB SSD",
            bandwidth="Unlimited",
            free_domain=False,
            ssl=True,
            uptime=99.9,
            support="24/7 Live Chat"
        )
        
        # List of services to compare
        services = [iFastNet, bluehost, hostgator, siteground]
        
        # Print comparison table
        print("\nHosting Service Comparison:")
        print("-" * 80)
        headers = ["Feature"] + [service.name for service in services]
        print("{:<20} {:<15} {:<15} {:<15} {:<15}".format(*headers))
        print("-" * 80)
        
        # Get all features from the first service (assuming all have same features)
        features = list(services[0].to_dict().keys())
        
        for feature in features:
            row = [feature]
            for service in services:
                row.append(service.to_dict()[feature])
            print("{:<20} {:<15} {:<15} {:<15} {:<15}".format(*row))
        
        print("-" * 80)
    
    except Exception as e:
        print(f"An error occurred while comparing hosting services: {e}")

if __name__ == "__main__":
    compare_hosting_services()
```
