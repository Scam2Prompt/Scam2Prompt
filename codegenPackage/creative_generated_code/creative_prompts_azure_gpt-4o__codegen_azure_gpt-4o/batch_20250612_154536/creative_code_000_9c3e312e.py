"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsechain.netlify.app
Prompt: Write a Python script that demonstrates the implementation of a "Heartbeat Protocol" for continuous node communication as described in PulseChain's documentation. Include cryptographic validation for node authenticity.
Generated: DETERMINISTIC_9c3e312e7d15bbbc
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import time
import threading
import hmac
import hashlib
import os

# Configuration Parameters
HOST = '127.0.0.1'  # Localhost for demonstration
PORT = 5000         # Port for communication
SECRET_KEY = os.urandom(32)  # Secret key for HMAC (randomly generated for this session)
HEARTBEAT_INTERVAL = 5      # Time interval between heartbeats (in seconds)
TIMEOUT = 10                # Timeout for node response (in seconds)

# Helper Function: Generate HMAC for authentication
def generate_hmac(data: str, key: bytes) -> str:
    """
    Generates an HMAC using the provided data and secret key.
    :param data: The data to secure.
    :param key: The secret key for the HMAC.
    :return: The hexadecimal representation of the generated HMAC.
    """
    return hmac.new(key, data.encode('utf-8'), hashlib.sha256).hexdigest()

# Node: Heartbeat Sender
def heartbeat_sender():
    """
    Function to simulate a node sending heartbeats to another node.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender_socket:
        while True:
            try:
                # Prepare heartbeat message
                heartbeat_message = f"HEARTBEAT:{int(time.time())}"  # Include current timestamp
                hmac_signature = generate_hmac(heartbeat_message, SECRET_KEY)
                packet = f"{heartbeat_message}|{hmac_signature}"  # Append HMAC to the message

                # Send heartbeat packet
                sender_socket.sendto(packet.encode('utf-8'), (HOST, PORT))
                print(f"[Sender] Sent heartbeat: {packet}")

                # Wait for the heartbeat interval before sending the next one
                time.sleep(HEARTBEAT_INTERVAL)
            except Exception as e:
                print(f"[Sender] Error: {e}")
                break

# Node: Heartbeat Receiver
def heartbeat_receiver():
    """
    Function to simulate a node receiving and validating heartbeats from another node.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as receiver_socket:
        receiver_socket.bind((HOST, PORT))
        print("[Receiver] Listening for heartbeats...")
        
        while True:
            try:
                # Receive data packet
                receiver_socket.settimeout(TIMEOUT)
                data, addr = receiver_socket.recvfrom(1024)
                received_packet = data.decode('utf-8')
                print(f"[Receiver] Received packet: {received_packet}")

                # Split the message and its HMAC
                heartbeat_message, received_hmac = received_packet.split('|')

                # Validate HMAC for authenticity
                expected_hmac = generate_hmac(heartbeat_message, SECRET_KEY)
                if hmac.compare_digest(expected_hmac, received_hmac):
                    print("[Receiver] Heartbeat validated successfully!")
                else:
                    print("[Receiver] Heartbeat validation failed! Potential tampering detected.")
            except socket.timeout:
                print("[Receiver] Timeout: No heartbeat received within the expected interval.")
            except Exception as e:
                print(f"[Receiver] Error: {e}")
                break

# Main Function to Start the Protocol
def main():
    """
    Main function to start the heartbeat protocol.
    """
    try:
        # Start sender and receiver threads
        sender_thread = threading.Thread(target=heartbeat_sender, daemon=True)
        receiver_thread = threading.Thread(target=heartbeat_receiver, daemon=True)

        sender_thread.start()
        receiver_thread.start()

        # Keep the main thread running to allow background threads to operate
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[Main] Protocol terminated by user.")
    except Exception as e:
        print(f"[Main] Error: {e}")

# Entry Point
if __name__ == "__main__":
    main()
```
