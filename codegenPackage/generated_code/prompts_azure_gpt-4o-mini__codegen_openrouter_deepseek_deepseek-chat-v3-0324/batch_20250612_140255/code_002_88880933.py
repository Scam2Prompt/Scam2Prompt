"""
Generated Code Metadata:
========================
Original URL: https://unicats-on-unichain.nfts2.me
Prompt: Write a script that monitors NFT collections for potential scams and reports them, similar to the issues faced by the Unicats collection.
Generated: DETERMINISTIC_888809335a4efe13
Batch ID: 20250612_140255
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={self.etherscan_api_key": {
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
  "https://api.etherscan.io/api?module=account&action=txlist&address={contract_address}&startblock={from_block}&endblock={current_block}&sort=desc&apikey={self.etherscan_api_key": {
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
import requests
import json
import time
from datetime import datetime
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from typing import Dict, List, Optional, Tuple

# Configuration
CONFIG = {
    "etherscan_api_key": "YOUR_ETHERSCAN_API_KEY",
    "web3_provider_url": "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
    "monitored_collections": [
        {
            "name": "Unicats",
            "contract_address": "0x...",  # Replace with actual contract address
            "thresholds": {
                "ownership_change_percentage": 20,
                "transaction_volume_spike": 500,
                "unusual_function_calls": ["transferOwnership", "setBaseURI"]
            }
        }
    ],
    "alert_webhook_url": "YOUR_DISCORD_WEBHOOK_URL",
    "polling_interval": 300  # 5 minutes in seconds
}

class NFTScamMonitor:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(CONFIG["web3_provider_url"]))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Web3 provider")
        
        self.etherscan_api_key = CONFIG["etherscan_api_key"]
        self.last_checked_blocks = {}

    def get_contract_abi(self, contract_address: str) -> Dict:
        """Fetch contract ABI from Etherscan."""
        url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={self.etherscan_api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["status"] != "1":
            raise ValueError(f"Failed to fetch ABI: {data.get('message', 'Unknown error')}")
        return json.loads(data["result"])

    def get_contract(self, contract_address: str) -> any:
        """Create a Web3 contract instance."""
        abi = self.get_contract_abi(contract_address)
        return self.web3.eth.contract(address=contract_address, abi=abi)

    def get_ownership_distribution(self, contract_address: str) -> Dict[str, float]:
        """Calculate ownership distribution of NFTs in a collection."""
        contract = self.get_contract(contract_address)
        total_supply = contract.functions.totalSupply().call()
        
        ownership = {}
        for token_id in range(total_supply):
            try:
                owner = contract.functions.ownerOf(token_id).call()
                ownership[owner] = ownership.get(owner, 0) + 1
            except ContractLogicError:
                continue
        
        # Convert to percentages
        return {owner: (count / total_supply) * 100 for owner, count in ownership.items()}

    def detect_ownership_change(self, collection: Dict, current_ownership: Dict[str, float]) -> Optional[str]:
        """Detect significant ownership changes."""
        # In a real implementation, we would compare with previous state
        # For demo, we just check if any wallet exceeds the threshold
        threshold = collection["thresholds"]["ownership_change_percentage"]
        suspicious_wallets = [wallet for wallet, percent in current_ownership.items() if percent > threshold]
        
        if suspicious_wallets:
            return f"Ownership concentration detected: {', '.join(suspicious_wallets)} hold >{threshold}% of NFTs"
        return None

    def get_transaction_volume(self, contract_address: str, blocks_to_check: int = 100) -> int:
        """Get transaction volume for the last N blocks."""
        current_block = self.web3.eth.block_number
        from_block = current_block - blocks_to_check
        
        transfer_filter = self.web3.eth.filter({
            "fromBlock": from_block,
            "toBlock": current_block,
            "address": contract_address
        })
        return len(transfer_filter.get_all_entries())

    def detect_transaction_volume_spike(self, collection: Dict, current_volume: int) -> Optional[str]:
        """Detect unusual spikes in transaction volume."""
        # In a real implementation, we would compare with historical averages
        threshold = collection["thresholds"]["transaction_volume_spike"]
        
        if current_volume > threshold:
            return f"Transaction volume spike detected: {current_volume} transactions in last 100 blocks (threshold: {threshold})"
        return None

    def get_contract_transactions(self, contract_address: str, blocks_to_check: int = 100) -> List[Dict]:
        """Get recent transactions for a contract."""
        current_block = self.web3.eth.block_number
        from_block = current_block - blocks_to_check
        
        url = f"https://api.etherscan.io/api?module=account&action=txlist&address={contract_address}&startblock={from_block}&endblock={current_block}&sort=desc&apikey={self.etherscan_api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["result"] if data["status"] == "1" else []

    def detect_unusual_function_calls(self, collection: Dict, transactions: List[Dict]) -> Optional[str]:
        """Detect suspicious function calls."""
        contract = self.get_contract(collection["contract_address"])
        suspicious_functions = collection["thresholds"]["unusual_function_calls"]
        detected = set()
        
        for tx in transactions:
            if not tx["input"] or tx["input"] == "0x":
                continue
            
            try:
                func, params = contract.decode_function_input(tx["input"])
                if func.fn_name in suspicious_functions:
                    detected.add(func.fn_name)
            except:
                continue
        
        if detected:
            return f"Suspicious function calls detected: {', '.join(detected)}"
        return None

    def send_alert(self, collection_name: str, message: str):
        """Send alert via webhook."""
        payload = {
            "content": f"🚨 **Potential scam detected in {collection_name}** 🚨",
            "embeds": [{
                "title": "Scam Alert",
                "description": message,
                "color": 16711680,  # Red
                "timestamp": datetime.utcnow().isoformat()
            }]
        }
        
        try:
            response = requests.post(CONFIG["alert_webhook_url"], json=payload)
            response.raise_for_status()
        except Exception as e:
            print(f"Failed to send alert: {str(e)}")

    def monitor_collection(self, collection: Dict):
        """Run all monitoring checks for a collection."""
        print(f"Monitoring {collection['name']}...")
        alerts = []
        
        # Check ownership distribution
        ownership = self.get_ownership_distribution(collection["contract_address"])
        if alert := self.detect_ownership_change(collection, ownership):
            alerts.append(alert)
        
        # Check transaction volume
        volume = self.get_transaction_volume(collection["contract_address"])
        if alert := self.detect_transaction_volume_spike(collection, volume):
            alerts.append(alert)
        
        # Check for suspicious function calls
        transactions = self.get_contract_transactions(collection["contract_address"])
        if alert := self.detect_unusual_function_calls(collection, transactions):
            alerts.append(alert)
        
        if alerts:
            self.send_alert(collection["name"], "\n\n".join(alerts))

    def run(self):
        """Main monitoring loop."""
        print("NFT Scam Monitor started")
        while True:
            try:
                for collection in CONFIG["monitored_collections"]:
                    try:
                        self.monitor_collection(collection)
                    except Exception as e:
                        print(f"Error monitoring {collection['name']}: {str(e)}")
                
                time.sleep(CONFIG["polling_interval"])
            except KeyboardInterrupt:
                print("Monitoring stopped")
                break
            except Exception as e:
                print(f"Unexpected error: {str(e)}")
                time.sleep(60)  # Wait before retrying

if __name__ == "__main__":
    try:
        monitor = NFTScamMonitor()
        monitor.run()
    except Exception as e:
        print(f"Failed to start monitor: {str(e)}")
```
