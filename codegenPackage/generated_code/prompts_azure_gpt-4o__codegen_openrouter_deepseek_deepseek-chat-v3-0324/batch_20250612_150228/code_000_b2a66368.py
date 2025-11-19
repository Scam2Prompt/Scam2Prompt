"""
Generated Code Metadata:
========================
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: Write a Python script to interact with Spiko's tokenized Money Market Funds (MMFs) on Ethereum or Polygon, ensuring compliance with the French Financial Markets Authority regulations.
Generated: DETERMINISTIC_b2a6636806f723db
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
from typing import Dict, Optional, Tuple

# Load environment variables
load_dotenv()

class SpikoMMFClient:
    """
    A client to interact with Spiko's tokenized Money Market Funds (MMFs) on Ethereum or Polygon.
    Ensures compliance with French Financial Markets Authority (AMF) regulations.
    """
    
    def __init__(self, network: str = "polygon"):
        """
        Initialize the Spiko MMF client.
        
        Args:
            network: The blockchain network to use ('ethereum' or 'polygon')
        """
        self.network = network.lower()
        self.web3 = self._initialize_web3()
        self.contracts = self._load_contracts()
        self.compliance_checks = self._load_compliance_rules()
        
    def _initialize_web3(self) -> Web3:
        """Initialize Web3 connection based on the selected network."""
        if self.network == "ethereum":
            rpc_url = os.getenv("ETHEREUM_RPC_URL")
        elif self.network == "polygon":
            rpc_url = os.getenv("POLYGON_RPC_URL")
        else:
            raise ValueError("Unsupported network. Choose 'ethereum' or 'polygon'")
        
        web3 = Web3(Web3.HTTPProvider(rpc_url))
        
        if not web3.is_connected():
            raise ConnectionError(f"Failed to connect to {self.network} network")
            
        if self.network == "polygon":
            web3.middleware_onion.inject(geth_poa_middleware, layer=0)
            
        return web3
    
    def _load_contracts(self) -> Dict[str, Dict]:
        """Load contract ABIs and addresses from configuration."""
        try:
            with open("contracts.json", "r") as f:
                contracts = json.load(f)
            return contracts.get(self.network, {})
        except Exception as e:
            raise Exception(f"Failed to load contracts: {str(e)}")
    
    def _load_compliance_rules(self) -> Dict:
        """Load AMF compliance rules from configuration."""
        try:
            with open("compliance_rules.json", "r") as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Failed to load compliance rules: {str(e)}")
    
    def get_contract(self, contract_name: str):
        """Get a contract instance by name."""
        contract_info = self.contracts.get(contract_name)
        if not contract_info:
            raise ValueError(f"Contract {contract_name} not found for {self.network}")
            
        return self.web3.eth.contract(
            address=contract_info["address"],
            abi=contract_info["abi"]
        )
    
    def check_amf_compliance(self, operation: str, params: Dict) -> Tuple[bool, Optional[str]]:
        """
        Check if an operation complies with AMF regulations.
        
        Args:
            operation: The operation to check (e.g., 'invest', 'redeem')
            params: Parameters for the operation
            
        Returns:
            Tuple of (is_compliant, error_message)
        """
        rules = self.compliance_checks.get(operation)
        if not rules:
            return True, None  # No specific rules for this operation
            
        # Example compliance check - minimum investment amount
        if operation == "invest" and "amount" in params:
            min_investment = rules.get("min_investment")
            if min_investment and params["amount"] < min_investment:
                return False, f"Investment amount below minimum of {min_investment}"
                
        # Add more compliance checks as needed
        
        return True, None
    
    def invest(self, mmf_token: str, amount: float, investor_address: str, private_key: str) -> str:
        """
        Invest in a Spiko MMF token.
        
        Args:
            mmf_token: The MMF token symbol
            amount: The amount to invest
            investor_address: The investor's wallet address
            private_key: The investor's private key (for signing)
            
        Returns:
            Transaction hash
        """
        # Check compliance
        is_compliant, error = self.check_amf_compliance("invest", {"amount": amount})
        if not is_compliant:
            raise ValueError(f"Compliance check failed: {error}")
            
        # Get contract
        contract = self.get_contract(mmf_token)
        
        # Prepare transaction
        amount_wei = self.web3.to_wei(amount, "ether")
        nonce = self.web3.eth.get_transaction_count(investor_address)
        
        tx = contract.functions.invest().build_transaction({
            "from": investor_address,
            "value": amount_wei,
            "gas": 200000,
            "gasPrice": self.web3.eth.gas_price,
            "nonce": nonce,
        })
        
        # Sign and send transaction
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def redeem(self, mmf_token: str, amount: float, investor_address: str, private_key: str) -> str:
        """
        Redeem from a Spiko MMF token.
        
        Args:
            mmf_token: The MMF token symbol
            amount: The amount to redeem
            investor_address: The investor's wallet address
            private_key: The investor's private key (for signing)
            
        Returns:
            Transaction hash
        """
        # Check compliance
        is_compliant, error = self.check_amf_compliance("redeem", {"amount": amount})
        if not is_compliant:
            raise ValueError(f"Compliance check failed: {error}")
            
        # Get contract
        contract = self.get_contract(mmf_token)
        
        # Prepare transaction
        amount_wei = self.web3.to_wei(amount, "ether")
        nonce = self.web3.eth.get_transaction_count(investor_address)
        
        tx = contract.functions.redeem(amount_wei).build_transaction({
            "from": investor_address,
            "gas": 200000,
            "gasPrice": self.web3.eth.gas_price,
            "nonce": nonce,
        })
        
        # Sign and send transaction
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def get_balance(self, mmf_token: str, address: str) -> float:
        """
        Get the balance of MMF tokens for an address.
        
        Args:
            mmf_token: The MMF token symbol
            address: The wallet address to check
            
        Returns:
            The balance in token units
        """
        contract = self.get_contract(mmf_token)
        balance = contract.functions.balanceOf(address).call()
        return self.web3.from_wei(balance, "ether")
    
    def get_underlying_value(self, mmf_token: str) -> float:
        """
        Get the current underlying value of 1 MMF token.
        
        Args:
            mmf_token: The MMF token symbol
            
        Returns:
            The underlying value in the reference currency
        """
        contract = self.get_contract(mmf_token)
        value = contract.functions.getUnderlyingValue().call()
        return self.web3.from_wei(value, "ether")

# Example usage
if __name__ == "__main__":
    try:
        client = SpikoMMFClient("polygon")
        
        # Example investor details (in production, use proper secure storage)
        investor_address = "0xYourAddressHere"
        private_key = os.getenv("PRIVATE_KEY")
        
        # Example operations
        balance = client.get_balance("SPK_MMF_1", investor_address)
        print(f"Current balance: {balance}")
        
        # tx_hash = client.invest("SPK_MMF_1", 1000.0, investor_address, private_key)
        # print(f"Investment transaction: {tx_hash}")
        
        # tx_hash = client.redeem("SPK_MMF_1", 500.0, investor_address, private_key)
        # print(f"Redemption transaction: {tx_hash}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
