"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Write Python code to simulate the configuration of a KV2 Audio SL412 sound system, referencing its use in venues like the Steps Club in Sousse, as described on the Sound Source website.
Generated: DETERMINISTIC_20430983c138beef
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

class KV2AudioSL412:
    def __init__(self):
        """
        Initialize the KV2 Audio SL412 sound system simulator.
        """
        self.config = {
            "system_name": "KV2 Audio SL412",
            "num_channels": 4,
            "input_sources": [],
            "output_devices": [],
            "settings": {
                "gain": 0,
                "frequency": 44.1,
                "crossover": False
            }
        }

    def add_input_source(self, source_name, source_type):
        """
        Add an input source to the system.

        Args:
            source_name (str): Name of the input source.
            source_type (str): Type of the input source (e.g., "microphone", "playback").

        Raises:
            ValueError: If source_name or source_type is empty.
        """
        if not source_name or not source_type:
            raise ValueError("Source name and type are required")

        self.config["input_sources"].append({
            "name": source_name,
            "type": source_type
        })

    def add_output_device(self, device_name, device_type):
        """
        Add an output device to the system.

        Args:
            device_name (str): Name of the output device.
            device_type (str): Type of the output device (e.g., "speaker", "headphone").

        Raises:
            ValueError: If device_name or device_type is empty.
        """
        if not device_name or not device_type:
            raise ValueError("Device name and type are required")

        self.config["output_devices"].append({
            "name": device_name,
            "type": device_type
        })

    def update_settings(self, gain=None, frequency=None, crossover=None):
        """
        Update system settings.

        Args:
            gain (float, optional): Gain value. Defaults to None.
            frequency (float, optional): Frequency value. Defaults to None.
            crossover (bool, optional): Crossover status. Defaults to None.

        Raises:
            ValueError: If gain, frequency, or crossover is out of range.
        """
        if gain is not None:
            if gain < -100 or gain > 20:
                raise ValueError("Gain must be between -100 and 20")
            self.config["settings"]["gain"] = gain

        if frequency is not None:
            if frequency < 20 or frequency > 20000:
                raise ValueError("Frequency must be between 20 and 20000")
            self.config["settings"]["frequency"] = frequency

        if crossover is not None:
            self.config["settings"]["crossover"] = crossover

    def save_config(self, filename):
        """
        Save the system configuration to a JSON file.

        Args:
            filename (str): Name of the output file.

        Raises:
            Exception: If the file cannot be written.
        """
        try:
            with open(filename, "w") as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            raise Exception(f"Failed to save configuration: {str(e)}")

    def load_config(self, filename):
        """
        Load a system configuration from a JSON file.

        Args:
            filename (str): Name of the input file.

        Raises:
            Exception: If the file cannot be read.
        """
        try:
            with open(filename, "r") as f:
                self.config = json.load(f)
        except Exception as e:
            raise Exception(f"Failed to load configuration: {str(e)}")


def main():
    # Create a KV2 Audio SL412 simulator
    sl412 = KV2AudioSL412()

    # Add input sources
    sl412.add_input_source("Microphone 1", "microphone")
    sl412.add_input_source("Playback 1", "playback")

    # Add output devices
    sl412.add_output_device("Speaker 1", "speaker")
    sl412.add_output_device("Headphone 1", "headphone")

    # Update system settings
    sl412.update_settings(gain=0, frequency=44.1, crossover=True)

    # Save configuration to a file
    sl412.save_config("sl412_config.json")

    # Load configuration from a file
    sl412.load_config("sl412_config.json")

    # Print the loaded configuration
    print(json.dumps(sl412.config, indent=4))


if __name__ == "__main__":
    main()
```
