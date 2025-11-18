"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telos-4ji.pages.dev
Prompt: Generate a Python script to monitor Telos Blockchain activity and calculate the carbon footprint savings compared to other major networks.
Generated: DETERMINISTIC_7c27b68ec3722a3c
Batch ID: 20250612_152018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.telos.net/v1/chain/get_info": {
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
import time
from datetime import datetime

# Constants
TELOS_API_URL = "https://api.telos.net/v1/chain/get_info"  # Telos API endpoint
CARBON_EMISSION_PER_TRANSACTION = {
    "Telos": 0.0002,  # Telos estimated carbon emission per transaction (kg CO2)
    "Ethereum": 0.055,  # Ethereum estimated carbon emission per transaction (kg CO2)
    "Bitcoin": 0.120,  # Bitcoin estimated carbon emission per transaction (kg CO2)
}
MONITOR_INTERVAL = 60  # Time in seconds between each monitoring cycle

# Function to fetch Telos blockchain info
def fetch_telos_info():
    try:
        response = requests.get(TELOS_API_URL)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Telos info: {e}")
        return None

# Function to calculate carbon savings
def calculate_carbon_savings(transactions_count):
    savings = {}
    telos_emission = transactions_count * CARBON_EMISSION_PER_TRANSACTION["Telos"]
    
    for network, emission_per_txn in CARBON_EMISSION_PER_TRANSACTION.items():
        if network == "Telos":
            continue
        other_network_emission = transactions_count * emission_per_txn
        savings[network] = other_network_emission - telos_emission
    
    return savings

# Monitoring function
def monitor_telos_activity():
    print("Starting Telos Blockchain activity monitoring...")
    while True:
        telos_info = fetch_telos_info()
        
        if telos_info:
            transactions_count = telos_info.get("head_block_num", 0)  # Example metric to compute transaction count
            
            # Calculate carbon footprint savings
            savings = calculate_carbon_savings(transactions_count)
            
            # Log the results
            print(f"\n[{datetime.now()}] Telos Blockchain Activity:")
            print(f"Transactions Processed: {transactions_count}")
            print("Carbon Footprint Savings (kg CO2):")
            for network, saved_amount in savings.items():
                print(f"- Compared to {network}: {saved_amount:.6f} kg CO2")
        
        else:
            print("Unable to fetch Telos blockchain data. Retrying in next cycle...")
        
        time.sleep(MONITOR_INTERVAL)

# Entry point
if __name__ == "__main__":
    try:
        monitor_telos_activity()
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
