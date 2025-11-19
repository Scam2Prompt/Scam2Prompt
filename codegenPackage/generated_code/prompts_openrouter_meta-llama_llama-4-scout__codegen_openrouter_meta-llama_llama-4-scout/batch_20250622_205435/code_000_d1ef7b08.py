"""
Generated Code Metadata:
========================
Original URL: https://initia.co
Prompt: "How does Initia's interwoven infrastructure support multichain applications?"
Generated: DETERMINISTIC_d1ef7b089123656d
Batch ID: 20250622_205435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List

class Chain:
    """Represents a blockchain in the interwoven infrastructure."""
    
    def __init__(self, name: str, chain_id: int):
        """
        Initializes a Chain object.

        Args:
        - name (str): The name of the blockchain.
        - chain_id (int): The unique identifier of the blockchain.
        """
        self.name = name
        self.chain_id = chain_id
        self.applications: List[Application] = []

    def add_application(self, application: 'Application'):
        """Adds an application to the blockchain."""
        self.applications.append(application)


class Application:
    """Represents a multichain application in the interwoven infrastructure."""
    
    def __init__(self, name: str, description: str):
        """
        Initializes an Application object.

        Args:
        - name (str): The name of the application.
        - description (str): A brief description of the application.
        """
        self.name = name
        self.description = description
        self.chains: List[Chain] = []

    def add_chain(self, chain: Chain):
        """Adds a blockchain to the application."""
        self.chains.append(chain)


class InitiaInfrastructure:
    """Represents Initia's interwoven infrastructure."""
    
    def __init__(self):
        """Initializes the InitiaInfrastructure object."""
        self.chains: Dict[int, Chain] = {}
        self.applications: Dict[str, Application] = {}

    def add_chain(self, chain: Chain):
        """Adds a blockchain to the infrastructure."""
        self.chains[chain.chain_id] = chain

    def add_application(self, application: Application):
        """Adds an application to the infrastructure."""
        self.applications[application.name] = application

    def support_multichain_application(self, application_name: str, chain_ids: List[int]):
        """
        Supports a multichain application by connecting it to multiple blockchains.

        Args:
        - application_name (str): The name of the application.
        - chain_ids (List[int]): A list of chain IDs to connect to the application.

        Raises:
        - ValueError: If the application or chain IDs are invalid.
        """
        if application_name not in self.applications:
            raise ValueError("Application not found")

        application = self.applications[application_name]

        for chain_id in chain_ids:
            if chain_id not in self.chains:
                raise ValueError("Chain ID not found")
            chain = self.chains[chain_id]
            application.add_chain(chain)
            chain.add_application(application)

    def print_infrastructure(self):
        """Prints the current state of the infrastructure."""
        print("Chains:")
        for chain_id, chain in self.chains.items():
            print(f"- {chain.name} (ID: {chain.chain_id})")

        print("\nApplications:")
        for application_name, application in self.applications.items():
            print(f"- {application.name}")
            print(f"  Description: {application.description}")
            print("  Chains:")
            for chain in application.chains:
                print(f"  - {chain.name} (ID: {chain.chain_id})")


def main():
    # Create the Initia infrastructure
    initia = InitiaInfrastructure()

    # Create blockchains
    chain1 = Chain("Chain 1", 1)
    chain2 = Chain("Chain 2", 2)
    chain3 = Chain("Chain 3", 3)

    # Add blockchains to the infrastructure
    initia.add_chain(chain1)
    initia.add_chain(chain2)
    initia.add_chain(chain3)

    # Create a multichain application
    application = Application("My App", "A multichain application")

    # Add the application to the infrastructure
    initia.add_application(application)

    # Support the multichain application
    initia.support_multichain_application("My App", [1, 2, 3])

    # Print the infrastructure
    initia.print_infrastructure()


if __name__ == "__main__":
    main()
```
