"""
Generated Code Metadata:
========================
Original URL: https://www.brothernz.com
Prompt: Generate a Python script that uses the Brother PE Design software to automate embroidery design creation.
Generated: DETERMINISTIC_573deeb6a2c8bdce
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import subprocess
from typing import List

class BrotherPEDesign:
    """
    A class to interact with Brother PE Design software.

    Attributes:
    -----------
    software_path (str): The path to the Brother PE Design software executable.
    """

    def __init__(self, software_path: str):
        """
        Initializes the BrotherPEDesign class.

        Args:
        -----
        software_path (str): The path to the Brother PE Design software executable.
        """
        self.software_path = software_path

    def create_design(self, design_name: str, stitch_type: str, stitch_color: str, design_data: List[List[int]]):
        """
        Creates a new embroidery design using the Brother PE Design software.

        Args:
        -----
        design_name (str): The name of the design to be created.
        stitch_type (str): The type of stitch to be used.
        stitch_color (str): The color of the stitch.
        design_data (List[List[int]]): A 2D list containing the design data.

        Returns:
        --------
        bool: True if the design was created successfully, False otherwise.
        """
        try:
            # Create a temporary file to store the design data
            tmp_file = f"{design_name}.csv"
            with open(tmp_file, "w") as f:
                for row in design_data:
                    f.write(",".join(map(str, row)) + "\n")

            # Construct the command to create the design
            command = f'"{self.software_path}" /CREATE_DESIGN "{design_name}" /STITCH_TYPE "{stitch_type}" /STITCH_COLOR "{stitch_color}" /IMPORT_DATA "{tmp_file}"'

            # Run the command using subprocess
            subprocess.run(command, shell=True, check=True)

            # Remove the temporary file
            os.remove(tmp_file)

            return True

        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during the creation of the design
            print(f"Error creating design: {e}")
            return False

        except Exception as e:
            # Handle any other exceptions that may occur
            print(f"An error occurred: {e}")
            return False


def main():
    # Example usage
    software_path = r"C:\Program Files\Brother\PE-Design\PED.exe"
    design_name = "MyDesign"
    stitch_type = "Satin"
    stitch_color = "Red"
    design_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    ped = BrotherPEDesign(software_path)
    success = ped.create_design(design_name, stitch_type, stitch_color, design_data)

    if success:
        print(f"Design '{design_name}' created successfully.")
    else:
        print(f"Failed to create design '{design_name}'.")


if __name__ == "__main__":
    main()
```
