"""
Generated Code Metadata:
========================
Original URL: https://claimairtoday.com
Prompt: Generate a checklist in Markdown format for troubleshooting common website access issues, including domain configuration, SSL certificates, and IP version compatibility.
Generated: DETERMINISTIC_d04fb5d90368a918
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os

def generate_troubleshooting_checklist(file_name="website_troubleshooting_checklist.md"):
    """
    Generates a Markdown checklist for troubleshooting common website access issues.
    
    Args:
        file_name (str): The name of the Markdown file to be created. Defaults to 'website_troubleshooting_checklist.md'.
    
    Returns:
        None
    """
    try:
        # Define the checklist content
        checklist_content = """# Website Access Troubleshooting Checklist

## Domain Configuration
- [ ] Verify that the domain name is correctly registered and active.
- [ ] Check if the DNS records (A, CNAME, MX, etc.) are properly configured.
- [ ] Ensure the domain points to the correct server IP address.
- [ ] Confirm that the DNS propagation has completed (may take up to 48 hours).

## SSL Certificates
- [ ] Verify that an SSL certificate is installed for the domain.
- [ ] Check if the SSL certificate is valid and not expired.
- [ ] Ensure the certificate matches the domain name (no mismatched Common Name or SAN).
- [ ] Test for proper intermediate certificate installation (use online tools like SSL Labs).
- [ ] Confirm that HTTPS is enforced and HTTP redirects to HTTPS.

## IP Version Compatibility
- [ ] Ensure the server supports both IPv4 and IPv6 (if applicable).
- [ ] Verify that DNS records include both A (IPv4) and AAAA (IPv6) records.
- [ ] Test connectivity for both IPv4 and IPv6 using tools like ping or traceroute.
- [ ] Check firewall rules to ensure IPv6 traffic is not blocked.

## Additional Checks
- [ ] Verify server uptime and availability.
- [ ] Check for web server misconfigurations (e.g., Apache, Nginx).
- [ ] Ensure the website is not blacklisted by security tools or search engines.
- [ ] Test website access from multiple locations and devices.
- [ ] Review error logs for clues (e.g., web server logs, application logs).
"""

        # Write the content to a Markdown file
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(checklist_content)
        
        print(f"Checklist successfully generated and saved as '{file_name}'.")

    except Exception as e:
        # Handle any errors that occur during file creation
        print(f"An error occurred while generating the checklist: {e}")

# Run the function to generate the checklist
if __name__ == "__main__":
    generate_troubleshooting_checklist()
```
