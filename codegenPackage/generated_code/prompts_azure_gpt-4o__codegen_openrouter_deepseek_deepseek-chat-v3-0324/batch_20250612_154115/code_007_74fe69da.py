"""
Generated Code Metadata:
========================
Original URL: https://steemit-monadscore.blogspot.com
Prompt: Write code to implement a secure and transparent payment system for AI solutions in a blockchain-based marketplace like Anaphora AI.
Generated: DETERMINISTIC_74fe69dab2c43b39
Batch ID: 20250612_154115
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
import hashlib
import json
from time import time
from uuid import uuid4
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from web3 import Web3, HTTPProvider
from web3.contract import Contract
from web3.middleware import geth_poa_middleware

# Configuration
CONTRACT_ADDRESS = "0xYourSmartContractAddressHere"
PROVIDER_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
PRIVATE_KEY_PATH = "path/to/your/private_key.pem"
GAS_LIMIT = 200000
GAS_PRICE = Web3.toWei('50', 'gwei')

# Initialize Web3
w3 = Web3(HTTPProvider(PROVIDER_URL))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load contract ABI
with open('PaymentContractABI.json') as f:
    CONTRACT_ABI = json.load(f)

@dataclass
class PaymentDetails:
    payment_id: str = field(default_factory=lambda: str(uuid4()))
    buyer_address: str
    seller_address: str
    amount: float  # in ETH
    service_id: str
    timestamp: float = field(default_factory=time)
    status: str = "pending"
    transaction_hash: Optional[str] = None

class PaymentSystem:
    def __init__(self):
        self.contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
        self._load_private_key()

    def _load_private_key(self):
        """Load private key from PEM file for transaction signing"""
        with open(PRIVATE_KEY_PATH, "rb") as key_file:
            self.private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )

    def _sign_transaction(self, transaction: Dict) -> Dict:
        """Sign a transaction with the private key"""
        signed_txn = w3.eth.account.sign_transaction(transaction, self.private_key)
        return signed_txn

    def _send_transaction(self, transaction: Dict) -> str:
        """Send a signed transaction to the blockchain"""
        signed_txn = self._sign_transaction(transaction)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return tx_hash.hex()

    def create_payment(self, payment_details: PaymentDetails) -> str:
        """
        Create a new payment transaction on the blockchain
        Returns transaction hash
        """
        nonce = w3.eth.getTransactionCount(payment_details.buyer_address)
        
        tx = self.contract.functions.createPayment(
            payment_details.payment_id,
            payment_details.seller_address,
            Web3.toWei(payment_details.amount, 'ether'),
            payment_details.service_id
        ).buildTransaction({
            'chainId': w3.eth.chain_id,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': nonce,
        })

        tx_hash = self._send_transaction(tx)
        payment_details.transaction_hash = tx_hash
        return tx_hash

    def confirm_payment(self, payment_id: str, seller_address: str) -> str:
        """
        Confirm payment receipt by seller
        Returns transaction hash
        """
        nonce = w3.eth.getTransactionCount(seller_address)
        
        tx = self.contract.functions.confirmPayment(
            payment_id
        ).buildTransaction({
            'chainId': w3.eth.chain_id,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': nonce,
        })

        return self._send_transaction(tx)

    def dispute_payment(self, payment_id: str, buyer_address: str) -> str:
        """
        Initiate a payment dispute
        Returns transaction hash
        """
        nonce = w3.eth.getTransactionCount(buyer_address)
        
        tx = self.contract.functions.disputePayment(
            payment_id
        ).buildTransaction({
            'chainId': w3.eth.chain_id,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': nonce,
        })

        return self._send_transaction(tx)

    def get_payment_status(self, payment_id: str) -> Dict:
        """
        Retrieve payment status from blockchain
        Returns payment details
        """
        return self.contract.functions.getPaymentDetails(payment_id).call()

    def verify_payment(self, payment_id: str, expected_amount: float) -> bool:
        """
        Verify payment details on blockchain
        Returns True if payment is valid
        """
        payment_details = self.get_payment_status(payment_id)
        if not payment_details:
            return False
            
        actual_amount = Web3.fromWei(payment_details[2], 'ether')
        return (
            payment_details[5] == "completed" and  # status
            float(actual_amount) == expected_amount
        )

    def _generate_escrow_hash(self, payment_details: PaymentDetails) -> str:
        """Generate a unique hash for escrow verification"""
        data = f"{payment_details.payment_id}{payment_details.buyer_address}{payment_details.seller_address}{payment_details.amount}{payment_details.service_id}"
        return hashlib.sha256(data.encode()).hexdigest()

class PaymentSecurity:
    @staticmethod
    def encrypt_data(data: str, public_key: str) -> bytes:
        """Encrypt sensitive data using RSA public key"""
        pub_key = serialization.load_pem_public_key(
            public_key.encode(),
            backend=default_backend()
        )
        return pub_key.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def decrypt_data(encrypted_data: bytes, private_key: str) -> str:
        """Decrypt data using RSA private key"""
        priv_key = serialization.load_pem_private_key(
            private_key.encode(),
            password=None,
            backend=default_backend()
        )
        return priv_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

    @staticmethod
    def verify_signature(data: str, signature: bytes, public_key: str) -> bool:
        """Verify digital signature of data"""
        pub_key = serialization.load_pem_public_key(
            public_key.encode(),
            backend=default_backend()
        )
        try:
            pub_key.verify(
                signature,
                data.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

# Example usage
if __name__ == "__main__":
    payment_system = PaymentSystem()
    
    # Create a new payment
    payment = PaymentDetails(
        buyer_address="0xBuyerAddress",
        seller_address="0xSellerAddress",
        amount=0.5,
        service_id="AI_MODEL_123"
    )
    
    tx_hash = payment_system.create_payment(payment)
    print(f"Payment created with TX hash: {tx_hash}")
    
    # Verify payment
    is_valid = payment_system.verify_payment(payment.payment_id, payment.amount)
    print(f"Payment valid: {is_valid}")
```
