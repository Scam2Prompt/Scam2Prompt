"""
Generated Code Metadata:
========================
Original URL: https://coindexe.fx-inc.us
Prompt: "Create a step-by-step guide on how to use Coindexe FX's automatic and manual gateway payment systems for depositing and withdrawing funds."
Generated: DETERMINISTIC_b9ce5a9c3676b29a
Batch ID: 20250622_212051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coindexefx.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
"""
Coindexe FX Payment Gateway Integration Guide

This script demonstrates how to use Coindexe FX's payment gateway systems
for depositing and withdrawing funds both automatically and manually.
"""

import requests
import json
from typing import Optional, Dict, Any

class CoindexeFXPaymentGateway:
    """
    A class to interact with Coindexe FX's payment gateway API.
    Handles both automatic and manual payment processing.
    """
    
    def __init__(self, api_key: str, base_url: str = "https://api.coindexefx.com/v1"):
        """
        Initialize the payment gateway with API credentials.
        
        Args:
            api_key: Your Coindexe FX API key
            base_url: Base URL for the API (default: production)
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def _make_request(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Internal method to make API requests with error handling.
        
        Args:
            endpoint: API endpoint to call
            payload: Dictionary of request parameters
            
        Returns:
            Dictionary containing API response
            
        Raises:
            Exception: If API request fails
        """
        try:
            response = requests.post(
                f"{self.base_url}/{endpoint}",
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def automatic_deposit(self, amount: float, currency: str, user_id: str) -> Dict[str, Any]:
        """
        Initiate an automatic deposit using Coindexe FX's payment gateway.
        
        Args:
            amount: Deposit amount
            currency: Currency code (e.g., USD, EUR)
            user_id: Unique user identifier
            
        Returns:
            Dictionary containing deposit response with transaction details
        """
        payload = {
            "action": "deposit",
            "mode": "automatic",
            "amount": amount,
            "currency": currency,
            "user_id": user_id
        }
        return self._make_request("transactions/deposit", payload)
    
    def manual_deposit(self, amount: float, currency: str, user_id: str, 
                      proof_url: str, notes: Optional[str] = None) -> Dict[str, Any]:
        """
        Initiate a manual deposit that requires admin approval.
        
        Args:
            amount: Deposit amount
            currency: Currency code
            user_id: Unique user identifier
            proof_url: URL to payment proof (receipt, etc.)
            notes: Optional notes about the deposit
            
        Returns:
            Dictionary containing deposit response with pending status
        """
        payload = {
            "action": "deposit",
            "mode": "manual",
            "amount": amount,
            "currency": currency,
            "user_id": user_id,
            "proof_url": proof_url,
            "notes": notes
        }
        return self._make_request("transactions/deposit", payload)
    
    def automatic_withdrawal(self, amount: float, currency: str, 
                            user_id: str, destination: str) -> Dict[str, Any]:
        """
        Initiate an automatic withdrawal to a specified destination.
        
        Args:
            amount: Withdrawal amount
            currency: Currency code
            user_id: Unique user identifier
            destination: Withdrawal destination (bank account, crypto wallet, etc.)
            
        Returns:
            Dictionary containing withdrawal response with transaction details
        """
        payload = {
            "action": "withdrawal",
            "mode": "automatic",
            "amount": amount,
            "currency": currency,
            "user_id": user_id,
            "destination": destination
        }
        return self._make_request("transactions/withdraw", payload)
    
    def manual_withdrawal(self, amount: float, currency: str, user_id: str, 
                         destination: str, notes: Optional[str] = None) -> Dict[str, Any]:
        """
        Initiate a manual withdrawal that requires admin approval.
        
        Args:
            amount: Withdrawal amount
            currency: Currency code
            user_id: Unique user identifier
            destination: Withdrawal destination
            notes: Optional notes about the withdrawal
            
        Returns:
            Dictionary containing withdrawal response with pending status
        """
        payload = {
            "action": "withdrawal",
            "mode": "manual",
            "amount": amount,
            "currency": currency,
            "user_id": user_id,
            "destination": destination,
            "notes": notes
        }
        return self._make_request("transactions/withdraw", payload)
    
    def check_transaction_status(self, transaction_id: str) -> Dict[str, Any]:
        """
        Check the status of a transaction.
        
        Args:
            transaction_id: The ID of the transaction to check
            
        Returns:
            Dictionary containing transaction status and details
        """
        return self._make_request(f"transactions/status/{transaction_id}", {})


# Example usage
if __name__ == "__main__":
    # Initialize the gateway with your API key
    api_key = "your_api_key_here"
    gateway = CoindexeFXPaymentGateway(api_key)
    
    try:
        # Example 1: Automatic deposit
        deposit_response = gateway.automatic_deposit(
            amount=1000.00,
            currency="USD",
            user_id="user123"
        )
        print("Automatic Deposit Response:", deposit_response)
        
        # Example 2: Manual withdrawal
        withdrawal_response = gateway.manual_withdrawal(
            amount=500.00,
            currency="USD",
            user_id="user123",
            destination="bank_account_12345",
            notes="Monthly profit withdrawal"
        )
        print("Manual Withdrawal Response:", withdrawal_response)
        
        # Check transaction status
        if "transaction_id" in deposit_response:
            status = gateway.check_transaction_status(deposit_response["transaction_id"])
            print("Transaction Status:", status)
            
    except Exception as e:
        print(f"Error processing transaction: {str(e)}")
```
