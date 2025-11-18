"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.com
Prompt: Create a Python program to analyze the weekly sales data of "BasePaint" NFTs from OpenSea and generate a summary report.
Generated: DETERMINISTIC_b512dabbda666ca2
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1/events": {
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
import datetime
import sys

class NFTSalesAnalyzer:
    """
    This class fetches and analyzes weekly sales data for "BasePaint" NFTs from OpenSea.
    """
    def __init__(self, collection_slug):
        self.collection_slug = collection_slug
        self.api_url = f"https://api.opensea.io/api/v1/events"
        self.session = requests.Session()
        self.headers = {
            "Accept": "application/json",
            "User-Agent": "BasePaint-NFT-Sales-Analyzer"
        }

    def fetch_weekly_sales(self):
        """
        Fetches sales data from OpenSea for the past 7 days.
        
        :return: List of events representing NFT sales for the given collection.
        """
        end_time = datetime.datetime.utcnow()
        start_time = end_time - datetime.timedelta(days=7)
        params = {
            "collection_slug": self.collection_slug,
            "event_type": "successful",
            "only_opensea": "false",
            "occurred_after": int(start_time.timestamp()),  # Start of the 7-day window
            "occurred_before": int(end_time.timestamp()),  # End of the 7-day window
            "limit": 50  # API results per page
        }

        sales_data = []
        while True:
            try:
                response = self.session.get(self.api_url, headers=self.headers, params=params)
                response.raise_for_status()  # Raise an exception for HTTP errors
                data = response.json()
                if "asset_events" not in data or not data["asset_events"]:
                    break  # Exit if no more sales events are returned

                sales_data.extend(data["asset_events"])

                # Update pagination cursor for subsequent requests
                cursor = data.get("next")
                if not cursor:
                    break
                params["cursor"] = cursor
            except requests.exceptions.RequestException as err:
                print(f"Error fetching sales data: {err}", file=sys.stderr)
                break

        return sales_data

    def analyze_sales(self, sales_data):
        """
        Analyzes the sales data and generates a summary report.

        :param sales_data: List of sales events.
        :return: A dictionary containing the summary report.
        """
        total_sales = len(sales_data)
        total_volume = 0.0
        unique_buyers = set()
        unique_sellers = set()

        for sale in sales_data:
            # Extract price (in Ethereum) and buyer/seller information
            price_eth = float(sale.get("total_price", 0)) / (10 ** 18)  # Convert Wei to ETH
            total_volume += price_eth
            buyer_address = sale.get("winner_account", {}).get("address", "Unknown")
            seller_address = sale.get("seller", {}).get("address", "Unknown")
            unique_buyers.add(buyer_address)
            unique_sellers.add(seller_address)

        # Construct the summary report
        summary = {
            "total_sales": total_sales,
            "total_volume_eth": total_volume,
            "unique_buyers_count": len(unique_buyers),
            "unique_sellers_count": len(unique_sellers),
            "average_sale_price_eth": (total_volume / total_sales) if total_sales > 0 else 0.0
        }

        return summary

    def generate_report(self):
        """
        Main method to fetch sales data, analyze it, and print a summary report.
        """
        print("Fetching weekly sales data...")
        sales_data = self.fetch_weekly_sales()
        if not sales_data:
            print("No sales data found for the past week.")
            return

        print("Analyzing sales data...")
        summary = self.analyze_sales(sales_data)

        # Display the summary report
        print("\nWeekly Sales Report for 'BasePaint' NFTs:")
        print("------------------------------------------------")
        print(f"Total Sales: {summary['total_sales']}")
        print(f"Total Volume: {summary['total_volume_eth']:.2f} ETH")
        print(f"Unique Buyers: {summary['unique_buyers_count']}")
        print(f"Unique Sellers: {summary['unique_sellers_count']}")
        print(f"Average Sale Price: {summary['average_sale_price_eth']:.2f} ETH")
        print("------------------------------------------------")


if __name__ == "__main__":
    # Define the collection slug for "BasePaint" NFTs
    COLLECTION_SLUG = "basepaint"

    # Initialize and run the NFT sales analyzer
    analyzer = NFTSalesAnalyzer(COLLECTION_SLUG)
    analyzer.generate_report()
```
