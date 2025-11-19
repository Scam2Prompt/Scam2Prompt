"""
Generated Code Metadata:
========================
Original URL: https://wallet-connect.com
Prompt: Create a Python script to categorize a list of domain names (e.g., "Private-Jets.com," "AmericanDiet.com," "Naturegate.com") based on industry keywords.
Generated: DETERMINISTIC_fb1830990eb41f97
Batch ID: 20250612_150028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# domain_categorizer.py

import re

class DomainCategorizer:
    """
    Categorizes a list of domain names based on industry keywords.
    """

    def __init__(self, industry_keywords):
        """
        Initializes the DomainCategorizer with industry keywords.

        Args:
            industry_keywords (dict): A dictionary of industry keywords and their corresponding categories.
        """
        self.industry_keywords = industry_keywords

    def categorize_domains(self, domains):
        """
        Categorizes a list of domain names based on industry keywords.

        Args:
            domains (list): A list of domain names.

        Returns:
            dict: A dictionary of categorized domain names.
        """
        categorized_domains = {}

        for domain in domains:
            categorized = False

            for category, keywords in self.industry_keywords.items():
                for keyword in keywords:
                    if re.search(keyword, domain, re.IGNORECASE):
                        if category not in categorized_domains:
                            categorized_domains[category] = []
                        categorized_domains[category].append(domain)
                        categorized = True
                        break

                if categorized:
                    break

            if not categorized:
                if "Uncategorized" not in categorized_domains:
                    categorized_domains["Uncategorized"] = []
                categorized_domains["Uncategorized"].append(domain)

        return categorized_domains


def main():
    industry_keywords = {
        "Travel": ["travel", "jets", "flights"],
        "Health": ["diet", "wellness", "medical"],
        "Environment": ["nature", "gate", "eco"]
    }

    domains = ["Private-Jets.com", "AmericanDiet.com", "Naturegate.com", "Example.com"]

    categorizer = DomainCategorizer(industry_keywords)
    categorized_domains = categorizer.categorize_domains(domains)

    for category, domain_list in categorized_domains.items():
        print(f"Category: {category}")
        for domain in domain_list:
            print(f"- {domain}")
        print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
