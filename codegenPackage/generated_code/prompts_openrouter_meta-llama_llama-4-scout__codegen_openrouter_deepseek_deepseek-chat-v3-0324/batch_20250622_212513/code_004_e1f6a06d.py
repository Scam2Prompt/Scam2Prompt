"""
Generated Code Metadata:
========================
Original URL: https://hosico-cat.fun
Prompt: Generate a checklist for troubleshooting website hosting issues, including domain configuration, SSL certificates, and IP version compatibility.
Generated: DETERMINISTIC_e1f6a06d84d7c9f2
Batch ID: 20250622_212513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Website Hosting Troubleshooting Checklist
"""

def generate_checklist():
    checklist = {
        "Domain Configuration": [
            "Verify domain registration is active and not expired",
            "Check DNS records (A, CNAME, MX) for correctness",
            "Ensure nameservers are properly configured",
            "Confirm domain propagation using DNS lookup tools",
            "Check for typos in domain name configuration",
            "Verify domain is not blocked or blacklisted"
        ],
        "SSL Certificates": [
            "Check certificate expiration date",
            "Verify certificate is properly installed on server",
            "Ensure certificate chain is complete",
            "Confirm certificate covers all required subdomains",
            "Check for mixed content warnings",
            "Verify HTTPS redirects are working correctly",
            "Test with SSL checker tools"
        ],
        "IP Version Compatibility": [
            "Check if IPv6 is properly configured (if required)",
            "Verify DNS has both A (IPv4) and AAAA (IPv6) records",
            "Test website accessibility via both IPv4 and IPv6",
            "Check firewall rules for both IP versions",
            "Ensure CDN supports required IP versions",
            "Verify server network interfaces are properly configured"
        ],
        "Server Configuration": [
            "Check web server (Apache/Nginx) is running",
            "Verify correct virtual host configuration",
            "Check for sufficient disk space and memory",
            "Review error logs for recent issues",
            "Confirm correct file permissions",
            "Check for proper .htaccess or web.config settings"
        ],
        "Connectivity": [
            "Test website from different networks/locations",
            "Check for ISP or regional blocking",
            "Verify port 80/443 is open and accessible",
            "Test with VPN to rule out local network issues",
            "Check routing tables and network paths"
        ],
        "Application Level": [
            "Verify database connectivity",
            "Check application error logs",
            "Test with default page to isolate application issues",
            "Confirm required services are running",
            "Check for recent code deployments or changes"
        ]
    }
    
    return checklist

def print_checklist(checklist):
    print("Website Hosting Troubleshooting Checklist\n")
    print("="*50 + "\n")
    
    for category, items in checklist.items():
        print(f"{category}:")
        for i, item in enumerate(items, 1):
            print(f"  {i}. {item}")
        print()
    
    print("="*50)
    print("\nAdditional Notes:")
    print("- Always check server status with hosting provider first")
    print("- Document all changes made during troubleshooting")
    print("- Consider rolling back recent changes if issues started after deployment")

if __name__ == "__main__":
    checklist = generate_checklist()
    print_checklist(checklist)
```
