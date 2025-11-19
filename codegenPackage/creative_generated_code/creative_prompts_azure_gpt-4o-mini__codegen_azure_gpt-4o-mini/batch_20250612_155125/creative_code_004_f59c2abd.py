"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cadv.io
Prompt: Generate a step-by-step guide on exporting a CAD model from software to cadvio in DWG format for visualization.
Generated: DETERMINISTIC_f59c2abdd4dc0335
Batch ID: 20250612_155125
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def export_cad_model_to_dwg(cad_software_path, model_file_path, output_directory):
    """
    Export a CAD model from specified CAD software to DWG format for visualization in CadVio.

    Parameters:
        cad_software_path (str): The file path to the CAD software executable.
        model_file_path (str): The full path to the CAD model file to export.
        output_directory (str): The directory where the exported DWG file will be saved.

    Returns:
        str: The full path to the exported DWG file if successful, None otherwise.
    """
    try:
        # Check if the CAD model file exists
        if not os.path.isfile(model_file_path):
            logging.error(f"Model file does not exist: {model_file_path}")
            return None

        # Check if the output directory exists; create if it doesn't
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
            logging.info(f"Created output directory: {output_directory}")

        # Prepare the output file path
        dwg_file_name = os.path.splitext(os.path.basename(model_file_path))[0] + '.dwg'
        dwg_file_path = os.path.join(output_directory, dwg_file_name)

        # Build the command to export the model as DWG
        command = [cad_software_path, model_file_path, dwg_file_path]

        # Call the CAD software to export the file
        logging.info(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True)

        # Check for errors in the process execution
        if result.returncode != 0:
            logging.error(f"Error exporting model: {result.stderr}")
            return None
        
        logging.info(f"Export successful: {dwg_file_path}")
        return dwg_file_path

    except Exception as e:
        logging.exception("An exception occurred during the export process.")
        return None

# Example usage
if __name__ == "__main__":
    cad_software_path = "path/to/your/cad/software/executable"
    model_file_path = "path/to/your/model/file.cad"
    output_directory = "path/to/your/output/directory"

    exported_file = export_cad_model_to_dwg(cad_software_path, model_file_path, output_directory)
    if exported_file:
        print(f"Exported DWG file: {exported_file}")
    else:
        print("Export failed.")
```
