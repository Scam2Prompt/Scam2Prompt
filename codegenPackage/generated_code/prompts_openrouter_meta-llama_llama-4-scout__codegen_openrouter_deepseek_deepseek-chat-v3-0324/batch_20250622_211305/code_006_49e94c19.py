"""
Generated Code Metadata:
========================
Original URL: https://www.immediateapexai.org
Prompt: Create a customizable color scheme for a trading platform's charting and analysis tools, allowing users to personalize their trading experience, similar to Immediate Apex AI's color customization feature.
Generated: DETERMINISTIC_49e94c19b7fd113d
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Optional, Union
from dataclasses import dataclass, asdict
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ColorScheme:
    """Dataclass representing a customizable color scheme for trading charts."""
    background: str = "#1E1E2D"
    grid_lines: str = "#2D2D42"
    text: str = "#E0E0E0"
    bullish_candle: str = "#26A69A"
    bearish_candle: str = "#EF5350"
    buy_signal: str = "#00D1FF"
    sell_signal: str = "#FF6B6B"
    volume_up: str = "#4CAF50"
    volume_down: str = "#F44336"
    indicator_line: str = "#FFA726"
    crosshair: str = "#FFFFFF"

    def to_dict(self) -> Dict[str, str]:
        """Convert the color scheme to a dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, color_dict: Dict[str, str]) -> 'ColorScheme':
        """Create a ColorScheme instance from a dictionary."""
        return cls(**color_dict)

class ColorSchemeManager:
    """Manager for handling color scheme customization and persistence."""
    
    def __init__(self, config_file: str = "color_schemes.json"):
        self.config_file = config_file
        self.schemes: Dict[str, ColorScheme] = {}
        self.load_schemes()

    def load_schemes(self) -> None:
        """Load color schemes from the configuration file."""
        try:
            with open(self.config_file, 'r') as f:
                schemes_data = json.load(f)
                self.schemes = {
                    name: ColorScheme.from_dict(scheme) 
                    for name, scheme in schemes_data.items()
                }
            logger.info("Color schemes loaded successfully.")
        except FileNotFoundError:
            logger.info("No existing color schemes file found. Starting fresh.")
            self.schemes = {
                "default": ColorScheme(),
                "dark": ColorScheme(
                    background="#121212",
                    grid_lines="#1E1E1E",
                    text="#FFFFFF"
                ),
                "light": ColorScheme(
                    background="#FFFFFF",
                    grid_lines="#E0E0E0",
                    text="#000000",
                    bullish_candle="#4CAF50",
                    bearish_candle="#F44336"
                )
            }
            self.save_schemes()
        except Exception as e:
            logger.error(f"Error loading color schemes: {e}")
            raise

    def save_schemes(self) -> None:
        """Save current color schemes to the configuration file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(
                    {name: scheme.to_dict() for name, scheme in self.schemes.items()},
                    f,
                    indent=4
                )
            logger.info("Color schemes saved successfully.")
        except Exception as e:
            logger.error(f"Error saving color schemes: {e}")
            raise

    def get_scheme(self, name: str) -> Optional[ColorScheme]:
        """Get a color scheme by name."""
        return self.schemes.get(name)

    def add_scheme(self, name: str, scheme: ColorScheme) -> None:
        """Add or update a color scheme."""
        if not name:
            raise ValueError("Scheme name cannot be empty.")
        self.schemes[name] = scheme
        self.save_schemes()

    def delete_scheme(self, name: str) -> bool:
        """Delete a color scheme."""
        if name in self.schemes:
            del self.schemes[name]
            self.save_schemes()
            return True
        return False

    def list_schemes(self) -> Dict[str, ColorScheme]:
        """List all available color schemes."""
        return self.schemes.copy()

# Example usage
if __name__ == "__main__":
    manager = ColorSchemeManager()
    
    # Create a custom scheme
    custom_scheme = ColorScheme(
        background="#0A0A0A",
        grid_lines="#1A1A1A",
        text="#CCCCCC",
        bullish_candle="#00C853",
        bearish_candle="#FF3D00"
    )
    
    # Add the custom scheme
    manager.add_scheme("my_custom_scheme", custom_scheme)
    
    # Retrieve and print all schemes
    print("Available color schemes:")
    for name, scheme in manager.list_schemes().items():
        print(f"{name}: {scheme}")
```
