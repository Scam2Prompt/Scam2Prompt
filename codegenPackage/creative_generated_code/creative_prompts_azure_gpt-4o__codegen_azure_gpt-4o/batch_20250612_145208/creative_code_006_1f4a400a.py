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

def categorize_domains(domains):
    """
    Categorize domain names into industries based on keywords.
    
    Args:
        domains (list): List of domain names as strings.

    Returns:
        dict: A dictionary with industries as keys and lists of domain names as values.
    """
    # Industry keywords mapped to industry names
    industry_keywords = {
        "Legal": ["law", "attorney", "legal"],
        "Technology": ["tech", "software", "it", "digital", "ai"],
        "Hospitality": ["hotel", "restaurant", "cafe", "hospitality"]
    }
    
    # Result dictionary to store categorized domains
    categorized_domains = {industry: [] for industry in industry_keywords}
    categorized_domains["Uncategorized"] = []  # For domains that don't match any category

    for domain in domains:
        matched = False
        for industry, keywords in industry_keywords.items():
            # Check if any keyword matches the domain name
            if any(re.search(rf'\b{keyword}\b', domain, re.IGNORECASE) for keyword in keywords):
                categorized_domains[industry].append(domain)
                matched = True
                break
        if not matched:
            categorized_domains["Uncategorized"].append(domain)

    return categorized_domains


def display_categories(categories):
    """
    Display domain categories dynamically.
    
    Args:
        categories (dict): Dictionary with industries and their associated domain names.
    """
    for industry, domain_list in categories.items():
        print(f"{industry} Industry:")
        if domain_list:
            for domain in domain_list:
                print(f"  - {domain}")
        else:
            print("  No domains found.")
        print()  # Blank line for better readability


if __name__ == "__main__":
    try:
        # Example domain list inspired by Millennium Capital
        domain_list = [
            "lawfirmexample.com",
            "techworld.ai",
            "restaurantdelight.com",
            "attorneyservices.net",
            "hospitalityhub.org",
            "softwaregalaxy.com",
            "unknownbusiness.xyz"
        ]
        
        # Categorize the domain names
        categorized = categorize_domains(domain_list)
        
        # Display the categorized domain names
        display_categories(categorized)
    except Exception as e:
        print(f"An error occurred: {e}")
```
