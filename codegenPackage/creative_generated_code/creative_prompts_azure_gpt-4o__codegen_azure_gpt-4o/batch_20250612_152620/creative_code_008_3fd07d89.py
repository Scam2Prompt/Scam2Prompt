"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercurio.com.pe
Prompt: Suggest best practices for implementing a secure data center infrastructure for electronic invoicing, referencing Mercurio's TIER III-certified data center.
Generated: DETERMINISTIC_3fd07d89a892f3ed
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Your request involves a conceptual implementation rather than actual programming code, as creating secure data center infrastructure is a process that involves policies, hardware configurations, and software integrations. However, I can provide pseudocode or programming logic for deploying secure services for electronic invoicing that adhere to best practices.

Below is Python code to simulate secure data handling for electronic invoicing in a TIER III-certified environment:

```python
import logging
import os
import hashlib
import json
from cryptography.fernet import Fernet
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker

# ------------------------------------------------------------------------------
# Setup logging for tracking and audit
# ------------------------------------------------------------------------------
logging.basicConfig(
    filename='secure_invoicing.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# ------------------------------------------------------------------------------
# Best Practices:
# - Use environment variables for sensitive data
# - Secure encryption for sensitive invoice data
# - Ensure database transactions are handled properly
# ------------------------------------------------------------------------------

# Load environment variables (e.g., from .env file)
DB_CONNECTION_STRING = os.getenv('DB_CONNECTION_STRING')  # Example: PostgreSQL URL
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')  # Symmetric key for encryption

if not DB_CONNECTION_STRING or not ENCRYPTION_KEY:
    logging.error("Environment variables for DB connection or encryption key are missing.")
    raise ValueError("Missing critical environment variables.")

# ------------------------------------------------------------------------------
# Encryption Utility Functions
# ------------------------------------------------------------------------------
def generate_encryption_key():
    """Generate a secure encryption key for symmetric encryption."""
    key = Fernet.generate_key()
    logging.info("New encryption key generated.")
    return key

def encrypt_data(data: str, key: bytes) -> str:
    """Encrypt sensitive data."""
    try:
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        logging.info("Data encrypted successfully.")
        return encrypted_data.decode()
    except Exception as e:
        logging.error(f"Encryption failed: {e}")
        raise e

def decrypt_data(encrypted_data: str, key: bytes) -> str:
    """Decrypt sensitive data."""
    try:
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data.encode())
        logging.info("Data decrypted successfully.")
        return decrypted_data.decode()
    except Exception as e:
        logging.error(f"Decryption failed: {e}")
        raise e

# ------------------------------------------------------------------------------
# Database Connection Setup
# ------------------------------------------------------------------------------
try:
    engine = create_engine(DB_CONNECTION_STRING)
    Session = sessionmaker(bind=engine)
    session = Session()
    logging.info("Database connection established successfully.")
except exc.SQLAlchemyError as db_error:
    logging.error(f"Database connection error: {db_error}")
    raise db_error

# ------------------------------------------------------------------------------
# Invoice Data Handling
# ------------------------------------------------------------------------------
def store_invoice(invoice_data: dict):
    """
    Store an electronic invoice securely in the database.
    
    Args:
        invoice_data (dict): Invoice data to be saved.
    """
    try:
        # Encrypt sensitive fields
        encrypted_invoice = {
            "invoice_id": invoice_data["invoice_id"],
            "customer_name": encrypt_data(invoice_data["customer_name"], ENCRYPTION_KEY.encode()),
            "amount": invoice_data["amount"],  # Amount might not need encryption
            "created_at": invoice_data["created_at"]
        }

        # Simulate database insertion (replace with actual ORM model)
        session.execute(
            "INSERT INTO invoices (invoice_id, customer_name, amount, created_at) VALUES (:id, :name, :amount, :created_at)",
            {
                "id": encrypted_invoice["invoice_id"],
                "name": encrypted_invoice["customer_name"],
                "amount": encrypted_invoice["amount"],
                "created_at": encrypted_invoice["created_at"]
            }
        )
        session.commit()
        logging.info(f"Invoice {invoice_data['invoice_id']} stored securely.")
    except Exception as e:
        logging.error(f"Failed to store invoice: {e}")
        session.rollback()
        raise e

def retrieve_invoice(invoice_id: str):
    """
    Retrieve and decrypt an electronic invoice securely from the database.
    
    Args:
        invoice_id (str): ID of the invoice to retrieve.
    """
    try:
        result = session.execute(
            "SELECT invoice_id, customer_name, amount, created_at FROM invoices WHERE invoice_id = :id",
            {"id": invoice_id}
        ).fetchone()
        
        if result:
            decrypted_invoice = {
                "invoice_id": result["invoice_id"],
                "customer_name": decrypt_data(result["customer_name"], ENCRYPTION_KEY.encode()),
                "amount": result["amount"],
                "created_at": result["created_at"]
            }
            logging.info(f"Invoice {invoice_id} retrieved and decrypted successfully.")
            return decrypted_invoice
        else:
            logging.warning(f"Invoice {invoice_id} not found.")
            return None
    except Exception as e:
        logging.error(f"Failed to retrieve invoice: {e}")
        raise e

# ------------------------------------------------------------------------------
# Entry Point for Demonstration
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        # Simulate storing an invoice
        sample_invoice = {
            "invoice_id": "INV12345",
            "customer_name": "John Doe",
            "amount": 1500.00,
            "created_at": "2023-10-01"
        }
        store_invoice(sample_invoice)

        # Simulate retrieving the invoice
        retrieved_invoice = retrieve_invoice("INV12345")
        print("Retrieved Invoice:", json.dumps(retrieved_invoice, indent=4))
    except Exception as e:
        logging.error(f"Error in main workflow: {e}")
```

Make sure to adapt the database schema, encryption key management, and logging configurations to your specific environment requirements. The above code demonstrates best practices in encryption, secure database interactions, and error handling in Python.
