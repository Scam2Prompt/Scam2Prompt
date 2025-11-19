"""
Generated Code Metadata:
========================
Original URL: https://vascavotivadinoceto.it
Prompt: Generate a Python script to create a virtual tour of the Museo Vasca Votiva di Noceto, incorporating multimedia elements as described on the website.
Generated: DETERMINISTIC_ae72abfece4e8cab
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import pygame
import json
from pygame.locals import *
from typing import Dict, List, Optional, Tuple

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
ASSETS_DIR = "assets"
TOUR_DATA_FILE = os.path.join(ASSETS_DIR, "tour_data.json")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

class VirtualTour:
    """Main class for the virtual tour application."""
    
    def __init__(self):
        """Initialize the virtual tour."""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Museo Vasca Votiva di Noceto - Virtual Tour")
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_room = None
        self.tour_data = self.load_tour_data()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.audio_channels = {}
        self.loaded_images = {}
        self.loaded_audio = {}
        self.navigation_buttons = []
        self.info_button = None
        self.media_button = None
        self.active_media = None
        
        if not self.tour_data:
            print("Failed to load tour data. Exiting.")
            sys.exit(1)
            
        self.setup_initial_room()
    
    def load_tour_data(self) -> Optional[Dict]:
        """Load tour data from JSON file."""
        try:
            with open(TOUR_DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading tour data: {e}")
            return None
    
    def setup_initial_room(self):
        """Set up the initial room of the tour."""
        if "initial_room" in self.tour_data:
            self.change_room(self.tour_data["initial_room"])
    
    def change_room(self, room_id: str):
        """Change to a different room in the tour."""
        if room_id not in self.tour_data["rooms"]:
            print(f"Room {room_id} not found in tour data.")
            return
            
        self.current_room = self.tour_data["rooms"][room_id]
        self.load_room_assets()
        self.setup_navigation()
        self.setup_info_button()
        self.setup_media_button()
        self.stop_all_audio()
        self.active_media = None
    
    def load_room_assets(self):
        """Load assets for the current room."""
        # Load background image
        bg_path = os.path.join(ASSETS_DIR, self.current_room["background"])
        if bg_path not in self.loaded_images:
            try:
                image = pygame.image.load(bg_path).convert()
                self.loaded_images[bg_path] = image
            except pygame.error as e:
                print(f"Error loading image {bg_path}: {e}")
                # Fallback to black background
                self.loaded_images[bg_path] = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                self.loaded_images[bg_path].fill(BLACK)
        
        # Load audio files
        if "audio" in self.current_room:
            audio_path = os.path.join(ASSETS_DIR, self.current_room["audio"])
            if audio_path not in self.loaded_audio:
                try:
                    sound = pygame.mixer.Sound(audio_path)
                    self.loaded_audio[audio_path] = sound
                except pygame.error as e:
                    print(f"Error loading audio {audio_path}: {e}")
    
    def setup_navigation(self):
        """Set up navigation buttons for the current room."""
        self.navigation_buttons = []
        
        if "exits" not in self.current_room:
            return
            
        for i, exit_data in enumerate(self.current_room["exits"]):
            button_rect = pygame.Rect(
                50 + (i * 200),
                SCREEN_HEIGHT - 100,
                180,
                50
            )
            self.navigation_buttons.append({
                "rect": button_rect,
                "text": exit_data["label"],
                "target": exit_data["room_id"]
            })
    
    def setup_info_button(self):
        """Set up the info button for the current room."""
        if "description" not in self.current_room:
            self.info_button = None
            return
            
        self.info_button = {
            "rect": pygame.Rect(SCREEN_WIDTH - 150, 20, 130, 40),
            "text": "Info"
        }
    
    def setup_media_button(self):
        """Set up the media button if the room has media."""
        if "media" not in self.current_room or not self.current_room["media"]:
            self.media_button = None
            return
            
        self.media_button = {
            "rect": pygame.Rect(SCREEN_WIDTH - 150, 70, 130, 40),
            "text": "Media"
        }
    
    def stop_all_audio(self):
        """Stop all currently playing audio."""
        for channel in self.audio_channels.values():
            if channel and channel.get_busy():
                channel.stop()
        self.audio_channels.clear()
    
    def play_audio(self, audio_path: str, loop: bool = False):
        """Play an audio file."""
        full_path = os.path.join(ASSETS_DIR, audio_path)
        if full_path in self.loaded_audio:
            channel = pygame.mixer.find_channel()
            if channel:
                if loop:
                    self.loaded_audio[full_path].play(-1)
                else:
                    self.loaded_audio[full_path].play()
                self.audio_channels[full_path] = channel
    
    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.handle_click(event.pos)
    
    def handle_click(self, pos: Tuple[int, int]):
        """Handle mouse clicks on interactive elements."""
        # Check navigation buttons
        for button in self.navigation_buttons:
            if button["rect"].collidepoint(pos):
                self.change_room(button["target"])
                return
                
        # Check info button
        if self.info_button and self.info_button["rect"].collidepoint(pos):
            self.show_info()
            return
            
        # Check media button
        if self.media_button and self.media_button["rect"].collidepoint(pos):
            self.show_media_selector()
            return
            
        # Check active media close button
        if self.active_media and "close_rect" in self.active_media:
            if self.active_media["close_rect"].collidepoint(pos):
                self.active_media = None
                return
    
    def show_info(self):
        """Display room information."""
        if "description" not in self.current_room:
            return
            
        self.active_media = {
            "type": "info",
            "text": self.current_room["description"],
            "close_rect": pygame.Rect(SCREEN_WIDTH - 50, 20, 30, 30)
        }
    
    def show_media_selector(self):
        """Display available media for the room."""
        if "media" not in self.current_room or not self.current_room["media"]:
            return
            
        self.active_media = {
            "type": "media_selector",
            "items": self.current_room["media"],
            "close_rect": pygame.Rect(SCREEN_WIDTH - 50, 20, 30, 30)
        }
    
    def play_selected_media(self, media_item: Dict):
        """Play the selected media item."""
        if media_item["type"] == "audio":
            self.play_audio(media_item["path"])
            self.active_media = {
                "type": "media_player",
                "media": media_item,
                "close_rect": pygame.Rect(SCREEN_WIDTH - 50, 20, 30, 30)
            }
        elif media_item["type"] == "image":
            try:
                image = pygame.image.load(os.path.join(ASSETS_DIR, media_item["path"])).convert()
                self.active_media = {
                    "type": "media_player",
                    "media": media_item,
                    "image": image,
                    "close_rect": pygame.Rect(SCREEN_WIDTH - 50, 20, 30, 30)
                }
            except pygame.error as e:
                print(f"Error loading media image: {e}")
    
    def render(self):
        """Render the current state of the tour."""
        # Clear screen
        self.screen.fill(BLACK)
        
        # Draw background
