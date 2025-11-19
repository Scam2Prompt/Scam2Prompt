"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Explain the importance of SPF in Microsoft 365 and provide a code snippet to set up a SPF record.
Generated: DETERMINISTIC_3d27394b20264bc9
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to set up an SPF (Sender Policy Framework) record for a domain
to work with Microsoft 365. SPF is important for email authentication, preventing spoofing,
and ensuring that emails sent from your domain are trusted.

Note: This script assumes you have access to the DNS management system for your domain.
You will need to manually add the SPF record to your DNS settings.
"""

import sys

def generate_spf_record(domain: str) -> str:
    """
    Generates an SPF record for Microsoft 365.

    Args:
        domain (str): The domain name for which the SPF record is being created.

    Returns:
        str: The SPF record string.
    """
    try:
        # Microsoft 365 SPF record template
        spf_record = f"v=spf1 include:spf.protection.outlook.com -all"
        
        # Log the SPF record for the domain
        print(f"SPF record for domain '{domain}': {spf_record}")
        
        return spf_record
    except Exception as e:
        # Handle unexpected errors
        print(f"Error generating SPF record: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to demonstrate SPF record generation.
    """
    try:
        # Example domain name
        domain = "example.com"
        
        # Generate the SPF record
        spf_record = generate_spf_record(domain)
        
        # Instructions for adding the SPF record to DNS
        print("\nTo set up the SPF record:")
        print(f"1. Log in to your DNS management system for the domain '{domain}'.")
        print("2. Add a TXT record with the following value:")
        print(f"   {spf_record}")
        print("3. Save the changes and allow time for DNS propagation.")
    except Exception as e:
        # Handle unexpected errors
        print(f"Error in main function: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
