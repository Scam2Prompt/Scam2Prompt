"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect.com
Prompt: Create a Python script to categorize a list of domain names (e.g., "Private-Jets.com," "AmericanDiet.com," "Naturegate.com") based on industry keywords.
Generated: DETERMINISTIC_fb1830990eb41f97
Batch ID: 20250612_150028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List, Dict

class DomainCategorizer:
    def __init__(self):
        # Define industry keywords and their corresponding categories
        self.keywords: Dict[str, str] = {
            'jet': 'Aviation',
            'diet': 'Health',
            'nature': 'Environment',
            'finance': 'Finance',
            'tech': 'Technology',
            'food': 'Food',
            'travel': 'Travel',
            'fitness': 'Health',
            'education': 'Education'
        }

    def categorize_domains(self, domains: List[str]) -> Dict[str, List[str]]:
        """
        Categorize a list of domain names based on predefined industry keywords.

        :param domains: List of domain names to categorize
        :return: Dictionary with categories as keys and lists of domain names as values
        """
        categorized_domains = {category: [] for category in self.keywords.values()}
        
        for domain in domains:
            # Normalize domain to lowercase and remove non-alphanumeric characters
            domain_cleaned = self._clean_domain(domain)
            category_found = False

            # Check for keywords in the cleaned domain
            for keyword, category in self.keywords.items():
                if keyword in domain_cleaned:
                    categorized_domains[category].append(domain)
                    category_found = True
                    break
            
            # If no category found, classify as 'Uncategorized'
            if not category_found:
                if 'Uncategorized' not in categorized_domains:
                    categorized_domains['Uncategorized'] = []
                categorized_domains['Uncategorized'].append(domain)

        return categorized_domains

    @staticmethod
    def _clean_domain(domain: str) -> str:
        """
        Clean the domain name by normalizing it to lowercase and removing
        non-alphanumeric characters.

        :param domain: The domain name to clean
        :return: Cleaned domain name
        """
        return re.sub(r'[^a-zA-Z0-9]', '', domain.lower())

def main():
    # Example domain list
    domains = ["Private-Jets.com", "AmericanDiet.com", "Naturegate.com", 
               "FinanceWorld.com", "TechInnovations.com", "HealthyFood.com"]

    # Create a DomainCategorizer instance
    categorizer = DomainCategorizer()

    # Categorize the provided domain names
    categorized = categorizer.categorize_domains(domains)

    # Print the categorized domains
    for category, domain_list in categorized.items():
        print(f"{category}: {', '.join(domain_list)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
