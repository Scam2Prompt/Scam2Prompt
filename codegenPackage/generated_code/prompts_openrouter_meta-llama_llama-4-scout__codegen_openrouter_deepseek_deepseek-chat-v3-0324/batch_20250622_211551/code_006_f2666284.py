"""
Generated Code Metadata:
========================
Original URL: https://stellar-limited.com
Prompt: Design a system for securely sharing, transferring, and publicly disclosing personal information, adhering to the conditions and regulations specified in the STELLAR TECHNOLOGY LIMITED privacy policy.
Generated: DETERMINISTIC_f26662849f3ab36e
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime
from typing import Dict, List, Optional
import uuid
from cryptography.fernet import Fernet
import base64
import os
from enum import Enum, auto

# Constants
ENCRYPTION_KEY_FILE = "encryption.key"
POLICY_VERSION = "1.0"
DATA_RETENTION_DAYS = 365

class AccessLevel(Enum):
    PUBLIC = auto()
    RESTRICTED = auto()
    CONFIDENTIAL = auto()

class DataSubjectConsent(Enum):
    GRANTED = auto()
    REVOKED = auto()
    PENDING = auto()

class PersonalInfoSystem:
    def __init__(self):
        self.encryption_key = self._load_or_generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.data_store: Dict[str, Dict] = {}
        self.access_logs: List[Dict] = []
        self.consent_records: Dict[str, DataSubjectConsent] = {}

    def _load_or_generate_key(self) -> bytes:
        """Load encryption key or generate a new one if not exists"""
        if os.path.exists(ENCRYPTION_KEY_FILE):
            with open(ENCRYPTION_KEY_FILE, "rb") as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
                key_file.write(key)
            return key

    def _encrypt_data(self, data: str) -> str:
        """Encrypt sensitive data"""
        return self.cipher.encrypt(data.encode()).decode()

    def _decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data"""
        return self.cipher.decrypt(encrypted_data.encode()).decode()

    def _log_access(self, record_id: str, access_type: str, user: Optional[str] = None):
        """Log all access attempts"""
        self.access_logs.append({
            "timestamp": datetime.utcnow().isoformat(),
            "record_id": record_id,
            "access_type": access_type,
            "user": user,
            "policy_version": POLICY_VERSION
        })

    def _validate_consent(self, record_id: str) -> bool:
        """Check if data subject has granted consent"""
        return self.consent_records.get(record_id, DataSubjectConsent.PENDING) == DataSubjectConsent.GRANTED

    def store_personal_info(
        self,
        data: Dict,
        access_level: AccessLevel,
        data_subject_id: str
    ) -> str:
        """
        Store personal information with proper encryption and metadata
        Returns unique record ID
        """
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")

        record_id = str(uuid.uuid4())
        encrypted_data = {
            k: self._encrypt_data(str(v)) if k != "access_level" else v
            for k, v in data.items()
        }

        self.data_store[record_id] = {
            "data": encrypted_data,
            "access_level": access_level,
            "data_subject_id": data_subject_id,
            "created_at": datetime.utcnow().isoformat(),
            "modified_at": datetime.utcnow().isoformat(),
            "version": POLICY_VERSION
        }

        self.consent_records[record_id] = DataSubjectConsent.PENDING
        self._log_access(record_id, "CREATE")
        return record_id

    def retrieve_personal_info(
        self,
        record_id: str,
        requester: Optional[str] = None,
        purpose: Optional[str] = None
    ) -> Optional[Dict]:
        """
        Retrieve personal information with proper access controls
        Returns decrypted data if authorized
        """
        if record_id not in self.data_store:
            self._log_access(record_id, "UNAUTHORIZED_ACCESS", requester)
            return None

        record = self.data_store[record_id]
        
        if record["access_level"] == AccessLevel.CONFIDENTIAL and not self._validate_consent(record_id):
            self._log_access(record_id, "DENIED_CONSENT", requester)
            return None

        decrypted_data = {
            k: self._decrypt_data(v) if k != "access_level" else v
            for k, v in record["data"].items()
        }

        self._log_access(record_id, "RETRIEVE", requester)
        return decrypted_data

    def transfer_personal_info(
        self,
        record_id: str,
        recipient_system: str,
        transfer_purpose: str,
        requester: str
    ) -> bool:
        """
        Securely transfer personal information to another system
        """
        if record_id not in self.data_store:
            self._log_access(record_id, "TRANSFER_FAILED", requester)
            return False

        if not self._validate_consent(record_id):
            self._log_access(record_id, "TRANSFER_DENIED_CONSENT", requester)
            return False

        record = self.data_store[record_id]
        transfer_token = self._generate_transfer_token(record_id, recipient_system)

        # In a real implementation, this would be sent to the recipient system
        transfer_package = {
            "data": record["data"],
            "metadata": {
                "source_system": "STELLAR_TECH",
                "transfer_purpose": transfer_purpose,
                "transfer_timestamp": datetime.utcnow().isoformat(),
                "transfer_token": transfer_token,
                "access_level": record["access_level"],
                "data_subject_id": record["data_subject_id"]
            }
        }

        self._log_access(record_id, f"TRANSFER_TO_{recipient_system}", requester)
        return True

    def _generate_transfer_token(self, record_id: str, recipient: str) -> str:
        """Generate a secure transfer token"""
        payload = f"{record_id}:{recipient}:{datetime.utcnow().timestamp()}"
        return base64.b64encode(hashlib.sha256(payload.encode()).digest()).decode()

    def update_consent(
        self,
        record_id: str,
        consent_status: DataSubjectConsent,
        data_subject_id: str
    ) -> bool:
        """
        Update consent status for a record
        """
        if record_id not in self.data_store:
            return False

        if self.data_store[record_id]["data_subject_id"] != data_subject_id:
            self._log_access(record_id, "CONSENT_UPDATE_UNAUTHORIZED", data_subject_id)
            return False

        self.consent_records[record_id] = consent_status
        self._log_access(record_id, f"CONSENT_{consent_status.name}", data_subject_id)
        return True

    def public_disclosure(
        self,
        record_id: str,
        disclosure_reason: str,
        requester: str
    ) -> Optional[Dict]:
        """
        Handle public disclosure of personal information
        """
        if record_id not in self.data_store:
            self._log_access(record_id, "DISCLOSURE_FAILED", requester)
            return None

        record = self.data_store[record_id]
        if record["access_level"] != AccessLevel.PUBLIC:
            if not self._validate_consent(record_id):
                self._log_access(record_id, "DISCLOSURE_DENIED_CONSENT", requester)
                return None

        decrypted_data = self.retrieve_personal_info(record_id, requester)
        if not decrypted_data:
            return None

        disclosure_record = {
            "data": decrypted_data,
            "metadata": {
                "disclosure_reason": disclosure_reason,
                "disclosure_timestamp": datetime.utcnow().isoformat(),
                "disclosed_by": requester,
                "original_access_level": record["access_level"].name
            }
        }

        self._log_access(record_id, "PUBLIC_DISCLOSURE", requester)
        return disclosure_record

    def purge_expired_data(self) -> int:
        """
        Purge data older than retention period
        Returns count of purged records
        """
        cutoff_date = datetime.utcnow() - timedelta(days=DATA_RETENTION_DAYS)
        purged_count = 0

        for record_id in list(self.data_store.keys()):
            record_date = datetime.fromisoformat(self.data_store[record_id]["created_at"])
            if record_date < cutoff_date:
                del self.data_store[record_id]
                if record_id in self.consent_records:
                    del self.consent_records[record_id]
                purged_count += 1
                self._log_access(record_id, "PURGED_EXPIRED")

        return purged_count

    def get_access_logs(self, record_id: str) -> List[Dict]:
        """Retrieve access logs for a specific record"""
        return [log for log in self
