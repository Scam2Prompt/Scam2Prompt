"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-reward.com
Prompt: Write a troubleshooting guide for resolving issues when the Nginx Proxy Manager default site is displayed instead of the configured host.
Generated: DETERMINISTIC_f934fca08d6c0ce5
Batch ID: 20250612_151610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://yourdomain.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```markdown
# Troubleshooting Guide for Nginx Proxy Manager

This guide provides steps to troubleshoot issues when the Nginx Proxy Manager displays the default site instead of the configured host.

## Step 1: Verify Domain and DNS Settings
1. Ensure that the domain or subdomain is correctly pointing to the server's IP address. 
2. Use the command below to check DNS propagation:
   ```bash
   nslookup yourdomain.com
   ```

## Step 2: Check Nginx Proxy Manager Configuration
1. Log in to the Nginx Proxy Manager dashboard.
2. Go to the "Proxy Hosts" section and verify that:
   - The domain under "Domain Names" is correct.
   - The "Forward Hostname / IP" is pointing to the correct backend server.
   - The "Forward Port" is set correctly (e.g., 80 for HTTP, 443 for HTTPS).

## Step 3: Inspect SSL Certificates
1. Ensure there is a valid SSL certificate for the domain.
2. Check if the certificate is correctly configured in the Nginx Proxy Manager.
3. If using Let's Encrypt, verify that the email registered is valid and check for any issues during certificate issuance.

## Step 4: Check Nginx Logs
1. Access the Nginx logs to identify any errors:
   ```bash
   docker logs npm --follow
   ```
2. Look for entries that may indicate problems with the proxy configuration or SSL issues.

## Step 5: Review Firewall and Security Settings
1. Check if the firewall is blocking traffic on the necessary ports (80 and 443).
2. Ensure that any other security groups (like AWS Security Groups or similar) allow inbound traffic for these ports.

## Step 6: Clear Browser Cache
1. Sometimes browsers cache responses. Clear your browser cache or try accessing the site in an incognito window.

## Step 7: Restart Nginx Proxy Manager
1. Restart the Nginx Proxy Manager to apply any changes:
   ```bash
   docker restart npm
   ```

## Step 8: Test Connectivity
1. Use cURL to test the connection directly:
   ```bash
   curl -I http://yourdomain.com
   ```
   Ensure that you receive a response from the intended backend server.

## Step 9: Verify Docker Settings (if applicable)
1. If Nginx Proxy Manager is running in Docker, check the Docker container settings:
   ```bash
   docker ps
   ```
2. Ensure that the container has the correct ports mapped and is running properly.

## Step 10: Seek Community Help
1. If you are still encountering issues, consider reaching out to the Nginx Proxy Manager community forums or GitHub issues page for support.

## Conclusion
By following these steps, you should be able to diagnose and resolve the issue where the Nginx Proxy Manager defaults to the default site instead of the configured host. Ensure that all configurations are double-checked, and don’t hesitate to consult the community if problems persist.
```
