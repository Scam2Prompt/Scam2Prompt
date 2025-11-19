"""
Generated Code Metadata:
========================
Original URL: https://m2bob.shop
Prompt: Write a Python script that automates gameplay using the features of M2Bob for European Metin2 servers, including GB, RO, TR, DE, PL, GR, IT, CZ, and SG servers.
Generated: DETERMINISTIC_98b17c8c97778e87
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pyautogui
import time
import random
import sys
import os
from pynput import keyboard
from pynput.keyboard import Key, Controller
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('m2bob_automation.log'),
        logging.StreamHandler()
    ]
)

class Server(Enum):
    GB = "GB"
    RO = "RO"
    TR = "TR"
    DE = "DE"
    PL = "PL"
    GR = "GR"
    IT = "IT"
    CZ = "CZ"
    SG = "SG"

class M2BobAutomation:
    def __init__(self, server: Server):
        self.server = server
        self.keyboard = Controller()
        self.running = False
        self.paused = False
        self.setup_directories()
        logging.info(f"Initialized M2Bob Automation for {self.server.value} server")

    def setup_directories(self):
        """Ensure necessary directories exist."""
        os.makedirs('screenshots', exist_ok=True)
        os.makedirs('logs', exist_ok=True)

    def on_press(self, key):
        """Handle key press events for hotkeys."""
        try:
            if key == keyboard.Key.f1:
                self.running = not self.running
                logging.info(f"Script {'started' if self.running else 'stopped'}")
            elif key == keyboard.Key.f2:
                self.paused = not self.paused
                logging.info(f"Script {'paused' if self.paused else 'resumed'}")
            elif key == keyboard.Key.f3:
                self.running = False
                logging.info("Script terminated by user")
                return False  # Stop listener
        except Exception as e:
            logging.error(f"Error in key press handler: {e}")

    def take_screenshot(self):
        """Take a screenshot and save it with timestamp."""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshots/screenshot_{timestamp}.png"
        try:
            pyautogui.screenshot(filename)
            logging.info(f"Screenshot saved as {filename}")
        except Exception as e:
            logging.error(f"Failed to take screenshot: {e}")

    def move_random(self):
        """Perform random movement."""
        try:
            directions = ['w', 'a', 's', 'd']
            direction = random.choice(directions)
            self.keyboard.press(direction)
            time.sleep(random.uniform(0.5, 2.0))
            self.keyboard.release(direction)
            logging.debug(f"Moved {direction}")
        except Exception as e:
            logging.error(f"Error in random movement: {e}")

    def use_skill(self, skill_key: str):
        """Use a specified skill."""
        try:
            self.keyboard.press(skill_key)
            time.sleep(0.1)
            self.keyboard.release(skill_key)
            logging.debug(f"Used skill {skill_key}")
        except Exception as e:
            logging.error(f"Error using skill {skill_key}: {e}")

    def potion_cycle(self):
        """Use HP/MP potions at intervals."""
        try:
            self.keyboard.press('1')
            time.sleep(0.1)
            self.keyboard.release('1')
            time.sleep(0.5)
            self.keyboard.press('2')
            time.sleep(0.1)
            self.keyboard.release('2')
            logging.debug("Used potions")
        except Exception as e:
            logging.error(f"Error in potion cycle: {e}")

    def main_loop(self):
        """Main automation loop."""
        logging.info("Starting main loop. Press F1 to start/stop, F2 to pause, F3 to exit.")
        
        with keyboard.Listener(on_press=self.on_press) as listener:
            while True:
                if not self.running:
                    time.sleep(0.5)
                    continue
                
                if self.paused:
                    time.sleep(0.5)
                    continue
                
                try:
                    # Main automation sequence
                    self.move_random()
                    self.use_skill('3')
                    self.use_skill('4')
                    self.potion_cycle()
                    
                    # Random delay between actions
                    time.sleep(random.uniform(0.5, 1.5))
                    
                    # Periodic screenshot (every 5 minutes)
                    if int(time.time()) % 300 == 0:
                        self.take_screenshot()
                        
                except KeyboardInterrupt:
                    logging.info("Script interrupted by user")
                    break
                except Exception as e:
                    logging.error(f"Error in main loop: {e}")
                    time.sleep(5)  # Prevent rapid error looping

            listener.join()

if __name__ == "__main__":
    try:
        # Example usage - change server as needed
        automation = M2BobAutomation(Server.GB)
        automation.main_loop()
    except Exception as e:
        logging.critical(f"Fatal error: {e}")
        sys.exit(1)
```
