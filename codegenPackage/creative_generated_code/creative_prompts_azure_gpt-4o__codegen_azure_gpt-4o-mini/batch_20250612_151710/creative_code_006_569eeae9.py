"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-tools.org
Prompt: Write code to perform batch software updates for selected ASIC miners using BTC Tools.
Generated: DETERMINISTIC_569eeae93107ed39
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
import os
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ASICMinerUpdater:
    def __init__(self, miners: List[str], btc_tools_path: str):
        """
        Initializes the ASICMinerUpdater.

        :param miners: List of ASIC miner IP addresses or hostnames.
        :param btc_tools_path: Path to the BTC Tools executable.
        """
        self.miners = miners
        self.btc_tools_path = btc_tools_path

    def check_tools_path(self):
        """Check if the BTC Tools path is valid."""
        if not os.path.exists(self.btc_tools_path):
            raise FileNotFoundError(f"BTC Tools not found at: {self.btc_tools_path}")

    def update_miner(self, miner_ip: str):
        """
        Updates a single ASIC miner.

        :param miner_ip: IP address or hostname of the miner.
        """
        try:
            logging.info(f"Starting update for miner: {miner_ip}")
            # Replace with the actual command to update the miner using BTC Tools
            command = [self.btc_tools_path, 'update', miner_ip]
            result = subprocess.run(command, capture_output=True, text=True)

            # Check if the command was successful
            if result.returncode == 0:
                logging.info(f"Successfully updated miner: {miner_ip}")
            else:
                logging.error(f"Error updating miner {miner_ip}: {result.stderr}")

        except Exception as e:
            logging.error(f"Exception while updating miner {miner_ip}: {str(e)}")

    def update_all_miners(self):
        """Updates all selected ASIC miners."""
        self.check_tools_path()
        for miner in self.miners:
            self.update_miner(miner)

if __name__ == "__main__":
    # Example usage
    try:
        miner_ips = ['192.168.1.101', '192.168.1.102']  # List of miner IPs
        btc_tools_executable = '/path/to/btc_tools'  # Path to BTC Tools

        updater = ASICMinerUpdater(miners=miner_ips, btc_tools_path=btc_tools_executable)
        updater.update_all_miners()
    except Exception as e:
        logging.critical(f"Critical error: {str(e)}")
```
