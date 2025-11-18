"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://x1blockdag.pages.dev
Prompt: Create a command-line tool for direct interaction with BlockDAG's blockchain, including mining operations and node communication protocols.
Generated: DETERMINISTIC_2bf91abdf00afaf6
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for the command-line tool:

```python
import argparse
import hashlib
import json
import time
from typing import List, Dict, Any
import socket
import threading

# BlockDAG Node class: Handles blockchain operations and node communication
class BlockDAGNode:
    def __init__(self, node_address: str):
        """
        Initialize the Node with an address and an empty BlockDAG.
        :param node_address: Address of the node (IP:PORT).
        """
        self.node_address = node_address
        self.block_dag = []
        self.peers = []

    def create_block(self, data: str) -> Dict[str, Any]:
        """
        Create a new block with the given data.
        :param data: Transaction or data payload for the block.
        :return: The newly created block.
        """
        parent_block = self.block_dag[-1] if self.block_dag else None
        parent_hash = parent_block['hash'] if parent_block else None
        block = {
            'index': len(self.block_dag),
            'timestamp': time.time(),
            'data': data,
            'parent_hash': parent_hash,
        }
        # Calculate block hash
        block['hash'] = self._compute_hash(block)
        self.block_dag.append(block)
        return block

    def _compute_hash(self, block: Dict[str, Any]) -> str:
        """
        Compute SHA-256 hash for a block.
        :param block: Block data.
        :return: SHA-256 hash string.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_peer(self, peer_address: str):
        """
        Add a peer to the node's peer list.
        :param peer_address: Address of the peer (IP:PORT).
        """
        if peer_address not in self.peers:
            self.peers.append(peer_address)

    def broadcast_block(self, block: Dict[str, Any]):
        """
        Broadcast the newly mined block to all peers.
        :param block: Block to broadcast.
        """
        for peer in self.peers:
            try:
                self._send_block_to_peer(peer, block)
            except Exception as e:
                print(f"Failed to send block to {peer}: {e}")

    def _send_block_to_peer(self, peer_address: str, block: Dict[str, Any]):
        """
        Send the block to a specific peer via TCP socket.
        :param peer_address: Address of the peer (IP:PORT).
        :param block: Block data to send.
        """
        host, port = peer_address.split(':')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, int(port)))
            s.sendall(json.dumps(block).encode())

    def start_server(self):
        """
        Start the server to listen for incoming blocks from peers.
        """
        host, port = self.node_address.split(':')
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, int(port)))
        server_socket.listen(5)
        print(f"Node running at {self.node_address}...")
        
        while True:
            client_socket, addr = server_socket.accept()
            threading.Thread(target=self._handle_client_connection, args=(client_socket, addr)).start()

    def _handle_client_connection(self, client_socket: socket.socket, addr):
        """
        Handle incoming connections from peers.
        :param client_socket: Socket object for the client connection.
        :param addr: Address of the client.
        """
        try:
            data = client_socket.recv(1024).decode()
            block = json.loads(data)
            print(f"Received block from {addr}: {block}")
            self.block_dag.append(block)
        except Exception as e:
            print(f"Error handling connection from {addr}: {e}")
        finally:
            client_socket.close()


def main():
    """
    Main function to parse command-line arguments and execute node operations.
    """
    parser = argparse.ArgumentParser(description="BlockDAG Command-Line Tool")
    parser.add_argument("--node", type=str, required=True, help="Node address (e.g., IP:PORT)")
    parser.add_argument("--mine", type=str, help="Data to mine into a new block")
    parser.add_argument("--peer", type=str, help="Add a peer (IP:PORT)")
    parser.add_argument("--start-server", action="store_true", help="Start the node server")
    args = parser.parse_args()

    node = BlockDAGNode(args.node)

    if args.peer:
        node.add_peer(args.peer)
        print(f"Added peer: {args.peer}")

    if args.mine:
        new_block = node.create_block(args.mine)
        print(f"New block mined: {new_block}")
        node.broadcast_block(new_block)

    if args.start_server:
        node.start_server()


if __name__ == "__main__":
    main()
```
