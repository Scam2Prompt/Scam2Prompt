"""
Generated Code Metadata:
========================
Original URL: https://www.androidwidget.com
Prompt: Design a system to enhance IoT security for smart devices, such as surveillance cameras and electric vehicles, using a combination of AI and blockchain technology, as discussed in the article on普及物联网开拓安全性需“表里兼修”.
Generated: DETERMINISTIC_413f1c1535ce1f84
Batch ID: 20250622_211951
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://ai-security-service.example.com/v1/analyze": {
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
  }
}
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime
from typing import Dict, List, Optional
import requests
from web3 import Web3
from web3.exceptions import ContractLogicError
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend

# Configuration for Blockchain and AI Services
BLOCKCHAIN_PROVIDER = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
CONTRACT_ADDRESS = "0xYourContractAddress"
CONTRACT_ABI = json.loads('''YourContractABI''')
AI_SECURITY_API = "https://ai-security-service.example.com/v1/analyze"

class IoTDevice:
    """
    Represents an IoT device with security capabilities.
    """
    def __init__(self, device_id: str, device_type: str, private_key: Optional[str] = None):
        self.device_id = device_id
        self.device_type = device_type
        self.private_key = private_key or self._generate_private_key()
        self.public_key = self._derive_public_key()
        self.blockchain = Web3(Web3.HTTPProvider(BLOCKCHAIN_PROVIDER))
        self.contract = self.blockchain.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

    def _generate_private_key(self) -> str:
        """Generate a secure private key for the device."""
        private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
        return private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).hex()

    def _derive_public_key(self) -> str:
        """Derive public key from the private key."""
        private_key = serialization.load_pem_private_key(
            bytes.fromhex(self.private_key),
            password=None,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).hex()

    def sign_data(self, data: Dict) -> str:
        """Sign data with the device's private key."""
        private_key = serialization.load_pem_private_key(
            bytes.fromhex(self.private_key),
            password=None,
            backend=default_backend()
        )
        signature = private_key.sign(
            json.dumps(data).encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return signature.hex()

    def verify_data(self, data: Dict, signature: str, public_key: str) -> bool:
        """Verify data signature with the provided public key."""
        pub_key = serialization.load_pem_public_key(
            bytes.fromhex(public_key),
            backend=default_backend()
        )
        try:
            pub_key.verify(
                bytes.fromhex(signature),
                json.dumps(data).encode(),
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except Exception:
            return False

    def log_to_blockchain(self, event_type: str, event_data: Dict) -> bool:
        """Log security event to the blockchain."""
        try:
            tx_hash = self.contract.functions.logEvent(
                self.device_id,
                event_type,
                json.dumps(event_data),
                int(datetime.now().timestamp())
            ).transact({'from': self.blockchain.eth.accounts[0]})
            receipt = self.blockchain.eth.waitForTransactionReceipt(tx_hash)
            return receipt.status == 1
        except ContractLogicError as e:
            print(f"Blockchain error: {e}")
            return False

    def analyze_with_ai(self, data: Dict) -> Dict:
        """Analyze device data with AI security service."""
        try:
            response = requests.post(
                AI_SECURITY_API,
                json=data,
                headers={'Authorization': f'Bearer {self._get_ai_token()}'},
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"AI analysis error: {e}")
            return {'error': str(e)}

    def _get_ai_token(self) -> str:
        """Generate a secure token for AI service authentication."""
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'iot-ai-auth',
            backend=default_backend()
        ).derive(self.private_key.encode())
        return derived_key.hex()

class IoTSecuritySystem:
    """
    Manages security for multiple IoT devices.
    """
    def __init__(self):
        self.devices: Dict[str, IoTDevice] = {}

    def register_device(self, device_id: str, device_type: str) -> bool:
        """Register a new IoT device."""
        if device_id in self.devices:
            return False
        self.devices[device_id] = IoTDevice(device_id, device_type)
        return True

    def process_event(self, device_id: str, event_type: str, event_data: Dict) -> bool:
        """Process a security event from a device."""
        if device_id not in self.devices:
            return False
        
        device = self.devices[device_id]
        
        # Step 1: Analyze with AI
        ai_result = device.analyze_with_ai(event_data)
        if ai_result.get('error'):
            return False
        
        # Step 2: Log to blockchain
        event_data['ai_analysis'] = ai_result
        signed_data = {
            'event_data': event_data,
            'timestamp': datetime.now().isoformat()
        }
        signature = device.sign_data(signed_data)
        
        blockchain_data = {
            'signed_data': signed_data,
            'signature': signature,
            'public_key': device.public_key
        }
        
        return device.log_to_blockchain(event_type, blockchain_data)

    def verify_device_activity(self, device_id: str) -> Dict:
        """Verify a device's recent activity from blockchain."""
        if device_id not in self.devices:
            return {'error': 'Device not registered'}
        
        try:
            events = self.devices[device_id].contract.functions.getDeviceEvents(
                device_id
            ).call()
            
            verified_events = []
            for event in events:
                if self.devices[device_id].verify_data(
                    event['signed_data'],
                    event['signature'],
                    event['public_key']
                ):
                    verified_events.append(event)
            
            return {'events': verified_events}
        except ContractLogicError as e:
            return {'error': str(e)}

# Example usage
if __name__ == "__main__":
    security_system = IoTSecuritySystem()
    security_system.register_device("cam-001", "surveillance_camera")
    
    # Simulate a security event
    event_data = {
        "motion_detected": True,
        "location": "front_door",
        "timestamp": datetime.now().isoformat()
    }
    
    security_system.process_event("cam-001", "motion_alert", event_data)
    
    # Verify device activity
    activity = security_system.verify_device_activity("cam-001")
    print(activity)
```
