"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Generate a Python script to implement a multiplayer game similar to SCATTER HITAM that allows players to collaborate or compete using a local network.
Generated: DETERMINISTIC_a6828b41b755b827
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import threading
import json

# Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port for the server
BUFFER_SIZE = 1024  # Size of data chunks
ENCODING = 'utf-8'  # Encoding type

# Game state management
game_state = {
    "players": {},  # Stores player information
    "scores": {}    # Stores player scores
}
lock = threading.Lock()  # Lock for synchronizing access to game_state

def handle_client(client_socket, address):
    """
    Handles communication with a connected client.
    """
    try:
        print(f"New connection from {address}")
        while True:
            # Receive data from client
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            
            # Decode and process message
            message = data.decode(ENCODING)
            print(f"Received from {address}: {message}")
            
            # Parse JSON message for player actions
            try:
                action = json.loads(message)
            except json.JSONDecodeError:
                client_socket.sendall("Invalid JSON format.".encode(ENCODING))
                continue

            with lock:
                # Handle 'join' action
                if action['type'] == 'join':
                    player_id = action['player_id']
                    if player_id not in game_state['players']:
                        game_state['players'][player_id] = {"address": address}
                        game_state['scores'][player_id] = 0
                        client_socket.sendall(f"Welcome, {player_id}!".encode(ENCODING))
                    else:
                        client_socket.sendall("Player already exists.".encode(ENCODING))
                
                # Handle 'score' action
                elif action['type'] == 'score':
                    player_id = action['player_id']
                    score = action.get('score', 0)
                    if player_id in game_state['scores']:
                        game_state['scores'][player_id] += score
                        client_socket.sendall(f"Score updated. Total: {game_state['scores'][player_id]}".encode(ENCODING))
                    else:
                        client_socket.sendall("Player not found.".encode(ENCODING))
                
                # Handle 'state' action
                elif action['type'] == 'state':
                    state_json = json.dumps(game_state)
                    client_socket.sendall(state_json.encode(ENCODING))
                
                else:
                    client_socket.sendall("Unknown action.".encode(ENCODING))
    
    except Exception as e:
        print(f"Error with client {address}: {e}")
    finally:
        print(f"Closing connection with {address}")
        client_socket.close()

def start_server():
    """
    Starts the game server to accept connections and handle players.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # Listen for up to 5 connections
    print(f"Server started on {HOST}:{PORT}")
    
    try:
        while True:
            # Accept new client connection
            client_socket, address = server_socket.accept()
            
            # Start a new thread for the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Shutting down the server.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
```
