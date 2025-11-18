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
import cryptonext  # Import CryptoNext's Quantum Safe Software Suite
import logging
import os

# Configure logging for error handling and monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("migration.log"),
        logging.StreamHandler()
    ]
)

class PKIQuantumMigration:
    """
    A class to handle multi-layer migration of PKI infrastructure to post-quantum security
    using CryptoNext's Quantum Safe Software Suite.
    """
    
    def __init__(self, current_pki_path: str, quantum_safe_pki_path: str):
        """
        Initialize the migration class with paths to the current and new PKI infrastructures.

        Args:
            current_pki_path (str): Path to the current PKI infrastructure.
            quantum_safe_pki_path (str): Path to the quantum-safe PKI infrastructure.
        """
        self.current_pki_path = current_pki_path
        self.quantum_safe_pki_path = quantum_safe_pki_path

        # Initialize quantum-safe suite
        self.qsafe_suite = cryptonext.QuantumSafe.init()

    def validate_paths(self):
        """
        Validate the paths to the PKI infrastructure directories.

        Raises:
            FileNotFoundError: If the paths are invalid or inaccessible.
        """
        if not os.path.exists(self.current_pki_path):
            raise FileNotFoundError(f"Current PKI path '{self.current_pki_path}' does not exist.")
        if not os.path.exists(self.quantum_safe_pki_path):
            raise FileNotFoundError(f"Quantum-safe PKI path '{self.quantum_safe_pki_path}' does not exist.")
        logging.info("PKI paths validated successfully.")

    def backup_pki(self):
        """
        Create a backup of the current PKI infrastructure.
        """
        backup_path = f"{self.current_pki_path}_backup"
        try:
            cryptonext.utils.backup_directory(self.current_pki_path, backup_path)
            logging.info(f"Backup of current PKI completed: {backup_path}")
        except Exception as e:
            logging.error(f"Failed to backup current PKI: {e}")
            raise

    def generate_post_quantum_keys(self):
        """
        Generate post-quantum cryptographic keys.
        """
        try:
            self.qsafe_suite.generate_keys(destination=self.quantum_safe_pki_path)
            logging.info("Post-quantum keys generated successfully.")
        except Exception as e:
            logging.error(f"Failed to generate post-quantum keys: {e}")
            raise

    def reissue_certificates(self):
        """
        Reissue certificates using post-quantum keys.
        """
        try:
            self.qsafe_suite.reissue_certificates(
                current_pki=self.current_pki_path,
                new_pki=self.quantum_safe_pki_path
            )
            logging.info("Certificates reissued using post-quantum keys.")
        except Exception as e:
            logging.error(f"Failed to reissue certificates: {e}")
            raise

    def test_infrastructure(self):
        """
        Test the new PKI infrastructure for functionality and integrity.
        """
        try:
            self.qsafe_suite.test_pki(pki_path=self.quantum_safe_pki_path)
            logging.info("Quantum-safe PKI infrastructure tested successfully.")
        except Exception as e:
            logging.error(f"Failed to test quantum-safe PKI infrastructure: {e}")
            raise

    def migrate(self):
        """
        Perform the entire migration process.
        """
        try:
            # Step 1: Validate paths
            self.validate_paths()

            # Step 2: Backup current PKI
            self.backup_pki()

            # Step 3: Generate post-quantum cryptographic keys
            self.generate_post_quantum_keys()

            # Step 4: Reissue certificates
            self.reissue_certificates()

            # Step 5: Test the new infrastructure
            self.test_infrastructure()

            logging.info("PKI infrastructure migrated to post-quantum security successfully.")
        except Exception as e:
            logging.error(f"Migration failed: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Define paths for current and quantum-safe PKI infrastructures
        current_pki = "/path/to/current/pki"
        quantum_safe_pki = "/path/to/quantum-safe/pki"

        # Instantiate migration class
        migration = PKIQuantumMigration(current_pki, quantum_safe_pki)
        
        # Perform migration
        migration.migrate()
    except Exception as e:
        logging.critical(f"Migration process encountered a critical failure: {e}")
```
