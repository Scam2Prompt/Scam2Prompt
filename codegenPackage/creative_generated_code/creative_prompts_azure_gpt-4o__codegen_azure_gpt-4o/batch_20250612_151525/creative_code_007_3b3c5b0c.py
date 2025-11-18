"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Write code for a local multiplayer game that supports device connectivity and interaction, inspired by SCATTER HITAM's multiplayer features.
Generated: DETERMINISTIC_3b3c5b0cbc5e7f0d
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example of clean, production-ready Python code for a local multiplayer game using sockets for device connectivity and interaction. This code sets up a basic server-client architecture for local multiplayer:

```python
import socket
import threading
import json

# Constants
HOST = '127.0.0.1'  # Localhost (for local multiplayer)
PORT = 12345        # Arbitrary port number
BUFFER_SIZE = 1024  # Size of the data buffer
ENCODING = 'utf-8'  # Encoding for data communication

# Game state shared across clients
game_state = {
    "players": {},  # Each player will be tracked by their ID
}

# Thread lock to manage shared game state
game_state_lock = threading.Lock()


def handle_client(client_socket, address):
    """
    Function to handle communication with a connected client.

    :param client_socket: The socket connection for the client.
    :param address: The address of the client.
    """
    print(f"[INFO] New connection from {address}")

    try:
        # Receive initial handshake with player information
        data = client_socket.recv(BUFFER_SIZE).decode(ENCODING)
        player_data = json.loads(data)  # Expecting JSON data
        player_id = player_data.get("id")
        
        if not player_id:
            client_socket.send("Error: Missing player ID".encode(ENCODING))
            client_socket.close()
            return

        # Add player to game state
        with game_state_lock:
            game_state["players"][player_id] = {"address": address, "score": 0}

        # Notify the client of successful connection
        client_socket.send("Connected successfully!".encode(ENCODING))

        # Listen for game updates from the client
        while True:
            data = client_socket.recv(BUFFER_SIZE).decode(ENCODING)
            if not data:
                break  # Disconnect if no data is received
            
            # Process client's game action
            action = json.loads(data)
            if action.get("type") == "update_score":
                with game_state_lock:
                    game_state["players"][player_id]["score"] += action.get("score", 0)

                # Broadcast game state to all clients
                broadcast_game_state()
            elif action.get("type") == "disconnect":
                break  # Handle player disconnect

    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON data from {address}")
    except Exception as e:
        print(f"[ERROR] An error occurred with client {address}: {e}")
    finally:
        # Clean up on client disconnect
        with game_state_lock:
            if player_id in game_state["players"]:
                del game_state["players"][player_id]
        
        client_socket.close()
        print(f"[INFO] Client {address} disconnected")


def broadcast_game_state():
    """
    Broadcast the current game state to all connected clients.
    """
    with game_state_lock:
        state_data = json.dumps(game_state).encode(ENCODING)
        for player_id, player_info in game_state["players"].items():
            try:
                client_socket = player_info["socket"]
                client_socket.send(state_data)
            except Exception as e:
                print(f"[WARNING] Failed to send game state to {player_id}: {e}")


def start_server():
    """
    Starts the multiplayer server and listens for incoming connections.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # Allow up to 5 simultaneous connections
    print(f"[INFO] Server started at {HOST}:{PORT}")

    while True:
        try:
            client_socket, address = server_socket.accept()
            # Start a new thread to handle the client
            threading.Thread(target=handle_client, args=(client_socket, address)).start()
        except Exception as e:
            print(f"[ERROR] An error occurred while accepting a connection: {e}")


if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("[INFO] Server shutting down...")
```

### Notes:
- The server listens for incoming connections and manages clients using threads.
- The game state is shared across clients and updated using a thread-safe lock (`game_state_lock`).
- Each client sends updates to the server, which processes the data and broadcasts the updated game state to all clients.

This code is modular, adheres to best practices, and is suitable for small-scale local multiplayer games.
