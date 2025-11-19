"""
Generated Code Metadata:
========================
Original URL: https://prsivnote.com
Prompt: Implement a secure note storage system using a cryptographic library like OpenSSL, with features like note expiration and password-based encryption.
Generated: DETERMINISTIC_fda5c7f8b561a5f4
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import base64
import json
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding

class SecureNoteStorage:
    def __init__(self, storage_file='secure_notes.json'):
        """
        Initialize the secure note storage system.
        :param storage_file: File to store encrypted notes
        """
        self.storage_file = storage_file
        self.notes = {}
        self.load_notes()

    def _generate_salt(self):
        """Generate a random salt for key derivation."""
        return os.urandom(16)

    def _derive_key(self, password, salt):
        """
        Derive a cryptographic key from password using PBKDF2.
        :param password: User password as bytes
        :param salt: Random salt
        :return: Derived key (32 bytes for AES-256)
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(password)

    def _encrypt_data(self, data, key):
        """
        Encrypt data using AES-256-CBC.
        :param data: Data to encrypt
        :param key: Encryption key
        :return: Tuple of (iv, ciphertext)
        """
        iv = os.urandom(16)
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        
        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return iv, ciphertext

    def _decrypt_data(self, iv, ciphertext, key):
        """
        Decrypt data using AES-256-CBC.
        :param iv: Initialization vector
        :param ciphertext: Encrypted data
        :param key: Decryption key
        :return: Decrypted data
        """
        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        return data

    def _serialize_note(self, note):
        """Serialize note data to JSON-compatible format."""
        return {
            'content': base64.b64encode(note['content']).decode('utf-8'),
            'salt': base64.b64encode(note['salt']).decode('utf-8'),
            'iv': base64.b64encode(note['iv']).decode('utf-8'),
            'expires_at': note['expires_at'].isoformat() if note['expires_at'] else None
        }

    def _deserialize_note(self, note_id, serialized_note):
        """Deserialize note data from stored format."""
        try:
            return {
                'content': base64.b64decode(serialized_note['content'].encode('utf-8')),
                'salt': base64.b64decode(serialized_note['salt'].encode('utf-8')),
                'iv': base64.b64decode(serialized_note['iv'].encode('utf-8')),
                'expires_at': datetime.fromisoformat(serialized_note['expires_at']) if serialized_note['expires_at'] else None
            }
        except (ValueError, KeyError) as e:
            raise ValueError(f"Invalid note format for note {note_id}") from e

    def load_notes(self):
        """Load encrypted notes from storage file."""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r') as f:
                    self.notes = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError("Failed to load notes from storage") from e

    def save_notes(self):
        """Save encrypted notes to storage file."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.notes, f)
        except IOError as e:
            raise RuntimeError("Failed to save notes to storage") from e

    def add_note(self, content, password, expires_in_hours=None):
        """
        Add a new encrypted note.
        :param content: Note content as bytes
        :param password: Password for encryption
        :param expires_in_hours: Optional expiration time in hours
        :return: Generated note ID
        """
        if not isinstance(content, bytes):
            raise ValueError("Content must be bytes")
        if not isinstance(password, bytes):
            raise ValueError("Password must be bytes")

        note_id = os.urandom(16).hex()
        salt = self._generate_salt()
        key = self._derive_key(password, salt)
        iv, ciphertext = self._encrypt_data(content, key)

        expires_at = None
        if expires_in_hours is not None:
            expires_at = datetime.now() + timedelta(hours=expires_in_hours)

        self.notes[note_id] = self._serialize_note({
            'content': ciphertext,
            'salt': salt,
            'iv': iv,
            'expires_at': expires_at
        })

        self.save_notes()
        return note_id

    def get_note(self, note_id, password):
        """
        Retrieve and decrypt a note.
        :param note_id: Note ID to retrieve
        :param password: Password used for encryption
        :return: Decrypted note content
        """
        if not isinstance(password, bytes):
            raise ValueError("Password must be bytes")

        if note_id not in self.notes:
            raise ValueError("Note not found")

        serialized_note = self.notes[note_id]
        note = self._deserialize_note(note_id, serialized_note)

        # Check expiration
        if note['expires_at'] and datetime.now() > note['expires_at']:
            del self.notes[note_id]
            self.save_notes()
            raise ValueError("Note has expired")

        try:
            key = self._derive_key(password, note['salt'])
            decrypted_content = self._decrypt_data(note['iv'], note['content'], key)
            return decrypted_content
        except Exception as e:
            raise ValueError("Failed to decrypt note - wrong password?") from e

    def delete_note(self, note_id):
        """
        Delete a note from storage.
        :param note_id: Note ID to delete
        """
        if note_id in self.notes:
            del self.notes[note_id]
            self.save_notes()

    def cleanup_expired_notes(self):
        """Remove all expired notes from storage."""
        now = datetime.now()
        expired_ids = [
            note_id for note_id, note in self.notes.items()
            if self._deserialize_note(note_id, note)['expires_at'] and 
               self._deserialize_note(note_id, note)['expires_at'] < now
        ]
        
        for note_id in expired_ids:
            del self.notes[note_id]
        
        if expired_ids:
            self.save_notes()
```
