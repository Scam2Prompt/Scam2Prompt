"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Provide an example of how to implement a skin preview tool for a game character in a blockchain FPS similar to ev.io.
Generated: DETERMINISTIC_1cb3b003b636d105
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: skin_preview_tool.py

import sys
import json
from typing import Dict, Optional
import pygame

# Constants for the application
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (30, 30, 30)
FPS = 60

# Error classes
class SkinPreviewError(Exception):
    """Custom exception for skin preview tool errors."""
    pass

# Skin Preview Tool implementation
class SkinPreviewTool:
    def __init__(self, skin_data_file: str):
        """
        Initializes the SkinPreviewTool.
        
        :param skin_data_file: Path to the JSON file containing skin data.
        """
        try:
            self.skin_data = self._load_skin_data(skin_data_file)
        except Exception as e:
            raise SkinPreviewError(f"Failed to load skin data: {e}")
        
        # Initialize PyGame
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Skin Preview Tool - FPS Character")
        self.clock = pygame.time.Clock()

    def _load_skin_data(self, filepath: str) -> Dict:
        """
        Loads skin data from a JSON file.
        
        :param filepath: Path to the JSON file.
        :return: Parsed JSON as a dictionary.
        """
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise SkinPreviewError(f"Skin data file not found: {filepath}")
        except json.JSONDecodeError:
            raise SkinPreviewError(f"Invalid JSON format in file: {filepath}")

    def _get_skin_image(self, skin_id: str) -> Optional[pygame.Surface]:
        """
        Loads the skin image based on its ID.
        
        :param skin_id: ID of the skin to preview.
        :return: PyGame Surface object for the skin image, or None if not found.
        """
        skin_info = self.skin_data.get(skin_id)
        if not skin_info:
            raise SkinPreviewError(f"Skin ID '{skin_id}' not found in skin data.")
        
        image_path = skin_info.get("image_path")
        if not image_path:
            raise SkinPreviewError(f"Image path missing for skin ID '{skin_id}'.")
        
        try:
            return pygame.image.load(image_path).convert_alpha()
        except pygame.error:
            raise SkinPreviewError(f"Failed to load image: {image_path}")

    def preview_skin(self, skin_id: str):
        """
        Runs the skin preview tool for the given skin ID.
        
        :param skin_id: ID of the skin to preview.
        """
        try:
            skin_image = self._get_skin_image(skin_id)
            if not skin_image:
                raise SkinPreviewError(f"Skin image for ID '{skin_id}' could not be loaded.")
            
            skin_rect = skin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                
                # Fill screen with background color
                self.screen.fill(BACKGROUND_COLOR)
                
                # Draw the skin image
                self.screen.blit(skin_image, skin_rect)
                
                # Update the display
                pygame.display.flip()
                
                # Cap the frame rate
                self.clock.tick(FPS)
        
        except SkinPreviewError as e:
            print(f"Error: {e}", file=sys.stderr)
        finally:
            # Clean up PyGame resources
            pygame.quit()

# Entry point for the tool
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python skin_preview_tool.py <skin_data_file> <skin_id>", file=sys.stderr)
        sys.exit(1)

    skin_data_file = sys.argv[1]
    skin_id = sys.argv[2]

    try:
        tool = SkinPreviewTool(skin_data_file)
        tool.preview_skin(skin_id)
    except SkinPreviewError as e:
        print(f"Skin Preview Tool Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        sys.exit(1)
```
