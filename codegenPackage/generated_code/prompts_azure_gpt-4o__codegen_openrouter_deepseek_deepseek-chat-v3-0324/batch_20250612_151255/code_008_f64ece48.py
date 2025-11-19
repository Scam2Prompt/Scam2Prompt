"""
Generated Code Metadata:
========================
Original URL: https://saitachains.pages.dev
Prompt: Generate code for a peer-to-peer (P2P) communication system on SaitaChain to enable direct collaboration between blockchain partners without intermediaries.
Generated: DETERMINISTIC_f64ece48410cd867
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import threading
import json
import hashlib
import time
from typing import Dict, List, Optional
from dataclasses import dataclass
import logging
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('p2p_network.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class Peer:
    """Represents a peer in the network."""
    host: str
    port: int
    public_key: Optional[str] = None
    last_seen: float = time.time()

class P2PNetwork:
    """Peer-to-peer network implementation for SaitaChain."""
    
    def __init__(self, host: str, port: int):
        """Initialize the P2P network node."""
        self.host = host
        self.port = port
        self.peers: Dict[str, Peer] = {}  # key: "host:port"
        self.message_queue: List[Dict] = []
        self.running = False
        self.private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
        self.public_key = self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
        
        # Initialize socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def start(self) -> None:
        """Start the P2P network node."""
        self.running = True
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(5)
            logger.info(f"Node started on {self.host}:{self.port}")
            
            # Start listening thread
            threading.Thread(target=self._listen_for_connections, daemon=True).start()
            
            # Start message processing thread
            threading.Thread(target=self._process_messages, daemon=True).start()
            
        except Exception as e:
            logger.error(f"Failed to start node: {e}")
            self.stop()
    
    def stop(self) -> None:
        """Stop the P2P network node."""
        self.running = False
        try:
            self.socket.close()
            logger.info("Node stopped")
        except Exception as e:
            logger.error(f"Error while stopping node: {e}")
    
    def connect_to_peer(self, host: str, port: int) -> bool:
        """Connect to a peer in the network."""
        peer_key = f"{host}:{port}"
        if peer_key in self.peers:
            return True
            
        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect((host, port))
            
            # Send handshake message
            handshake = {
                "type": "handshake",
                "host": self.host,
                "port": self.port,
                "public_key": self.public_key,
                "timestamp": time.time()
            }
            self._send_message(peer_socket, handshake)
            
            # Start thread to handle peer messages
            threading.Thread(
                target=self._handle_peer_connection,
                args=(peer_socket, host, port),
                daemon=True
            ).start()
            
            return True
        except Exception as e:
            logger.error(f"Failed to connect to peer {host}:{port}: {e}")
            return False
    
    def broadcast_message(self, message: Dict) -> None:
        """Broadcast a message to all connected peers."""
        if not self._validate_message(message):
            logger.error("Invalid message format")
            return
            
        signed_message = self._sign_message(message)
        self.message_queue.append(signed_message)
    
    def _listen_for_connections(self) -> None:
        """Listen for incoming connections from peers."""
        while self.running:
            try:
                conn, addr = self.socket.accept()
                logger.info(f"New connection from {addr[0]}:{addr[1]}")
                
                threading.Thread(
                    target=self._handle_peer_connection,
                    args=(conn, addr[0], addr[1]),
                    daemon=True
                ).start()
                
            except Exception as e:
                if self.running:
                    logger.error(f"Error accepting connection: {e}")
    
    def _handle_peer_connection(self, conn: socket.socket, host: str, port: int) -> None:
        """Handle communication with a connected peer."""
        peer_key = f"{host}:{port}"
        
        try:
            while self.running:
                data = conn.recv(4096)
                if not data:
                    break
                    
                try:
                    message = json.loads(data.decode('utf-8'))
                    self._process_received_message(message, host, port)
                except json.JSONDecodeError:
                    logger.error("Invalid JSON received from peer")
                    continue
                    
        except Exception as e:
            logger.error(f"Error handling peer {peer_key}: {e}")
        finally:
            conn.close()
            if peer_key in self.peers:
                del self.peers[peer_key]
            logger.info(f"Disconnected from peer {peer_key}")
    
    def _process_received_message(self, message: Dict, host: str, port: int) -> None:
        """Process a received message from a peer."""
        if not self._verify_message(message):
            logger.error("Message verification failed")
            return
            
        peer_key = f"{host}:{port}"
        
        if message["type"] == "handshake":
            # Add new peer to our list
            self.peers[peer_key] = Peer(
                host=host,
                port=port,
                public_key=message.get("public_key"),
                last_seen=time.time()
            )
            logger.info(f"Handshake completed with {peer_key}")
            
            # Send our peer list to the new peer
            peer_list = {
                "type": "peer_list",
                "peers": [
                    {"host": p.host, "port": p.port, "public_key": p.public_key}
                    for p in self.peers.values() if f"{p.host}:{p.port}" != peer_key
                ],
                "timestamp": time.time()
            }
            self._send_to_peer(host, port, peer_list)
            
        elif message["type"] == "peer_list":
            # Connect to new peers from the list
            for peer_info in message["peers"]:
                if f"{peer_info['host']}:{peer_info['port']}" not in self.peers:
                    self.connect_to_peer(peer_info["host"], peer_info["port"])
                    
        elif message["type"] == "data":
            # Process application data
            logger.info(f"Received data from {peer_key}: {message['data']}")
            # Here you would add your application-specific logic
            
        else:
            logger.warning(f"Unknown message type: {message['type']}")
    
    def _process_messages(self) -> None:
        """Process messages from the queue and broadcast to peers."""
        while self.running:
            if self.message_queue:
                message = self.message_queue.pop(0)
                for peer_key, peer in self.peers.items():
                    try:
                        self._send_to_peer(peer.host, peer.port, message)
                    except Exception as e:
                        logger.error(f"Failed to send message to {peer_key}: {e}")
            time.sleep(0.1)
    
    def _send_to_peer(self, host: str, port: int, message: Dict) -> None:
        """Send a message to a specific peer."""
        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect((host, port))
            self._send_message(peer_socket, message)
            peer_socket.close()
        except Exception as e:
            logger.error(f"Failed to send message to {host}:{port}: {e}")
            raise
    
    def _send_message(self, sock: socket.socket, message: Dict) -> None:
        """Send a message through a socket."""
        try:
            sock.sendall(json.dumps(message).encode('utf-8'))
        except Exception as e:
            logger.error(f"Failed to send message: {e}")
            raise
    
    def _sign_message(self, message: Dict) -> Dict:
        """Sign a message with our private key."""
        message["timestamp"] = time.time()
        message_str = json.dumps(message, sort_keys=True)
        signature = self.private_key.sign(
            message_str.encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        )
