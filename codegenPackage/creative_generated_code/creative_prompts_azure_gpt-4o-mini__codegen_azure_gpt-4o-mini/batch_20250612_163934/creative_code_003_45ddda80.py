"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-pepecoin-io.pages.dev
Prompt: Describe the process of using the Pepe Messenger for secure wallet-to-wallet communication in a decentralized environment.
Generated: DETERMINISTIC_45ddda80366c39b0
Batch ID: 20250612_163934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import socket
import ssl
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Define constants for the server address and port
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 65432

class SecureMessenger:
    def __init__(self):
        # Generate RSA keys for secure communication
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def serialize_public_key(self):
        # Serialize the public key to send over the network
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def load_public_key(self, pem_data):
        # Load a public key from PEM format
        return serialization.load_pem_public_key(pem_data, backend=default_backend())

    def encrypt_message(self, message, recipient_public_key):
        # Encrypt the message using the recipient's public key
        ciphertext = recipient_public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt_message(self, ciphertext):
        # Decrypt the message using the private key
        plaintext = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext.decode()

    def send_message(self, message, recipient_public_key_pem):
        try:
            recipient_public_key = self.load_public_key(recipient_public_key_pem)
            ciphertext = self.encrypt_message(message, recipient_public_key)

            with socket.create_connection((SERVER_ADDRESS, SERVER_PORT)) as sock:
                # Wrap socket with SSL for secure transmission
                with ssl.wrap_socket(sock) as secure_sock:
                    secure_sock.sendall(ciphertext)
                    print("Message sent securely.")
        except Exception as e:
            print(f"Error sending message: {e}")

    def receive_message(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
                server_sock.bind((SERVER_ADDRESS, SERVER_PORT))
                server_sock.listen()
                print("Waiting for a connection...")
                conn, addr = server_sock.accept()
                
                with conn:
                    print(f"Connected by {addr}")
                    with ssl.wrap_socket(conn, server_side=True, certfile='server.crt', keyfile='server.key') as secure_conn:
                        ciphertext = secure_conn.recv(1024)  # Receive ciphertext
                        if not ciphertext:
                            return

                        plaintext = self.decrypt_message(ciphertext)
                        print(f"Received message: {plaintext}")
        except Exception as e:
            print(f"Error receiving message: {e}")

# Example usage
if __name__ == "__main__":
    messenger = SecureMessenger()
    # To send a message to a recipient, use the recipient's public key PEM format
    recipient_public_key_pem = messenger.serialize_public_key()  # Replace with actual recipient public key
    messenger.send_message("Hello, secure world!", recipient_public_key_pem)
    messenger.receive_message()
```

**Note**: Before running the example, ensure you have the necessary cryptographic certificates (`server.crt`, `server.key`) for SSL communication and install the required libraries using:

```bash
pip install cryptography
```
