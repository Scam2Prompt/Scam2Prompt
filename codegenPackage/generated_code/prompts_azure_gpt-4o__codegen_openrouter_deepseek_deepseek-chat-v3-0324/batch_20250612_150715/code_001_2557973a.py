"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Create a script to launch a Fan Token auction on Farcaster using Moxie Batch Auctions for fair price discovery. Include steps to integrate bonding curves for utility emphasis.
Generated: DETERMINISTIC_2557973a20aae8bc
Batch ID: 20250612_150715
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://etherscan.io/tx/{tx_hash": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://moxie.xyz/auctions/{tx_hash": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.farcaster.xyz/v2": {
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
import json
import requests
from web3 import Web3
from typing import Dict, Any, Optional
from dataclasses import dataclass

# Configuration
CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
    "moxie_auction_contract": "0x...",  # Replace with actual Moxie Batch Auction contract address
    "farcaster_api_url": "https://api.farcaster.xyz/v2",
    "farcaster_api_key": "YOUR_FARCASTER_API_KEY",
}

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(CONFIG["rpc_url"]))

@dataclass
class AuctionParams:
    token_address: str
    token_name: str
    token_symbol: str
    token_decimals: int
    auction_start_time: int
    auction_end_time: int
    initial_price: int
    min_raise: int
    token_amount: int
    bonding_curve_type: str = "linear"  # Can be 'linear', 'exponential', or 'polynomial'
    bonding_curve_params: Optional[Dict[str, Any]] = None

class AuctionLauncher:
    def __init__(self, private_key: str):
        self.private_key = private_key
        self.account = w3.eth.account.from_key(private_key)
        self.nonce = w3.eth.get_transaction_count(self.account.address)
        
        # Load Moxie Auction ABI (simplified for example)
        with open("MoxieAuctionABI.json") as f:
            self.auction_abi = json.load(f)
            
        self.auction_contract = w3.eth.contract(
            address=CONFIG["moxie_auction_contract"],
            abi=self.auction_abi
        )
    
    def _get_bonding_curve_params(self, auction_params: AuctionParams) -> Dict[str, Any]:
        """Generate bonding curve parameters based on type"""
        if auction_params.bonding_curve_params:
            return auction_params.bonding_curve_params
            
        if auction_params.bonding_curve_type == "linear":
            return {"slope": 1, "intercept": 0}
        elif auction_params.bonding_curve_type == "exponential":
            return {"base": 2, "scale": 1}
        elif auction_params.bonding_curve_type == "polynomial":
            return {"coefficients": [0, 1, 0.1]}  # ax² + bx + c
        else:
            raise ValueError("Invalid bonding curve type")
    
    def _sign_and_send_transaction(self, tx: Dict[str, Any]) -> str:
        """Helper to sign and send transaction"""
        signed_tx = w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def create_auction(self, auction_params: AuctionParams) -> str:
        """Create a new auction on Moxie"""
        bonding_params = self._get_bonding_curve_params(auction_params)
        
        tx = self.auction_contract.functions.createAuction(
            auction_params.token_address,
            auction_params.token_name,
            auction_params.token_symbol,
            auction_params.token_decimals,
            auction_params.auction_start_time,
            auction_params.auction_end_time,
            auction_params.initial_price,
            auction_params.min_raise,
            auction_params.token_amount,
            json.dumps(bonding_params)
        ).build_transaction({
            "from": self.account.address,
            "nonce": self.nonce,
            "gas": 500000,
            "gasPrice": w3.eth.gas_price
        })
        
        tx_hash = self._sign_and_send_transaction(tx)
        self.nonce += 1
        return tx_hash
    
    def announce_on_farcaster(self, auction_params: AuctionParams, tx_hash: str) -> bool:
        """Announce the auction on Farcaster"""
        message = (
            f"New Fan Token Auction for {auction_params.token_name} ({auction_params.token_symbol})!\n"
            f"Starting at {auction_params.auction_start_time} with initial price {auction_params.initial_price}\n"
            f"Bonding curve: {auction_params.bonding_curve_type}\n"
            f"View on Etherscan: https://etherscan.io/tx/{tx_hash}"
        )
        
        headers = {
            "Authorization": f"Bearer {CONFIG['farcaster_api_key']}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "text": message,
            "embeds": [{
                "url": f"https://moxie.xyz/auctions/{tx_hash}"
            }]
        }
        
        try:
            response = requests.post(
                f"{CONFIG['farcaster_api_url']}/casts",
                headers=headers,
                json=payload
            )
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error announcing on Farcaster: {e}")
            return False

def main():
    # Example usage
    private_key = "YOUR_PRIVATE_KEY"  # In production, use environment variables or secure storage
    
    auction_params = AuctionParams(
        token_address="0x...",  # Your ERC20 token address
        token_name="Fan Token",
        token_symbol="FAN",
        token_decimals=18,
        auction_start_time=int(w3.eth.get_block("latest").timestamp) + 3600,  # 1 hour from now
        auction_end_time=int(w3.eth.get_block("latest").timestamp) + 86400,  # 24 hours from now
        initial_price=10**15,  # 0.001 ETH
        min_raise=10**14,  # 0.0001 ETH
        token_amount=10**24,  # 1,000,000 tokens with 18 decimals
        bonding_curve_type="linear"
    )
    
    launcher = AuctionLauncher(private_key)
    
    try:
        print("Creating auction...")
        tx_hash = launcher.create_auction(auction_params)
        print(f"Auction created! TX Hash: {tx_hash}")
        
        print("Announcing on Farcaster...")
        success = launcher.announce_on_farcaster(auction_params, tx_hash)
        if success:
            print("Successfully announced on Farcaster!")
        else:
            print("Failed to announce on Farcaster")
    except Exception as e:
        print(f"Error launching auction: {e}")

if __name__ == "__main__":
    main()
```
