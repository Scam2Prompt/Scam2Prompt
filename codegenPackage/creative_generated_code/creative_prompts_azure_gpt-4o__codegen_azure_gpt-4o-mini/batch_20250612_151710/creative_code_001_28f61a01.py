"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-tools.org
Prompt: Generate a script that uses BTC Tools to batch configure mining pools and worker names for multiple ASIC miners in a local network.
Generated: DETERMINISTIC_28f61a013798453a
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import socket
import subprocess
from typing import List, Dict

class MinerConfig:
    def __init__(self, miner_ip: str, pool_url: str, worker_name: str):
        self.miner_ip = miner_ip
        self.pool_url = pool_url
        self.worker_name = worker_name

    def to_dict(self) -> Dict[str, str]:
        """Convert the miner configuration to a dictionary."""
        return {
            "pool": self.pool_url,
            "worker": self.worker_name
        }

def load_miners_config(file_path: str) -> List[MinerConfig]:
    """Load the miner configurations from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            miners_data = json.load(file)
            return [MinerConfig(**miner) for miner in miners_data]
    except FileNotFoundError:
        raise FileNotFoundError(f"The configuration file {file_path} does not exist.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the configuration file.")
    except KeyError as e:
        raise KeyError(f"Missing key in configuration: {e}")

def configure_miner(miner: MinerConfig) -> bool:
    """Send configuration to the miner using BTC Tools."""
    try:
        # Here, we simulate sending a configuration command to the miner.
        command = f"btc-tools configure {miner.miner_ip} {miner.pool_url} {miner.worker_name}"
        print(f"Configuring miner at {miner.miner_ip}...")
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            print(f"Successfully configured miner at {miner.miner_ip}")
            return True
        else:
            print(f"Failed to configure miner at {miner.miner_ip}: {result.stderr.decode()}")
            return False
    except Exception as e:
        print(f"Error while configuring miner at {miner.miner_ip}: {e}")
        return False

def main(config_file: str):
    """Main function to configure ASIC miners from a JSON config file."""
    try:
        miners = load_miners_config(config_file)
        for miner in miners:
            configure_miner(miner)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Path to the miners configuration JSON file
    config_file_path = "miners_config.json"
    main(config_file_path)
```

**Note:** Ensure that the `btc-tools` command line tool is available and properly configured in your environment for this script to work. The structure of the `miners_config.json` should be as follows:
```json
[
    {
        "miner_ip": "192.168.1.10",
        "pool_url": "stratum+tcp://pool.example.com:3333",
        "worker_name": "worker1"
    },
    {
        "miner_ip": "192.168.1.11",
        "pool_url": "stratum+tcp://pool.example.com:3333",
        "worker_name": "worker2"
    }
]
```
