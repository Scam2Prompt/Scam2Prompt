"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millennium-capital.com
Prompt: Create a Python script to filter domain names based on keywords like "marine," "diet," or "technology," similar to the domain examples listed on Millennium Capital's webpage.
Generated: DETERMINISTIC_4383b3afb38ec2eb
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

class DomainFilter:
    def __init__(self, keywords):
        """
        Initializes the DomainFilter with a list of keywords.
        
        :param keywords: List of keywords to filter domain names.
        """
        self.keywords = keywords

    def is_valid_domain(self, domain):
        """
        Validates the domain name format using a regular expression.
        
        :param domain: The domain name to validate.
        :return: True if valid, False otherwise.
        """
        domain_regex = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$'
        return re.match(domain_regex, domain) is not None

    def filter_domains(self, domains):
        """
        Filters the list of domain names based on the defined keywords.
        
        :param domains: List of domain names to filter.
        :return: List of domain names that contain any of the keywords.
        """
        if not isinstance(domains, list):
            raise ValueError("Input must be a list of domain names.")

        filtered_domains = []
        for domain in domains:
            if not self.is_valid_domain(domain):
                print(f"Warning: '{domain}' is not a valid domain name and will be skipped.")
                continue
            
            if any(keyword.lower() in domain.lower() for keyword in self.keywords):
                filtered_domains.append(domain)
        
        return filtered_domains

def main():
    """
    Main function to execute the domain filtering.
    """
    # Define keywords to filter by
    keywords = ["marine", "diet", "technology"]
    
    # Sample domain names
    sample_domains = [
        "marinebiologist.com",
        "healthydiet.org",
        "technews.net",
        "invalid_domain_name",
        "marine-tours.com",
        "gadgetreview.tech",
        "diet-plans.info"
    ]
    
    # Create a DomainFilter instance
    domain_filter = DomainFilter(keywords)
    
    try:
        # Filter domains based on keywords
        filtered = domain_filter.filter_domains(sample_domains)
        print("Filtered domains:", filtered)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
