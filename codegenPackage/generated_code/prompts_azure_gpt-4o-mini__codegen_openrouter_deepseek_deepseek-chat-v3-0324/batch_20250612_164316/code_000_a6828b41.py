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
import random
import json
from enum import Enum

# Constants
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5555
MAX_PLAYERS = 4
BUFFER_SIZE = 4096

# Game state enums
class GameState(Enum):
    LOBBY = 0
    IN_GAME = 1
    GAME_OVER = 2

class Player:
    def __init__(self, conn, addr, name):
        self.conn = conn
        self.addr = addr
        self.name = name
        self.score = 0
        self.ready = False

    def send(self, data):
        try:
            self.conn.sendall(json.dumps(data).encode('utf-8'))
        except Exception as e:
            print(f"Error sending data to {self.name}: {e}")

class ScatterHitamGame:
    def __init__(self):
        self.players = []
        self.game_state = GameState.LOBBY
        self.current_turn = 0
        self.game_board = []
        self.winner = None
        self.lock = threading.Lock()

    def broadcast(self, data, exclude=None):
        exclude = exclude or []
        with self.lock:
            for player in self.players:
                if player not in exclude:
                    player.send(data)

    def handle_player(self, player):
        try:
            while True:
                data = player.conn.recv(BUFFER_SIZE)
                if not data:
                    break

                message = json.loads(data.decode('utf-8'))
                self.handle_message(player, message)

        except Exception as e:
            print(f"Player {player.name} disconnected: {e}")
        finally:
            self.remove_player(player)

    def handle_message(self, player, message):
        if message['type'] == 'ready':
            player.ready = message['ready']
            self.broadcast({
                'type': 'player_ready',
                'name': player.name,
                'ready': player.ready
            })
            self.check_all_ready()

        elif message['type'] == 'move':
            if self.game_state == GameState.IN_GAME and player == self.players[self.current_turn]:
                # Process move logic here
                self.process_move(player, message['move'])
                
        elif message['type'] == 'chat':
            self.broadcast({
                'type': 'chat',
                'name': player.name,
                'message': message['message']
            })

    def process_move(self, player, move):
        # Implement game-specific move logic here
        # Update game board, scores, etc.
        
        # Example: Simple turn-based logic
        self.broadcast({
            'type': 'move_made',
            'name': player.name,
            'move': move
        })
        
        # Switch to next player's turn
        self.current_turn = (self.current_turn + 1) % len(self.players)
        self.broadcast({
            'type': 'turn_update',
            'current_player': self.players[self.current_turn].name
        })

    def check_all_ready(self):
        if all(player.ready for player in self.players) and len(self.players) >= 2:
            self.start_game()

    def start_game(self):
        self.game_state = GameState.IN_GAME
        self.current_turn = random.randint(0, len(self.players) - 1)
        
        # Initialize game board (customize for your game)
        self.game_board = [[0 for _ in range(8)] for _ in range(8)]
        
        self.broadcast({
            'type': 'game_start',
            'board': self.game_board,
            'current_player': self.players[self.current_turn].name
        })

    def remove_player(self, player):
        with self.lock:
            if player in self.players:
                self.players.remove(player)
                self.broadcast({
                    'type': 'player_left',
                    'name': player.name,
                    'players': [p.name for p in self.players]
                })
                
                if self.game_state == GameState.IN_GAME and len(self.players) < 2:
                    self.end_game(forced=True)

    def end_game(self, forced=False):
        self.game_state = GameState.GAME_OVER
        if not forced:
            # Determine winner based on game logic
            self.winner = max(self.players, key=lambda p: p.score)
        
        self.broadcast({
            'type': 'game_over',
            'winner': self.winner.name if self.winner else None,
            'forced': forced,
            'scores': {p.name: p.score for p in self.players}
        })

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((SERVER_HOST, SERVER_PORT))
        server.listen()
        print(f"Server started on {SERVER_HOST}:{SERVER_PORT}")
        
        game = ScatterHitamGame()
        
        while True:
            conn, addr = server.accept()
            print(f"New connection from {addr}")
            
            try:
                # Get player name
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    conn.close()
                    continue
                    
                name = json.loads(data.decode('utf-8'))['name']
                
                if len(game.players) >= MAX_PLAYERS:
                    conn.sendall(json.dumps({
                        'type': 'error',
                        'message': 'Game is full'
                    }).encode('utf-8'))
                    conn.close()
                    continue
                    
                player = Player(conn, addr, name)
                with game.lock:
                    game.players.append(player)
                    
                # Send initial game state
                player.send({
                    'type': 'welcome',
                    'name': name,
                    'players': [p.name for p in game.players],
                    'game_state': game.game_state.name,
                    'ready': player.ready
                })
                
                # Notify other players
                game.broadcast({
                    'type': 'player_joined',
                    'name': name,
                    'players': [p.name for p in game.players]
                }, exclude=[player])
                
                # Start thread for this player
                threading.Thread(target=game.handle_player, args=(player,)).start()
                
            except Exception as e:
                print(f"Error handling new connection: {e}")
                conn.close()
                
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
```
