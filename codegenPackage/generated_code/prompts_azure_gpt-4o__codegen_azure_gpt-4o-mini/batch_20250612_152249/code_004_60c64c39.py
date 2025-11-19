"""
Generated Code Metadata:
========================
Original URL: https://harvest-kfi.pages.dev
Prompt: Write code to implement a multi-layer migration strategy using CryptoNext's Quantum Safe Software Suite for transitioning a PKI infrastructure to post-quantum security.
Generated: DETERMINISTIC_60c64c39f72881a3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from cryptonext import QuantumSafePKI, MigrationManager, KeyPair, Certificate

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PKIMigration:
    def __init__(self, current_pki: QuantumSafePKI, new_pki: QuantumSafePKI):
        """
        Initialize the PKIMigration class.

        :param current_pki: The current PKI infrastructure instance.
        :param new_pki: The new PKI infrastructure instance with post-quantum capabilities.
        """
        self.current_pki = current_pki
        self.new_pki = new_pki
        self.migration_manager = MigrationManager(current_pki, new_pki)

    def migrate_keys(self):
        """
        Migrate keys from the current PKI to the new PKI.
        """
        try:
            logging.info("Starting key migration...")
            for key in self.current_pki.get_all_keys():
                new_key = KeyPair.generate_post_quantum_key()
                self.new_pki.store_key(new_key)
                logging.info(f"Successfully migrated key: {key.id} to new key: {new_key.id}")
            logging.info("Key migration completed successfully.")
        except Exception as e:
            logging.error(f"Error during key migration: {e}")
            raise

    def migrate_certificates(self):
        """
        Migrate certificates from the current PKI to the new PKI.
        """
        try:
            logging.info("Starting certificate migration...")
            for cert in self.current_pki.get_all_certificates():
                new_cert = Certificate.create_from_existing(cert, self.new_pki)
                self.new_pki.store_certificate(new_cert)
                logging.info(f"Successfully migrated certificate: {cert.id} to new certificate: {new_cert.id}")
            logging.info("Certificate migration completed successfully.")
        except Exception as e:
            logging.error(f"Error during certificate migration: {e}")
            raise

    def run_migration(self):
        """
        Execute the full migration process.
        """
        try:
            self.migrate_keys()
            self.migrate_certificates()
            logging.info("PKI migration completed successfully.")
        except Exception as e:
            logging.critical(f"Migration process failed: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        current_pki = QuantumSafePKI.load_current_pki()
        new_pki = QuantumSafePKI.initialize_new_pki()
        
        pki_migration = PKIMigration(current_pki, new_pki)
        pki_migration.run_migration()
    except Exception as e:
        logging.critical(f"Failed to initialize migration: {e}")
```
