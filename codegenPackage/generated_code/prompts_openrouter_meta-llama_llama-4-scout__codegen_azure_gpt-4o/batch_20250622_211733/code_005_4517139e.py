"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: How would you implement a secure and organized system for storing and retrieving legal documents for a firm like Sardagna Poeta Advogados, considering data protection laws in Brazil?
Generated: DETERMINISTIC_4517139e291194be
Batch ID: 20250622_211733
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
import hashlib
import base64
from cryptography.fernet import Fernet
from datetime import datetime

# Constants
DOCUMENTS_DIR = "legal_documents"
METADATA_FILE = "metadata.json"
ENCRYPTION_KEY_FILE = "encryption_key.key"

# Ensure compliance with Brazil's LGPD (Lei Geral de Proteção de Dados)
# Generate encryption key if not already present
def generate_encryption_key():
    if not os.path.exists(ENCRYPTION_KEY_FILE):
        key = Fernet.generate_key()
        with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
            key_file.write(key)

# Load encryption key
def load_encryption_key():
    if not os.path.exists(ENCRYPTION_KEY_FILE):
        raise FileNotFoundError("Encryption key not found. Please generate one.")
    with open(ENCRYPTION_KEY_FILE, "rb") as key_file:
        return key_file.read()

# Encrypt document content
def encrypt_content(content, key):
    fernet = Fernet(key)
    return fernet.encrypt(content.encode())

# Decrypt document content
def decrypt_content(encrypted_content, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_content).decode()

# Save document securely
def save_document(document_name, content, metadata):
    try:
        # Ensure the documents directory exists
        os.makedirs(DOCUMENTS_DIR, exist_ok=True)

        # Load encryption key
        key = load_encryption_key()

        # Encrypt content
        encrypted_content = encrypt_content(content, key)

        # Save encrypted document
        document_path = os.path.join(DOCUMENTS_DIR, document_name)
        with open(document_path, "wb") as doc_file:
            doc_file.write(encrypted_content)

        # Save metadata
        metadata_path = os.path.join(DOCUMENTS_DIR, METADATA_FILE)
        metadata["document_name"] = document_name
        metadata["timestamp"] = datetime.now().isoformat()
        metadata["hash"] = hashlib.sha256(content.encode()).hexdigest()

        if os.path.exists(metadata_path):
            with open(metadata_path, "r") as meta_file:
                existing_metadata = json.load(meta_file)
        else:
            existing_metadata = {}

        existing_metadata[document_name] = metadata

        with open(metadata_path, "w") as meta_file:
            json.dump(existing_metadata, meta_file, indent=4)

        print(f"Document '{document_name}' saved successfully.")
    except Exception as e:
        print(f"Error saving document: {e}")

# Retrieve document securely
def retrieve_document(document_name):
    try:
        # Load encryption key
        key = load_encryption_key()

        # Locate document
        document_path = os.path.join(DOCUMENTS_DIR, document_name)
        if not os.path.exists(document_path):
            raise FileNotFoundError(f"Document '{document_name}' not found.")

        # Decrypt content
        with open(document_path, "rb") as doc_file:
            encrypted_content = doc_file.read()
        content = decrypt_content(encrypted_content, key)

        # Retrieve metadata
        metadata_path = os.path.join(DOCUMENTS_DIR, METADATA_FILE)
        if os.path.exists(metadata_path):
            with open(metadata_path, "r") as meta_file:
                metadata = json.load(meta_file)
                document_metadata = metadata.get(document_name, {})
        else:
            document_metadata = {}

        print(f"Document '{document_name}' retrieved successfully.")
        return content, document_metadata
    except Exception as e:
        print(f"Error retrieving document: {e}")
        return None, None

# Example usage
if __name__ == "__main__":
    # Generate encryption key if not already present
    generate_encryption_key()

    # Save a document
    document_name = "contract_123.txt"
    document_content = "This is a confidential legal contract."
    document_metadata = {"author": "John Doe", "category": "Contract"}
    save_document(document_name, document_content, document_metadata)

    # Retrieve the document
    retrieved_content, retrieved_metadata = retrieve_document(document_name)
    if retrieved_content:
        print("Retrieved Content:", retrieved_content)
        print("Retrieved Metadata:", retrieved_metadata)
```
