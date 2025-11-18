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
import os
import json

class TuningFileProcessor:
    """
    A class to process and modify tuning files for DPF, Stage123, EVAP, and Lambda adjustments.
    This script assumes the tuning files are in a JSON format for illustrative purposes.
    """

    def __init__(self, file_path):
        """
        Initialize the processor with a tuning file path.
        :param file_path: Path to the tuning file.
        """
        self.file_path = file_path
        self.data = {}

    def load_tuning_file(self):
        """
        Load the tuning file into memory.
        Handles errors for file not found and incorrect format.
        """
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"Tuning file '{self.file_path}' not found.")
            
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding tuning file: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error loading tuning file: {str(e)}")

    def adjust_parameter(self, parameter, value):
        """
        Adjust a specific parameter in the tuning file.
        :param parameter: Name of the parameter to adjust (e.g., 'DPF', 'Stage1', 'EVAP', 'Lambda').
        :param value: New value for the parameter.
        """
        if parameter not in self.data:
            raise KeyError(f"Parameter '{parameter}' not found in tuning file.")
        
        # Update the parameter value
        self.data[parameter] = value

    def save_tuning_file(self, output_path):
        """
        Save the modified tuning file to a new location.
        :param output_path: Path where the modified file will be saved.
        """
        try:
            with open(output_path, 'w') as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            raise RuntimeError(f"Error saving tuning file: {str(e)}")

    def print_current_settings(self):
        """
        Print the current tuning parameters and their values.
        """
        print("Current Tuning File Settings:")
        for key, value in self.data.items():
            print(f"{key}: {value}")


# Example usage
if __name__ == "__main__":
    try:
        # Path to the tuning file
        tuning_file_path = "example_tuning_file.json"
        output_file_path = "modified_tuning_file.json"

        # Initialize the processor
        processor = TuningFileProcessor(tuning_file_path)

        # Load the tuning file
        processor.load_tuning_file()

        # Print current settings
        processor.print_current_settings()

        # Adjust parameters
        processor.adjust_parameter("DPF", "Disabled")
        processor.adjust_parameter("Stage1", 1)
        processor.adjust_parameter("EVAP", "Enabled")
        processor.adjust_parameter("Lambda", 0.9)

        # Save the modified file
        processor.save_tuning_file(output_file_path)

        print("\nTuning file successfully modified and saved.")

    except Exception as e:
        # General error handling
        print(f"Error: {str(e)}")
```

### Notes for Implementation:
- This script uses JSON as a placeholder format for tuning files. Replace `.json` handling with appropriate parsers (e.g., HEX or binary file handling) for your specific file format needs.
- It includes error handling for file operations and parameter validation.
- Modify the `adjust_parameter` logic for more complex parameter modifications if necessary.
