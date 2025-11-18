"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p30mag.com
Prompt: Write Python code to automate the process of analyzing follower retention rates after purchasing followers from sites like "دیجی فالوور" or "کافه فالوور" as described on p30mag.com.
Generated: DETERMINISTIC_966109246010b5d3
Batch ID: 20250612_151947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api": {
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
import time
import csv
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(
    filename='follower_analysis.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_followers(api_url: str, account_id: str) -> List[str]:
    """
    Fetch the list of followers for a given account.

    Args:
        api_url (str): The API URL or endpoint to fetch followers.
        account_id (str): The account's unique identifier.

    Returns:
        List[str]: A list of follower usernames/IDs.
    """
    try:
        response = requests.get(f"{api_url}/followers/{account_id}")
        response.raise_for_status()  # Raise an exception for HTTP errors
        followers = response.json().get("followers", [])
        return followers
    except requests.RequestException as e:
        logging.error(f"Failed to fetch followers: {e}")
        return []

def analyze_retention(initial_followers: List[str], current_followers: List[str]) -> Dict[str, float]:
    """
    Analyze follower retention rates.

    Args:
        initial_followers (List[str]): List of follower usernames/IDs at the purchase time.
        current_followers (List[str]): List of current follower usernames/IDs.

    Returns:
        Dict[str, float]: A dictionary containing retention rate and loss percentage.
    """
    initial_count = len(initial_followers)
    current_count = len(current_followers)
    
    if initial_count == 0:
        logging.error("Initial follower count is zero, cannot calculate retention rates.")
        return {"retention_rate": 0.0, "loss_percentage": 100.0}
    
    retention_rate = (current_count / initial_count) * 100
    loss_percentage = 100 - retention_rate

    return {
        "retention_rate": retention_rate,
        "loss_percentage": loss_percentage
    }

def save_results_to_csv(data: Dict[str, float], filename: str) -> None:
    """
    Save retention analysis results to a CSV file.

    Args:
        data (Dict[str, float]): Retention analysis results.
        filename (str): The output file name.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Retention Rate (%)", "Loss Percentage (%)"])
            writer.writerow([data["retention_rate"], data["loss_percentage"]])
        logging.info(f"Results successfully saved to {filename}.")
    except Exception as e:
        logging.error(f"Failed to save results to CSV: {e}")

def main():
    """
    Main function to orchestrate the analysis process.
    """
    # Configurable parameters
    api_url = "https://example.com/api"  # Replace with actual API URL
    account_id = "12345"  # Replace with the actual account ID
    initial_data_file = "initial_followers.csv"
    results_file = "retention_results.csv"

    # Load initial followers from a file (simulating purchase time data)
    try:
        with open(initial_data_file, mode='r', encoding='utf-8') as file:
            initial_followers = [line.strip() for line in file.readlines()]
    except Exception as e:
        logging.error(f"Failed to load initial followers from file: {e}")
        return
    
    # Simulate a waiting period (e.g., days after purchasing followers)
    time.sleep(5)  # Adjust as needed for real-world usage

    # Fetch current followers from the API
    current_followers = fetch_followers(api_url, account_id)
    
    # Perform retention analysis
    results = analyze_retention(initial_followers, current_followers)

    # Save results to a CSV file
    save_results_to_csv(results, results_file)

if __name__ == "__main__":
    main()
```
