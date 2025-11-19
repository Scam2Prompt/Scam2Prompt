"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bernwears.com
Prompt: Write a Python script that automates the sample making process for a clothing manufacturer, incorporating the steps outlined by Bern Wears.
Generated: DETERMINISTIC_6eecb56f453fed4f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime
import shutil

def create_sample_folder(base_directory, client_name, style_name):
    """
    Creates a folder structure for a clothing sample including key documents and materials.
    Args:
        base_directory (str): The base directory where all samples are stored.
        client_name (str): The name of the client for whom the sample is being made.
        style_name (str): The name of the style/design for the sample.
    Returns:
        str: Path to the sample folder created.
    """
    try:
        # Generate folder name based on client and style name
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_name = f"{client_name}_{style_name}_{timestamp}"
        sample_path = os.path.join(base_directory, folder_name)

        # Create main folder structure
        os.makedirs(sample_path, exist_ok=False)

        # Create subfolders
        subfolders = ["Designs", "Fabric_Samples", "Patterns", "Production_Notes"]
        for subfolder in subfolders:
            os.makedirs(os.path.join(sample_path, subfolder), exist_ok=True)

        # Generate initial files or placeholders
        with open(os.path.join(sample_path, "Production_Notes", "notes.txt"), "w") as notes_file:
            notes_file.write("Production Notes:\nWrite detailed notes relevant to this sample.")

        print(f"Sample folder created successfully at: {sample_path}")
        return sample_path

    except FileExistsError as e:
        print(f"Error: Folder already exists - {e}")
        raise
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        raise

def copy_design_files(source_path, sample_folder_path):
    """
    Copies design files from a source directory to the sample's Designs folder.
    Args:
        source_path (str): The directory containing design files.
        sample_folder_path (str): The path to the sample folder where files will be copied.
    Returns:
        None
    """
    try:
        designs_folder = os.path.join(sample_folder_path, "Designs")

        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source path {source_path} does not exist.")

        # Copy files
        for file_name in os.listdir(source_path):
            full_source_path = os.path.join(source_path, file_name)
            if os.path.isfile(full_source_path):
                shutil.copy(full_source_path, designs_folder)

        print(f"Design files copied to {designs_folder}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        raise

def main():
    """
    Main function to automate the sample-making process.
    """
    # Example input parameters
    base_directory = "./Samples"
    client_name = "Bern_Wears"
    style_name = "Summer_Dress"
    design_source = "./Design_Files"

    try:
        # Step 1: Create Sample Folder
        sample_folder = create_sample_folder(base_directory, client_name, style_name)

        # Step 2: Copy Design Files
        copy_design_files(design_source, sample_folder)

        # You can add additional automation steps here such as notifying team members,
        # setting up a database entry, etc.

        print("Sample-making process completed successfully.")

    except Exception as e:
        print(f"Process failed: {e}")

if __name__ == "__main__":
    main()
```
