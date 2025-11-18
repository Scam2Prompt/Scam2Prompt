"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soundsource.tn
Prompt: Write Python code to simulate the configuration of a KV2 Audio SL412 sound system, referencing its use in venues like the Steps Club in Sousse, as described on the Sound Source website.
Generated: DETERMINISTIC_20430983c138beef
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to simulate configuration of a KV2 Audio SL412 sound system.
Inspired by its use in venues like the Steps Club in Sousse, as described on the Sound Source website.

This script provides a basic simulation of setting up the audio system in a venue,
with configuration options for input sources, speaker units, and volume settings.
"""

import logging

# Configure logging for error handling and system status
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants representing the audio system specifications
DEFAULT_VOLUME = 50  # Default volume level (0-100)
MAX_VOLUME = 100     # Maximum allowable volume
MIN_VOLUME = 0       # Minimum allowable volume
SPEAKER_UNITS = ["SL412 Left", "SL412 Right"]  # Represents two directional speaker units


class KV2AudioSL412:
    """
    Class to represent and simulate the configuration of a KV2 Audio SL412 sound system.
    """

    def __init__(self, venue_name):
        """
        Initializes the audio system for the specified venue.

        :param venue_name: Name of the venue where the system is being configured.
        """
        self.venue_name = venue_name
        self.volume_level = DEFAULT_VOLUME
        self.input_sources = []
        self.speakers = SPEAKER_UNITS
        logging.info(f"KV2 Audio SL412 initialized for venue: {self.venue_name}")

    def add_input_source(self, source_name):
        """
        Adds an input source to the audio system.

        :param source_name: Name of the input source (e.g., "DJ Mixer", "Live Band", "Background Music").
        """
        if source_name not in self.input_sources:
            self.input_sources.append(source_name)
            logging.info(f"Input source '{source_name}' added to the system.")
        else:
            logging.warning(f"Input source '{source_name}' is already configured.")

    def remove_input_source(self, source_name):
        """
        Removes an input source from the audio system.

        :param source_name: Name of the input source to remove.
        """
        if source_name in self.input_sources:
            self.input_sources.remove(source_name)
            logging.info(f"Input source '{source_name}' removed from the system.")
        else:
            logging.warning(f"Input source '{source_name}' is not currently configured.")

    def set_volume(self, volume):
        """
        Sets the volume level of the audio system.

        :param volume: Desired volume level (0-100).
        """
        if volume < MIN_VOLUME or volume > MAX_VOLUME:
            logging.error("Volume level out of range. Must be between 0 and 100.")
            raise ValueError("Volume must be between 0 and 100.")
        self.volume_level = volume
        logging.info(f"Volume level set to {volume}%.")

    def display_configuration(self):
        """
        Displays the current configuration of the audio system.
        """
        print("\n--- KV2 Audio SL412 Configuration ---")
        print(f"Venue: {self.venue_name}")
        print(f"Volume Level: {self.volume_level}%")
        print(f"Input Sources: {', '.join(self.input_sources) if self.input_sources else 'None'}")
        print(f"Speakers: {', '.join(self.speakers)}")
        print("------------------------------------")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the audio system for the venue
        audio_system = KV2AudioSL412(venue_name="Steps Club, Sousse")

        # Add input sources
        audio_system.add_input_source("DJ Mixer")
        audio_system.add_input_source("Live Band")

        # Set volume level
        audio_system.set_volume(75)

        # Display the current system configuration
        audio_system.display_configuration()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
