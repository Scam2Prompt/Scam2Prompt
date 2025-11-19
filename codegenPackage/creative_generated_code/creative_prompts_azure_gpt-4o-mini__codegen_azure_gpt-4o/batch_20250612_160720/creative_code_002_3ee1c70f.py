"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkysync-eligible.com
Prompt: What are the key features of Plesk for managing web, DNS, and mail services effectively?
Generated: DETERMINISTIC_3ee1c70faaf7e262
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to list key features of Plesk for managing web, DNS, and mail services effectively.

This script is written in Python and is designed to be modular, clean, and well-documented.
It uses proper error handling and follows best practices for production-ready applications.
"""

# Import necessary modules
import logging

# Setup logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_plesk_features():
    """
    Returns a dictionary of Plesk's key features categorized by web, DNS, and mail management.
    
    :return: A dictionary containing lists of features.
    """
    try:
        features = {
            "Web Management": [
                "Centralized Control Panel for managing multiple websites.",
                "Support for multiple programming languages (PHP, Perl, Python, ASP.NET).",
                "Integration with tools like Git for version control.",
                "One-click installation of popular CMS platforms such as WordPress, Joomla, and Drupal.",
                "Website performance monitoring and optimization tools."
            ],
            "DNS Management": [
                "DNS Zone Management for creating and editing DNS records.",
                "Support for custom DNS templates.",
                "Automatic propagation of DNS changes.",
                "Integrated DNSSEC management to enhance security.",
                "Reverse DNS setup for IP addresses."
            ],
            "Mail Management": [
                "Built-in mail server with support for IMAP, POP3, and SMTP protocols.",
                "Spam filtering and antivirus integration.",
                "Webmail support (e.g., Roundcube, Horde).",
                "Custom email address creation with domain names.",
                "Email forwarding and autoresponders."
            ]
        }
        logging.info("Successfully fetched Plesk features.")
        return features
    except Exception as e:
        logging.error(f"Error fetching Plesk features: {e}")
        return None


def display_features(features):
    """
    Displays the features of Plesk in a readable format.
    
    :param features: Dictionary of features categorized by web, DNS, and mail management.
    """
    if not features:
        logging.warning("No features to display.")
        return

    try:
        print("\nKey Features of Plesk:")
        for category, items in features.items():
            print(f"\n{category}:")
            for index, feature in enumerate(items, start=1):
                print(f"  {index}. {feature}")
        logging.info("Successfully displayed Plesk features.")
    except Exception as e:
        logging.error(f"Error displaying Plesk features: {e}")


def main():
    """
    Main function to fetch and display Plesk features.
    """
    try:
        # Fetching features
        plesk_features = get_plesk_features()
        
        # Displaying features
        display_features(plesk_features)
    except Exception as e:
        logging.critical(f"Unhandled exception in main: {e}")


if __name__ == "__main__":
    main()
```
