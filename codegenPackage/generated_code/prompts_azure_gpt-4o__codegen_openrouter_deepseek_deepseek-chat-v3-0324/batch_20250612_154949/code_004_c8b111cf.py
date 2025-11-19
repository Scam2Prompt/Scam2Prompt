"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Write code to generate printable scorecards for slowpitch softball games in PSD or PNG format, inspired by the free tools available on Slo-Pitch Central.
Generated: DETERMINISTIC_c8b111cfd0f9c098
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

class SoftballScorecardGenerator:
    """
    A class to generate printable slowpitch softball scorecards in PNG format.
    Inspired by Slo-Pitch Central's free tools.
    """
    
    def __init__(self, home_team="Home Team", away_team="Away Team", date=None, location="Ballpark"):
        """
        Initialize the scorecard generator with basic game information.
        
        Args:
            home_team (str): Name of the home team
            away_team (str): Name of the away team
            date (str, optional): Game date in YYYY-MM-DD format. Defaults to today.
            location (str, optional): Game location. Defaults to "Ballpark".
        """
        self.home_team = home_team
        self.away_team = away_team
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.location = location
        
        # Scorecard dimensions (in pixels)
        self.width = 2550
        self.height = 3300
        
        # Colors
        self.bg_color = (255, 255, 255)  # White
        self.line_color = (0, 0, 0)      # Black
        self.text_color = (0, 0, 0)      # Black
        self.highlight_color = (200, 200, 200)  # Light gray
        
        # Fonts
        try:
            self.title_font = ImageFont.truetype("arial.ttf", 72)
            self.header_font = ImageFont.truetype("arial.ttf", 48)
            self.text_font = ImageFont.truetype("arial.ttf", 36)
            self.small_font = ImageFont.truetype("arial.ttf", 24)
        except IOError:
            # Fallback to default fonts if Arial is not available
            self.title_font = ImageFont.load_default()
            self.header_font = ImageFont.load_default()
            self.text_font = ImageFont.load_default()
            self.small_font = ImageFont.load_default()
    
    def _draw_grid(self, draw, x, y, rows, cols, cell_width, cell_height):
        """
        Draw a grid at the specified position.
        
        Args:
            draw (ImageDraw.Draw): Drawing context
            x (int): Starting x position
            y (int): Starting y position
            rows (int): Number of rows
            cols (int): Number of columns
            cell_width (int): Width of each cell
            cell_height (int): Height of each cell
        """
        # Draw vertical lines
        for col in range(cols + 1):
            draw.line(
                [(x + col * cell_width, y), (x + col * cell_width, y + rows * cell_height)],
                fill=self.line_color,
                width=2
            )
        
        # Draw horizontal lines
        for row in range(rows + 1):
            draw.line(
                [(x, y + row * cell_height), (x + cols * cell_width, y + row * cell_height)],
                fill=self.line_color,
                width=2
            )
    
    def _draw_centered_text(self, draw, x, y, width, height, text, font, color=None):
        """
        Draw centered text within a specified rectangle.
        
        Args:
            draw (ImageDraw.Draw): Drawing context
            x (int): Rectangle x position
            y (int): Rectangle y position
            width (int): Rectangle width
            height (int): Rectangle height
            text (str): Text to draw
            font (ImageFont.FreeTypeFont): Font to use
            color (tuple, optional): Text color. Defaults to self.text_color.
        """
        if color is None:
            color = self.text_color
            
        text_width, text_height = draw.textsize(text, font=font)
        draw.text(
            (x + (width - text_width) / 2, y + (height - text_height) / 2),
            text,
            fill=color,
            font=font
        )
    
    def generate_scorecard(self, output_path=None, format="PNG"):
        """
        Generate and save the scorecard image.
        
        Args:
            output_path (str, optional): Output file path. Defaults to "scorecard_{date}.png".
            format (str, optional): Output format ("PNG" or "PSD"). Defaults to "PNG".
            
        Returns:
            str: Path to the generated file
        """
        # Create a new image with white background
        image = Image.new("RGB", (self.width, self.height), self.bg_color)
        draw = ImageDraw.Draw(image)
        
        # Draw header
        self._draw_centered_text(draw, 0, 50, self.width, 100, "SLOWPITCH SOFTBALL SCORECARD", self.title_font)
        
        # Draw game info
        game_info_y = 200
        self._draw_centered_text(draw, 0, game_info_y, self.width, 50, f"Date: {self.date}", self.header_font)
        self._draw_centered_text(draw, 0, game_info_y + 60, self.width, 50, f"Location: {self.location}", self.header_font)
        
        # Draw team names
        team_y = game_info_y + 150
        team_width = self.width // 2 - 100
        self._draw_centered_text(draw, 50, team_y, team_width, 80, f"Home: {self.home_team}", self.header_font)
        self._draw_centered_text(draw, self.width // 2 + 50, team_y, team_width, 80, f"Away: {self.away_team}", self.header_font)
        
        # Draw score grid
        score_y = team_y + 120
        self._draw_grid(draw, 100, score_y, 9, 10, 100, 80)
        
        # Draw inning headers
        for inning in range(1, 10):
            self._draw_centered_text(draw, 100 + inning * 100, score_y, 100, 80, str(inning), self.text_font)
        
        # Draw "R" (runs) and "H" (hits) headers
        self._draw_centered_text(draw, 100, score_y + 80, 100, 80, "R", self.text_font)
        self._draw_centered_text(draw, 100, score_y + 160, 100, 80, "H", self.text_font)
        
        # Draw team labels in score grid
        self._draw_centered_text(draw, 100, score_y + 240, 100, 80, self.home_team[:12], self.small_font)
        self._draw_centered_text(draw, 100, score_y + 320, 100, 80, self.away_team[:12], self.small_font)
        
        # Draw batting order section
        batting_y = score_y + 500
        self._draw_centered_text(draw, 100, batting_y - 60, self.width - 200, 50, "BATTING ORDER", self.header_font)
        
        # Home team batting order
        self._draw_grid(draw, 100, batting_y, 12, 6, 150, 60)
        self._draw_centered_text(draw, 100, batting_y, 150, 60, "#", self.text_font)
        self._draw_centered_text(draw, 250, batting_y, 150, 60, "Name", self.text_font)
        self._draw_centered_text(draw, 400, batting_y, 150, 60, self.home_team[:10], self.small_font)
        
        # Away team batting order
        away_batting_x = self.width // 2 + 50
        self._draw_grid(draw, away_batting_x, batting_y, 12, 6, 150, 60)
        self._draw_centered_text(draw, away_batting_x, batting_y, 150, 60, "#", self.text_font)
        self._draw_centered_text(draw, away_batting_x + 150, batting_y, 150, 60, "Name", self.text_font)
        self._draw_centered_text(draw, away_batting_x + 300, batting_y, 150, 60, self.away_team[:10], self.small_font)
        
        # Draw notes section
        notes_y = batting_y + 800
        self._draw_centered_text(draw, 100, notes_y - 60, self.width - 200, 50, "NOTES", self.header_font)
        draw.rectangle([100, notes_y, self.width
