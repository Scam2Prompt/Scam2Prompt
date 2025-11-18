"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.optimism.rs
Prompt: Write a program to filter and display domain names from a list, focusing on Serbian (.rs) domains, inspired by the examples on optimism.rs.
Generated: DETERMINISTIC_2e56c9cbbbc68044
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List, Optional

def filter_serbian_domains(domain_list: List[str]) -> List[str]:
    """
    Filters a list of domain names and returns only those that are Serbian (.rs).
    
    Args:
        domain_list (List[str]): A list of domain names to filter.
    
    Returns:
        List[str]: A list of Serbian domain names.
    """
    serbian_domains = []
    # Regular expression pattern for matching .rs domains
    pattern = re.compile(r'^[a-zA-Z0-9.-]+\.(rs|RS)$')

    for domain in domain_list:
        if pattern.match(domain):
            serbian_domains.append(domain)
    
    return serbian_domains

def main() -> None:
    """
    Main function to execute the domain filtering.
    It handles input and output while ensuring error handling.
    """
    try:
        # Example list of domain names
        domain_list = [
            'example.rs', 'test.com', 'example.org', 'site.rs', 'not-a-domain',
            'another-example.RS', 'valid-domain.rs', 'invalid-domain.xyz', 
            'example.rs/test', 'example'
        ]
        
        # Filter the Serbian domains
        filtered_domains = filter_serbian_domains(domain_list)
        
        # Display the filtered domains
        print("Filtered Serbian Domains:")
        for domain in filtered_domains:
            print(domain)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
