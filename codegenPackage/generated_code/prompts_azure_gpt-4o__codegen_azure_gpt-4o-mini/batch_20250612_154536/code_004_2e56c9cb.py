"""
Generated Code Metadata:
========================
Original URL: https://www.optimism.rs
Prompt: Write a program to filter and display domain names from a list, focusing on Serbian (.rs) domains, inspired by the examples on optimism.rs.
Generated: DETERMINISTIC_2e56c9cbbbc68044
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List

def filter_serbian_domains(domains: List[str]) -> List[str]:
    """
    Filters the given list of domain names to return only those that end with the Serbian TLD (.rs).

    Args:
        domains (List[str]): A list of domain names to filter.

    Returns:
        List[str]: A list of domain names that are Serbian (.rs).
    """
    # Regular expression pattern to match .rs domains
    pattern = re.compile(r'\.rs$', re.IGNORECASE)
    
    # Filter domains using the regex pattern
    serbian_domains = [domain for domain in domains if pattern.search(domain)]
    
    return serbian_domains

def main():
    """
    Main function to execute the domain filtering process.
    """
    # Sample list of domain names
    domain_list = [
        "example.com",
        "optimism.rs",
        "test.rs",
        "example.org",
        "anotherdomain.rs",
        "notserbian.net"
    ]
    
    try:
        # Filter Serbian domains
        filtered_domains = filter_serbian_domains(domain_list)
        
        # Display the filtered domains
        print("Filtered Serbian Domains:")
        for domain in filtered_domains:
            print(domain)
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
