"""
Generated Code Metadata:
========================
Original URL: https://gominings.net
Prompt: Explain how GoMining ensures the legitimacy of its bitcoin mining operations and the verification process for service providers.
Generated: DETERMINISTIC_6f35eff4a58e9e2b
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GoMining:
    """
    A class to represent the GoMining operations and ensure the legitimacy of its bitcoin mining operations.
    """

    def __init__(self):
        """
        Initializes the GoMining instance with an empty list of service providers.
        """
        self.service_providers = []

    def add_service_provider(self, provider):
        """
        Adds a service provider to the GoMining operations after verification.

        Args:
            provider (dict): A dictionary containing provider details such as name, id, and verification status.

        Raises:
            ValueError: If the provider is already added or if the provider details are incomplete.
        """
        if not self._is_provider_valid(provider):
            raise ValueError("Provider details are incomplete or invalid.")

        if provider['id'] in [p['id'] for p in self.service_providers]:
            raise ValueError("Provider is already added.")

        self.service_providers.append(provider)
        print(f"Service provider {provider['name']} added successfully.")

    def _is_provider_valid(self, provider):
        """
        Validates the service provider details.

        Args:
            provider (dict): A dictionary containing provider details.

        Returns:
            bool: True if the provider is valid, False otherwise.
        """
        required_keys = ['name', 'id', 'is_verified']
        return all(key in provider for key in required_keys) and provider['is_verified']

    def verify_service_provider(self, provider_id):
        """
        Verifies a service provider by their ID.

        Args:
            provider_id (str): The ID of the service provider to verify.

        Raises:
            ValueError: If the provider ID is not found.
        """
        for provider in self.service_providers:
            if provider['id'] == provider_id:
                provider['is_verified'] = True
                print(f"Service provider {provider['name']} verified successfully.")
                return

        raise ValueError("Service provider ID not found.")

    def get_verified_providers(self):
        """
        Returns a list of verified service providers.

        Returns:
            list: A list of verified service providers.
        """
        return [provider for provider in self.service_providers if provider['is_verified']]

# Example usage
if __name__ == "__main__":
    go_mining = GoMining()

    # Adding service providers
    try:
        go_mining.add_service_provider({'name': 'Provider A', 'id': '001', 'is_verified': False})
        go_mining.add_service_provider({'name': 'Provider B', 'id': '002', 'is_verified': True})
        
        # Verifying a service provider
        go_mining.verify_service_provider('001')
        
        # Getting verified providers
        verified_providers = go_mining.get_verified_providers()
        print("Verified Service Providers:", verified_providers)

    except ValueError as e:
        print(f"Error: {e}")
```
