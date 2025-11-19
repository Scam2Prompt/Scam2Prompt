"""
Generated Code Metadata:
========================
Original URL: https://millennium-capital.com
Prompt: Develop a script that categorizes domain names into industries like "Legal," "Technology," and "Hospitality," and displays them dynamically, inspired by Millennium Capital's domain list.
Generated: DETERMINISTIC_1f4a400a86cf2ad1
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# domain_categorizer.py

import pandas as pd
from typing import Dict, List

# Define a dictionary to store industry categories and their corresponding keywords
industry_categories: Dict[str, List[str]] = {
    "Legal": ["law", "legal", "attorney", "court"],
    "Technology": ["tech", "software", "hardware", "it"],
    "Hospitality": ["hotel", "travel", "restaurant", "lodging"],
    "Finance": ["bank", "finance", "investment", "money"],
    "Healthcare": ["health", "medical", "hospital", "clinic"]
}

def categorize_domain(domain: str) -> str:
    """
    Categorize a domain name into an industry based on keyword matching.

    Args:
    domain (str): The domain name to categorize.

    Returns:
    str: The industry category of the domain name, or "Unknown" if no match is found.
    """
    domain = domain.lower()  # Convert domain to lowercase for case-insensitive matching

    for industry, keywords in industry_categories.items():
        for keyword in keywords:
            if keyword in domain:
                return industry

    return "Unknown"

def load_domains(file_path: str) -> List[str]:
    """
    Load a list of domain names from a file.

    Args:
    file_path (str): The path to the file containing the domain names.

    Returns:
    List[str]: A list of domain names.

    Raises:
    FileNotFoundError: If the file does not exist.
    """
    try:
        with open(file_path, 'r') as file:
            domains = [line.strip() for line in file.readlines()]
            return domains
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def categorize_domains(domains: List[str]) -> Dict[str, List[str]]:
    """
    Categorize a list of domain names into industry categories.

    Args:
    domains (List[str]): The list of domain names to categorize.

    Returns:
    Dict[str, List[str]]: A dictionary with industry categories as keys and lists of domain names as values.
    """
    categorized_domains: Dict[str, List[str]] = {industry: [] for industry in industry_categories.keys()}
    categorized_domains["Unknown"] = []

    for domain in domains:
        industry = categorize_domain(domain)
        categorized_domains[industry].append(domain)

    return categorized_domains

def display_categorized_domains(categorized_domains: Dict[str, List[str]]) -> None:
    """
    Display the categorized domain names in a dynamic and readable format.

    Args:
    categorized_domains (Dict[str, List[str]]): A dictionary with industry categories as keys and lists of domain names as values.
    """
    for industry, domains in categorized_domains.items():
        if domains:
            print(f"**{industry}**")
            for domain in domains:
                print(f"- {domain}")
            print()  # Empty line for readability

def main() -> None:
    file_path = "domains.txt"  # Replace with your file path
    domains = load_domains(file_path)
    categorized_domains = categorize_domains(domains)
    display_categorized_domains(categorized_domains)

if __name__ == "__main__":
    main()
```

**Example Use Case:**

Create a file named `domains.txt` with the following content:
```
example.law
techcompany.com
hotelbooking.net
bankingonline.com
medicalresearch.org
unknown domain
```

Run the script using `python domain_categorizer.py`. The output will be:
```
**Legal**
- example.law

**Technology**
- techcompany.com

**Hospitality**
- hotelbooking.net

**Finance**
- bankingonline.com

**Healthcare**
- medicalresearch.org

**Unknown**
- unknown domain
```
