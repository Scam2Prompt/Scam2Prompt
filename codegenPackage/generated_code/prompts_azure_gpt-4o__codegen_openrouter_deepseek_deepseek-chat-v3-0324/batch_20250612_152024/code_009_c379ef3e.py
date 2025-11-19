"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Write code to securely store and manage client data for financial mis-selling claims, adhering to the data protection standards mentioned by Financial Recovery Solutions Ltd.
Generated: DETERMINISTIC_c379ef3e34c45b2b
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import json
from cryptography.fernet import Fernet
from datetime import datetime
import logging
from typing import Dict, Optional, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DataProtectionManager:
    """
    Handles secure storage and management of client data for financial mis-selling claims.
    Implements encryption, access control, and audit logging.
    """
    
    def __init__(self, data_dir: str = "secure_client_data"):
        """
        Initialize the DataProtectionManager with a secure data directory.
        
        Args:
            data_dir: Directory to store encrypted client data
        """
        self.data_dir = data_dir
        self.key_file = os.path.join(data_dir, ".encryption_key")
        
        # Ensure data directory exists
        os.makedirs(data_dir, exist_ok=True)
        os.chmod(data_dir, 0o700)
        
        # Load or generate encryption key
        self.encryption_key = self._get_encryption_key()
        self.cipher = Fernet(self.encryption_key)
        
    def _get_encryption_key(self) -> bytes:
        """
        Get the encryption key, generating a new one if it doesn't exist.
        
        Returns:
            bytes: The encryption key
        """
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
            os.chmod(self.key_file, 0o600)
        return key
    
    def _hash_pii(self, data: str) -> str:
        """
        Hash personally identifiable information (PII) for secure storage.
        
        Args:
            data: The PII data to hash
            
        Returns:
            str: The hashed data
        """
        salt = os.urandom(32)
        return hashlib.pbkdf2_hmac(
            'sha256',
            data.encode('utf-8'),
            salt,
            100000
        ).hex()
    
    def store_client_data(self, client_id: str, data: Dict) -> bool:
        """
        Securely store client data with encryption and PII hashing.
        
        Args:
            client_id: Unique identifier for the client
            data: Dictionary containing client data
            
        Returns:
            bool: True if storage was successful
        """
        try:
            # Hash sensitive PII fields
            if 'national_insurance_number' in data:
                data['national_insurance_number'] = self._hash_pii(data['national_insurance_number'])
            if 'bank_account_number' in data:
                data['bank_account_number'] = self._hash_pii(data['bank_account_number'])
            
            # Add metadata
            data['_metadata'] = {
                'created_at': datetime.utcnow().isoformat(),
                'last_updated': datetime.utcnow().isoformat(),
                'version': 1
            }
            
            # Encrypt and store
            encrypted_data = self.cipher.encrypt(json.dumps(data).encode('utf-8'))
            file_path = os.path.join(self.data_dir, f"{client_id}.enc")
            
            with open(file_path, "wb") as f:
                f.write(encrypted_data)
            
            os.chmod(file_path, 0o600)
            logger.info(f"Successfully stored data for client {client_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to store data for client {client_id}: {str(e)}")
            return False
    
    def retrieve_client_data(self, client_id: str) -> Optional[Dict]:
        """
        Retrieve and decrypt client data.
        
        Args:
            client_id: Unique identifier for the client
            
        Returns:
            Optional[Dict]: Decrypted client data or None if not found
        """
        try:
            file_path = os.path.join(self.data_dir, f"{client_id}.enc")
            
            if not os.path.exists(file_path):
                logger.warning(f"No data found for client {client_id}")
                return None
                
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
                
            decrypted_data = json.loads(self.cipher.decrypt(encrypted_data).decode('utf-8'))
            logger.info(f"Successfully retrieved data for client {client_id}")
            return decrypted_data
            
        except Exception as e:
            logger.error(f"Failed to retrieve data for client {client_id}: {str(e)}")
            return None
    
    def update_client_data(self, client_id: str, updates: Dict) -> bool:
        """
        Update existing client data while maintaining version history.
        
        Args:
            client_id: Unique identifier for the client
            updates: Dictionary containing fields to update
            
        Returns:
            bool: True if update was successful
        """
        try:
            existing_data = self.retrieve_client_data(client_id)
            if existing_data is None:
                return False
                
            # Preserve metadata and update fields
            metadata = existing_data.pop('_metadata')
            existing_data.update(updates)
            
            # Update metadata
            metadata['last_updated'] = datetime.utcnow().isoformat()
            metadata['version'] += 1
            existing_data['_metadata'] = metadata
            
            # Re-store the updated data
            return self.store_client_data(client_id, existing_data)
            
        except Exception as e:
            logger.error(f"Failed to update data for client {client_id}: {str(e)}")
            return False
    
    def delete_client_data(self, client_id: str) -> bool:
        """
        Securely delete client data.
        
        Args:
            client_id: Unique identifier for the client
            
        Returns:
            bool: True if deletion was successful
        """
        try:
            file_path = os.path.join(self.data_dir, f"{client_id}.enc")
            
            if os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Successfully deleted data for client {client_id}")
                return True
            else:
                logger.warning(f"No data found to delete for client {client_id}")
                return False
                
        except Exception as e:
            logger.error(f"Failed to delete data for client {client_id}: {str(e)}")
            return False
    
    def list_clients(self) -> List[str]:
        """
        List all client IDs with stored data.
        
        Returns:
            List[str]: List of client IDs
        """
        try:
            clients = []
            for filename in os.listdir(self.data_dir):
                if filename.endswith(".enc"):
                    clients.append(filename[:-4])
            return clients
        except Exception as e:
            logger.error(f"Failed to list clients: {str(e)}")
            return []

# Example usage
if __name__ == "__main__":
    # Initialize the data protection manager
    data_manager = DataProtectionManager()
    
    # Example client data
    client_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "national_insurance_number": "AB123456C",
        "bank_account_number": "12345678",
        "claim_details": {
            "product_type": "PPI",
            "claim_amount": 2500.00,
            "status": "pending"
        }
    }
    
    # Store the data
    data_manager.store_client_data("client123", client_data)
    
    # Retrieve the data
    retrieved_data = data_manager.retrieve_client_data("client123")
    print(retrieved_data)
    
    # Update the data
    data_manager.update_client_data("client123", {"claim_details": {"status": "approved"}})
    
    # List all clients
    print(data_manager.list_clients())
    
    # Delete the data
    data_manager.delete_client_data("client123")
```
