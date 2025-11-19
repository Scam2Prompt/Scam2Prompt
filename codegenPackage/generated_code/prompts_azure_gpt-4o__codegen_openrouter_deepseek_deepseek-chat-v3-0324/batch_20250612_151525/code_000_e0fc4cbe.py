"""
Generated Code Metadata:
========================
Original URL: https://miamigojesus.edu.pe
Prompt: Write code to create a local multiplayer game interface inspired by SCATTER HITAM, allowing players to connect via a local network and collaborate or compete in real-time.
Generated: DETERMINISTIC_e0fc4cbe4d0b7bdc
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import socket
import threading
import json
import sys
from enum import Enum

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
SERVER_PORT = 5555
MAX_PLAYERS = 4

# Game states
class GameState(Enum):
    LOBBY = 0
    PLAYING = 1
    GAME_OVER = 2

# Player class
class Player:
    def __init__(self, id, name, color, position=(0, 0)):
        self.id = id
        self.name = name
        self.color = color
        self.position = position
        self.score = 0
        self.ready = False

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
            'position': self.position,
            'score': self.score,
            'ready': self.ready
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data['id'], data['name'], data['color'], data['position'])
        player.score = data['score']
        player.ready = data['ready']
        return player

# Game server
class GameServer:
    def __init__(self):
        self.players = {}
        self.game_state = GameState.LOBBY
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('0.0.0.0', SERVER_PORT))
        self.server_socket.listen(MAX_PLAYERS)
        self.lock = threading.Lock()

    def handle_client(self, client_socket, address):
        try:
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break

                message = json.loads(data.decode())
                self.process_message(client_socket, message)

        except (ConnectionResetError, json.JSONDecodeError) as e:
            print(f"Client disconnected: {address}")
        finally:
            with self.lock:
                for player_id, player in list(self.players.items()):
                    if player.get('socket') == client_socket:
                        del self.players[player_id]
                        self.broadcast_state()
                        break
            client_socket.close()

    def process_message(self, client_socket, message):
        with self.lock:
            if message['type'] == 'join':
                player = Player.from_dict(message['player'])
                self.players[player.id] = {'player': player, 'socket': client_socket}
                self.broadcast_state()

            elif message['type'] == 'update':
                player_id = message['player_id']
                if player_id in self.players:
                    self.players[player_id]['player'].position = message['position']
                    self.broadcast_state()

            elif message['type'] == 'ready':
                player_id = message['player_id']
                if player_id in self.players:
                    self.players[player_id]['player'].ready = message['ready']
                    self.broadcast_state()

                    # Check if all players are ready
                    if all(p['player'].ready for p in self.players.values()):
                        self.game_state = GameState.PLAYING
                        self.broadcast_state()

            elif message['type'] == 'score':
                player_id = message['player_id']
                if player_id in self.players:
                    self.players[player_id]['player'].score += message['points']
                    self.broadcast_state()

    def broadcast_state(self):
        state = {
            'type': 'state',
            'game_state': self.game_state.name,
            'players': [p['player'].to_dict() for p in self.players.values()]
        }
        message = json.dumps(state).encode()
        
        for player_data in self.players.values():
            try:
                player_data['socket'].sendall(message)
            except ConnectionError:
                continue

    def start(self):
        print(f"Server started on port {SERVER_PORT}")
        try:
            while True:
                client_socket, address = self.server_socket.accept()
                print(f"New connection from {address}")
                threading.Thread(target=self.handle_client, args=(client_socket, address)).start()
        except KeyboardInterrupt:
            print("Shutting down server...")
        finally:
            self.server_socket.close()

# Game client
class GameClient:
    def __init__(self, player_name, player_color):
        self.player = Player(0, player_name, player_color)
        self.players = {}
        self.game_state = GameState.LOBBY
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
        self.running = False

    def connect(self, server_ip):
        try:
            self.client_socket.connect((server_ip, SERVER_PORT))
            self.running = True
            threading.Thread(target=self.receive_messages).start()
            
            # Send join message
            join_message = {
                'type': 'join',
                'player': self.player.to_dict()
            }
            self.send_message(join_message)
            return True
        except ConnectionError:
            return False

    def send_message(self, message):
        try:
            self.client_socket.sendall(json.dumps(message).encode())
        except ConnectionError:
            self.running = False

    def receive_messages(self):
        try:
            while self.running:
                data = self.client_socket.recv(4096)
                if not data:
                    self.running = False
                    break

                message = json.loads(data.decode())
                if message['type'] == 'state':
                    self.game_state = GameState[message['game_state']]
                    self.players = {
                        p['id']: Player.from_dict(p) for p in message['players']
                    }
        except (ConnectionResetError, json.JSONDecodeError):
            self.running = False

    def update_position(self, position):
        self.player.position = position
        message = {
            'type': 'update',
            'player_id': self.player.id,
            'position': position
        }
        self.send_message(message)

    def toggle_ready(self):
        self.player.ready = not self.player.ready
        message = {
            'type': 'ready',
            'player_id': self.player.id,
            'ready': self.player.ready
        }
        self.send_message(message)

    def add_score(self, points):
        message = {
            'type': 'score',
            'player_id': self.player.id,
            'points': points
        }
        self.send_message(message)

    def disconnect(self):
        self.running = False
        self.client_socket.close()

# Game interface
class ScatterHitamGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Scatter Hitam")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        
        self.is_host = False
        self.server = None
        self.client = None
        self.player_name = "Player"
        self.player_color = (255, 0, 0)
        self.input_text = ""
        self.active_input = None

    def start_server(self):
        self.is_host = True
        self.server = GameServer()
        threading.Thread(target=self.server.start, daemon=True).start()
        self.connect_to_server("127.0.0.1")

    def connect_to_server(self, ip):
        self.client = GameClient(self.player_name, self.player_color)
        if not self.client.connect(ip):
            print("Failed to connect to server")
            return False
        return True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if self.active_input == "name":
                    if event.key == pygame.K_RETURN:
                        self.player_name = self.input_text
                        self.active_input = None
                        self.input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        self.input_text += event.unicode

                elif event.key == pygame.K_ESCAPE:
                    return False

                # Game controls
                if self.client and self.client.game_state == GameState.PLAYING:
                    if event.key == pygame.K_LEFT:
                        new_pos = (self.client.player.position[0] - 10, self.client.player.position[1])
                        self.client.update_position(new_pos)
                    elif event.key == pygame.K_RIGHT:
                        new_pos = (self.client.player.position[0] + 10, self.client.player.position[1])
                        self.client.update_position(new_pos)
                    elif event.key == pygame.K_UP:
                        new_pos = (self.client.player.position[0], self.client.player.position[1] - 10)
                        self.client.update_position(new_pos)
                    elif event.key ==
