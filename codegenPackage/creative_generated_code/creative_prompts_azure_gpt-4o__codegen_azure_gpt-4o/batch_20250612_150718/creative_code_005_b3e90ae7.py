"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui.direct
Prompt: Create a script to run your own node for sui.direct and customize its functionality for decentralized version control.
Generated: DETERMINISTIC_b3e90ae7490f7ad3
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import asyncio
from aiohttp import web
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

# Constants
NODE_PORT = 8080
DATA_DIR = "./node_data"
REPO_DIR = f"{DATA_DIR}/repositories"
PEER_FILE = f"{DATA_DIR}/peers.json"
KEY_FILE = f"{DATA_DIR}/node_key.json"

# Ensure necessary directories exist
os.makedirs(REPO_DIR, exist_ok=True)

# Utility function: Load peers from file
def load_peers():
    if not os.path.exists(PEER_FILE):
        return []
    with open(PEER_FILE, "r") as file:
        return json.load(file)

# Utility function: Save peers to file
def save_peers(peers):
    with open(PEER_FILE, "w") as file:
        json.dump(peers, file)

# Utility function: Create or load the node's keypair
def load_or_generate_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as file:
            key_data = json.load(file)
            private_key = Ed25519PrivateKey.from_private_bytes(bytes.fromhex(key_data["private_key"]))
            return private_key
    else:
        private_key = Ed25519PrivateKey.generate()
        private_key_bytes = private_key.private_bytes(Encoding.Raw, PublicFormat.Raw, None)
        key_data = {"private_key": private_key_bytes.hex()}
        with open(KEY_FILE, "w") as file:
            json.dump(key_data, file)
        return private_key

# Initialize node keypair
node_private_key = load_or_generate_key()
node_public_key = node_private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw).hex()

# Functionality: Decentralized version control - Push & Pull
async def handle_push(request):
    """
    Handle push requests: Receive repository data and store it locally.
    """
    try:
        data = await request.json()
        repo_name = data.get("repository_name")
        repo_content = data.get("content")
        
        if not repo_name or not repo_content:
            return web.json_response({"status": "error", "message": "Invalid data"}, status=400)
        
        repo_path = os.path.join(REPO_DIR, f"{repo_name}.json")
        with open(repo_path, "w") as repo_file:
            json.dump(repo_content, repo_file)
        
        return web.json_response({"status": "success", "message": f"Repository '{repo_name}' stored."})
    except Exception as e:
        return web.json_response({"status": "error", "message": f"Failed to process push: {str(e)}"}, status=500)

async def handle_pull(request):
    """
    Handle pull requests: Send requested repository data to the client.
    """
    try:
        repo_name = request.query.get("repository_name")
        
        if not repo_name:
            return web.json_response({"status": "error", "message": "Repository name required"}, status=400)
        
        repo_path = os.path.join(REPO_DIR, f"{repo_name}.json")
        if not os.path.exists(repo_path):
            return web.json_response({"status": "error", "message": "Repository not found"}, status=404)
        
        with open(repo_path, "r") as repo_file:
            repo_content = json.load(repo_file)
        
        return web.json_response({"status": "success", "repository_name": repo_name, "content": repo_content})
    except Exception as e:
        return web.json_response({"status": "error", "message": f"Failed to process pull: {str(e)}"}, status=500)

# Peer management handlers
async def handle_add_peer(request):
    """
    Add a new peer to the node's peer list.
    """
    try:
        data = await request.json()
        peer_address = data.get("peer_address")
        
        if not peer_address:
            return web.json_response({"status": "error", "message": "Peer address required"}, status=400)
        
        peers = load_peers()
        if peer_address not in peers:
            peers.append(peer_address)
            save_peers(peers)
        
        return web.json_response({"status": "success", "message": f"Peer '{peer_address}' added."})
    except Exception as e:
        return web.json_response({"status": "error", "message": f"Failed to add peer: {str(e)}"}, status=500)

async def handle_list_peers(request):
    """
    List all peers connected to the node.
    """
    try:
        peers = load_peers()
        return web.json_response({"status": "success", "peers": peers})
    except Exception as e:
        return web.json_response({"status": "error", "message": f"Failed to list peers: {str(e)}"}, status=500)

# Server Setup
app = web.Application()
app.router.add_post("/push", handle_push)
app.router.add_get("/pull", handle_pull)
app.router.add_post("/add_peer", handle_add_peer)
app.router.add_get("/list_peers", handle_list_peers)

# Start the node
if __name__ == "__main__":
    web.run_app(app, port=NODE_PORT)
```
