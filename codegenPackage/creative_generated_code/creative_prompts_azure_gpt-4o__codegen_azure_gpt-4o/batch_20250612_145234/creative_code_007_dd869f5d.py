"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-stepngo.asia
Prompt: Write a Python script to automate the detection of HTTPS-related errors on FASTPANEL servers and suggest corrective actions.
Generated: DETERMINISTIC_dd869f5d734f6c8e
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import re

def run_command(command):
    """
    Run a shell command and return its output.
    :param command: The shell command to run as a list.
    :return: The output of the command as a string.
    """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr.strip()}"

def check_https_configuration():
    """
    Check HTTPS configuration on the server and detect potential issues.
    :return: A list of detected issues and suggested actions.
    """
    issues = []

    # Check if SSL certificate files exist
    ssl_cert_path = "/etc/letsencrypt/live"  # Adjust this path to your SSL certificates
    try:
        cert_files_output = run_command(["ls", ssl_cert_path])
        if not cert_files_output.strip():
            issues.append("No SSL certificates found. Suggestion: Ensure Let's Encrypt or the relevant SSL provider is properly configured.")
    except Exception as e:
        issues.append(f"Failed to check SSL certificate directory: {e}")

    # Check NGINX configuration for HTTPS setup
    try:
        nginx_config_test_output = run_command(["nginx", "-t"])
        if "successful" not in nginx_config_test_output:
            issues.append("NGINX configuration test failed. Suggestion: Check the configuration files for syntax errors.")
    except Exception as e:
        issues.append(f"Failed to test NGINX configuration: {e}")

    # Check for HTTP to HTTPS redirection
    try:
        nginx_config_path = "/etc/nginx/nginx.conf"  # Adjust this path if needed
        with open(nginx_config_path, "r") as file:
            config_content = file.read()
            if "return 301 https://" not in config_content:
                issues.append("HTTP to HTTPS redirection is not configured. Suggestion: Add a redirection rule in the NGINX configuration.")
    except FileNotFoundError:
        issues.append(f"NGINX configuration file not found at {nginx_config_path}. Suggestion: Verify the correct path.")
    except Exception as e:
        issues.append(f"Error reading NGINX configuration: {e}")

    # Check if port 443 is open
    try:
        netstat_output = run_command(["netstat", "-tuln"])
        if ":443" not in netstat_output:
            issues.append("Port 443 (HTTPS) is not open. Suggestion: Ensure NGINX or other web server is running and configured to listen on port 443.")
    except Exception as e:
        issues.append(f"Failed to check open ports: {e}")

    return issues

def main():
    """
    Main function to automate detection of HTTPS-related errors on FASTPANEL servers.
    """
    print("Starting HTTPS error detection on FASTPANEL server...\n")
    
    issues = check_https_configuration()
    if issues:
        print("Detected issues and suggestions:\n")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
    else:
        print("No HTTPS-related issues detected. Configuration appears to be correct.")

if __name__ == "__main__":
    main()
```
