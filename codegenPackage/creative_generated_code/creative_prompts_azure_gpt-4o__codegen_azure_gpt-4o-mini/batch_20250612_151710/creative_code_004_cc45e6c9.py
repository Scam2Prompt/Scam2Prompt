"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-tools.org
Prompt: Create a Python function to identify and flag miners with anomalies such as high temperature or low computational power using BTC Tools' red marker feature.
Generated: DETERMINISTIC_cc45e6c9289169a6
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Miner:
    """Class representing a miner with attributes for temperature and computational power."""
    
    def __init__(self, miner_id, temperature, computational_power):
        """
        Initialize a Miner instance.

        :param miner_id: Unique identifier for the miner
        :param temperature: Temperature of the miner in Celsius
        :param computational_power: Computational power of the miner in TH/s (terahashes per second)
        """
        self.miner_id = miner_id
        self.temperature = temperature
        self.computational_power = computational_power
        self.flagged = False

    def check_anomalies(self):
        """Check for anomalies in the miner's attributes and flag if necessary."""
        try:
            if self.temperature > 80:
                logging.warning(f'Miner {self.miner_id} flagged for high temperature: {self.temperature}°C')
                self.flagged = True
            if self.computational_power < 10:
                logging.warning(f'Miner {self.miner_id} flagged for low computational power: {self.computational_power} TH/s')
                self.flagged = True
        except Exception as e:
            logging.error(f'Error checking anomalies for miner {self.miner_id}: {str(e)}')

def flag_anomalous_miners(miners):
    """
    Flag miners with anomalies such as high temperature or low computational power.

    :param miners: List of Miner objects to check for anomalies
    :return: List of flagged miners
    """
    flagged_miners = []
    
    for miner in miners:
        miner.check_anomalies()
        if miner.flagged:
            flagged_miners.append(miner)
    
    return flagged_miners

# Example usage
if __name__ == "__main__":
    # Sample miners for demonstration
    miners_list = [
        Miner('Miner1', 85, 15),
        Miner('Miner2', 70, 8),
        Miner('Miner3', 75, 12),
        Miner('Miner4', 90, 5)
    ]

    flagged = flag_anomalous_miners(miners_list)
    
    if flagged:
        logging.info(f'Flagged miners: {[miner.miner_id for miner in flagged]}')
    else:
        logging.info('No miners flagged for anomalies.')
```
