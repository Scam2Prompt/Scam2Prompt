"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celaroopl.xyz
Prompt: Generate a script to calculate the total interest paid across all lending pools using data from Clearpool's API.
Generated: DETERMINISTIC_619b8e42742e02a7
Batch ID: 20250612_153812
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.clearpool.xyz/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClearpoolAPI:
    BASE_URL = "https://api.clearpool.xyz/v1"

    @staticmethod
    def get_lending_pools():
        """Fetches the lending pools data from Clearpool's API."""
        try:
            response = requests.get(f"{ClearpoolAPI.BASE_URL}/lending_pools")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching lending pools: {e}")
            return None

class InterestCalculator:
    @staticmethod
    def calculate_total_interest(pools):
        """Calculates the total interest paid across all lending pools.

        Args:
            pools (list): List of lending pool data.

        Returns:
            float: Total interest paid.
        """
        total_interest = 0.0

        for pool in pools:
            try:
                interest = float(pool.get("interest_paid", 0))
                total_interest += interest
            except (ValueError, TypeError) as e:
                logging.warning(f"Invalid interest value in pool {pool.get('id')}: {e}")

        return total_interest

def main():
    """Main function to execute the interest calculation."""
    logging.info("Fetching lending pools data...")
    
    pools = ClearpoolAPI.get_lending_pools()
    
    if pools is None:
        logging.error("Failed to retrieve lending pools data.")
        return

    total_interest = InterestCalculator.calculate_total_interest(pools)
    logging.info(f"Total interest paid across all lending pools: ${total_interest:.2f}")

if __name__ == "__main__":
    main()
```
