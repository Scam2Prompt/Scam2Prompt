"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m2bob.shop
Prompt: Create a script to use M2Bob's features for farming resources in Metin2, referencing the specific server compatibility details mentioned on the M2Bob site.
Generated: DETERMINISTIC_b23ed0a5d55ecc71
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# M2Bob Resource Farming Script for Metin2

import time
import random

class M2BobFarmingBot:
    def __init__(self, server_name):
        """
        Initialize the bot with server details.

        :param server_name: str: The name of the Metin2 server to connect to.
        """
        self.server_name = server_name
        self.is_running = False

    def start(self):
        """
        Start the farming bot.
        """
        self.is_running = True
        print(f"[INFO] Starting farming on server: {self.server_name}")
        try:
            self.farm_resources()
        except Exception as e:
            print(f"[ERROR] An error occurred: {str(e)}")
        finally:
            self.stop()

    def farm_resources(self):
        """
        Continuously farm resources until the bot is stopped.
        """
        while self.is_running:
            try:
                # Simulate farming process
                print("[INFO] Farming resources...")
                time.sleep(random.uniform(1, 3))  # Simulate time taken to farm resources
                
                # Placeholder for actual farming logic
                if random.random() < 0.1:  # Simulate a potential error
                    raise RuntimeError("Failed to harvest resources.")

                print("[INFO] Resources harvested successfully.")

            except RuntimeError as re:
                print(f"[WARNING] {str(re)}. Retrying...")
                time.sleep(2)  # Wait before retrying
            
            except Exception as e:
                print(f"[ERROR] Unexpected error during farming: {str(e)}")
                self.is_running = False

    def stop(self):
        """
        Stop the farming bot gracefully.
        """
        self.is_running = False
        print("[INFO] Stopping the farming bot.")

# Example usage
if __name__ == "__main__":
    server = "ExampleMetin2Server"  # Replace with actual server name
    bot = M2BobFarmingBot(server)
    bot.start()
```
