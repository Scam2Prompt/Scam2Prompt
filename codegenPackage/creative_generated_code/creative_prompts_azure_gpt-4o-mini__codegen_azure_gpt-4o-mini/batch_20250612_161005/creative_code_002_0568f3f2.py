"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comu.su
Prompt: What are the key features of Plesk for managing DNS and mail services in a hosting environment?
Generated: DETERMINISTIC_0568f3f222892971
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Plesk Feature Overview for Managing DNS and Mail Services
This script provides an overview of key features of Plesk related to managing DNS and mail services in a hosting environment.
"""

class PleskFeatures:
    def __init__(self):
        """
        Initialize the PleskFeatures class with key features for DNS and mail services.
        """
        self.dns_features = []
        self.mail_features = []

    def add_dns_feature(self, feature: str):
        """
        Add a DNS feature to the list.

        :param feature: Description of the DNS feature
        """
        if feature:
            self.dns_features.append(feature)
        else:
            raise ValueError("Feature description cannot be empty.")

    def add_mail_feature(self, feature: str):
        """
        Add a mail feature to the list.

        :param feature: Description of the mail feature
        """
        if feature:
            self.mail_features.append(feature)
        else:
            raise ValueError("Feature description cannot be empty.")

    def display_features(self):
        """
        Display the key features for DNS and mail services.
        """
        print("Key DNS Features in Plesk:")
        for feature in self.dns_features:
            print(f"- {feature}")
        
        print("\nKey Mail Features in Plesk:")
        for feature in self.mail_features:
            print(f"- {feature}")

def main():
    """
    Main function to create a PleskFeatures instance and populate it with key features.
    """
    try:
        plesk = PleskFeatures()

        # Adding key DNS features
        plesk.add_dns_feature("User-friendly DNS management interface")
        plesk.add_dns_feature("Support for multiple DNS records (A, CNAME, MX, etc.)")
        plesk.add_dns_feature("DNSSEC support for enhanced security")
        plesk.add_dns_feature("Automatic DNS updates for domain changes")

        # Adding key mail features
        plesk.add_mail_feature("Comprehensive mail server configuration")
        plesk.add_mail_feature("Webmail access for users")
        plesk.add_mail_feature("Spam protection and filtering options")
        plesk.add_mail_feature("Email forwarding and autoresponders")

        # Display the features
        plesk.display_features()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
