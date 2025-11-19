"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defillama-app.github.io
Prompt: Describe how to build a borrowing aggregator that pulls market-wide data from DefiLlama's resources.
Generated: DETERMINISTIC_d13dd0aad8a14dc1
Batch ID: 20250612_155650
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi": {
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

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DefiBorrowingAggregator:
    """
    A class to aggregate borrowing data from DeFiLlama's resources.
    """

    def __init__(self):
        """
        Initializes the borrowing aggregator with the base URL for DeFiLlama API.
        """
        self.base_url = "https://api.llama.fi"

    def fetch_borrowing_data(self):
        """
        Fetches market-wide borrowing data from DeFiLlama's API.

        Returns:
            dict: A dictionary containing borrowing data.

        Raises:
            ValueError: If the response contains an error or invalid data.
        """
        endpoint = f"{self.base_url}/borrowing"
        logging.info("Fetching borrowing data from: %s", endpoint)

        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            data = response.json()

            if "error" in data:
                raise ValueError(f"API returned an error: {data['error']}")

            logging.info("Successfully fetched borrowing data.")
            return data
        except requests.exceptions.RequestException as e:
            logging.error("Error occurred while fetching borrowing data: %s", e)
            return None
        except ValueError as ve:
            logging.error("Error in API response: %s", ve)
            return None

    def aggregate_data(self, data):
        """
        Aggregates borrowing data for summary metrics.

        Args:
            data (dict): Raw borrowing data from the API.

        Returns:
            dict: Aggregated borrowing metrics.
        """
        logging.info("Aggregating borrowing data.")

        if not data or "protocols" not in data:
            logging.warning("No valid data to aggregate.")
            return None

        total_borrowed = sum(
            protocol.get("totalBorrowedUSD", 0) for protocol in data["protocols"]
        )
        total_protocols = len(data["protocols"])

        logging.info("Data aggregation complete.")
        return {
            "total_borrowed_usd": total_borrowed,
            "total_protocols": total_protocols,
        }

    def run(self):
        """
        Executes the borrowing aggregator workflow.

        Returns:
            dict: Aggregated borrowing metrics or None if an error occurred.
        """
        logging.info("Starting borrowing aggregator workflow.")

        borrowing_data = self.fetch_borrowing_data()
        if borrowing_data is None:
            logging.error("Unable to fetch borrowing data. Exiting workflow.")
            return None

        aggregated_data = self.aggregate_data(borrowing_data)
        if aggregated_data is None:
            logging.error("Unable to aggregate borrowing data. Exiting workflow.")
            return None

        logging.info("Borrowing aggregator workflow completed successfully.")
        return aggregated_data


if __name__ == "__main__":
    # Main entry point for the borrowing aggregator
    aggregator = DefiBorrowingAggregator()

    # Running the workflow
    result = aggregator.run()
    if result:
        logging.info("Aggregated Borrowing Data: %s", result)
    else:
        logging.error("Borrowing aggregator failed to produce results.")
```
