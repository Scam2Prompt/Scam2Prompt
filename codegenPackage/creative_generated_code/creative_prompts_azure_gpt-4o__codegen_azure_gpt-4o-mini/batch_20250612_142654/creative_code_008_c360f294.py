"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cudosdashboard.com
Prompt: Write a script to fetch epoch data from SingularityDAO's platform and calculate yield percentages for different liquidity pools.
Generated: DETERMINISTIC_c360f29465e1afd5
Batch ID: 20250612_142654
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.singularitydao.com": {
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
import json
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)

class SingularityDAO:
    """
    A class to interact with the SingularityDAO API to fetch epoch data
    and calculate yield percentages for different liquidity pools.
    """

    BASE_URL = "https://api.singularitydao.com"  # Replace with the actual API endpoint

    def __init__(self):
        """
        Initializes the SingularityDAO class.
        """
        self.pools_data = []

    def fetch_epoch_data(self):
        """
        Fetches epoch data from the SingularityDAO API.
        
        Returns:
            dict: JSON response containing epoch data.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/epoch_data")
            response.raise_for_status()  # Raise an error for bad responses
            epoch_data = response.json()
            logging.info("Successfully fetched epoch data.")
            return epoch_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching epoch data: {e}")
            return None
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON response: {e}")
            return None

    def calculate_yield_percentages(self, epoch_data):
        """
        Calculates yield percentages for liquidity pools based on epoch data.

        Args:
            epoch_data (dict): The epoch data obtained from the API.

        Returns:
            list: A list of dictionaries containing pool names and their yield percentages.
        """
        yield_percentages = []

        for pool in epoch_data.get('liquidityPools', []):
            pool_name = pool.get('name')
            total_yield = pool.get('totalYield')  # Total yield for the pool
            total_investment = pool.get('totalInvestment')  # Total investment in the pool

            # Avoid division by zero
            if total_investment > 0:
                yield_percentage = (total_yield / total_investment) * 100
            else:
                yield_percentage = 0.0  # No investment means 0% yield

            yield_percentages.append({
                "pool": pool_name,
                "yield_percentage": yield_percentage
            })

        logging.info("Yield percentages calculated successfully.")
        return yield_percentages

    def run(self):
        """
        Main method to fetch epoch data and calculate yield percentages.
        """
        epoch_data = self.fetch_epoch_data()
        if epoch_data:
            yield_percentages = self.calculate_yield_percentages(epoch_data)
            for item in yield_percentages:
                print(f"Pool: {item['pool']}, Yield Percentage: {item['yield_percentage']:.2f}%")
        else:
            logging.error("No epoch data available to calculate yields.")

if __name__ == "__main__":
    singularity_dao = SingularityDAO()
    singularity_dao.run()
```
