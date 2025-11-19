"""
Generated Code Metadata:
========================
Original URL: https://miamigojesus.edu.pe
Prompt: Generate a Python script to implement a multiplayer game similar to SCATTER HITAM that allows players to collaborate or compete using a local network.
Generated: DETERMINISTIC_a6828b41b755b827
Batch ID: 20250612_164316
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

# Constants
HOST = '127.0.0.1'  # Localhost for testing
PORT = 12345        # Port for the server
BUFFER_SIZE = 1024  # Size of data buffer
ENCODING = 'utf-8'  # Encoding for data transmission

# Game state
game_state = {
    "players": {},  # Stores player data: {player_id: {"score": int, "name": str}}
    "game_active": True
}

# Lock for thread-safe access to game state
game_state_lock = threading.Lock()

def handle_client(client_socket, client_address):
    """
    Handles communication with a connected client.
    """
    try:
        print(f"New connection from {client_address}")
        client_socket.send("Welcome to Scatter Hitam! Enter your name:".encode(ENCODING))
        
        # Receive player name
        player_name = client_socket.recv(BUFFER_SIZE).decode(ENCODING).strip()
        if not player_name:
            client_socket.send("Invalid name. Disconnecting.".encode(ENCODING))
            client_socket.close()
            return
        
        # Register player
        with game_state_lock:
            player_id = len(game_state["players"]) + 1
            game_state["players"][player_id] = {"score": 0, "name": player_name}
        
        client_socket.send(f"Welcome, {player_name}! Your player ID is {player_id}.".encode(ENCODING))
        
        # Game loop
        while game_state["game_active"]:
            client_socket.send("Enter a command (score, state, quit):".encode(ENCODING))
            command = client_socket.recv(BUFFER_SIZE).decode(ENCODING).strip().lower()
            
            if command == "score":
                # Increment player's score
                with game_state_lock:
                    game_state["players"][player_id]["score"] += 1
                client_socket.send(f"Your score is now {game_state['players'][player_id]['score']}.".encode(ENCODING))
            
            elif command == "state":
                # Send current game state
                with game_state_lock:
                    state = json.dumps(game_state)
                client_socket.send(f"Game state: {state}".encode(ENCODING))
            
            elif command == "quit":
                # Player quits the game
                client_socket.send("Goodbye!".encode(ENCODING))
                break
            
            else:
                client_socket.send("Invalid command. Try again.".encode(ENCODING))
        
        # Remove player from game state
        with game_state_lock:
            del game_state["players"][player_id]
        
        print(f"Player {player_name} disconnected.")
        client_socket.close()
    
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
        client_socket.close()

def start_server():
    """
    Starts the game server and listens for incoming connections.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # Allow up to 5 simultaneous connections
    print(f"Server started on {HOST}:{PORT}")
    
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Shutting down server...")
        server_socket.close()
        with game_state_lock:
            game_state["game_active"] = False

if __name__ == "__main__":
    start_server()
```
