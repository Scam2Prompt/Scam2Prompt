"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuninghex.com
Prompt: Recommend a library or tool to process and modify tuning files for DPF, Stage123, EVAP, and Lambda adjustments, as described on the TuningHEX website.
Generated: DETERMINISTIC_613f2569377881c9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class TuningFileProcessor:
    """A class to process and modify tuning files for various vehicle adjustments."""

    def __init__(self, file_path):
        """
        Initializes the TuningFileProcessor with the specified file path.

        Args:
            file_path (str): The path to the tuning file.

        Raises:
            FileNotFoundError: If the tuning file does not exist.
            ValueError: If the file format is unsupported.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Tuning file not found: {file_path}")

        self.file_path = file_path
        self.data = self._load_tuning_file()

    def _load_tuning_file(self):
        """Loads the tuning file data.

        Returns:
            dict: The parsed tuning data.

        Raises:
            ValueError: If the tuning file is not a valid JSON.
        """
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid tuning file format. Must be valid JSON.") from e

    def modify_setting(self, key, value):
        """Modifies a specific tuning setting.

        Args:
            key (str): The key of the tuning setting to modify.
            value: The new value to assign to the tuning setting.

        Raises:
            KeyError: If the specified key does not exist in the tuning data.
        """
        if key not in self.data:
            raise KeyError(f"Setting '{key}' not found in tuning data.")
        self.data[key] = value

    def save_tuning_file(self, output_path=None):
        """Saves the modified tuning data back to a file.

        Args:
            output_path (str, optional): The path to save the modified file. 
                                          If None, overwrites the original file.

        Raises:
            IOError: If there is an error writing the file.
        """
        if output_path is None:
            output_path = self.file_path

        try:
            with open(output_path, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving tuning file to {output_path}.") from e

    def get_setting(self, key):
        """Retrieves the value of a specific tuning setting.

        Args:
            key (str): The key of the tuning setting to retrieve.

        Returns:
            The value of the tuning setting.

        Raises:
            KeyError: If the specified key does not exist in the tuning data.
        """
        if key not in self.data:
            raise KeyError(f"Setting '{key}' not found in tuning data.")
        return self.data[key]

# Example usage
if __name__ == "__main__":
    try:
        processor = TuningFileProcessor("tuning_file.json")
        print(processor.get_setting("DPF"))
        processor.modify_setting("Stage123", 1)
        processor.save_tuning_file("modified_tuning_file.json")
    except (FileNotFoundError, ValueError, KeyError, IOError) as e:
        print(f"Error: {e}")
```
