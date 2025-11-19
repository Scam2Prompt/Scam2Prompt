"""
Generated Code Metadata:
========================
Original URL: https://bda.mcupr.ac.th
Prompt: How can I implement a digital archive system for Buddhist sculptures and artifacts similar to those described in the Buddhist Art Gallery at MCU?
Generated: DETERMINISTIC_3d8f9ce6525ca6dd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime

class DigitalArchive:
    """
    A class to implement a digital archive system for Buddhist sculptures and artifacts.
    """

    def __init__(self, archive_directory="archive"):
        """
        Initialize the digital archive system.

        :param archive_directory: Directory where archive data will be stored.
        """
        self.archive_directory = archive_directory
        if not os.path.exists(self.archive_directory):
            os.makedirs(self.archive_directory)  # Create directory if it doesn't exist

    def add_artifact(self, artifact_id, name, description, origin, date_discovered, image_path):
        """
        Add a new artifact to the archive.

        :param artifact_id: Unique identifier for the artifact.
        :param name: Name of the artifact.
        :param description: Description of the artifact.
        :param origin: Origin or location where the artifact was found.
        :param date_discovered: Date the artifact was discovered (YYYY-MM-DD).
        :param image_path: Path to the image file of the artifact.
        :return: None
        """
        try:
            # Validate date format
            datetime.strptime(date_discovered, "%Y-%m-%d")

            # Validate image file existence
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image file '{image_path}' not found.")

            # Create artifact data
            artifact_data = {
                "artifact_id": artifact_id,
                "name": name,
                "description": description,
                "origin": origin,
                "date_discovered": date_discovered,
                "image_path": image_path
            }

            # Save artifact data to a JSON file
            artifact_file = os.path.join(self.archive_directory, f"{artifact_id}.json")
            with open(artifact_file, "w") as file:
                json.dump(artifact_data, file, indent=4)

            print(f"Artifact '{name}' added successfully.")

        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_artifact(self, artifact_id):
        """
        View details of an artifact.

        :param artifact_id: Unique identifier for the artifact.
        :return: None
        """
        try:
            artifact_file = os.path.join(self.archive_directory, f"{artifact_id}.json")
            if not os.path.exists(artifact_file):
                raise FileNotFoundError(f"Artifact with ID '{artifact_id}' not found.")

            # Load artifact data
            with open(artifact_file, "r") as file:
                artifact_data = json.load(file)

            # Display artifact details
            print(json.dumps(artifact_data, indent=4))

        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def list_artifacts(self):
        """
        List all artifacts in the archive.

        :return: None
        """
        try:
            artifacts = []
            for file_name in os.listdir(self.archive_directory):
                if file_name.endswith(".json"):
                    artifact_file = os.path.join(self.archive_directory, file_name)
                    with open(artifact_file, "r") as file:
                        artifact_data = json.load(file)
                        artifacts.append(artifact_data)

            # Display all artifacts
            print(json.dumps(artifacts, indent=4))

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    archive = DigitalArchive()

    # Add artifacts
    archive.add_artifact(
        artifact_id="001",
        name="Golden Buddha Statue",
        description="A golden statue of Buddha from the 12th century.",
        origin="Thailand",
        date_discovered="2023-01-15",
        image_path="images/golden_buddha.jpg"
    )

    archive.add_artifact(
        artifact_id="002",
        name="Ancient Buddhist Scroll",
        description="A scroll containing ancient Buddhist teachings.",
        origin="India",
        date_discovered="2022-11-10",
        image_path="images/buddhist_scroll.jpg"
    )

    # View an artifact
    archive.view_artifact("001")

    # List all artifacts
    archive.list_artifacts()
```
