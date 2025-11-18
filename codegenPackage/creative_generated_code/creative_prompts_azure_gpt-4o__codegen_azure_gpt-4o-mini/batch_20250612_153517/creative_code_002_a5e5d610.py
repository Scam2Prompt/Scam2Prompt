"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payeshnirooco.com
Prompt: Generate code for automating the synchronization of power generators using changeover panels, referencing the technical details provided by پایش نیرو.
Generated: DETERMINISTIC_a5e5d610bd8e0963
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

class PowerGenerator:
    """Class to represent a power generator with status and load capacity."""
    
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity  # Maximum load this generator can handle
        self.is_running = False

    def start(self):
        """Start the generator."""
        if not self.is_running:
            self.is_running = True
            logging.info(f"Generator {self.id} started.")
        else:
            logging.warning(f"Generator {self.id} is already running.")

    def stop(self):
        """Stop the generator."""
        if self.is_running:
            self.is_running = False
            logging.info(f"Generator {self.id} stopped.")
        else:
            logging.warning(f"Generator {self.id} is already stopped.")

class ChangeoverPanel:
    """Class to manage changeover panel logic for synchronizing generators."""
    
    def __init__(self):
        self.generators = []
        self.active_generator = None

    def add_generator(self, generator):
        """Add a generator to the changeover panel."""
        self.generators.append(generator)
        logging.info(f"Generator {generator.id} added to the changeover panel.")

    def synchronize(self):
        """Synchronize the power generators."""
        try:
            if not self.generators:
                raise ValueError("No generators available for synchronization.")

            for generator in self.generators:
                if not generator.is_running:
                    generator.start()
            
            self.active_generator = self.generators[0]  # Set the first generator as active
            logging.info(f"Active generator is now {self.active_generator.id}.")
        except Exception as e:
            logging.error(f"Error during synchronization: {str(e)}")

    def switch_generators(self):
        """Switch to the next generator in the sequence."""
        try:
            if not self.generators:
                raise ValueError("No generators available for switching.")
                
            if self.active_generator:
                current_index = self.generators.index(self.active_generator)
                next_index = (current_index + 1) % len(self.generators)
                self.active_generator.stop()
                self.active_generator = self.generators[next_index]
                self.active_generator.start()
                logging.info(f"Switched to generator {self.active_generator.id}.")
            else:
                raise RuntimeError("No active generator to switch from.")
        except Exception as e:
            logging.error(f"Error during generator switch: {str(e)}")

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Initialize changeover panel
    panel = ChangeoverPanel()
    
    # Create and add generators
    generator1 = PowerGenerator(id=1, capacity=100)
    generator2 = PowerGenerator(id=2, capacity=150)

    panel.add_generator(generator1)
    panel.add_generator(generator2)

    # Synchronize generators
    panel.synchronize()

    # Simulate generator switching every 10 seconds
    try:
        while True:
            time.sleep(10)  # Wait for 10 seconds
            panel.switch_generators()
    except KeyboardInterrupt:
        logging.info("Synchronization process interrupted by user.")
        for generator in panel.generators:
            generator.stop()

if __name__ == "__main__":
    main()
```
