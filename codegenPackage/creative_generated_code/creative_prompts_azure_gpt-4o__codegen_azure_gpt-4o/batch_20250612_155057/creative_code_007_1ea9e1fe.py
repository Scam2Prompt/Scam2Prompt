"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadday23.testnet.nfts2.me
Prompt: Develop a tool to track and maximize referral earnings by analyzing minting activity through referral links on the Monad Day 23 platform.
Generated: DETERMINISTIC_1ea9e1fea17d4d38
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ReferralTracker:
    """
    A tool to track and maximize referral earnings by analyzing minting activity through referral links.

    Attributes:
        referral_data (Dict): Dictionary holding referral link metadata and minting activity.
        earnings (Dict): Dictionary holding earnings data for each referral link.
    """

    def __init__(self):
        """
        Initialize the ReferralTracker with empty data.
        """
        self.referral_data = {}
        self.earnings = {}

    def load_data(self, file_path: str) -> None:
        """
        Load referral and minting data from a JSON file.

        Args:
            file_path (str): Path to the JSON file containing referral data.

        Raises:
            FileNotFoundError: If file_path does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.referral_data = json.load(file)
                logging.info("Referral data loaded successfully.")
        except FileNotFoundError:
            logging.error("File not found: %s", file_path)
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON data from file: %s", file_path)
            raise

    def analyze_data(self) -> None:
        """
        Analyze minting activity from referral links and calculate earnings.
        """
        for referral_link, activities in self.referral_data.items():
            total_earnings = 0
            for activity in activities:
                mint_amount = activity.get("mint_amount", 0)
                referral_rate = activity.get("referral_rate", 0)
                total_earnings += mint_amount * referral_rate
            self.earnings[referral_link] = total_earnings
        logging.info("Data analysis completed. Earnings calculated for all referral links.")

    def maximize_earnings(self) -> List[str]:
        """
        Determine the referral links with the highest earnings.

        Returns:
            List[str]: A list of referral links ordered by highest earnings.
        """
        sorted_links = sorted(self.earnings, key=self.earnings.get, reverse=True)
        logging.info("Referral links sorted by earnings.")
        return sorted_links

    def display_earnings(self) -> None:
        """
        Display earnings for each referral link.
        """
        logging.info("Displaying referral earnings:")
        for referral_link, earnings in self.earnings.items():
            print(f"Referral Link: {referral_link} | Earnings: {earnings:.2f}")

    def save_earnings_report(self, file_path: str) -> None:
        """
        Save earnings data to a JSON file.

        Args:
            file_path (str): Path to the file where earnings data will be saved.

        Raises:
            IOError: If there is an error writing the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.earnings, file, indent=4)
                logging.info("Earnings report saved successfully to %s", file_path)
        except IOError:
            logging.error("Error saving earnings report to file: %s", file_path)
            raise


if __name__ == "__main__":
    # Example usage
    tracker = ReferralTracker()

    # Load referral minting data from a file (update the file path as necessary)
    try:
        tracker.load_data("referral_data.json")

        # Analyze data and calculate earnings
        tracker.analyze_data()

        # Display the calculated earnings
        tracker.display_earnings()

        # Save the earnings report to a file
        tracker.save_earnings_report("earnings_report.json")

        # Print the top-earning referral links
        top_links = tracker.maximize_earnings()
        print("\nTop Referral Links by Earnings:")
        for link in top_links:
            print(link)

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
```

Ensure you provide the necessary input files (`referral_data.json`) with the correct structure for this program to function.
