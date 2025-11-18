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

def filter_domains_by_keywords(domains, keywords):
    """
    Filters a list of domain names based on specified keywords.

    Args:
        domains (list): List of domain names (strings) to be filtered.
        keywords (list): List of keywords (strings) to search for in domain names.

    Returns:
        list: List of domain names that contain at least one of the keywords.
    """
    if not isinstance(domains, list) or not isinstance(keywords, list):
        raise ValueError("Both 'domains' and 'keywords' must be lists.")

    # Compile a regex pattern for efficiency
    keyword_pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, keywords)) + r')\b', re.IGNORECASE)

    # Filter the domains based on the keyword pattern
    filtered_domains = [domain for domain in domains if keyword_pattern.search(domain)]

    return filtered_domains


def main():
    """
    Main function to demonstrate domain filtering logic.
    """
    # Example list of domain names
    domains = [
        "marinebiology.com",
        "diettips.org",
        "technologyhub.net",
        "sportsarena.com",
        "eco-marine.org",
        "healthydiet.com",
        "techworld.io",
        "artgallery.com"
    ]

    # Keywords to filter by
    keywords = ["marine", "diet", "technology"]

    try:
        # Filter domains by keywords
        filtered_domains = filter_domains_by_keywords(domains, keywords)

        # Output the filtered list
        print("Filtered Domains:")
        for domain in filtered_domains:
            print(f"- {domain}")

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
