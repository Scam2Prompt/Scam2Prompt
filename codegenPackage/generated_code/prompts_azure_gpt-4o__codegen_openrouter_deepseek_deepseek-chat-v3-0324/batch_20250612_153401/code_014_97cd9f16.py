"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Generate code for a decentralized IoT device management system on Aleph Zero, ensuring data privacy and scalability.
Generated: DETERMINISTIC_97cd9f16f513e566
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
import hashlib
from typing import Dict, List, Optional
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

# Constants
ALEPH_ZERO_NODE_URL = "wss://ws.test.azero.dev"
DEVICE_REGISTRY_CONTRACT_ADDRESS = "5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY"
PRIVATE_KEY = "0xYourPrivateKeyHere"  # Replace with actual private key

class IoTDeviceManager:
    """
    A decentralized IoT device management system on Aleph Zero.
    Handles device registration, data storage, and access control.
    """
    
    def __init__(self):
        """
        Initialize the connection to Aleph Zero blockchain.
        """
        try:
            self.substrate = SubstrateInterface(
                url=ALEPH_ZERO_NODE_URL,
                ss58_format=42,
                type_registry_preset='substrate-node-template'
            )
            self.keypair = Keypair.create_from_uri(PRIVATE_KEY)
            self.device_registry = DEVICE_REGISTRY_CONTRACT_ADDRESS
        except SubstrateRequestException as e:
            raise ConnectionError(f"Failed to connect to Aleph Zero: {e}")

    def register_device(self, device_id: str, owner_address: str, metadata: Dict) -> str:
        """
        Register a new IoT device on the blockchain.
        
        Args:
            device_id: Unique identifier for the device
            owner_address: SS58 address of the device owner
            metadata: Additional device metadata
            
        Returns:
            Transaction hash
        """
        try:
            call = self.substrate.compose_call(
                call_module="SmartContract",
                call_function="call",
                call_params={
                    "dest": self.device_registry,
                    "gas_limit": 1000000000,
                    "value": 0,
                    "input_data": self._encode_register_device(device_id, owner_address, metadata)
                }
            )
            
            extrinsic = self.substrate.create_signed_extrinsic(call=call, keypair=self.keypair)
            receipt = self.substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            
            if receipt.is_success:
                return receipt.extrinsic_hash
            else:
                raise RuntimeError(f"Device registration failed: {receipt.error_message}")
        except Exception as e:
            raise RuntimeError(f"Error registering device: {e}")

    def store_device_data(self, device_id: str, data: Dict, encrypted: bool = True) -> str:
        """
        Store device data on the blockchain with optional encryption.
        
        Args:
            device_id: Device identifier
            data: Data to be stored
            encrypted: Whether to encrypt the data
            
        Returns:
            Transaction hash
        """
        try:
            if encrypted:
                data = self._encrypt_data(data)
                
            data_hash = self._calculate_data_hash(data)
            
            call = self.substrate.compose_call(
                call_module="SmartContract",
                call_function="call",
                call_params={
                    "dest": self.device_registry,
                    "gas_limit": 1000000000,
                    "value": 0,
                    "input_data": self._encode_store_data(device_id, data_hash, data)
                }
            )
            
            extrinsic = self.substrate.create_signed_extrinsic(call=call, keypair=self.keypair)
            receipt = self.substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            
            if receipt.is_success:
                return receipt.extrinsic_hash
            else:
                raise RuntimeError(f"Data storage failed: {receipt.error_message}")
        except Exception as e:
            raise RuntimeError(f"Error storing device data: {e}")

    def get_device_data(self, device_id: str) -> List[Dict]:
        """
        Retrieve device data from the blockchain.
        
        Args:
            device_id: Device identifier
            
        Returns:
            List of stored data entries
        """
        try:
            result = self.substrate.query(
                module="SmartContract",
                storage_function="ContractStorage",
                params=[self.device_registry, self._encode_get_data(device_id)]
            )
            
            if result and result.value:
                return self._decode_device_data(result.value)
            return []
        except Exception as e:
            raise RuntimeError(f"Error retrieving device data: {e}")

    def grant_access(self, device_id: str, recipient_address: str) -> str:
        """
        Grant access to device data for another address.
        
        Args:
            device_id: Device identifier
            recipient_address: Address to grant access to
            
        Returns:
            Transaction hash
        """
        try:
            call = self.substrate.compose_call(
                call_module="SmartContract",
                call_function="call",
                call_params={
                    "dest": self.device_registry,
                    "gas_limit": 1000000000,
                    "value": 0,
                    "input_data": self._encode_grant_access(device_id, recipient_address)
                }
            )
            
            extrinsic = self.substrate.create_signed_extrinsic(call=call, keypair=self.keypair)
            receipt = self.substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            
            if receipt.is_success:
                return receipt.extrinsic_hash
            else:
                raise RuntimeError(f"Access grant failed: {receipt.error_message}")
        except Exception as e:
            raise RuntimeError(f"Error granting access: {e}")

    def revoke_access(self, device_id: str, recipient_address: str) -> str:
        """
        Revoke access to device data for an address.
        
        Args:
            device_id: Device identifier
            recipient_address: Address to revoke access from
            
        Returns:
            Transaction hash
        """
        try:
            call = self.substrate.compose_call(
                call_module="SmartContract",
                call_function="call",
                call_params={
                    "dest": self.device_registry,
                    "gas_limit": 1000000000,
                    "value": 0,
                    "input_data": self._encode_revoke_access(device_id, recipient_address)
                }
            )
            
            extrinsic = self.substrate.create_signed_extrinsic(call=call, keypair=self.keypair)
            receipt = self.substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            
            if receipt.is_success:
                return receipt.extrinsic_hash
            else:
                raise RuntimeError(f"Access revocation failed: {receipt.error_message}")
        except Exception as e:
            raise RuntimeError(f"Error revoking access: {e}")

    def _encode_register_device(self, device_id: str, owner_address: str, metadata: Dict) -> bytes:
        """Encode device registration data for smart contract."""
        data = {
            "action": "register_device",
            "device_id": device_id,
            "owner": owner_address,
            "metadata": metadata
        }
        return json.dumps(data).encode()

    def _encode_store_data(self, device_id: str, data_hash: str, data: Dict) -> bytes:
        """Encode device data storage for smart contract."""
        data = {
            "action": "store_data",
            "device_id": device_id,
            "data_hash": data_hash,
            "data": data
        }
        return json.dumps(data).encode()

    def _encode_get_data(self, device_id: str) -> bytes:
        """Encode device data retrieval for smart contract."""
        data = {
            "action": "get_data",
            "device_id": device_id
        }
        return json.dumps(data).encode()

    def _encode_grant_access(self, device_id: str, recipient_address: str) -> bytes:
        """Encode access grant for smart contract."""
        data = {
            "action": "grant_access",
            "device_id": device_id,
            "recipient": recipient_address
        }
        return json.dumps(data).encode()

    def _encode_revoke_access(self, device_id: str, recipient_address: str) -> bytes:
        """Encode access revocation for smart contract."""
        data = {
            "action": "revoke_access",
            "device_id": device_id,
            "recipient": recipient_address
        }
        return json.dumps(data).encode()

    def _calculate_data_hash(self, data: Dict) -> str:
        """Calculate SHA-256 hash of the data."""
        data_str = json.dumps(data, sort_keys=True)
        return hashlib.sha256(data_str.encode()).hexdigest()

    def _encrypt_data(self, data: Dict) -> Dict:
        """Encrypt sensitive data before storage."""
        # In production, implement proper encryption (e.g., AES)
        return {"encrypted": True, "data": data}

    def _decode_device_data(self, encoded_data: bytes) -> List[Dict]:
        """Decode stored device data from blockchain."""
        try:
            return json.loads(encoded_data.decode())
        except json.JSONDecodeError:
            raise ValueError("Failed to decode device data")

# Example usage
if __name__ == "__main__":
    try:
        manager = IoTDeviceManager()
