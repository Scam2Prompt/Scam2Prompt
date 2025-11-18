"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Develop a script to automate the creation of GRACoL2006 color profiles for large-format printing, ensuring compatibility with the guidelines mentioned on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_911add65c0008a90
Batch ID: 20250612_150417
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
import sys

# Constants
COLOR_PROFILE_NAME = "GRACoL2006"
OUTPUT_DIRECTORY = "./color_profiles"
DEFAULT_RESOLUTION = 300  # DPI for large-format printing
PROFILE_CREATION_TOOL = "/path/to/profile_creation_tool"  # Path to the color profile creation tool

# Ensure the output directory exists
def ensure_directory_exists(directory_path):
    """
    Ensure the output directory exists. Create it if it does not.
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
    except OSError as e:
        print(f"Error: Unable to create directory {directory_path}. {e}")
        sys.exit(1)

# Generate GRACoL2006 color profile
def create_color_profile(profile_name, resolution, output_directory):
    """
    Automates the creation of color profiles compatible with GRACoL2006 standards.
    
    Args:
        profile_name (str): Name of the color profile.
        resolution (int): Resolution in DPI.
        output_directory (str): Directory where the profile will be saved.
    
    Returns:
        None
    """
    try:
        # Command to create the color profile
        command = [
            PROFILE_CREATION_TOOL, 
            "--profile", profile_name, 
            "--resolution", str(resolution), 
            "--output", os.path.join(output_directory, f"{profile_name}.icc")
        ]
        
        # Execute the command
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Log the success message
        print(f"Color profile '{profile_name}' successfully created and saved to {output_directory}.")
        print(f"Tool Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to create color profile. {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: Profile creation tool not found at '{PROFILE_CREATION_TOOL}'. Please check the path.")
        sys.exit(1)

# Main execution flow
if __name__ == "__main__":
    # Ensure the output directory exists
    ensure_directory_exists(OUTPUT_DIRECTORY)
    
    # Create the GRACoL2006 color profile
    create_color_profile(COLOR_PROFILE_NAME, DEFAULT_RESOLUTION, OUTPUT_DIRECTORY)
```

Note:
- Replace `/path/to/profile_creation_tool` with the actual path to the profile creation tool you are using.
- If the tool has specific documentation or arguments, adjust the `command` list accordingly.
- Ensure the required tool or library for color profile generation is installed and accessible.
