"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-tools.org
Prompt: Write code to import, configure, and scan network segments for ASIC miners using BTC Tools' network management features.
Generated: DETERMINISTIC_c3163634d691d62b
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ipaddress
from typing import List

# Function to scan a network segment for active devices
def scan_network_segment(network_segment: str, port: int = 4028, timeout: float = 1.0) -> List[str]:
    """
    Scans the given network segment for active ASIC miners running BTC Tools.

    Args:
        network_segment (str): CIDR notation of the network segment to scan (e.g., "192.168.1.0/24").
        port (int): The port to check for BTC Tools service (default: 4028).
        timeout (float): Timeout for socket connection in seconds (default: 1.0).

    Returns:
        List[str]: List of IPs where ASIC miners are found.
    """
    active_miners = []
    try:
        # Generate all IP addresses within the network segment
        network = ipaddress.ip_network(network_segment, strict=False)
        for ip in network.hosts():
            ip_address = str(ip)
            try:
                # Create a socket to test the connection
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(timeout)
                    # Attempt to connect to the target IP and port
                    result = sock.connect_ex((ip_address, port))
                    if result == 0:  # Connection successful
                        active_miners.append(ip_address)
            except socket.error as e:
                # Log error (optional debugging)
                print(f"Error connecting to {ip_address}:{port} - {e}")
    except ValueError as e:
        # Handle invalid network segment
        raise ValueError(f"Invalid network segment: {network_segment}") from e

    return active_miners

# Main function for demonstration purposes
if __name__ == "__main__":
    # Example: Scanning the network segment 192.168.1.0/24 for ASIC miners
    network_segment = "192.168.1.0/24"
    port_to_scan = 4028  # Default BTC Tools port
    try:
        print(f"Scanning network segment: {network_segment} for ASIC miners...")
        miners = scan_network_segment(network_segment, port_to_scan)
        if miners:
            print(f"Active ASIC miners found at: {miners}")
        else:
            print("No active ASIC miners found.")
    except Exception as e:
        print(f"An error occurred during scanning: {e}")
```
