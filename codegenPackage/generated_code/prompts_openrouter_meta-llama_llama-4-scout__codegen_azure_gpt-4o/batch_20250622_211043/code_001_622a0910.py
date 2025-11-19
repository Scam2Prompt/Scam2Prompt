"""
Generated Code Metadata:
========================
Original URL: https://www3.celestia.net
Prompt: What are the steps to create a custom 3D model for Celestia, and how can I integrate it into the software?
Generated: DETERMINISTIC_622a091003b0b31b
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Creating a custom 3D model for Celestia involves creating a 3D model file (e.g., in `.3ds` or `.obj` format), converting it to Celestia's `.cmod` format, and integrating it into Celestia by editing its configuration files. Below is Python code to automate the conversion and integration process:

```python
import os
import subprocess
import shutil

# Constants
MODEL_FILE = "custom_model.obj"  # Path to your 3D model file (.obj or .3ds)
CMOD_CONVERTER = "3ds2cmod"      # Celestia's model converter tool
OUTPUT_CMOD = "custom_model.cmod"  # Output .cmod file
CELESTIA_MODELS_DIR = "/path/to/celestia/models"  # Path to Celestia's models directory
CELESTIA_CONFIG_FILE = "/path/to/celestia/config/your_config.ssc"  # Path to Celestia's .ssc file

def convert_to_cmod(model_file, output_file):
    """
    Converts a 3D model file to Celestia's .cmod format using the 3ds2cmod tool.
    """
    try:
        print(f"Converting {model_file} to {output_file}...")
        subprocess.run([CMOD_CONVERTER, model_file, output_file], check=True)
        print(f"Conversion successful: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        raise

def move_cmod_to_celestia(output_file, destination_dir):
    """
    Moves the .cmod file to Celestia's models directory.
    """
    try:
        print(f"Moving {output_file} to {destination_dir}...")
        shutil.move(output_file, os.path.join(destination_dir, os.path.basename(output_file)))
        print("Move successful.")
    except Exception as e:
        print(f"Error during file move: {e}")
        raise

def update_celestia_config(config_file, model_name, model_path):
    """
    Updates Celestia's configuration file (.ssc) to include the new model.
    """
    try:
        print(f"Updating Celestia configuration file: {config_file}...")
        with open(config_file, "a") as f:
            f.write(f"""
# Custom 3D Model
"CustomObject" "Sol/Earth"
{{
    Mesh "{model_path}"
    Radius 1000
}}
""")
        print("Configuration updated successfully.")
    except Exception as e:
        print(f"Error updating configuration file: {e}")
        raise

def main():
    """
    Main function to automate the process of integrating a custom 3D model into Celestia.
    """
    try:
        # Step 1: Convert the 3D model to .cmod format
        convert_to_cmod(MODEL_FILE, OUTPUT_CMOD)

        # Step 2: Move the .cmod file to Celestia's models directory
        move_cmod_to_celestia(OUTPUT_CMOD, CELESTIA_MODELS_DIR)

        # Step 3: Update Celestia's configuration file
        model_name = os.path.splitext(os.path.basename(OUTPUT_CMOD))[0]
        model_path = f"models/{model_name}.cmod"
        update_celestia_config(CELESTIA_CONFIG_FILE, model_name, model_path)

        print("Custom 3D model integration completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
1. Replace `/path/to/celestia/models` and `/path/to/celestia/config/your_config.ssc` with the actual paths to your Celestia installation.
2. Ensure the `3ds2cmod` tool is installed and accessible in your system's PATH.
3. The `.ssc` configuration file is updated to include the new model under the "Sol/Earth" hierarchy. Adjust the hierarchy and parameters (e.g., `Radius`) as needed for your use case.
