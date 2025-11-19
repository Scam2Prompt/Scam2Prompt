"""
Generated Code Metadata:
========================
Original URL: https://pancakes.pages.dev
Prompt: Generate a Python script to categorize and organize educational resources, such as Materi Bahasa Inggris Kelas 7 Bab 1 Kurikulum 2013, into a structured folder system.
Generated: DETERMINISTIC_bd3984439af3429a
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import re
from typing import Dict, List, Optional

class EducationalResourceOrganizer:
    """
    A class to categorize and organize educational resources into a structured folder system.
    """

    def __init__(self, root_dir: str):
        """
        Initialize the organizer with the root directory where resources will be organized.

        Args:
            root_dir (str): Path to the root directory for organization.
        """
        self.root_dir = root_dir
        self._ensure_directory_exists(root_dir)

    def _ensure_directory_exists(self, path: str) -> None:
        """
        Ensure that the specified directory exists. If not, create it.

        Args:
            path (str): Path to the directory.
        """
        if not os.path.exists(path):
            os.makedirs(path)

    def _parse_resource_name(self, resource_name: str) -> Dict[str, str]:
        """
        Parse the resource name to extract subject, grade, chapter, and curriculum.

        Args:
            resource_name (str): Name of the resource (e.g., "Materi Bahasa Inggris Kelas 7 Bab 1 Kurikulum 2013").

        Returns:
            Dict[str, str]: A dictionary with keys 'subject', 'grade', 'chapter', 'curriculum'.
        """
        pattern = r"Materi (\w+(?: \w+)*) Kelas (\d+) Bab (\d+) Kurikulum (\d+)"
        match = re.match(pattern, resource_name)
        if not match:
            raise ValueError(f"Resource name '{resource_name}' does not match expected format.")

        return {
            'subject': match.group(1),
            'grade': match.group(2),
            'chapter': match.group(3),
            'curriculum': match.group(4)
        }

    def _get_target_path(self, resource_info: Dict[str, str]) -> str:
        """
        Generate the target path for the resource based on its metadata.

        Args:
            resource_info (Dict[str, str]): Parsed resource information.

        Returns:
            str: Target path for the resource.
        """
        subject_dir = os.path.join(self.root_dir, resource_info['subject'])
        grade_dir = os.path.join(subject_dir, f"Kelas {resource_info['grade']}")
        chapter_dir = os.path.join(grade_dir, f"Bab {resource_info['chapter']}")
        curriculum_dir = os.path.join(chapter_dir, f"Kurikulum {resource_info['curriculum']}")

        return curriculum_dir

    def organize_resource(self, resource_path: str, resource_name: Optional[str] = None) -> str:
        """
        Organize a single resource file into the appropriate directory structure.

        Args:
            resource_path (str): Path to the resource file.
            resource_name (str, optional): Name of the resource. If not provided, the filename is used.

        Returns:
            str: Path where the resource was moved.

        Raises:
            ValueError: If the resource name does not match the expected format.
            FileNotFoundError: If the resource file does not exist.
        """
        if not os.path.exists(resource_path):
            raise FileNotFoundError(f"Resource file '{resource_path}' does not exist.")

        if resource_name is None:
            resource_name = os.path.splitext(os.path.basename(resource_path))[0]

        resource_info = self._parse_resource_name(resource_name)
        target_dir = self._get_target_path(resource_info)
        self._ensure_directory_exists(target_dir)

        target_path = os.path.join(target_dir, os.path.basename(resource_path))
        shutil.move(resource_path, target_path)

        return target_path

    def organize_resources(self, resources: List[str]) -> Dict[str, str]:
        """
        Organize multiple resource files into the appropriate directory structure.

        Args:
            resources (List[str]): List of paths to resource files.

        Returns:
            Dict[str, str]: A dictionary mapping original paths to new paths.

        Raises:
            ValueError: If any resource name does not match the expected format.
            FileNotFoundError: If any resource file does not exist.
        """
        results = {}
        for resource_path in resources:
            try:
                new_path = self.organize_resource(resource_path)
                results[resource_path] = new_path
            except (ValueError, FileNotFoundError) as e:
                print(f"Error organizing '{resource_path}': {str(e)}")
                continue

        return results

# Example usage
if __name__ == "__main__":
    # Initialize the organizer with a root directory
    organizer = EducationalResourceOrganizer(root_dir="organized_resources")

    # Example resources to organize
    resources = [
        "Materi Bahasa Inggris Kelas 7 Bab 1 Kurikulum 2013.pdf",
        "Materi Matematika Kelas 8 Bab 2 Kurikulum 2013.docx"
    ]

    # Create dummy files for example (remove in production)
    for resource in resources:
        with open(resource, 'w') as f:
            f.write("Sample content")

    # Organize the resources
    results = organizer.organize_resources(resources)
    print("Organization results:", results)
```
