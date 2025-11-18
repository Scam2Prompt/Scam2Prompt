"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixers.money
Prompt: Create a Python program that generates PGP keys for secure communication with mixers.money, using the example key format provided on the website.
Generated: DETERMINISTIC_8c7e4d463f156c4c
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import gnupg
import os

class PGPKeyGenerator:
    """
    A class to generate PGP keys for secure communication.
    """

    def __init__(self, gpg_home=None):
        """
        Initializes the PGPKeyGenerator with a specified GPG home directory.

        :param gpg_home: Optional; Directory where GPG keys will be stored.
        """
        self.gpg = gnupg.GPG(gnupghome=gpg_home or os.path.join(os.getcwd(), 'gpg_keys'))
        self.key = None

    def generate_key(self, name, email, passphrase):
        """
        Generates a PGP key pair.

        :param name: The name of the key owner.
        :param email: The email of the key owner.
        :param passphrase: Passphrase for the private key.
        :return: The fingerprint of the generated key or an error message.
        """
        input_data = f"""
        Key-Type: default
        Key-Length: 2048
        Name-Real: {name}
        Name-Email: {email}
        Passphrase: {passphrase}
        %no-protection
        """
        
        try:
            # Generate the key
            key_input = self.gpg.gen_key_input(key_type='RSA', key_length=2048, name_real=name, name_email=email, passphrase=passphrase)
            self.key = self.gpg.gen_key(key_input)
            return self.key.fingerprint
        except Exception as e:
            return f"Error generating key: {str(e)}"

    def export_key(self, fingerprint):
        """
        Exports the public key associated with the given fingerprint.

        :param fingerprint: The fingerprint of the key to export.
        :return: The public key as a string or an error message.
        """
        try:
            public_key = self.gpg.export_keys(fingerprint)
            return public_key
        except Exception as e:
            return f"Error exporting key: {str(e)}"

    def export_private_key(self, fingerprint, passphrase):
        """
        Exports the private key associated with the given fingerprint.

        :param fingerprint: The fingerprint of the key to export.
        :param passphrase: The passphrase to access the private key.
        :return: The private key as a string or an error message.
        """
        try:
            private_key = self.gpg.export_keys(fingerprint, true=True, passphrase=passphrase)
            return private_key
        except Exception as e:
            return f"Error exporting private key: {str(e)}"

if __name__ == "__main__":
    # Example usage of the PGPKeyGenerator
    key_gen = PGPKeyGenerator()

    # User input for generating key
    name = "John Doe"
    email = "john.doe@example.com"
    passphrase = "securepassphrase"

    fingerprint = key_gen.generate_key(name, email, passphrase)
    print(f"Generated key with fingerprint: {fingerprint}")

    if fingerprint and "Error" not in fingerprint:
        public_key = key_gen.export_key(fingerprint)
        print(f"Public Key:\n{public_key}")

        private_key = key_gen.export_private_key(fingerprint, passphrase)
        print(f"Private Key:\n{private_key}")
```

Make sure to install the `python-gnupg` package before running the code by executing:

```bash
pip install python-gnupg
```

Also, ensure that GnuPG is installed on your system and accessible in your PATH.
