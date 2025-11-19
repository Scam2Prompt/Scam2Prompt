"""
Generated Code Metadata:
========================
Original URL: https://getpromo.me
Prompt: Generate a script for automating the creation of 3D explainer videos using CreateStudio, as discussed on getPROMO.me.
Generated: DETERMINISTIC_a41e39a9cdaba1ea
Batch ID: 20250612_154454
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

class CreateStudioAutomation:
    def __init__(self, project_name, output_directory):
        """
        Initializes the CreateStudioAutomation class.

        :param project_name: Name of the project to be created
        :param output_directory: Directory where the output video will be saved
        """
        self.project_name = project_name
        self.output_directory = output_directory
        self.create_studio_path = "C:\\Path\\To\\CreateStudio.exe"  # Update with the actual path to CreateStudio

    def create_project(self):
        """
        Creates a new project in CreateStudio.
        """
        try:
            logging.info(f"Creating project: {self.project_name}")
            # Command to create a new project
            command = [self.create_studio_path, "--create", self.project_name]
            subprocess.run(command, check=True)
            logging.info("Project created successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to create project: {e}")
            raise

    def add_scene(self, scene_name):
        """
        Adds a scene to the project.

        :param scene_name: Name of the scene to be added
        """
        try:
            logging.info(f"Adding scene: {scene_name}")
            command = [self.create_studio_path, "--add-scene", scene_name]
            subprocess.run(command, check=True)
            logging.info("Scene added successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to add scene: {e}")
            raise

    def export_video(self):
        """
        Exports the project as a video file.
        """
        try:
            output_file = os.path.join(self.output_directory, f"{self.project_name}.mp4")
            logging.info(f"Exporting video to: {output_file}")
            command = [self.create_studio_path, "--export", output_file]
            subprocess.run(command, check=True)
            logging.info("Video exported successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to export video: {e}")
            raise

    def run(self):
        """
        Executes the automation process.
        """
        self.create_project()
        self.add_scene("Intro Scene")
        self.add_scene("Main Content Scene")
        self.add_scene("Outro Scene")
        self.export_video()

if __name__ == "__main__":
    # Define project name and output directory
    project_name = "3D_Explainer_Video"
    output_directory = "C:\\Path\\To\\Output"  # Update with the actual output directory

    # Create an instance of CreateStudioAutomation
    automation = CreateStudioAutomation(project_name, output_directory)

    # Run the automation process
    try:
        automation.run()
    except Exception as e:
        logging.error(f"An error occurred during the automation process: {e}")
```
