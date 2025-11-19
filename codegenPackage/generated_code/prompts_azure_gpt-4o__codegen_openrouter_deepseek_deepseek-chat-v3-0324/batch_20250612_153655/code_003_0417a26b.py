"""
Generated Code Metadata:
========================
Original URL: https://wallstreetpepe.club
Prompt: Generate code to perform DNS resolution for a domain using Google Public DNS and display the results in a user-friendly format.
Generated: DETERMINISTIC_0417a26b0e1d66a3
Batch ID: 20250612_153655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import dns.resolver
from dns.exception import DNSException
from typing import List, Dict, Union

def resolve_dns(domain: str) -> Dict[str, Union[List[str], str]]:
    """
    Perform DNS resolution for a given domain using Google Public DNS.
    
    Args:
        domain: Domain name to resolve (e.g., 'example.com')
    
    Returns:
        Dictionary containing DNS records or error message
    """
    result = {
        'domain': domain,
        'A': [],
        'AAAA': [],
        'MX': [],
        'NS': [],
        'TXT': [],
        'CNAME': None,
        'error': None
    }
    
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Google Public DNS
    
    try:
        # Resolve A records
        try:
            answers = resolver.resolve(domain, 'A')
            result['A'] = [str(r) for r in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            pass
        
        # Resolve AAAA records
        try:
            answers = resolver.resolve(domain, 'AAAA')
            result['AAAA'] = [str(r) for r in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            pass
        
        # Resolve MX records
        try:
            answers = resolver.resolve(domain, 'MX')
            result['MX'] = [f"{r.preference} {str(r.exchange)}" for r in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            pass
        
        # Resolve NS records
        try:
            answers = resolver.resolve(domain, 'NS')
            result['NS'] = [str(r) for r in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            pass
        
        # Resolve TXT records
        try:
            answers = resolver.resolve(domain, 'TXT')
            result['TXT'] = [str(r) for r in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            pass
        
        # Resolve CNAME record
        try:
            answers = resolver.resolve(domain, 'CNAME')
            result['CNAME'] = str(answers[0])
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            pass
            
    except DNSException as e:
        result['error'] = f"DNS resolution failed: {str(e)}"
    except Exception as e:
        result['error'] = f"Unexpected error: {str(e)}"
    
    return result

def format_dns_results(results: Dict[str, Union[List[str], str]]) -> str:
    """
    Format DNS results in a user-friendly string.
    
    Args:
        results: Dictionary containing DNS records
        
    Returns:
        Formatted string with DNS information
    """
    if results.get('error'):
        return f"Error resolving {results['domain']}:\n{results['error']}"
    
    output = [f"DNS records for {results['domain']}:"]
    
    if results['A']:
        output.append("\nA Records (IPv4):")
        output.extend(f"  - {ip}" for ip in results['A'])
    
    if results['AAAA']:
        output.append("\nAAAA Records (IPv6):")
        output.extend(f"  - {ip}" for ip in results['AAAA'])
    
    if results['MX']:
        output.append("\nMX Records (Mail Servers):")
        output.extend(f"  - {mx}" for mx in results['MX'])
    
    if results['NS']:
        output.append("\nNS Records (Name Servers):")
        output.extend(f"  - {ns}" for ns in results['NS'])
    
    if results['TXT']:
        output.append("\nTXT Records:")
        output.extend(f"  - {txt}" for txt in results['TXT'])
    
    if results['CNAME']:
        output.append(f"\nCNAME Record:\n  - {results['CNAME']}")
    
    if not any([results['A'], results['AAAA'], results['MX'], 
                results['NS'], results['TXT'], results['CNAME']]):
        output.append("\nNo DNS records found for this domain.")
    
    return "\n".join(output)

def main():
    """Main function to handle user input and display results."""
    try:
        domain = input("Enter domain to resolve: ").strip()
        if not domain:
            print("Error: Domain cannot be empty")
            return
        
        print(f"\nResolving {domain} using Google Public DNS...")
        results = resolve_dns(domain)
        print(format_dns_results(results))
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
