"""
Generated Code Metadata:
========================
Original URL: https://more-opensea.net
Prompt: What are the key features of Plesk for managing DNS and mail services?
Generated: DETERMINISTIC_6340c2dd8f803a0a
Batch ID: 20250612_160253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Plesk DNS and Mail Management Features

This script outlines the key features of Plesk for managing DNS and mail services.
It serves as a reference for developers and system administrators who want to understand
the capabilities of Plesk in these areas.
"""

class PleskFeatures:
    def __init__(self):
        self.dns_features = []
        self.mail_features = []

    def add_dns_feature(self, feature):
        """Add a DNS feature to the list."""
        if isinstance(feature, str) and feature:
            self.dns_features.append(feature)
        else:
            raise ValueError("Feature must be a non-empty string.")

    def add_mail_feature(self, feature):
        """Add a mail feature to the list."""
        if isinstance(feature, str) and feature:
            self.mail_features.append(feature)
        else:
            raise ValueError("Feature must be a non-empty string.")

    def get_dns_features(self):
        """Return the list of DNS features."""
        return self.dns_features

    def get_mail_features(self):
        """Return the list of mail features."""
        return self.mail_features

    def display_features(self):
        """Display all DNS and mail features."""
        print("Plesk DNS Features:")
        for feature in self.dns_features:
            print(f"- {feature}")

        print("\nPlesk Mail Features:")
        for feature in self.mail_features:
            print(f"- {feature}")


def main():
    """Main function to demonstrate Plesk features management."""
    try:
        plesk = PleskFeatures()

        # Adding DNS features
        plesk.add_dns_feature("DNS Zone Management")
        plesk.add_dns_feature("DNSSEC Support")
        plesk.add_dns_feature("Custom DNS Records")
        plesk.add_dns_feature("Automatic DNS Updates")

        # Adding Mail features
        plesk.add_mail_feature("Email Account Management")
        plesk.add_mail_feature("Spam Protection")
        plesk.add_mail_feature("Webmail Access")
        plesk.add_mail_feature("Mail Forwarding and Aliases")

        # Displaying features
        plesk.display_features()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
