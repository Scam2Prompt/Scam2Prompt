"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millennium-capital.com
Prompt: Develop a script that categorizes domain names into industries like "Legal," "Technology," and "Hospitality," and displays them dynamically, inspired by Millennium Capital's domain list.
Generated: DETERMINISTIC_1f4a400a86cf2ad1
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from collections import defaultdict

# Define a class to categorize domain names
class DomainCategorizer:
    def __init__(self):
        # Initialize a dictionary to hold categories and their corresponding domains
        self.categories = defaultdict(list)
    
    def categorize_domain(self, domain):
        """
        Categorizes a domain name based on its content.

        :param domain: str, the domain name to categorize
        :raises ValueError: if the domain format is invalid
        """
        # Validate the domain format using a regex pattern
        if not self.is_valid_domain(domain):
            raise ValueError(f"Invalid domain format: {domain}")

        # Categorize the domain based on keywords
        if re.search(r'\b(law|legal|attorney|court|lawyer)\b', domain, re.IGNORECASE):
            self.categories['Legal'].append(domain)
        elif re.search(r'\b(tech|technology|software|cloud|digital)\b', domain, re.IGNORECASE):
            self.categories['Technology'].append(domain)
        elif re.search(r'\b(hotel|hospitality|travel|tourism)\b', domain, re.IGNORECASE):
            self.categories['Hospitality'].append(domain)
        else:
            self.categories['Others'].append(domain)

    @staticmethod
    def is_valid_domain(domain):
        """
        Checks if the domain name is valid.

        :param domain: str, the domain name to validate
        :return: bool, True if valid, False otherwise
        """
        # Basic regex for validating domain names
        pattern = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$'
        return re.match(pattern, domain) is not None

    def display_categories(self):
        """
        Displays the categorized domains in a formatted manner.
        """
        print("Categorized Domain Names:")
        for category, domains in self.categories.items():
            print(f"{category}:")
            for domain in domains:
                print(f"  - {domain}")
            print()  # Add an extra line for better readability

# Example usage:
if __name__ == "__main__":
    domain_categorizer = DomainCategorizer()

    # List of example domain names
    domains_to_categorize = [
        "bestlawfirm.com",
        "innovativetechsolutions.com",
        "luxuryhotelparis.com",
        "unknownentity.net",
        "courtcaseupdates.org",
        "cloudstoragehub.com",
        "affordablehostels.com"
    ]

    # Categorize each domain and handle potential errors
    for domain in domains_to_categorize:
        try:
            domain_categorizer.categorize_domain(domain)
        except ValueError as e:
            print(e)

    # Display the results
    domain_categorizer.display_categories()
```
