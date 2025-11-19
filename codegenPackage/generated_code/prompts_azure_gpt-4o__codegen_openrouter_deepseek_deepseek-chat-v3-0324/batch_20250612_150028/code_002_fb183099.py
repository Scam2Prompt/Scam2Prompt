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
import re
from typing import Dict, List, Tuple

# Industry keywords mapping
INDUSTRY_KEYWORDS = {
    'aviation': ['jet', 'airline', 'aviation', 'flight', 'pilot', 'aircraft'],
    'health': ['diet', 'fitness', 'health', 'wellness', 'nutrition', 'vitamin'],
    'nature': ['nature', 'eco', 'green', 'environment', 'wildlife', 'sustainable'],
    'technology': ['tech', 'software', 'digital', 'computer', 'data', 'cloud'],
    'finance': ['finance', 'bank', 'money', 'invest', 'capital', 'wealth'],
}

def categorize_domain(domain: str) -> Tuple[str, str]:
    """
    Categorize a single domain based on industry keywords.
    
    Args:
        domain: Domain name to categorize
        
    Returns:
        Tuple of (domain, category) where category is the matched industry
        or 'uncategorized' if no match found
    """
    domain_lower = domain.lower()
    
    # Remove common TLDs and subdomains for better matching
    clean_domain = re.sub(r'^(www\.)|\.(com|net|org|io|co)$', '', domain_lower)
    
    for category, keywords in INDUSTRY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in clean_domain:
                return (domain, category)
    
    return (domain, 'uncategorized')

def categorize_domains(domains: List[str]) -> Dict[str, List[str]]:
    """
    Categorize multiple domains and return results grouped by category.
    
    Args:
        domains: List of domain names to categorize
        
    Returns:
        Dictionary with categories as keys and lists of domains as values
    """
    categorized = {}
    
    for domain in domains:
        _, category = categorize_domain(domain)
        
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(domain)
    
    return categorized

def main():
    """Main function to demonstrate domain categorization."""
    # Example domains
    domains = [
        "Private-Jets.com",
        "AmericanDiet.com",
        "Naturegate.com",
        "TechSolutions.io",
        "CapitalInvest.net",
        "RandomSite.org"
    ]
    
    # Categorize domains
    results = categorize_domains(domains)
    
    # Print results
    for category, domain_list in results.items():
        print(f"\n{category.upper()} ({len(domain_list)} domains):")
        for domain in domain_list:
            print(f"  - {domain}")

if __name__ == "__main__":
    main()
```
