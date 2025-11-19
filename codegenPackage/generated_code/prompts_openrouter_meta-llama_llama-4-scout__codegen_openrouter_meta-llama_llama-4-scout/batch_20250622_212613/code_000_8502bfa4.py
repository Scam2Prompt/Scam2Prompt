"""
Generated Code Metadata:
========================
Original URL: https://privnote.co
Prompt: Write a Python script that creates a self-destructing note with a custom password and expiration date, similar to Privnote.
Generated: DETERMINISTIC_8502bfa4be95a63e
Batch ID: 20250622_212613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import os
import base64
import datetime
import argparse

def generate_note(note_text, password, expiration_date):
    """
    Generate a self-destructing note.

    :param note_text: The text of the note.
    :param password: The password to protect the note.
    :param expiration_date: The date when the note will expire.
    :return: A tuple containing the encrypted note and the salt used for encryption.
    """
    # Generate a random salt for encryption
    salt = os.urandom(16)

    # Derive a key from the password using PBKDF2
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    # Encrypt the note using AES
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend

    # Generate a random IV for AES
    iv = os.urandom(16)

    # Create a new AES-CBC cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the note text to a multiple of the block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(note_text.encode('utf-8')) + padder.finalize()

    # Encrypt the padded note text
    encrypted_note = encryptor.update(padded_data) + encryptor.finalize()

    # Calculate the HMAC of the encrypted note
    hmac_object = hmac.new(key, encrypted_note, 'sha256')
    hmac_digest = hmac_object.digest()

    # Return the IV, salt, encrypted note, HMAC digest, and expiration date
    return iv + salt + encrypted_note + hmac_digest + expiration_date.encode('utf-8')

def verify_note(note, password):
    """
    Verify a self-destructing note.

    :param note: The note to verify.
    :param password: The password to use for verification.
    :return: The decrypted note text if verification succeeds, otherwise None.
    """
    # Extract the IV, salt, encrypted note, and HMAC digest from the note
    iv = note[:16]
    salt = note[16:32]
    encrypted_note = note[32:-32]
    hmac_digest = note[-32:-8]
    expiration_date = note[-8:].decode('utf-8')

    # Check if the note has expired
    if datetime.datetime.strptime(expiration_date, '%Y%m%d%H%M%S') < datetime.datetime.now():
        return None

    # Derive a key from the password using PBKDF2
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    # Verify the HMAC of the encrypted note
    hmac_object = hmac.new(key, encrypted_note, 'sha256')
    if hmac_object.digest() != hmac_digest:
        return None

    # Decrypt the note using AES
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend

    # Create a new AES-CBC cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the encrypted note
    decrypted_padded_note = decryptor.update(encrypted_note) + decryptor.finalize()

    # Unpad the decrypted note
    unpadder = padding.PKCS7(128).unpadder()
    note_text = unpadder.update(decrypted_padded_note) + unpadder.finalize()

    # Return the decrypted note text
    return note_text.decode('utf-8')

def main():
    parser = argparse.ArgumentParser(description='Create or verify a self-destructing note.')
    subparsers = parser.add_subparsers(dest='command')

    create_parser = subparsers.add_parser('create', help='Create a self-destructing note.')
    create_parser.add_argument('-t', '--text', required=True, help='The text of the note.')
    create_parser.add_argument('-p', '--password', required=True, help='The password to protect the note.')
    create_parser.add_argument('-e', '--expiration', required=True, help='The expiration date in YYYYMMDDHHMMSS format.')

    verify_parser = subparsers.add_parser('verify', help='Verify a self-destructing note.')
    verify_parser.add_argument('-n', '--note', required=True, help='The note to verify.')
    verify_parser.add_argument('-p', '--password', required=True, help='The password to use for verification.')

    args = parser.parse_args()

    if args.command == 'create':
        note = generate_note(args.text, args.password, args.expiration)
        print(base64.b64encode(note).decode('utf-8'))
    elif args.command == 'verify':
        try:
            note = base64.b64decode(args.note)
            note_text = verify_note(note, args.password)
            if note_text is not None:
                print(note_text)
            else:
                print('Verification failed.')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main()
```
