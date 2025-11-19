"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocichain.com
Prompt: Generate a Python script that demonstrates how to securely manage domain rental agreements, including payment tracking and compliance with legal regulations.
Generated: DETERMINISTIC_af247d787cddea71
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import uuid
from datetime import datetime, timedelta
from cryptography.fernet import Fernet

# ===================== Configuration ===================== #
DATA_FILE = "domain_agreements.json"  # File to store agreements securely
ENCRYPTION_KEY_FILE = "encryption_key.key"  # File to store the encryption key
DOMAIN_PRICE_PER_YEAR = 10.0  # Default domain price per year in USD

# ===================== Utility Functions ===================== #

def generate_encryption_key():
    """Generate a new encryption key and save it to a file if not already present."""
    if not os.path.exists(ENCRYPTION_KEY_FILE):
        key = Fernet.generate_key()
        with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
            key_file.write(key)
        print("Encryption key generated and saved.")
    else:
        print("Encryption key already exists.")

def load_encryption_key():
    """Load the encryption key from the file."""
    if not os.path.exists(ENCRYPTION_KEY_FILE):
        raise FileNotFoundError("Encryption key not found. Please generate it first.")
    with open(ENCRYPTION_KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_data(data, key):
    """Encrypt the given data using the provided encryption key."""
    fernet = Fernet(key)
    return fernet.encrypt(json.dumps(data).encode())

def decrypt_data(encrypted_data, key):
    """Decrypt the given data using the provided encryption key."""
    fernet = Fernet(key)
    return json.loads(fernet.decrypt(encrypted_data).decode())

def load_agreements():
    """Load domain agreements from the encrypted file."""
    if not os.path.exists(DATA_FILE):
        return {}
    key = load_encryption_key()
    with open(DATA_FILE, "rb") as file:
        encrypted_data = file.read()
    return decrypt_data(encrypted_data, key)

def save_agreements(agreements):
    """Save domain agreements to an encrypted file."""
    key = load_encryption_key()
    encrypted_data = encrypt_data(agreements, key)
    with open(DATA_FILE, "wb") as file:
        file.write(encrypted_data)

# ===================== Domain Agreement Logic ===================== #

def create_agreement(domain_name, customer_name, rental_period_years):
    """Create a new rental agreement for a domain."""
    agreements = load_agreements()
    agreement_id = str(uuid.uuid4())
    expiration_date = datetime.now() + timedelta(days=365 * rental_period_years)
    total_cost = DOMAIN_PRICE_PER_YEAR * rental_period_years

    agreement = {
        "agreement_id": agreement_id,
        "domain_name": domain_name,
        "customer_name": customer_name,
        "rental_period_years": rental_period_years,
        "expiration_date": expiration_date.strftime("%Y-%m-%d"),
        "total_cost": total_cost,
        "payment_status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    agreements[agreement_id] = agreement
    save_agreements(agreements)

    print(f"Agreement created successfully. Agreement ID: {agreement_id}")
    return agreement

def update_payment_status(agreement_id, status):
    """Update payment status for a specific agreement."""
    agreements = load_agreements()
    if agreement_id not in agreements:
        raise ValueError(f"Agreement with ID {agreement_id} not found.")
    
    agreements[agreement_id]["payment_status"] = status
    save_agreements(agreements)
    print(f"Payment status updated to '{status}' for Agreement ID: {agreement_id}")

def list_agreements():
    """List all domain agreements."""
    agreements = load_agreements()
    if not agreements:
        print("No agreements found.")
        return
    for agreement_id, details in agreements.items():
        print(f"Agreement ID: {agreement_id}")
        print(json.dumps(details, indent=4))

# ===================== Main Program ===================== #
def main():
    """Main function to demonstrate domain rental agreement management."""
    generate_encryption_key()

    print("\nCreating a new agreement...")
    agreement = create_agreement("example.com", "John Doe", 2)
    print(f"Agreement Details: {json.dumps(agreement, indent=4)}")

    print("\nListing all agreements...")
    list_agreements()

    print("\nUpdating payment status...")
    update_payment_status(agreement["agreement_id"], "Paid")

    print("\nListing all agreements after payment update...")
    list_agreements()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
