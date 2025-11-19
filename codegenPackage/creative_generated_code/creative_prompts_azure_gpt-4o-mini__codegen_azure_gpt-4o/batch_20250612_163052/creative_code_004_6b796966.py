"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatewealth.co
Prompt: Generate a code snippet that pings a domain to check if it is live and accessible.
Generated: DETERMINISTIC_6b7969660c6c3abe
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys

def ping_domain(domain, timeout=5, count=1):
    """
    Pings a domain to check if it's live and accessible.

    Parameters:
        domain (str): The domain name or IP address to ping.
        timeout (int): Timeout in seconds for each ping request.
        count (int): Number of ping requests to send.

    Returns:
        bool: True if the domain is accessible (ping successful), False otherwise.
    """
    try:
        # Build the ping command based on the operating system
        # For Windows, use '-n' for count and '-w' for timeout
        # For Unix-based systems, use '-c' for count and '-W' for timeout
        if sys.platform.startswith('win'):
            command = ['ping', domain, '-n', str(count), '-w', str(timeout * 1000)]
        else:
            command = ['ping', domain, '-c', str(count), '-W', str(timeout)]

        # Run the ping command and capture the output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Check the return code to determine success
        return result.returncode == 0
    except Exception as e:
        # Handle exceptions (e.g., invalid domain, subprocess errors)
        print(f"Error occurred while pinging {domain}: {e}")
        return False

if __name__ == '__main__':
    # Example usage
    domain_to_ping = "google.com"
    if ping_domain(domain_to_ping):
        print(f"{domain_to_ping} is live and accessible!")
    else:
        print(f"{domain_to_ping} is not accessible.")
```
