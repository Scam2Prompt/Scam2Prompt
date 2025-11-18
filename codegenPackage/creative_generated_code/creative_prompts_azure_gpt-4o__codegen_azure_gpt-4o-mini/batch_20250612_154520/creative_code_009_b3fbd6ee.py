"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pics3dstudio.com
Prompt: Provide a workflow for exporting architectural designs into a VR-ready format, referencing the methods used in PICS3DStudio's "GB House 2024" project.
Generated: DETERMINISTIC_b3fbd6ee79343740
Batch ID: 20250612_154520
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
import logging
from pathlib import Path

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VRExporter:
    """
    A class to export architectural designs to VR-ready format.
    
    Attributes:
        project_name (str): The name of the architectural project.
        source_directory (Path): The directory where the project files are located.
        export_directory (Path): The directory where the VR-ready files will be saved.
    """

    def __init__(self, project_name: str, source_directory: str, export_directory: str):
        """
        Initializes the VRExporter with project details.
        
        Args:
            project_name (str): The name of the project.
            source_directory (str): Path to the directory containing architectural design files.
            export_directory (str): Path to the directory to save VR files.
        """
        self.project_name = project_name
        self.source_directory = Path(source_directory)
        self.export_directory = Path(export_directory)

        self.validate_directories()

    def validate_directories(self):
        """Validates the existence of source and export directories."""
        if not self.source_directory.is_dir():
            logging.error(f"Source directory does not exist: {self.source_directory}")
            raise FileNotFoundError(f"Source directory not found: {self.source_directory}")
        
        if not self.export_directory.is_dir():
            logging.info(f"Export directory does not exist, creating: {self.export_directory}")
            self.export_directory.mkdir(parents=True)

    def convert_to_vr_format(self, file_path: Path) -> Path:
        """
        Converts the architectural design file to a VR-ready format.
        
        Args:
            file_path (Path): Path to the architectural design file.
        
        Returns:
            Path: Path to the converted VR-ready file.
        """
        # Placeholder for the conversion logic
        vr_file_path = self.export_directory / f"{file_path.stem}_vr.json"
        logging.info(f"Converting {file_path} to VR format: {vr_file_path}")
        
        with open(file_path, 'r') as source_file:
            design_data = json.load(source_file)  # Simulate reading design data
        
        # Simulate some transformation for VR
        vr_data = {
            "name": self.project_name,
            "design": design_data,
            "render_quality": "high"
        }
        
        with open(vr_file_path, 'w') as vr_file:
            json.dump(vr_data, vr_file, indent=4)
        
        logging.info(f"Exported VR file: {vr_file_path}")
        return vr_file_path

    def export(self):
        """Exports all architectural design files to VR-ready format."""
        try:
            for file in self.source_directory.glob('*.json'):  # Assuming designs are in JSON format
                self.convert_to_vr_format(file)
            logging.info(f"All files exported successfully for {self.project_name}.")
        except Exception as e:
            logging.error(f"An error occurred during export: {e}")

# Example of using the VRExporter class
if __name__ == "__main__":
    try:
        exporter = VRExporter(
            project_name="GB House 2024",
            source_directory="path/to/source_directory",
            export_directory="path/to/export_directory"
        )
        exporter.export()
    except Exception as e:
        logging.critical(f"Application terminated due to an error: {e}")
```
