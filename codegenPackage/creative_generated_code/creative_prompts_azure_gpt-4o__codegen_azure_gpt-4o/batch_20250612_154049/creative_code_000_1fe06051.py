"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deeper-net.works
Prompt: Write Python code to integrate enterprise-grade encryption for network security, referencing the features of Deeper Network's solutions.
Generated: DETERMINISTIC_1fe0605199249a6a
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

class SecureNetworkConnection:
    """
    A class that integrates enterprise-grade encryption for network security.
    This includes TLS for transport encryption and AES for additional data encryption.
    """
    def __init__(self, server_address, port, aes_key, aes_iv):
        """
        Initialize the secure connection parameters.

        :param server_address: The address of the server to connect to.
        :param port: The port on which the server is listening.
        :param aes_key: The AES encryption key (16, 24, or 32 bytes).
        :param aes_iv: The AES initialization vector (16 bytes).
        """
        self.server_address = server_address
        self.port = port
        self.aes_key = aes_key
        self.aes_iv = aes_iv
        self.socket = None

    def create_tls_connection(self):
        """
        Establish a TLS-secured connection using SSL.
        """
        try:
            # Create a socket and wrap it with SSL for secure communication
            context = ssl.create_default_context()
            self.socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=self.server_address)
            self.socket.connect((self.server_address, self.port))
            print("Secure TLS connection established.")
        except Exception as e:
            print(f"Error establishing TLS connection: {e}")
            raise

    def encrypt_data(self, plaintext):
        """
        Encrypt data using AES encryption.

        :param plaintext: The plain text data to encrypt (as bytes).
        :return: Encrypted data (as bytes).
        """
        try:
            # Initialize AES cipher in CBC mode
            cipher = Cipher(algorithms.AES(self.aes_key), modes.CBC(self.aes_iv), backend=default_backend())
            encryptor = cipher.encryptor()

            # Add PKCS7 padding to the plaintext before encryption
            padder = padding.PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(plaintext) + padder.finalize()

            # Encrypt the padded data
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
            return encrypted_data
        except Exception as e:
            print(f"Error encrypting data: {e}")
            raise

    def decrypt_data(self, ciphertext):
        """
        Decrypt data using AES encryption.

        :param ciphertext: The encrypted data to decrypt (as bytes).
        :return: Decrypted data (as bytes).
        """
        try:
            # Initialize AES cipher in CBC mode
            cipher = Cipher(algorithms.AES(self.aes_key), modes.CBC(self.aes_iv), backend=default_backend())
            decryptor = cipher.decryptor()

            # Decrypt the ciphertext
            decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

            # Remove PKCS7 padding from the decrypted data
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
            return unpadded_data
        except Exception as e:
            print(f"Error decrypting data: {e}")
            raise

    def send_encrypted_data(self, plaintext):
        """
        Encrypt and send data over the secure TLS connection.

        :param plaintext: The plain text data to send (as bytes).
        """
        try:
            if not self.socket:
                raise ConnectionError("No active TLS connection.")

            # Encrypt data using AES
            encrypted_data = self.encrypt_data(plaintext)

            # Send encrypted data over the secure connection
            self.socket.sendall(encrypted_data)
            print("Encrypted data sent successfully.")
        except Exception as e:
            print(f"Error sending encrypted data: {e}")
            raise

    def receive_encrypted_data(self):
        """
        Receive and decrypt data over the secure TLS connection.

        :return: Decrypted plain text data (as bytes).
        """
        try:
            if not self.socket:
                raise ConnectionError("No active TLS connection.")

            # Receive encrypted data
            encrypted_data = self.socket.recv(1024)

            # Decrypt received data using AES
            decrypted_data = self.decrypt_data(encrypted_data)
            print("Encrypted data received and decrypted successfully.")
            return decrypted_data
        except Exception as e:
            print(f"Error receiving encrypted data: {e}")
            raise

    def close_connection(self):
        """
        Close the TLS connection.
        """
        try:
            if self.socket:
                self.socket.close()
                print("Secure connection closed.")
        except Exception as e:
            print(f"Error closing connection: {e}")
            raise


# Example usage:
if __name__ == "__main__":
    # Define server details and AES encryption parameters
    SERVER_ADDRESS = "example.com"
    PORT = 443
    AES_KEY = b"thisisaverysecurekey1234"  # 32-byte key for AES-256
    AES_IV = b"thisisaninitialvectr"      # 16-byte IV

    # Initialize the secure connection
    secure_conn = SecureNetworkConnection(SERVER_ADDRESS, PORT, AES_KEY, AES_IV)

    # Establish secure TLS connection
    secure_conn.create_tls_connection()

    # Encrypt and send data
    plaintext_data = b"Hello, this is a secure message."
    secure_conn.send_encrypted_data(plaintext_data)

    # Receive and decrypt data
    decrypted_data = secure_conn.receive_encrypted_data()
    print("Decrypted Data:", decrypted_data)

    # Close the secure connection
    secure_conn.close_connection()
```
