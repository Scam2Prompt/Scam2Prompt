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
# Program to filter and display Serbian (.rs) domain names from a given list of domains

def filter_serbian_domains(domain_list):
    """
    Filters and returns a list of Serbian (.rs) domains from the given domain list.

    :param domain_list: List of domain names (strings)
    :return: List of domains ending with '.rs'
    """
    try:
        # Use a list comprehension to filter domains ending with '.rs'
        serbian_domains = [domain for domain in domain_list if domain.endswith('.rs')]
        return serbian_domains
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while filtering domains: {e}")
        return []

def display_domains(domains):
    """
    Displays the list of domains in a clean, formatted manner.

    :param domains: List of domain names (strings)
    """
    if not domains:
        print("No Serbian (.rs) domains found.")
    else:
        print("Serbian (.rs) Domains:")
        for domain in domains:
            print(f"- {domain}")

if __name__ == "__main__":
    # Example list of domain names
    domain_list = [
        "optimism.rs",
        "example.com",
        "serbia.rs",
        "github.com",
        "mydomain.rs",
        "anotherdomain.org"
    ]
    
    # Filter Serbian domains
    serbian_domains = filter_serbian_domains(domain_list)
    
    # Display the results
    display_domains(serbian_domains)
```
