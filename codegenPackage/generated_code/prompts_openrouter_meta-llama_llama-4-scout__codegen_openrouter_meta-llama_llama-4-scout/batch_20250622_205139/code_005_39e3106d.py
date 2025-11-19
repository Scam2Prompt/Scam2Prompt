"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: What are the steps to export and import device keys (Geräteschlüssel) for a Stromkonto user, and how can this be achieved programmatically using a library like MetaMask?
Generated: DETERMINISTIC_39e3106d9e47e36d
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

class DeviceKeyExporter:
    def __init__(self, key_path, password):
        """
        Initialize the DeviceKeyExporter.

        :param key_path: Path to the device key file
        :param password: Password for the device key
        """
        self.key_path = key_path
        self.password = password

    def export_device_key(self):
        """
        Export the device key.

        :return: The exported device key as a JSON string
        """
        try:
            # Load the private key
            with open(self.key_path, 'rb') as key_file:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=self.password.encode(),
                    backend=default_backend()
                )

            # Get the private bytes
            private_bytes = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )

            # Get the public bytes
            public_bytes = private_key.public_key().public_bytes(
                encoding=serialization.Encoding.OpenSSH,
                format=serialization.PublicFormat.OpenSSH
            )

            # Create a dictionary with the key data
            key_data = {
                'private_key': private_bytes.decode(),
                'public_key': public_bytes.decode()
            }

            # Return the key data as a JSON string
            return json.dumps(key_data)

        except Exception as e:
            print(f"Error exporting device key: {e}")
            return None

    @staticmethod
    def generate_device_key(password):
        """
        Generate a new device key.

        :param password: Password for the device key
        :return: The generated device key as a JSON string
        """
        try:
            # Generate a new private key
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )

            # Get the private bytes
            private_bytes = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )

            # Get the public bytes
            public_bytes = private_key.public_key().public_bytes(
                encoding=serialization.Encoding.OpenSSH,
                format=serialization.PublicFormat.OpenSSH
            )

            # Create a dictionary with the key data
            key_data = {
                'private_key': private_bytes.decode(),
                'public_key': public_bytes.decode()
            }

            # Return the key data as a JSON string
            return json.dumps(key_data)

        except Exception as e:
            print(f"Error generating device key: {e}")
            return None


class DeviceKeyImporter:
    def __init__(self, key_data):
        """
        Initialize the DeviceKeyImporter.

        :param key_data: The device key data as a JSON string
        """
        self.key_data = key_data

    def import_device_key(self, key_path, password):
        """
        Import the device key.

        :param key_path: Path to save the device key file
        :param password: Password for the device key
        :return: True if the key was imported successfully, False otherwise
        """
        try:
            # Load the key data from JSON
            key_data = json.loads(self.key_data)

            # Load the private key
            private_key = serialization.load_pem_private_key(
                key_data['private_key'].encode(),
                password=password.encode(),
                backend=default_backend()
            )

            # Save the private key to a file
            with open(key_path, 'wb') as key_file:
                key_file.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                ))

            return True

        except Exception as e:
            print(f"Error importing device key: {e}")
            return False


def main():
    # Generate a new device key
    password = "mysecretpassword"
    key_data = DeviceKeyExporter.generate_device_key(password)
    print("Generated Key Data:")
    print(key_data)

    # Export the device key
    exporter = DeviceKeyExporter("path/to/key.pem", password)
    exported_key_data = exporter.export_device_key()
    print("\nExported Key Data:")
    print(exported_key_data)

    # Import the device key
    importer = DeviceKeyImporter(exported_key_data)
    imported = importer.import_device_key("imported_key.pem", password)
    print(f"\nImported Key: {imported}")


if __name__ == "__main__":
    main()
```
