"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ens.gifts
Prompt: Provide an example of using ENS to resolve a domain name to an Ethereum address in a gifting use case.
Generated: DETERMINISTIC_c41042b43825dc92
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from eth_utils import is_address
from ens import ENS

# Ensure you have the `ens` library installed: pip install eth-ens

# Function to resolve an ENS domain to an Ethereum address
def resolve_ens_to_address(domain):
    """Resolve an ENS domain to an Ethereum address.

    Args:
        domain (str): The ENS domain to resolve (e.g., 'example.eth').

    Returns:
        str: The Ethereum address associated with the ENS domain.

    Raises:
        ValueError: If the domain is invalid or cannot be resolved.
    """
    # Initialize an ENS object with the default provider
    ens = ENS()

    # Validate the domain format
    if not domain.endswith('.eth'):
        raise ValueError("Invalid ENS domain. It must end with '.eth'.")

    try:
        # Resolve the domain to an Ethereum address
        address = ens.address(domain)
        
        # Validate the resolved address
        if not is_address(address):
            raise ValueError(f"Resolved address '{address}' is not a valid Ethereum address.")
        
        return address

    except Exception as e:
        raise ValueError(f"Failed to resolve {domain}: {str(e)}")


# Example usage for gifting an Ethereum address
def main():
    """Main function to demonstrate ENS resolution for a gifting use case."""
    # Define the ENS domain to resolve
    ens_domain = 'example.eth'

    try:
        # Resolve the ENS domain to an Ethereum address
        eth_address = resolve_ens_to_address(ens_domain)
        print(f"The Ethereum address for {ens_domain} is: {eth_address}")

        # Proceed with the gifting logic here
        # Example: send_gift(eth_address, amount)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
