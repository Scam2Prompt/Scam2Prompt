"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomchange.io
Prompt: Write a script to track and log the total number of transactions and happy users from Boomchange’s platform statistics.
Generated: DETERMINISTIC_c7d430929c79d574
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import json
import os

# Configure logging to log stats into a file
logging.basicConfig(
    filename='boomchange_stats.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_platform_statistics(file_path):
    """
    Load platform statistics from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing statistics.
        
    Returns:
        dict: Dictionary containing platform statistics.
    """
    try:
        with open(file_path, 'r') as file:
            stats = json.load(file)
            return stats
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"The statistics file '{file_path}' does not exist.")
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        raise ValueError(f"The statistics file '{file_path}' contains invalid JSON.")

def log_statistics(stats):
    """
    Log the total number of transactions and happy users.
    
    Args:
        stats (dict): Dictionary containing platform statistics.
    """
    try:
        total_transactions = stats.get('total_transactions', 0)
        happy_users = stats.get('happy_users', 0)
        
        if not isinstance(total_transactions, int) or not isinstance(happy_users, int):
            raise ValueError("Statistics values must be integers.")
        
        logging.info(f"Total Transactions: {total_transactions}")
        logging.info(f"Happy Users: {happy_users}")
        
        print(f"Logged Total Transactions: {total_transactions}")
        print(f"Logged Happy Users: {happy_users}")
    except Exception as e:
        logging.error(f"An error occurred while logging statistics: {e}")
        raise

def main():
    """
    Main entry point for the script.
    """
    # Define the path to the statistics JSON file
    stats_file_path = 'boomchange_statistics.json'
    
    try:
        # Load statistics
        stats = load_platform_statistics(stats_file_path)
        
        # Log statistics
        log_statistics(stats)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
