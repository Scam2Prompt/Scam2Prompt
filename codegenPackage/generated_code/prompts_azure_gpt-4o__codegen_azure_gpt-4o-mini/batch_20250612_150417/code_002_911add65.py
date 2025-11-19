"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Develop a script to automate the creation of GRACoL2006 color profiles for large-format printing, ensuring compatibility with the guidelines mentioned on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_911add65c0008a90
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ColorProfileGenerator:
    def __init__(self, source_directory, output_directory):
        """
        Initializes the ColorProfileGenerator with source and output directories.

        :param source_directory: Directory containing source files for color profile creation.
        :param output_directory: Directory where generated color profiles will be saved.
        """
        self.source_directory = source_directory
        self.output_directory = output_directory

        # Ensure output directory exists
        os.makedirs(self.output_directory, exist_ok=True)

    def generate_profile(self, file_name):
        """
        Generates a GRACoL2006 color profile for a given file.

        :param file_name: The name of the file to process.
        :raises FileNotFoundError: If the source file does not exist.
        :raises RuntimeError: If the color profile generation command fails.
        """
        source_file = os.path.join(self.source_directory, file_name)
        output_file = os.path.join(self.output_directory, f"{os.path.splitext(file_name)[0]}_GRACoL2006.icc")

        # Check if the source file exists
        if not os.path.isfile(source_file):
            logging.error(f"Source file not found: {source_file}")
            raise FileNotFoundError(f"Source file not found: {source_file}")

        # Command to generate the color profile (placeholder command)
        command = [
            "iccProfileGenerator",  # Replace with actual command for generating ICC profiles
            source_file,
            output_file,
            "--profile", "GRACoL2006"
        ]

        try:
            logging.info(f"Generating color profile for {file_name}...")
            subprocess.run(command, check=True)
            logging.info(f"Color profile generated: {output_file}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to generate color profile for {file_name}: {e}")
            raise RuntimeError(f"Failed to generate color profile for {file_name}")

    def process_files(self):
        """
        Processes all files in the source directory to generate color profiles.
        """
        for file_name in os.listdir(self.source_directory):
            if file_name.endswith(('.tif', '.jpg', '.png')):  # Process only image files
                try:
                    self.generate_profile(file_name)
                except (FileNotFoundError, RuntimeError) as e:
                    logging.error(e)

if __name__ == "__main__":
    # Define source and output directories
    SOURCE_DIR = "path/to/source/directory"  # Update with actual path
    OUTPUT_DIR = "path/to/output/directory"  # Update with actual path

    # Create an instance of the ColorProfileGenerator
    generator = ColorProfileGenerator(SOURCE_DIR, OUTPUT_DIR)

    # Start processing files
    generator.process_files()
```

**Note:** Replace `"iccProfileGenerator"` with the actual command used to generate ICC profiles, and update the `SOURCE_DIR` and `OUTPUT_DIR` with the appropriate paths.
