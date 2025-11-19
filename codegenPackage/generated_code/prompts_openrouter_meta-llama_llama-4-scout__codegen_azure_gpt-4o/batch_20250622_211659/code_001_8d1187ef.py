"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: What are the benefits of Common Good Parachains in the Polkadot ecosystem, and how can they be used for governance-allocated parachains?
Generated: DETERMINISTIC_8d1187ef055fce6f
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides an overview of the benefits of Common Good Parachains in the Polkadot ecosystem
and demonstrates how they can be used for governance-allocated parachains. The code is designed to
be clean, efficient, and well-documented, following best practices for Python development.
"""

# Import necessary libraries
import json

# Define a class to represent Common Good Parachains
class CommonGoodParachain:
    """
    Represents a Common Good Parachain in the Polkadot ecosystem.
    """

    def __init__(self, name, purpose, governance_allocated):
        """
        Initialize a Common Good Parachain instance.

        :param name: Name of the parachain
        :param purpose: Purpose of the parachain (e.g., identity, bridge, etc.)
        :param governance_allocated: Boolean indicating if the parachain is governance-allocated
        """
        self.name = name
        self.purpose = purpose
        self.governance_allocated = governance_allocated

    def get_details(self):
        """
        Retrieve details about the parachain.

        :return: Dictionary containing parachain details
        """
        return {
            "name": self.name,
            "purpose": self.purpose,
            "governance_allocated": self.governance_allocated
        }

    def is_governance_allocated(self):
        """
        Check if the parachain is governance-allocated.

        :return: Boolean indicating governance allocation status
        """
        return self.governance_allocated


# Define a function to list the benefits of Common Good Parachains
def list_benefits():
    """
    List the benefits of Common Good Parachains in the Polkadot ecosystem.

    :return: List of benefits
    """
    benefits = [
        "Promote ecosystem-wide functionality (e.g., identity, bridges, etc.)",
        "Serve as neutral infrastructure for all parachains",
        "Enhance interoperability and shared services",
        "Governance-allocated parachains ensure fair distribution of resources",
        "Reduce duplication of effort across parachains"
    ]
    return benefits


# Define a function to demonstrate governance allocation
def demonstrate_governance_allocation(parachains):
    """
    Demonstrate how governance-allocated parachains can be used.

    :param parachains: List of CommonGoodParachain instances
    :return: List of governance-allocated parachains
    """
    governance_allocated_parachains = [
        parachain.get_details() for parachain in parachains if parachain.is_governance_allocated()
    ]
    return governance_allocated_parachains


# Main function to execute the script
def main():
    """
    Main function to demonstrate the benefits and usage of Common Good Parachains.
    """
    try:
        # Create a list of Common Good Parachains
        parachains = [
            CommonGoodParachain("IdentityChain", "Identity management", True),
            CommonGoodParachain("BridgeChain", "Cross-chain bridges", True),
            CommonGoodParachain("StorageChain", "Decentralized storage", False)
        ]

        # List the benefits of Common Good Parachains
        print("Benefits of Common Good Parachains:")
        for benefit in list_benefits():
            print(f"- {benefit}")

        # Demonstrate governance allocation
        print("\nGovernance-Allocated Parachains:")
        allocated_parachains = demonstrate_governance_allocation(parachains)
        print(json.dumps(allocated_parachains, indent=4))

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
