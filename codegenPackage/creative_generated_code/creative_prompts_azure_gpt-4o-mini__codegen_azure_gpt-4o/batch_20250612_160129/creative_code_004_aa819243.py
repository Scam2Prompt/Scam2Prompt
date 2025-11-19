"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://woo-finance.com
Prompt: Provide an example of how to use the WhoIs信息查询 service to check domain expiration dates programmatically.
Generated: DETERMINISTIC_aa8192438c2cc269
Batch ID: 20250612_160129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import whois
import sys

def get_domain_expiration_date(domain_name):
    """
    Fetches the expiration date of a domain using the 'whois' library.

    Args:
        domain_name (str): The domain name to query.

    Returns:
        str: The expiration date of the domain as a string, or an error message if the query fails.
    """
    try:
        # Perform WHOIS query
        domain_info = whois.whois(domain_name)
        
        # Check if expiration date is available
        if domain_info.expiration_date:
            # Handle cases where expiration_date may be a list (e.g., multiple WHOIS records)
            if isinstance(domain_info.expiration_date, list):
                return str(domain_info.expiration_date[0])  # Return the first expiration date
            return str(domain_info.expiration_date)
        else:
            return "Expiration date not found for the domain."
    except Exception as e:
        # Handle any errors that occur during the WHOIS query
        return f"An error occurred while fetching the domain information: {str(e)}"

if __name__ == "__main__":
    # Check if a domain name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python check_domain_expiration.py <domain_name>")
        sys.exit(1)

    domain_name = sys.argv[1]
    # Fetch expiration date for the provided domain name
    expiration_date = get_domain_expiration_date(domain_name)
    # Print the result to the console
    print(f"Expiration Date for '{domain_name}': {expiration_date}")
```

### Requirements:
1. Install the `whois` package first if not already installed:
   ```bash
   pip install python-whois
   ```

2. Save the code in a file named `check_domain_expiration.py` and execute it like:
   ```bash
   python check_domain_expiration.py example.com
   ```
