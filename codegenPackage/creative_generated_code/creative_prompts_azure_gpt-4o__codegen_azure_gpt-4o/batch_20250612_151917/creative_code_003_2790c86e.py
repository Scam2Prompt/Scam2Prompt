"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfi.pages.dev
Prompt: Create a script to compare the governance utility of non-transferable tokens like WLFI with tradable tokens from projects such as Uniswap (UNI) or MakerDAO (MKR).
Generated: DETERMINISTIC_2790c86ecb99b01f
Batch ID: 20250612_151917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to compare the governance utility of non-transferable tokens (e.g., WLFI) 
with tradable tokens (e.g., UNI, MKR).
This script aggregates governance participation data for both token types 
and calculates metrics to analyze utility differences.

Dependencies:
- web3.py for Ethereum blockchain interaction
- pandas for data manipulation
- dotenv for environment variable management

Ensure appropriate API keys and blockchain node endpoints are set in the environment.
"""

import os
import pandas as pd
from web3 import Web3
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Environment variables
INFURA_URL = os.getenv("INFURA_URL")
GOVERNANCE_API_URL = os.getenv("GOVERNANCE_API_URL")  # Example: API endpoint for governance data

if not INFURA_URL or not GOVERNANCE_API_URL:
    raise EnvironmentError("Missing required environment variables: INFURA_URL or GOVERNANCE_API_URL")

# Initialize web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.is_connected():
    raise ConnectionError("Failed to connect to Ethereum node.")

# Governance contracts and token addresses (Replace with actual contract addresses)
TOKENS = {
    "WLFI": {
        "address": "0xWLFI_TOKEN_ADDRESS",  # Replace with WLFI token address
        "type": "non-transferable"
    },
    "UNI": {
        "address": "0xUNI_TOKEN_ADDRESS",  # Replace with Uniswap token address
        "type": "tradable"
    },
    "MKR": {
        "address": "0xMKR_TOKEN_ADDRESS",  # Replace with MakerDAO token address
        "type": "tradable"
    }
}

def fetch_governance_data(token_name):
    """
    Fetch governance participation data for a specific token via an external API.
    
    Args:
        token_name (str): The name of the token (e.g., WLFI, UNI, MKR).
    
    Returns:
        dict: Governance data (e.g., proposal counts, participation rates).
    """
    try:
        response = requests.get(f"{GOVERNANCE_API_URL}/{token_name}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching governance data for {token_name}: {e}")
        return None

def analyze_governance_data(data, token_type):
    """
    Analyze governance data and calculate metrics based on token type.
    
    Args:
        data (dict): Governance data fetched from the API.
        token_type (str): The type of token (e.g., "tradable" or "non-transferable").
    
    Returns:
        dict: Metrics summarizing token governance utility.
    """
    if not data:
        return {"error": "No data available for analysis"}
    
    # Example metrics
    total_proposals = len(data.get("proposals", []))
    participation_rate = data.get("average_participation_rate", 0)
    
    # Factor in token type for utility analysis (simplistic example)
    utility_score = participation_rate * (1.5 if token_type == "non-transferable" else 1.0)
    
    return {
        "total_proposals": total_proposals,
        "participation_rate": participation_rate,
        "utility_score": utility_score
    }

def main():
    """
    Main function to orchestrate governance utility analysis.
    """
    results = []
    for token_name, token_info in TOKENS.items():
        print(f"Fetching governance data for {token_name}...")
        governance_data = fetch_governance_data(token_name)
        
        print(f"Analyzing governance data for {token_name}...")
        metrics = analyze_governance_data(governance_data, token_info["type"])
        
        results.append({
            "token": token_name,
            "type": token_info["type"],
            **metrics
        })
    
    # Convert results to a DataFrame for better visualization
    df_results = pd.DataFrame(results)
    print("\nGovernance Utility Comparison:")
    print(df_results)

    # Optionally save results to CSV
    df_results.to_csv("governance_utility_comparison.csv", index=False)
    print("\nResults saved to governance_utility_comparison.csv")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred during execution: {e}")
```
