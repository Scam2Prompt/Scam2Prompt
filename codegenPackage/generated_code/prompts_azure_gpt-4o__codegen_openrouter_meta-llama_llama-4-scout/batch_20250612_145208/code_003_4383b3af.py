"""
Generated Code Metadata:
========================
Original URL: https://millennium-capital.com
Prompt: Create a Python script to filter domain names based on keywords like "marine," "diet," or "technology," similar to the domain examples listed on Millennium Capital's webpage.
Generated: DETERMINISTIC_4383b3afb38ec2eb
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Domain Filter Script
======================

Filters domain names based on given keywords.

Usage:
    python domain_filter.py -d <domain_list_file> -k <keywords_file> -o <output_file>

Requirements:
    - Python 3.8+
    - argparse
    - pathlib
"""

import argparse
import pathlib

def load_keywords(keywords_file):
    """
    Load keywords from a file.

    Args:
        keywords_file (pathlib.Path): Path to the keywords file.

    Returns:
        list: List of keywords.

    Raises:
        FileNotFoundError: If the keywords file does not exist.
    """
    try:
        with open(keywords_file, 'r') as f:
            return [line.strip().lower() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: Keywords file '{keywords_file}' not found.")
        return []

def load_domains(domains_file):
    """
    Load domain names from a file.

    Args:
        domains_file (pathlib.Path): Path to the domain list file.

    Returns:
        list: List of domain names.

    Raises:
        FileNotFoundError: If the domain list file does not exist.
    """
    try:
        with open(domains_file, 'r') as f:
            return [line.strip().lower() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: Domain list file '{domains_file}' not found.")
        return []

def filter_domains(domains, keywords):
    """
    Filter domain names based on keywords.

    Args:
        domains (list): List of domain names.
        keywords (list): List of keywords.

    Returns:
        dict: Dictionary with keywords as keys and filtered domain lists as values.
    """
    filtered_domains = {keyword: [] for keyword in keywords}
    for domain in domains:
        for keyword in keywords:
            if keyword in domain:
                filtered_domains[keyword].append(domain)
    return filtered_domains

def save_filtered_domains(filtered_domains, output_file):
    """
    Save filtered domain names to a file.

    Args:
        filtered_domains (dict): Dictionary with keywords as keys and filtered domain lists as values.
        output_file (pathlib.Path): Path to the output file.
    """
    with open(output_file, 'w') as f:
        for keyword, domains in filtered_domains.items():
            f.write(f"Domains with keyword '{keyword}':\n")
            for domain in domains:
                f.write(f"- {domain}\n")
            f.write("\n")

def main():
    parser = argparse.ArgumentParser(description="Filter domain names based on keywords.")
    parser.add_argument("-d", "--domains", type=pathlib.Path, required=True, help="Path to the domain list file.")
    parser.add_argument("-k", "--keywords", type=pathlib.Path, required=True, help="Path to the keywords file.")
    parser.add_argument("-o", "--output", type=pathlib.Path, required=True, help="Path to the output file.")
    args = parser.parse_args()

    keywords = load_keywords(args.keywords)
    domains = load_domains(args.domains)

    if not keywords or not domains:
        return

    filtered_domains = filter_domains(domains, keywords)
    save_filtered_domains(filtered_domains, args.output)

if __name__ == "__main__":
    main()
```
