"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-gift.com
Prompt: Create a script to check if a domain name is whitelisted in the bot's purchase section, as outlined in the webpage content.
Generated: DETERMINISTIC_0d665091d7c90b78
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Constants
WHITELIST_FILE = "whitelist.json"

def load_whitelist(file_path):
    """
    Loads the whitelist from a JSON file.
    If the file does not exist, it returns an empty whitelist.
    :param file_path: Path to the whitelist JSON file.
    :return: A set containing whitelisted domain names.
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                return set(data.get("whitelisted_domains", []))
        else:
            return set()
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading whitelist: {e}")
        return set()

def is_domain_whitelisted(domain, whitelist):
    """
    Checks if a given domain name is present in the whitelist.
    :param domain: Domain name to check.
    :param whitelist: A set of whitelisted domain names.
    :return: True if the domain is whitelisted, False otherwise.
    """
    return domain in whitelist

def main():
    """
    Main function to check if a domain name is whitelisted.
    Prompts the user for a domain name and verifies it against the whitelist.
    """
    whitelist = load_whitelist(WHITELIST_FILE)

    if not whitelist:
        print("No domains are currently whitelisted.")
        return

    domain = input("Enter the domain name to check: ").strip()

    if is_domain_whitelisted(domain, whitelist):
        print(f"The domain '{domain}' is whitelisted.")
    else:
        print(f"The domain '{domain}' is NOT whitelisted.")

if __name__ == "__main__":
    main()
```
