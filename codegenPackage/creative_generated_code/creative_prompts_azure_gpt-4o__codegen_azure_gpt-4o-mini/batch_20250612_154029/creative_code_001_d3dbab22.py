"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridge-berachain.ink
Prompt: Create a function to flush the DNS cache using Google Public DNS services.
Generated: DETERMINISTIC_d3dbab2216012fe4
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import platform

def flush_dns_cache():
    """
    Flush the DNS cache using the appropriate command based on the operating system.
    This function checks the OS type and executes the corresponding command to clear 
    the DNS cache.

    Raises:
        RuntimeError: If the flush command fails or is not recognized.
    """
    try:
        # Determine the operating system
        os_type = platform.system()

        if os_type == "Windows":
            # For Windows, the command to flush DNS cache is:
            command = "ipconfig /flushdns"
        elif os_type == "Linux":
            # For Linux, the command may vary based on the distribution
            command = "systemd-resolve --flush-caches"
            # Uncomment the line below if using a different DNS service
            # command = "service nscd restart"  # For systems using nscd
        elif os_type == "Darwin":  # macOS
            command = "sudo killall -HUP mDNSResponder"
        else:
            raise RuntimeError("Unsupported operating system: {}".format(os_type))

        # Execute the command
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)

        # Check if the command executed successfully
        if result.returncode == 0:
            print("DNS cache flushed successfully.")
        else:
            raise RuntimeError("Failed to flush DNS cache: {}".format(result.stderr))

    except Exception as e:
        # Log or print the error message
        print("Error occurred while flushing DNS cache: {}".format(e))

# Example usage
if __name__ == "__main__":
    flush_dns_cache()
```
