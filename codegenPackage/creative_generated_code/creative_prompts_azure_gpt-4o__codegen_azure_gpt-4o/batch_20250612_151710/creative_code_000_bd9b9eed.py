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
import subprocess
import json
import re

def scan_asic_miners(network_segment):
    """
    Scans ASIC miners in a given local network segment using BTC Tools.
    
    Args:
        network_segment (str): The local network segment to scan (e.g., "192.168.1.0/24").
    
    Returns:
        list: A list of dictionaries containing miner details such as computational power,
              temperature, fan speed, and mining pool details.
    """
    try:
        # Run BTC Tools CLI command to scan the network segment
        # Assuming BTC Tools has a CLI command `btctools scan`
        # Replace 'btctools scan' with the actual binary path or command for BTC Tools
        result = subprocess.run(
            ['btctools', 'scan', '--network', network_segment, '--output', 'json'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check if the command ran successfully
        if result.returncode != 0:
            raise RuntimeError(f"BTC Tools scan failed: {result.stderr.strip()}")

        # Parse the JSON output from BTC Tools
        miners_data = json.loads(result.stdout)

        miners_info = []

        for miner in miners_data:
            # Extract relevant information from the miner data
            ip_address = miner.get("ip")
            if not ip_address:
                continue  # Skip entries without an IP address

            computational_power = miner.get("hashrate")
            temperature = miner.get("temperature")
            fan_speed = miner.get("fan_speed")
            mining_pool = miner.get("pool")

            # Organize miner details into a dictionary
            miner_info = {
                "ip_address": ip_address,
                "computational_power": computational_power,
                "temperature": temperature,
                "fan_speed": fan_speed,
                "mining_pool": mining_pool
            }

            miners_info.append(miner_info)

        return miners_info

    except json.JSONDecodeError:
        raise ValueError("Failed to parse BTC Tools output. Ensure JSON format is enabled.")
    except FileNotFoundError:
        raise FileNotFoundError("BTC Tools executable not found. Ensure it is installed and in the PATH.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while scanning ASIC miners: {str(e)}")

def main():
    # Replace with the appropriate local network segment (e.g., "192.168.1.0/24")
    network_segment = "192.168.1.0/24"

    try:
        # Scan ASIC miners in the specified network segment
        asic_miners = scan_asic_miners(network_segment)

        if not asic_miners:
            print("No ASIC miners detected in the network segment.")
        else:
            # Print the retrieved details of each miner
            print("Detected ASIC miners:")
            for miner in asic_miners:
                print(f"IP Address: {miner['ip_address']}")
                print(f"Computational Power: {miner['computational_power']} TH/s")
                print(f"Temperature: {miner['temperature']} °C")
                print(f"Fan Speed: {miner['fan_speed']} RPM")
                print(f"Mining Pool: {miner['mining_pool']}")
                print("-" * 40)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
