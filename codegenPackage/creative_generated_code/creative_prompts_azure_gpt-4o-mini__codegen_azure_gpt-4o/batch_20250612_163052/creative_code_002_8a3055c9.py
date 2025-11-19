"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatewealth.co
Prompt: How can I write a script to automate the checking of DNS records for a domain?
Generated: DETERMINISTIC_8a3055c9213ce5c6
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
import sys

def check_dns_records(domain):
    """
    Function to check various DNS records for a given domain.
    
    Args:
        domain (str): The domain name to check DNS records for.
        
    Returns:
        dict: A dictionary containing the queried DNS records.
    """
    # Define the types of DNS records to check
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']

    dns_records = {}

    for record_type in record_types:
        try:
            # Resolve the DNS record for the specified type
            answers = dns.resolver.resolve(domain, record_type)
            dns_records[record_type] = [str(answer) for answer in answers]
        except dns.resolver.NoAnswer:
            # Handle case where no answer is returned for the record type
            dns_records[record_type] = None
        except dns.resolver.NXDOMAIN:
            # Handle case where the domain does not exist
            dns_records[record_type] = None
        except dns.exception.Timeout:
            # Handle timeout exceptions
            dns_records[record_type] = "Query timed out"
        except Exception as e:
            # Catch-all for unexpected exceptions
            dns_records[record_type] = f"Error: {str(e)}"

    return dns_records

def main():
    """
    Main function to prompt the user for a domain name and check its DNS records.
    """
    try:
        # Prompt the user to enter a domain name
        domain = input("Enter the domain name to check DNS records (e.g., example.com): ").strip()

        if not domain:
            print("Error: Domain name cannot be empty.")
            sys.exit(1)
        
        # Call the function to check DNS records
        results = check_dns_records(domain)

        # Output the results
        print(f"\nDNS records for domain: {domain}\n")
        for record_type, records in results.items():
            print(f"{record_type} records:")
            if records:
                for record in records:
                    print(f"  {record}")
            else:
                print("  None found")
    except KeyboardInterrupt:
        # Gracefully handle user interruption (Ctrl+C)
        print("\nOperation cancelled by user.")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the script
    main()
```
