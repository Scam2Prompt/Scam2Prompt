"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-tools.org
Prompt: Write Python code to scan ASIC miners in a local network segment using BTC Tools, and retrieve their computational power, temperature, fan speed, and mining pool details.
Generated: DETERMINISTIC_bd9b9eede6b45a20
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
import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
ASIC_MINER_PORT = 4028  # Default port for ASIC miners
NETWORK_SEGMENT = "192.168.1."  # Adjust to your local network segment
IP_RANGE = range(1, 255)  # Scanning range for IP addresses

def get_miner_info(ip_address):
    """Retrieve miner information from a given IP address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout for socket connection
            s.connect((ip_address, ASIC_MINER_PORT))
            request = json.dumps({"command": "summary"}) + '\n'
            s.sendall(request.encode('utf-8'))
            response = s.recv(4096).decode('utf-8')
            return parse_miner_response(response)
    except (socket.timeout, ConnectionRefusedError):
        logging.warning(f"Connection failed for {ip_address}")
    except Exception as e:
        logging.error(f"Error retrieving data from {ip_address}: {e}")
    return None

def parse_miner_response(response):
    """Parse the response from the ASIC miner and return relevant details."""
    try:
        data = json.loads(response.strip())
        # Extract relevant details
        miner_info = {
            "power": data.get("SUMMARY", {}).get("MHS 5s", "N/A"),
            "temperature": data.get("SUMMARY", {}).get("Temperature", "N/A"),
            "fan_speed": data.get("SUMMARY", {}).get("Fan", "N/A"),
            "pool": data.get("SUMMARY", {}).get("Pool", "N/A")
        }
        return miner_info
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON response")
    except KeyError as e:
        logging.error(f"Missing expected key in data: {e}")
    return None

def scan_network():
    """Scan the local network segment for ASIC miners and retrieve their information."""
    miners_info = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_ip = {executor.submit(get_miner_info, f"{NETWORK_SEGMENT}{ip}"): ip for ip in IP_RANGE}
        for future in as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                miner_info = future.result()
                if miner_info:
                    miners_info[ip] = miner_info
                    logging.info(f"Found miner at {ip}: {miner_info}")
            except Exception as e:
                logging.error(f"Error processing IP {ip}: {e}")

    return miners_info

if __name__ == "__main__":
    """Main entry point of the script."""
    logging.info("Starting ASIC miner scan...")
    miners = scan_network()
    logging.info("Scan complete.")
    for ip, info in miners.items():
        print(f"IP: {ip}, Info: {info}")
```
