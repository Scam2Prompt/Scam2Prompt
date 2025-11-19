"""
Generated Code Metadata:
========================
Original URL: https://optimisms.xyz
Prompt: What are the steps to register a domain using both ICANN and on-chain registrars with 3DNS?
Generated: DETERMINISTIC_978e924160d04c14
Batch ID: 20250612_135152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# 3DNS Registrar Interface

import hashlib
import logging
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RegistrarInterface:
    def __init__(self, registrar_type: str):
        """
        Initialize the registrar interface.

        Args:
        - registrar_type (str): Type of registrar (ICANN or ONCHAIN)
        """
        self.registrar_type = registrar_type

    def register_domain(self, domain_name: str, registrant_info: Dict) -> str:
        """
        Register a domain using the specified registrar.

        Args:
        - domain_name (str): Name of the domain to register
        - registrant_info (Dict): Registrant information

        Returns:
        - registration_id (str): Unique ID for the registration
        """
        if self.registrar_type == "ICANN":
            return self.icann_register(domain_name, registrant_info)
        elif self.registrar_type == "ONCHAIN":
            return self.onchain_register(domain_name, registrant_info)
        else:
            raise ValueError("Invalid registrar type")

    def icann_register(self, domain_name: str, registrant_info: Dict) -> str:
        """
        Register a domain using an ICANN registrar.

        Args:
        - domain_name (str): Name of the domain to register
        - registrant_info (Dict): Registrant information

        Returns:
        - registration_id (str): Unique ID for the registration
        """
        try:
            # Simulate ICANN registration process
            registration_id = hashlib.sha256((domain_name + str(registrant_info)).encode()).hexdigest()
            logger.info(f"Registered domain {domain_name} with ICANN registrar, registration ID: {registration_id}")
            return registration_id
        except Exception as e:
            logger.error(f"Error registering domain with ICANN registrar: {str(e)}")
            raise

    def onchain_register(self, domain_name: str, registrant_info: Dict) -> str:
        """
        Register a domain using an on-chain registrar.

        Args:
        - domain_name (str): Name of the domain to register
        - registrant_info (Dict): Registrant information

        Returns:
        - registration_id (str): Unique ID for the registration
        """
        try:
            # Simulate on-chain registration process
            registration_id = hashlib.sha256((domain_name + str(registrant_info)).encode()).hexdigest()
            logger.info(f"Registered domain {domain_name} with on-chain registrar, registration ID: {registration_id}")
            return registration_id
        except Exception as e:
            logger.error(f"Error registering domain with on-chain registrar: {str(e)}")
            raise


class ThreeDNS:
    def __init__(self):
        self.registrars = {}

    def add_registrar(self, registrar_type: str, registrar_interface: RegistrarInterface):
        """
        Add a registrar to the 3DNS system.

        Args:
        - registrar_type (str): Type of registrar (ICANN or ONCHAIN)
        - registrar_interface (RegistrarInterface): Registrar interface instance
        """
        self.registrars[registrar_type] = registrar_interface

    def register_domain(self, domain_name: str, registrant_info: Dict, registrar_type: str) -> str:
        """
        Register a domain using the specified registrar.

        Args:
        - domain_name (str): Name of the domain to register
        - registrant_info (Dict): Registrant information
        - registrar_type (str): Type of registrar (ICANN or ONCHAIN)

        Returns:
        - registration_id (str): Unique ID for the registration
        """
        if registrar_type in self.registrars:
            return self.registrars[registrar_type].register_domain(domain_name, registrant_info)
        else:
            raise ValueError("Registrar not found")


# Example usage
if __name__ == "__main__":
    three_dns = ThreeDNS()

    icann_registrar = RegistrarInterface("ICANN")
    onchain_registrar = RegistrarInterface("ONCHAIN")

    three_dns.add_registrar("ICANN", icann_registrar)
    three_dns.add_registrar("ONCHAIN", onchain_registrar)

    domain_name = "example.com"
    registrant_info = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+1 123 456 7890"
    }

    icann_registration_id = three_dns.register_domain(domain_name, registrant_info, "ICANN")
    onchain_registration_id = three_dns.register_domain(domain_name, registrant_info, "ONCHAIN")

    logger.info(f"ICANN registration ID: {icann_registration_id}")
    logger.info(f"On-chain registration ID: {onchain_registration_id}")
```
