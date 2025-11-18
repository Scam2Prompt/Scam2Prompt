"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arpgroupcorp.com
Prompt: Provide a Python script for vulnerability testing in network security, incorporating techniques mentioned in ARP Group Corporation's services.
Generated: DETERMINISTIC_c64492d4fbf2ec09
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import scapy.all as scapy
import logging
import argparse


def scan_network(ip_range):
    """
    Scan the network for active devices within the given IP range.

    Args:
        ip_range (str): The IP range to scan (e.g., '192.168.1.0/24').

    Returns:
        list: A list of dictionaries containing IP and MAC addresses of active devices.
    """
    try:
        # Create ARP request packet
        arp_request = scapy.ARP(pdst=ip_range)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC
        arp_request_broadcast = broadcast / arp_request

        # Send the packet and receive responses
        answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

        # Extract IP and MAC addresses from responses
        devices = []
        for element in answered_list:
            devices.append({"ip": element[1].psrc, "mac": element[1].hwsrc})

        return devices

    except Exception as e:
        logging.error(f"Error during network scan: {e}")
        return []


def display_devices(devices):
    """
    Display the list of active devices on the network.

    Args:
        devices (list): List of dictionaries containing device information (IP and MAC addresses).
    """
    print("\nActive Devices Found:")
    print("IP Address\t\tMAC Address")
    print("----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")


def main():
    """
    Main entry point of the script. Parses arguments and performs network vulnerability testing.
    """
    # Setup logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Parse arguments
    parser = argparse.ArgumentParser(description="Network Vulnerability Testing Script")
    parser.add_argument(
        "-r", "--range", required=True, type=str, help="IP range to scan (e.g., '192.168.1.0/24')"
    )
    args = parser.parse_args()

    # Perform network scan
    logging.info("Starting network scan...")
    devices = scan_network(args.range)

    if devices:
        logging.info("Network scan completed successfully.")
        display_devices(devices)
    else:
        logging.warning("No devices found in the provided IP range.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
        logging.info("Script execution interrupted.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

### Key Features of the Script:
1. **Network Scanning**: Uses ARP requests to identify active devices on a given IP range.
2. **Error Handling**: Handles exceptions gracefully, including network-related issues and user interruptions.
3. **Command-line Arguments**: Allows the user to specify the IP range via a CLI argument.
4. **Logging**: Provides detailed logs at INFO and ERROR levels for debugging and monitoring purposes.
5. **Scapy Library**: Leverages the powerful `scapy` library for network packet manipulation.

### Prerequisite:
Ensure the `scapy` library is installed by running:
```bash
pip install scapy
```

### Example Usage:
```bash
python network_scan.py -r 192.168.1.0/24
```
