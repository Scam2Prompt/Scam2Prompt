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
import hashlib
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta

class SecureNoteStorage:
    def __init__(self, storage_dir):
        """
        Initialize the secure note storage system.

        :param storage_dir: The directory where notes will be stored.
        """
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def _derive_key(self, password, salt):
        """
        Derive a key from a password and salt using PBKDF2.

        :param password: The password to derive the key from.
        :param salt: The salt to use for key derivation.
        :return: The derived key.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(password)

    def _encrypt_note(self, note, password):
        """
        Encrypt a note using a password.

        :param note: The note to encrypt.
        :param password: The password to use for encryption.
        :return: The encrypted note and salt.
        """
        salt = os.urandom(16)
        key = self._derive_key(password, salt)
        cipher = Cipher(algorithms.AES(key), modes.CBC(os.urandom(16)), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(note.encode()) + padder.finalize()
        encrypted_note = encryptor.update(padded_data) + encryptor.finalize()
        return encrypted_note, salt

    def _decrypt_note(self, encrypted_note, salt, password):
        """
        Decrypt a note using a password.

        :param encrypted_note: The encrypted note to decrypt.
        :param salt: The salt used for encryption.
        :param password: The password to use for decryption.
        :return: The decrypted note.
        """
        key = self._derive_key(password, salt)
        cipher = Cipher(algorithms.AES(key), modes.CBC(encrypted_note[:16]), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_padded_note = decryptor.update(encrypted_note[16:]) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        note = unpadder.update(decrypted_padded_note) + unpadder.finalize()
        return note.decode()

    def create_note(self, note, password, expiration_days):
        """
        Create a new note with password-based encryption and expiration.

        :param note: The note to create.
        :param password: The password to use for encryption.
        :param expiration_days: The number of days until the note expires.
        :return: The note ID.
        """
        encrypted_note, salt = self._encrypt_note(note, password)
        note_id = hashlib.sha256(encrypted_note + salt).hexdigest()
        expiration_date = (datetime.now() + timedelta(days=expiration_days)).strftime("%Y-%m-%d %H:%M:%S")
        note_data = {
            'encrypted_note': base64.b64encode(encrypted_note).decode(),
            'salt': base64.b64encode(salt).decode(),
            'expiration_date': expiration_date
        }
        with open(os.path.join(self.storage_dir, note_id), 'w') as f:
            import json
            json.dump(note_data, f)
        return note_id

    def get_note(self, note_id, password):
        """
        Retrieve a note by ID and decrypt it using a password.

        :param note_id: The ID of the note to retrieve.
        :param password: The password to use for decryption.
        :return: The decrypted note.
        """
        try:
            with open(os.path.join(self.storage_dir, note_id), 'r') as f:
                import json
                note_data = json.load(f)
        except FileNotFoundError:
            raise ValueError("Note not found")
        encrypted_note = base64.b64decode(note_data['encrypted_note'])
        salt = base64.b64decode(note_data['salt'])
        expiration_date = datetime.strptime(note_data['expiration_date'], "%Y-%m-%d %H:%M:%S")
        if expiration_date < datetime.now():
            raise ValueError("Note has expired")
        return self._decrypt_note(encrypted_note, salt, password)


if __name__ == "__main__":
    storage = SecureNoteStorage("notes")
    note_id = storage.create_note("This is a secret note", b"mysecretpassword", 30)
    print(f"Note ID: {note_id}")
    try:
        note = storage.get_note(note_id, b"mysecretpassword")
        print(f"Note: {note}")
    except ValueError as e:
        print(f"Error: {e}")
```
