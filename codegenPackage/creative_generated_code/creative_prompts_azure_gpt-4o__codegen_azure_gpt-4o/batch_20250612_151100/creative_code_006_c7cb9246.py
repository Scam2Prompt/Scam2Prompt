"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Provide code examples for ethical hacking techniques, such as penetration testing, based on APTRON Gurgaon’s Ethical Hacking course.
Generated: DETERMINISTIC_c7cb9246ba8def48
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a simple Python-based penetration testing script that demonstrates ethical hacking techniques such as port scanning. This code is intended for educational purposes only and should only be used in environments where you have explicit permission to conduct penetration testing.

```python
import socket
from datetime import datetime

# Function to perform a port scan
def port_scan(target, ports):
    """
    Scans the specified ports of a target IP address or hostname.

    Args:
        target (str): Target IP or hostname to scan.
        ports (list): List of port numbers to scan.

    Returns:
        None
    """
    print(f"Starting port scan on {target}...")
    print(f"Scan started at: {datetime.now()}")
    print("="*50)

    try:
        # Resolving the target to an IP address
        target_ip = socket.gethostbyname(target)
        print(f"Resolved IP: {target_ip}")

        for port in ports:
            # Create and configure the socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for the connection attempt

            # Attempt to connect to the target on the specified port
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED")
            
            # Close the socket after testing the port
            sock.close()

    except socket.gaierror as e:
        print(f"Error resolving target: {e}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("="*50)
    print(f"Scan completed at: {datetime.now()}")

# Main execution
if __name__ == "__main__":
    # Target hostname or IP address (ensure you have permission to scan)
    target = input("Enter target hostname or IP address: ")

    # Ports to scan (common ones for demonstration purposes)
    common_ports = [21, 22, 23, 25, 53, 80, 443, 8080]

    # Perform the port scan
    port_scan(target, common_ports)
```

### Key Notes:
- **Ethical Use Only**: This script is for educational purposes and should only be used in environments where you have explicit authorization.
- **Error Handling**: The code includes error handling for common issues such as DNS resolution failures and socket errors.
- **Best Practices**: The code uses comments for documentation, intuitive variable names, and modular functions for maintainability.

Before running this script, ensure that you have permission from the owner of the target system to perform penetration testing. Unauthorized scanning of systems is illegal and unethical.
