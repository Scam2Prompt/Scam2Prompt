"""
Generated Code Metadata:
========================
Original URL: https://zk.fest.co
Prompt: What are the steps to purchase a domain name like Fest.co, and what information is required to start a conversation with the seller?
Generated: DETERMINISTIC_b2014bc63f89ae21
Batch ID: 20250622_204919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import whois
from typing import Optional, Dict

class DomainPurchaseAssistant:
    """
    A class to assist in purchasing a domain name by checking availability,
    finding contact information, and initiating purchase conversations.
    """
    
    def __init__(self, domain: str):
        """
        Initialize with the target domain name.
        
        Args:
            domain (str): The domain name to check/purchase (e.g., "fest.co")
        """
        self.domain = domain.lower().strip()
        self.whois_info = None
        
    def check_availability(self) -> bool:
        """
        Check if the domain is available for registration.
        
        Returns:
            bool: True if available, False if registered
        """
        try:
            domain_info = whois.whois(self.domain)
            return not domain_info.domain_name
        except Exception as e:
            print(f"Error checking domain availability: {e}")
            return False
    
    def get_whois_info(self) -> Optional[Dict]:
        """
        Retrieve WHOIS information for the domain.
        
        Returns:
            Optional[Dict]: WHOIS data if available, None otherwise
        """
        try:
            self.whois_info = whois.whois(self.domain)
            return self.whois_info
        except Exception as e:
            print(f"Error retrieving WHOIS info: {e}")
            return None
    
    def find_contact_info(self) -> Dict:
        """
        Extract contact information from WHOIS data.
        
        Returns:
            Dict: Dictionary containing relevant contact info
        """
        if not self.whois_info:
            self.get_whois_info()
            
        contact_info = {
            'registrar': None,
            'registrant_name': None,
            'registrant_email': None,
            'registrant_phone': None,
            'creation_date': None,
            'expiration_date': None
        }
        
        if self.whois_info:
            try:
                contact_info.update({
                    'registrar': self.whois_info.registrar,
                    'registrant_name': self.whois_info.name,
                    'registrant_email': self.whois_info.email,
                    'registrant_phone': self.whois_info.phone,
                    'creation_date': self.whois_info.creation_date,
                    'expiration_date': self.whois_info.expiration_date
                })
            except AttributeError:
                pass
                
        return contact_info
    
    def generate_initial_message(self) -> str:
        """
        Generate a professional initial message template for contacting the seller.
        
        Returns:
            str: Formatted message template
        """
        contact_info = self.find_contact_info()
        
        message = f"""Subject: Inquiry About {self.domain} Domain Purchase

Dear {contact_info['registrant_name'] or 'Domain Owner'},

I hope this message finds you well. I'm reaching out regarding the {self.domain} domain name, which appears to be registered under your name.

I'm interested in potentially acquiring this domain and would like to discuss:
1. Your interest in selling the domain
2. The asking price or your terms for transfer
3. The transfer process timeline

Please let me know your availability for a conversation or if you'd prefer to communicate via email.

Best regards,
[Your Name]
[Your Contact Information]
[Your Company (if applicable)]"""
        
        return message

# Example usage
if __name__ == "__main__":
    domain = "fest.co"
    assistant = DomainPurchaseAssistant(domain)
    
    if assistant.check_availability():
        print(f"{domain} is available for registration!")
    else:
        print(f"{domain} is already registered.")
        contact_info = assistant.find_contact_info()
        print("Contact Information:", contact_info)
        print("\nSample Initial Message:")
        print(assistant.generate_initial_message())
```
