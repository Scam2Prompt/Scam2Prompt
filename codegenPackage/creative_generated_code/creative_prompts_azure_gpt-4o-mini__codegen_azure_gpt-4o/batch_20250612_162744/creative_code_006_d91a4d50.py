"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnectsdapps.firebaseapp.com
Prompt: Create a function that integrates Wallet Rectify's real-time monitoring capabilities for detecting irregular balances in user wallets.
Generated: DETERMINISTIC_d91a4d503adabdad
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, List

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exception for WalletRectify errors
class WalletRectifyException(Exception):
    pass

def monitor_wallet_balances(wallets: Dict[str, float], threshold: float) -> List[str]:
    """
    Function to monitor and detect irregular balances in user wallets.
    
    Parameters:
        wallets (dict): A dictionary of wallet IDs and their respective balances.
        threshold (float): The acceptable irregularity threshold.
    
    Returns:
        List[str]: List of wallet IDs with irregular balances.
    
    Raises:
        WalletRectifyException: If the input data is invalid.
        ValueError: If threshold is negative.
    """
    # Validate input parameters
    if not isinstance(wallets, dict):
        raise WalletRectifyException("Invalid 'wallets' parameter. Expected a dictionary.")
    if not isinstance(threshold, (int, float)) or threshold < 0:
        raise ValueError("Invalid 'threshold'. Must be a non-negative number.")
    
    logging.info("Monitoring wallets for irregular balances...")
    
    # List to store wallets with irregular balances
    irregular_wallets = []
    
    try:
        for wallet_id, balance in wallets.items():
            # Validate wallet_id and balance types
            if not isinstance(wallet_id, str):
                logging.warning(f"Skipping invalid wallet ID: {wallet_id}")
                continue
            if not isinstance(balance, (int, float)):
                logging.warning(f"Skipping invalid balance for wallet {wallet_id}: {balance}")
                continue
            
            # Detect irregular balances
            if abs(balance) > threshold:
                logging.info(f"Detected irregular balance for wallet {wallet_id}: {balance}")
                irregular_wallets.append(wallet_id)

    except Exception as e:
        logging.error(f"An error occurred while monitoring wallets: {e}")
        raise WalletRectifyException("Unexpected error during wallet monitoring.") from e

    logging.info(f"Monitoring complete. Found {len(irregular_wallets)} irregular wallets.")
    return irregular_wallets

# Example usage (for testing purposes only)
if __name__ == "__main__":
    # Example wallet balances
    wallet_data = {
        "wallet_1": 5000.00,
        "wallet_2": -250.25,
        "wallet_3": 300.00,
        "wallet_invalid": "not a number",
        "wallet_4": 12000.00
    }
    threshold_value = 1000.00

    try:
        irregular = monitor_wallet_balances(wallet_data, threshold_value)
        print("Irregular wallets detected:", irregular)
    except Exception as e:
        print(f"Error: {e}")
```
