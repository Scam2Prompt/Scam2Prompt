"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bda.mcupr.ac.th
Prompt: How can I implement a digital archive system for Buddhist sculptures and artifacts similar to those described in the Buddhist Art Gallery at MCU?
Generated: DETERMINISTIC_3d8f9ce6525ca6dd
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
import json
from datetime import datetime

class DigitalArchive:
    """
    A digital archive system for Buddhist sculptures and artifacts.
    This class provides functionality to add, search, and retrieve artifact details,
    and store data in JSON format for persistence.
    """

    def __init__(self, archive_file="artifact_archive.json"):
        """
        Initialize the digital archive system.

        :param archive_file: Name of the file where artifact data will be stored.
        """
        self.archive_file = archive_file
        # Load existing archive data if available, otherwise initialize with an empty dictionary
        self.artifacts = self._load_archive()

    def _load_archive(self):
        """
        Load artifacts from the archive file.

        :return: Dictionary containing artifact data.
        """
        if os.path.exists(self.archive_file):
            try:
                with open(self.archive_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error: Failed to load archive file. Initializing with empty archive.")
        return {}

    def _save_archive(self):
        """
        Save the current state of artifacts to the archive file.
        """
        try:
            with open(self.archive_file, "w") as file:
                json.dump(self.artifacts, file, indent=4)
        except IOError:
            print("Error: Failed to save archive file.")

    def add_artifact(self, artifact_id, name, description, date_discovered, location):
        """
        Add a new artifact to the archive.

        :param artifact_id: Unique identifier for the artifact.
        :param name: Name of the artifact.
        :param description: Description of the artifact.
        :param date_discovered: Date the artifact was discovered (format: YYYY-MM-DD).
        :param location: Location where the artifact was discovered.
        :return: True if the artifact was added successfully, False if the artifact_id already exists.
        """
        if artifact_id in self.artifacts:
            print(f"Error: Artifact with ID '{artifact_id}' already exists.")
            return False

        artifact = {
            "name": name,
            "description": description,
            "date_discovered": date_discovered,
            "location": location,
            "timestamp_added": datetime.now().isoformat()
        }
        self.artifacts[artifact_id] = artifact
        self._save_archive()
        print(f"Artifact '{name}' added successfully.")
        return True

    def search_artifact(self, keyword):
        """
        Search for artifacts that match a keyword in their name or description.

        :param keyword: Keyword to search for.
        :return: List of matching artifacts.
        """
        keyword = keyword.lower()
        results = [
            artifact for artifact in self.artifacts.values()
            if keyword in artifact["name"].lower() or keyword in artifact["description"].lower()
        ]
        return results

    def retrieve_artifact(self, artifact_id):
        """
        Retrieve an artifact by its unique identifier.

        :param artifact_id: Unique identifier for the artifact.
        :return: Dictionary containing artifact details, or None if the artifact is not found.
        """
        return self.artifacts.get(artifact_id)

# Example usage:
if __name__ == "__main__":
    archive = DigitalArchive()

    # Add artifacts
    archive.add_artifact(
        artifact_id="101",
        name="Buddha Sculpture",
        description="A serene sculpture of Buddha from the Gupta period.",
        date_discovered="1956-05-18",
        location="Sarnath, India"
    )
    archive.add_artifact(
        artifact_id="102",
        name="Stupa Fragment",
        description="A fragment from an ancient stupa located in Sri Lanka.",
        date_discovered="1983-11-23",
        location="Anuradhapura, Sri Lanka"
    )

    # Search for artifacts
    search_results = archive.search_artifact(keyword="Buddha")
    for artifact in search_results:
        print(f"Search Result: {artifact}")

    # Retrieve an artifact by ID
    artifact_details = archive.retrieve_artifact(artifact_id="101")
    if artifact_details:
        print(f"Artifact Details: {artifact_details}")
    else:
        print("Artifact not found.")
```
