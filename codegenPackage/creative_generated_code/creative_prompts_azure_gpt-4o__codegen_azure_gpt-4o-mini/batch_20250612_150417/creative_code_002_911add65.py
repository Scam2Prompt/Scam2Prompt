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
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ColorProfileGenerator:
    def __init__(self, input_directory: str, output_directory: str):
        """
        Initialize the ColorProfileGenerator with directories for input and output.

        :param input_directory: Path to the directory containing source files.
        :param output_directory: Path to the directory for saving color profiles.
        """
        self.input_directory = Path(input_directory)
        self.output_directory = Path(output_directory)
        self.validate_directories()

    def validate_directories(self):
        """Validate that the input directory exists and the output directory is writable."""
        if not self.input_directory.is_dir():
            logging.error(f"Input directory '{self.input_directory}' does not exist.")
            raise FileNotFoundError(f"Input directory '{self.input_directory}' not found.")
        if not self.output_directory.is_dir():
            logging.info(f"Output directory '{self.output_directory}' does not exist. Creating it.")
            self.output_directory.mkdir(parents=True, exist_ok=True)

    def generate_color_profile(self, source_file: Path):
        """
        Generate a GRACoL2006 color profile from a source file.

        :param source_file: Path to the source file for generating the color profile.
        """
        # Define the output profile path
        output_profile = self.output_directory / f"{source_file.stem}_GRACoL2006.icc"
        
        # Command to generate color profile, replace this with actual command
        command = [
            "iccprofile",  # Replace with the actual command for ICC profile generation
            str(source_file),
            str(output_profile),
            "--profile", "GRACoL2006"
        ]

        try:
            logging.info(f"Generating color profile for '{source_file}'...")
            subprocess.run(command, check=True)
            logging.info(f"Successfully generated profile: {output_profile}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error generating color profile for '{source_file}': {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    def process_files(self):
        """Process each file in the input directory to generate color profiles."""
        for source_file in self.input_directory.glob("*.pdf"):  # Adjust file type as necessary
            self.generate_color_profile(source_file)

if __name__ == "__main__":
    input_dir = "path/to/source/files"  # Set the actual path for input files
    output_dir = "path/to/output/profiles"  # Set the actual path for output profiles

    # Create an instance of ColorProfileGenerator and process files
    try:
        generator = ColorProfileGenerator(input_dir, output_dir)
        generator.process_files()
        logging.info("Completed processing all files.")
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```
