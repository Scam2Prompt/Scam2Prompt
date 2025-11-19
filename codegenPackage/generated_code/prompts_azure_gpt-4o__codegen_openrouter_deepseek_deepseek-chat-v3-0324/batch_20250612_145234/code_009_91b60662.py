"""
Generated Code Metadata:
========================
Original URL: https://airdrop-stepngo.asia
Prompt: Generate a list of best practices for configuring domains and SSL certificates in FASTPANEL to avoid common server errors.
Generated: DETERMINISTIC_91b60662f7fc37c7
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# best_practices_fastpanel_ssl.py

def get_fastpanel_ssl_best_practices():
    """
    Returns a list of best practices for configuring domains and SSL certificates in FASTPANEL.
    Each item includes a practice and its importance level (Critical, High, Medium).
    """
    return [
        {
            "practice": "Always use a valid domain name that you own and control",
            "importance": "Critical"
        },
        {
            "practice": "Ensure DNS records (A/AAAA/CNAME) are properly configured before SSL setup",
            "importance": "Critical"
        },
        {
            "practice": "Use Let's Encrypt for free SSL certificates when possible",
            "importance": "High"
        },
        {
            "practice": "Verify domain ownership before certificate issuance",
            "importance": "Critical"
        },
        {
            "practice": "Set proper certificate validity periods (90 days for Let's Encrypt)",
            "importance": "High"
        },
        {
            "practice": "Configure automatic certificate renewal",
            "importance": "High"
        },
        {
            "practice": "Use 2048-bit or higher RSA keys for certificates",
            "importance": "High"
        },
        {
            "practice": "Enable HTTP to HTTPS redirection in FASTPANEL settings",
            "importance": "High"
        },
        {
            "practice": "Configure proper SSL protocols (TLS 1.2+) and disable older versions",
            "importance": "High"
        },
        {
            "practice": "Set up proper certificate chains to avoid browser warnings",
            "importance": "High"
        },
        {
            "practice": "Regularly monitor certificate expiration dates",
            "importance": "Medium"
        },
        {
            "practice": "Use wildcard certificates (*.domain.com) when managing multiple subdomains",
            "importance": "Medium"
        },
        {
            "practice": "Configure proper HSTS headers for enhanced security",
            "importance": "Medium"
        },
        {
            "practice": "Test SSL configuration using tools like SSL Labs after setup",
            "importance": "Medium"
        },
        {
            "practice": "Keep FASTPANEL and related software updated for security patches",
            "importance": "Critical"
        },
        {
            "practice": "Document all SSL certificate details including issuance and expiry dates",
            "importance": "Medium"
        },
        {
            "practice": "Configure proper file permissions for certificate files (600 or 400)",
            "importance": "High"
        },
        {
            "practice": "Set up monitoring for SSL certificate expiration",
            "importance": "Medium"
        },
        {
            "practice": "Verify certificate installation using online SSL checkers",
            "importance": "Medium"
        },
        {
            "practice": "Maintain backups of all SSL certificates and private keys",
            "importance": "High"
        }
    ]


def validate_ssl_configuration(domain):
    """
    Simulates basic SSL configuration validation for a domain.
    Returns a dictionary with validation results.
    """
    import ssl
    import socket
    from datetime import datetime
    
    results = {
        "domain": domain,
        "checks": [],
        "valid": True
    }
    
    try:
        # Check if domain resolves
        ip = socket.gethostbyname(domain)
        results["checks"].append({
            "check": "DNS Resolution",
            "status": "OK",
            "details": f"Resolves to {ip}"
        })
        
        # Check SSL certificate
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                
                # Check expiration
                expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                days_remaining = (expiry_date - datetime.now()).days
                
                results["checks"].append({
                    "check": "Certificate Validity",
                    "status": "OK" if days_remaining > 0 else "EXPIRED",
                    "details": f"Expires in {days_remaining} days"
                })
                
                # Check issuer
                issuer = dict(x[0] for x in cert['issuer'])
                results["checks"].append({
                    "check": "Certificate Issuer",
                    "status": "OK",
                    "details": f"Issued by {issuer.get('organizationName', 'Unknown')}"
                })
                
    except Exception as e:
        results["valid"] = False
        results["checks"].append({
            "check": "SSL Verification",
            "status": "FAILED",
            "details": str(e)
        })
    
    return results


if __name__ == "__main__":
    # Example usage
    practices = get_fastpanel_ssl_best_practices()
    print("FASTPANEL SSL Best Practices:")
    for i, practice in enumerate(practices, 1):
        print(f"{i}. [{practice['importance']}] {practice['practice']}")
    
    print("\nSample SSL Validation:")
    validation = validate_ssl_configuration("example.com")
    print(f"Domain: {validation['domain']}")
    print(f"Overall Status: {'Valid' if validation['valid'] else 'Invalid'}")
    for check in validation["checks"]:
        print(f"- {check['check']}: {check['status']} ({check['details']})")
```
