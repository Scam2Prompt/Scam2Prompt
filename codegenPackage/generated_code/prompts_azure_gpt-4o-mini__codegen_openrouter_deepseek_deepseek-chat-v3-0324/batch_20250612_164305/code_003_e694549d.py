"""
Generated Code Metadata:
========================
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: Generate an example of how to build a world in Pixels that allows for collaboration and competition among players.
Generated: DETERMINISTIC_e694549da75267ec
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Pixels World with Collaboration and Competition

```python
import pygame
import random
import json
import socket
import threading
from queue import Queue

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
PLAYER_SIZE = 15
COLORS = {
    'background': (50, 50, 50),
    'grid': (80, 80, 80),
    'player1': (255, 0, 0),
    'player2': (0, 0, 255),
    'resource': (0, 255, 0),
    'wall': (120, 120, 120)
}

# Game state class
class GameState:
    def __init__(self):
        self.players = {
            'player1': {'x': 100, 'y': 100, 'score': 0, 'color': COLORS['player1']},
            'player2': {'x': 700, 'y': 500, 'score': 0, 'color': COLORS['player2']}
        }
        self.resources = []
        self.walls = []
        self.generate_world()
        
    def generate_world(self):
        # Generate walls
        for _ in range(20):
            self.walls.append({
                'x': random.randint(0, SCREEN_WIDTH // GRID_SIZE) * GRID_SIZE,
                'y': random.randint(0, SCREEN_HEIGHT // GRID_SIZE) * GRID_SIZE
            })
        
        # Generate initial resources
        for _ in range(10):
            self.spawn_resource()
    
    def spawn_resource(self):
        while True:
            x = random.randint(0, SCREEN_WIDTH // GRID_SIZE) * GRID_SIZE
            y = random.randint(0, SCREEN_HEIGHT // GRID_SIZE) * GRID_SIZE
            
            # Check if position is occupied
            occupied = any(wall['x'] == x and wall['y'] == y for wall in self.walls)
            if not occupied:
                self.resources.append({'x': x, 'y': y})
                break
    
    def move_player(self, player_id, dx, dy):
        player = self.players[player_id]
        new_x = player['x'] + dx * GRID_SIZE
        new_y = player['y'] + dy * GRID_SIZE
        
        # Check boundaries
        if 0 <= new_x < SCREEN_WIDTH and 0 <= new_y < SCREEN_HEIGHT:
            # Check wall collisions
            wall_collision = any(
                wall['x'] == new_x and wall['y'] == new_y 
                for wall in self.walls
            )
            
            if not wall_collision:
                player['x'] = new_x
                player['y'] = new_y
                
                # Check resource collection
                for i, resource in enumerate(self.resources):
                    if resource['x'] == new_x and resource['y'] == new_y:
                        player['score'] += 1
                        self.resources.pop(i)
                        self.spawn_resource()
                        break
    
    def to_dict(self):
        return {
            'players': self.players,
            'resources': self.resources,
            'walls': self.walls
        }
    
    def from_dict(self, state_dict):
        self.players = state_dict['players']
        self.resources = state_dict['resources']
        self.walls = state_dict['walls']

# Network handler
class NetworkHandler:
    def __init__(self, host, port, is_server=False):
        self.is_server = is_server
        self.message_queue = Queue()
        
        if is_server:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((host, port))
            self.socket.listen(1)
            self.conn, _ = self.socket.accept()
        else:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
        
        # Start receive thread
        threading.Thread(target=self.receive_messages, daemon=True).start()
    
    def receive_messages(self):
        while True:
            try:
                data = self.socket.recv(4096).decode('utf-8')
                if data:
                    self.message_queue.put(json.loads(data))
            except (ConnectionError, json.JSONDecodeError):
                break
    
    def send_message(self, message):
        try:
            self.socket.sendall(json.dumps(message).encode('utf-8'))
        except ConnectionError:
            pass
    
    def close(self):
        self.socket.close()

# Main game class
class PixelWorld:
    def __init__(self, is_server=False):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pixel World")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.is_server = is_server
        self.game_state = GameState()
        
        # Network setup
        host = 'localhost'
        port = 5555
        self.network = NetworkHandler(host, port, is_server)
        
        # Player ID
        self.player_id = 'player1' if is_server else 'player2'
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                dx, dy = 0, 0
                if event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1
                elif event.key == pygame.K_UP:
                    dy = -1
                elif event.key == pygame.K_DOWN:
                    dy = 1
                
                if dx != 0 or dy != 0:
                    self.game_state.move_player(self.player_id, dx, dy)
                    if self.is_server:
                        # Server sends updated state to client
                        self.network.send_message(self.game_state.to_dict())
    
    def update(self):
        # Check for incoming network messages
        while not self.network.message_queue.empty():
            message = self.network.message_queue.get()
            if not self.is_server:
                # Client updates state from server
                self.game_state.from_dict(message)
            else:
                # Server could handle client messages here
                pass
    
    def render(self):
        self.screen.fill(COLORS['background'])
        
        # Draw grid
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, COLORS['grid'], (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, COLORS['grid'], (0, y), (SCREEN_WIDTH, y))
        
        # Draw walls
        for wall in self.game_state.walls:
            pygame.draw.rect(
                self.screen, COLORS['wall'],
                (wall['x'], wall['y'], GRID_SIZE, GRID_SIZE)
            )
        
        # Draw resources
        for resource in self.game_state.resources:
            pygame.draw.rect(
                self.screen, COLORS['resource'],
                (resource['x'], resource['y'], GRID_SIZE, GRID_SIZE)
            )
        
        # Draw players
        for player_id, player in self.game_state.players.items():
            pygame.draw.rect(
                self.screen, player['color'],
                (player['x'], player['y'], PLAYER_SIZE, PLAYER_SIZE)
            )
            
            # Draw score
            font = pygame.font.SysFont(None, 24)
            score_text = font.render(f"{player_id}: {player['score']}", True, player['color'])
            if player_id == 'player1':
                self.screen.blit(score_text, (10, 10))
            else:
                self.screen.blit(score_text, (SCREEN_WIDTH - 150, 10))
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        
        pygame.quit()
        self.network.close()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'server':
        game = PixelWorld(is_server=True)
    else:
        game = PixelWorld(is_server=False)
    
    game.run()
```
