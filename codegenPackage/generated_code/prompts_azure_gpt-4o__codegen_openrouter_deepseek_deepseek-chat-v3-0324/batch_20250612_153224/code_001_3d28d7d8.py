"""
Generated Code Metadata:
========================
Original URL: https://aerotraining.com.tr
Prompt: Generate code to create a virtual cockpit interface for an Airbus A320 flight simulator, incorporating emergency scenarios and online flight capabilities as detailed on the Aero Training Center webpage.
Generated: DETERMINISTIC_3d28d7d8c9ea936c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import sys
import socket
import threading
import json
import random
import time
from enum import Enum

# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 60
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Emergency scenarios
class Emergency(Enum):
    NONE = 0
    ENGINE_FAILURE = 1
    FIRE = 2
    LOSS_OF_HYDRAULICS = 3
    ELECTRICAL_FAILURE = 4

# Flight parameters
class FlightParams:
    def __init__(self):
        self.altitude = 0
        self.speed = 0
        self.heading = 0
        self.fuel = 100
        self.engine1_status = True
        self.engine2_status = True
        self.hydraulics_status = True
        self.electrical_status = True
        self.emergency = Emergency.NONE
        self.online = False

# Virtual Cockpit class
class VirtualCockpit:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Airbus A320 Virtual Cockpit")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 20)
        self.running = True
        self.flight_params = FlightParams()
        self.client_socket = None
        self.server_thread = None
        self.emergency_handling = False

    def connect_to_server(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((SERVER_HOST, SERVER_PORT))
            self.flight_params.online = True
            self.server_thread = threading.Thread(target=self.receive_data)
            self.server_thread.daemon = True
            self.server_thread.start()
        except Exception as e:
            print(f"Connection error: {e}")
            self.flight_params.online = False

    def receive_data(self):
        while self.flight_params.online:
            try:
                data = self.client_socket.recv(1024).decode('utf-8')
                if data:
                    params = json.loads(data)
                    self.update_flight_params(params)
            except Exception as e:
                print(f"Receive error: {e}")
                self.flight_params.online = False
                break

    def send_data(self):
        if self.flight_params.online:
            try:
                data = json.dumps({
                    'altitude': self.flight_params.altitude,
                    'speed': self.flight_params.speed,
                    'heading': self.flight_params.heading,
                    'fuel': self.flight_params.fuel,
                    'emergency': self.flight_params.emergency.value
                })
                self.client_socket.send(data.encode('utf-8'))
            except Exception as e:
                print(f"Send error: {e}")
                self.flight_params.online = False

    def update_flight_params(self, params):
        self.flight_params.altitude = params.get('altitude', self.flight_params.altitude)
        self.flight_params.speed = params.get('speed', self.flight_params.speed)
        self.flight_params.heading = params.get('heading', self.flight_params.heading)
        self.flight_params.fuel = params.get('fuel', self.flight_params.fuel)
        self.flight_params.emergency = Emergency(params.get('emergency', self.flight_params.emergency.value))

    def handle_emergency(self):
        if self.flight_params.emergency != Emergency.NONE and not self.emergency_handling:
            self.emergency_handling = True
            if self.flight_params.emergency == Emergency.ENGINE_FAILURE:
                self.flight_params.engine1_status = False
            elif self.flight_params.emergency == Emergency.FIRE:
                self.flight_params.engine1_status = False
                self.flight_params.fuel -= 20
            elif self.flight_params.emergency == Emergency.LOSS_OF_HYDRAULICS:
                self.flight_params.hydraulics_status = False
            elif self.flight_params.emergency == Emergency.ELECTRICAL_FAILURE:
                self.flight_params.electrical_status = False
        elif self.flight_params.emergency == Emergency.NONE:
            self.emergency_handling = False

    def draw_cockpit(self):
        self.screen.fill(BLACK)
        
        # Draw primary flight display
        pygame.draw.rect(self.screen, BLUE, (50, 50, 300, 200), 2)
        alt_text = self.font.render(f"Altitude: {self.flight_params.altitude} ft", True, WHITE)
        speed_text = self.font.render(f"Speed: {self.flight_params.speed} kts", True, WHITE)
        heading_text = self.font.render(f"Heading: {self.flight_params.heading}°", True, WHITE)
        fuel_text = self.font.render(f"Fuel: {self.flight_params.fuel}%", True, WHITE)
        
        self.screen.blit(alt_text, (60, 60))
        self.screen.blit(speed_text, (60, 90))
        self.screen.blit(heading_text, (60, 120))
        self.screen.blit(fuel_text, (60, 150))
        
        # Draw engine status
        engine1_color = GREEN if self.flight_params.engine1_status else RED
        engine2_color = GREEN if self.flight_params.engine2_status else RED
        pygame.draw.circle(self.screen, engine1_color, (400, 100), 20)
        pygame.draw.circle(self.screen, engine2_color, (500, 100), 20)
        engine1_text = self.font.render("ENG1", True, WHITE)
        engine2_text = self.font.render("ENG2", True, WHITE)
        self.screen.blit(engine1_text, (380, 130))
        self.screen.blit(engine2_text, (480, 130))
        
        # Draw system status
        hyd_color = GREEN if self.flight_params.hydraulics_status else RED
        elec_color = GREEN if self.flight_params.electrical_status else RED
        pygame.draw.rect(self.screen, hyd_color, (400, 200, 40, 20))
        pygame.draw.rect(self.screen, elec_color, (500, 200, 40, 20))
        hyd_text = self.font.render("HYD", True, WHITE)
        elec_text = self.font.render("ELEC", True, WHITE)
        self.screen.blit(hyd_text, (400, 230))
        self.screen.blit(elec_text, (500, 230))
        
        # Draw emergency status
        if self.flight_params.emergency != Emergency.NONE:
            emergency_text = self.font.render(f"EMERGENCY: {self.flight_params.emergency.name}", True, RED)
            self.screen.blit(emergency_text, (50, 300))
        
        # Draw online status
        online_color = GREEN if self.flight_params.online else RED
        online_text = self.font.render("ONLINE" if self.flight_params.online else "OFFLINE", True, online_color)
        self.screen.blit(online_text, (SCREEN_WIDTH - 150, 30))
        
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.flight_params.altitude += 1000
                elif event.key == pygame.K_DOWN:
                    self.flight_params.altitude -= 1000
                elif event.key == pygame.K_RIGHT:
                    self.flight_params.heading = (self.flight_params.heading + 10) % 360
                elif event.key == pygame.K_LEFT:
                    self.flight_params.heading = (self.flight_params.heading - 10) % 360
                elif event.key == pygame.K_c:
                    self.connect_to_server()
                elif event.key == pygame.K_e:
                    self.flight_params.emergency = Emergency(random.randint(1, 4))
                elif event.key == pygame.K_r:
                    self.flight_params.emergency = Emergency.NONE
                    self.flight_params.engine1_status = True
                    self.flight_params.engine2_status = True
                    self.flight_params.hydraulics_status = True
