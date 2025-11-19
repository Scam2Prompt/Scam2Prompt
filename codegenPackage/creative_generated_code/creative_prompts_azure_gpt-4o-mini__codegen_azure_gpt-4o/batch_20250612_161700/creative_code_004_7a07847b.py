"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://africafoodiesindustries.com
Prompt: How can I use a library to manage domain expiration checks and automate renewals for web hosting services?
Generated: DETERMINISTIC_7a07847bd59e8ba1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging
from typing import Dict, Optional

# Simulated library for domain management (example purposes)
class DomainManager:
    def __init__(self):
        self.domains = {}

    def add_domain(self, domain_name: str, expiry_date: datetime.date):
        """Add a domain with its expiration date."""
        self.domains[domain_name] = expiry_date

    def check_expiration(self, domain_name: str) -> Optional[datetime.date]:
        """Check the expiration date of a domain."""
        return self.domains.get(domain_name)

    def renew_domain(self, domain_name: str) -> bool:
        """Renew the domain registration by extending the expiration date."""
        if domain_name not in self.domains:
            return False
        self.domains[domain_name] = self.domains[domain_name] + datetime.timedelta(days=365)
        return True


# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def manage_domains(domain_manager: DomainManager, domains: Dict[str, datetime.date]):
    """
    Check the expiration dates of provided domains and renew those that are close to expiration.
    
    :param domain_manager: An instance of DomainManager.
    :param domains: A dictionary of domains and their expiration dates.
    """
    for domain_name, expiry_date in domains.items():
        try:
            # Add the domain to the manager
            domain_manager.add_domain(domain_name, expiry_date)
            
            # Check expiration
            expiration = domain_manager.check_expiration(domain_name)
            if expiration is None:
                logging.error(f"Domain '{domain_name}' not found in manager.")
                continue
            
            # Calculate days until expiration
            remaining_days = (expiration - datetime.date.today()).days
            logging.info(f"Domain '{domain_name}' expires in {remaining_days} days.")

            # Renew if less than 30 days remaining
            if remaining_days <= 30:
                success = domain_manager.renew_domain(domain_name)
                if success:
                    logging.info(f"Domain '{domain_name}' successfully renewed. New expiration: {domain_manager.check_expiration(domain_name)}")
                else:
                    logging.error(f"Failed to renew domain '{domain_name}'.")
        except Exception as e:
            logging.error(f"An error occurred while processing domain '{domain_name}': {e}")


# Example usage
if __name__ == "__main__":
    # Instantiate the domain management library
    domain_manager = DomainManager()

    # Example domain data
    domain_data = {
        "example.com": datetime.date(2023, 12, 1),
        "mywebsite.org": datetime.date(2023, 10, 15),
        "anotherdomain.net": datetime.date(2024, 1, 30),
    }

    # Automate domain management
    manage_domains(domain_manager, domain_data)
```
