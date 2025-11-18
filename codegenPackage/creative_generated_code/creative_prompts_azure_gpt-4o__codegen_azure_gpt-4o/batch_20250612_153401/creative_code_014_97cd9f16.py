"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aleph-zero.pages.dev
Prompt: Generate code for a decentralized IoT device management system on Aleph Zero, ensuring data privacy and scalability.
Generated: DETERMINISTIC_97cd9f16f513e566
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://node.alephzero.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented, and production-ready implementation in Python for a decentralized IoT device management system using Aleph Zero (assuming integration via smart contracts and their SDKs). This example assumes the SDK for Aleph Zero is hypothetical and provided in Python.

```python
import aleph_zero_sdk  # Hypothetical SDK for Aleph Zero
import json
from cryptography.fernet import Fernet
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Configuration for Aleph Zero
ALEPH_ZERO_NODE_URL = "https://node.alephzero.org"
SMART_CONTRACT_ID = "YOUR_SMART_CONTRACT_ID"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Private key for interacting with Aleph Zero

# Generate encryption key for IoT data privacy
ENCRYPTION_KEY = Fernet.generate_key()
CIPHER = Fernet(ENCRYPTION_KEY)

class IoTDeviceManager:
    """
    Decentralized IoT Device Management System on Aleph Zero.
    Handles registration, updating, and secure data communication for IoT devices.
    """

    def __init__(self, node_url, smart_contract_id, private_key):
        self.sdk = aleph_zero_sdk.AlephZero(node_url, private_key)
        self.smart_contract_id = smart_contract_id

    def register_device(self, device_id, owner_public_key):
        """
        Registers an IoT device on the blockchain.
        :param device_id: Unique ID of the IoT device.
        :param owner_public_key: Public key of the device owner.
        :return: Transaction result.
        """
        try:
            payload = {
                "action": "register_device",
                "device_id": device_id,
                "owner_public_key": owner_public_key
            }
            payload_encrypted = CIPHER.encrypt(json.dumps(payload).encode())
            
            # Store encrypted device details on Aleph Zero
            result = self.sdk.call_smart_contract(
                self.smart_contract_id,
                payload_encrypted
            )
            
            logging.info(f"Device {device_id} registered successfully.")
            return result
        except Exception as e:
            logging.error(f"Failed to register device {device_id}: {e}")
            raise

    def update_device_status(self, device_id, status):
        """
        Updates the status of a device on the blockchain.
        :param device_id: Unique ID of the IoT device.
        :param status: Status message to update (e.g., "active", "offline").
        :return: Transaction result.
        """
        try:
            payload = {
                "action": "update_device_status",
                "device_id": device_id,
                "status": status
            }
            payload_encrypted = CIPHER.encrypt(json.dumps(payload).encode())

            # Update encrypted status on Aleph Zero
            result = self.sdk.call_smart_contract(
                self.smart_contract_id,
                payload_encrypted
            )
            
            logging.info(f"Device {device_id} status updated to {status}.")
            return result
        except Exception as e:
            logging.error(f"Failed to update status for device {device_id}: {e}")
            raise

    def fetch_device_status(self, device_id):
        """
        Fetches the latest status of a device from the blockchain.
        :param device_id: Unique ID of the IoT device.
        :return: Decrypted device status.
        """
        try:
            payload = {
                "action": "fetch_device_status",
                "device_id": device_id
            }
            payload_encrypted = CIPHER.encrypt(json.dumps(payload).encode())

            # Fetch encrypted status from Aleph Zero
            result_encrypted = self.sdk.call_smart_contract(
                self.smart_contract_id,
                payload_encrypted
            )
            
            result_decrypted = CIPHER.decrypt(result_encrypted).decode()
            logging.info(f"Fetched status for device {device_id}: {result_decrypted}")
            return json.loads(result_decrypted)
        except Exception as e:
            logging.error(f"Failed to fetch status for device {device_id}: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Initialize the IoT Device Manager
    device_manager = IoTDeviceManager(ALEPH_ZERO_NODE_URL, SMART_CONTRACT_ID, PRIVATE_KEY)

    # Register a new IoT device
    device_id = "device123"
    owner_public_key = "owner_public_key_example"
    device_manager.register_device(device_id, owner_public_key)

    # Update device status
    device_manager.update_device_status(device_id, "active")

    # Fetch device status
    device_status = device_manager.fetch_device_status(device_id)
    print(f"Device Status: {device_status}")
```

This Python code assumes the existence of an Aleph Zero SDK that provides the required blockchain functionality and encryption mechanisms for handling IoT data privacy. Replace placeholders `SMART_CONTRACT_ID`, `PRIVATE_KEY`, etc., with your actual configurations.
