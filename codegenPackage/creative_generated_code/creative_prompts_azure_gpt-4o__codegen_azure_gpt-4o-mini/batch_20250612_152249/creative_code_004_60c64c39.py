"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harvest-kfi.pages.dev
Prompt: Write code to implement a multi-layer migration strategy using CryptoNext's Quantum Safe Software Suite for transitioning a PKI infrastructure to post-quantum security.
Generated: DETERMINISTIC_60c64c39f72881a3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from cryptonext import QuantumSafePKI, CryptoException

# Configure logger for the migration process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PKIMigration:
    def __init__(self, pki_config_path, quantum_safe_config_path):
        """
        Initialize the PKIMigration class.

        :param pki_config_path: Path to the existing PKI configuration.
        :param quantum_safe_config_path: Path to the Quantum Safe configuration.
        """
        self.pki_config_path = pki_config_path
        self.quantum_safe_config_path = quantum_safe_config_path
        self.pki_data = {}
        self.quantum_safe_data = {}

    def load_configurations(self):
        """Load existing PKI and Quantum Safe configurations."""
        try:
            with open(self.pki_config_path, 'r') as file:
                self.pki_data = json.load(file)
            with open(self.quantum_safe_config_path, 'r') as file:
                self.quantum_safe_data = json.load(file)
            logger.info("Configurations loaded successfully.")
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Error loading configurations: {e}")
            raise

    def migrate_certificates(self):
        """Migrate certificates from existing PKI to Quantum Safe PKI."""
        try:
            quantum_pki = QuantumSafePKI(configuration=self.quantum_safe_data)
            for cert in self.pki_data.get("certificates", []):
                # Convert the certificate to a quantum-safe format
                quantum_cert = quantum_pki.convert_certificate(cert)
                quantum_pki.store_certificate(quantum_cert)
                logger.info(f"Certificate {cert['id']} migrated successfully.")
        except CryptoException as e:
            logger.error(f"Crypto exception during migration: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during migration: {e}")
            raise

    def run_migration(self):
        """Run the entire migration process."""
        try:
            logger.info("Starting PKI migration process...")
            self.load_configurations()
            self.migrate_certificates()
            logger.info("PKI migration completed successfully.")
        except Exception as e:
            logger.error(f"Migration process failed: {e}")

# Entry point for the script
if __name__ == "__main__":
    # Paths to configuration files
    pki_config_path = "existing_pki_config.json"
    quantum_safe_config_path = "quantum_safe_config.json"
    
    migration = PKIMigration(pki_config_path, quantum_safe_config_path)
    migration.run_migration()
```

Make sure to adjust the paths `existing_pki_config.json` and `quantum_safe_config.json` to point to your actual configuration files before running the script.
