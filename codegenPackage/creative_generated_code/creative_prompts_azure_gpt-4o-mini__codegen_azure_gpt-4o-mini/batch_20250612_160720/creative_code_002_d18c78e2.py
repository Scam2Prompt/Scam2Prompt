"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvidia-bios-editor.ru
Prompt: What are the steps to edit memory timings using the NVIDIA BIOS Editor (NiBiTor) for optimal performance?
Generated: DETERMINISTIC_d18c78e2541d5dc0
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess

class NiBiTorEditor:
    """
    A class to automate the process of editing memory timings using the NVIDIA BIOS Editor (NiBiTor).
    """

    def __init__(self, nibitor_path: str, bios_file: str):
        """
        Initializes the NiBiTorEditor with the path to NiBiTor and the BIOS file.

        :param nibitor_path: The path to the NiBiTor executable.
        :param bios_file: The path to the NVIDIA BIOS file to be edited.
        """
        self.nibitor_path = nibitor_path
        self.bios_file = bios_file

    def check_file_exists(self, file_path: str) -> bool:
        """
        Check if a file exists at the given path.

        :param file_path: The path to the file to check.
        :return: True if the file exists, False otherwise.
        """
        return os.path.isfile(file_path)

    def edit_memory_timings(self, new_timings: dict) -> None:
        """
        Edits the memory timings in the NVIDIA BIOS and saves a new BIOS file.

        :param new_timings: A dictionary containing the new memory timings.
        :raises FileNotFoundError: If either the NiBiTor executable or the BIOS file does not exist.
        :raises Exception: For any errors encountered during the editing process.
        """
        # Check if the NiBiTor executable and BIOS file exist
        if not self.check_file_exists(self.nibitor_path):
            raise FileNotFoundError(f"NiBiTor executable not found at {self.nibitor_path}")
        if not self.check_file_exists(self.bios_file):
            raise FileNotFoundError(f"BIOS file not found at {self.bios_file}")

        # Prepare command to run NiBiTor with the provided BIOS file
        command = [self.nibitor_path, self.bios_file]

        try:
            # Run NiBiTor to perform the editing
            subprocess.run(command, check=True)
            self.apply_new_timings(new_timings)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Editing process failed: {e}")

    def apply_new_timings(self, new_timings: dict) -> None:
        """
        Applies the new memory timings to the BIOS file.

        :param new_timings: A dictionary containing the new memory timings.
        """
        # This is a placeholder for the actual implementation
        # The actual logic to edit the timing values should be added here
        print("Applying new memory timings...")
        for timing, value in new_timings.items():
            print(f"Setting {timing} to {value}")
        print("Memory timings updated successfully.")

if __name__ == "__main__":
    # Example usage of NiBiTorEditor
    nibitor_executable_path = "C:\\Path\\To\\NiBiTor.exe"  # Replace with actual path
    bios_file_path = "C:\\Path\\To\\BIOS.rom"  # Replace with actual path
    
    # Example new timings (this should be replaced with actual timings)
    new_memory_timings = {
        "Timing1": "5-5-5-15",
        "Timing2": "6-6-6-18"
    }

    # Create an instance of NiBiTorEditor
    editor = NiBiTorEditor(nibitor_executable_path, bios_file_path)

    # Perform the editing operation
    try:
        editor.edit_memory_timings(new_memory_timings)
    except Exception as e:
        print(f"An error occurred: {e}")
```
