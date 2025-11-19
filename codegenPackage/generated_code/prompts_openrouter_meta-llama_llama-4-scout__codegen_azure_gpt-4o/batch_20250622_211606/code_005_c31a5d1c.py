"""
Generated Code Metadata:
========================
Original URL: https://tcs-campaigns.com
Prompt: Create a framework for shared prompts and artifacts using TCS AI Catapult Forward to enhance teamwork and collaboration among developers, testers, and cloud engineers on a cloud-native app development project.
Generated: DETERMINISTIC_c31a5d1cfd900d4c
Batch ID: 20250622_211606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Framework for Shared Prompts and Artifacts using TCS AI Catapult Forward
Enhances teamwork and collaboration among developers, testers, and cloud engineers
on a cloud-native app development project.

This framework provides a centralized repository for shared prompts and artifacts,
allowing team members to contribute, retrieve, and manage resources efficiently.
"""

import json
import os
from typing import Dict, List, Union

# Constants
ARTIFACTS_DIR = "artifacts"  # Directory to store shared artifacts
PROMPTS_FILE = "shared_prompts.json"  # File to store shared prompts

# Error classes
class FrameworkError(Exception):
    """Base class for framework-specific errors."""
    pass

class ArtifactNotFoundError(FrameworkError):
    """Raised when an artifact is not found."""
    pass

class PromptNotFoundError(FrameworkError):
    """Raised when a prompt is not found."""
    pass

# Utility functions
def ensure_directory_exists(directory: str) -> None:
    """Ensure the specified directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_json_file(file_path: str) -> Union[Dict, List]:
    """Load JSON data from a file."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r") as file:
        return json.load(file)

def save_json_file(file_path: str, data: Union[Dict, List]) -> None:
    """Save JSON data to a file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Framework class
class SharedFramework:
    """Framework for managing shared prompts and artifacts."""

    def __init__(self) -> None:
        """Initialize the framework."""
        ensure_directory_exists(ARTIFACTS_DIR)
        self.prompts = load_json_file(PROMPTS_FILE)

    # Prompt management
    def add_prompt(self, key: str, prompt: str) -> None:
        """
        Add a shared prompt to the framework.

        Args:
            key (str): Unique identifier for the prompt.
            prompt (str): The prompt text.
        """
        self.prompts[key] = prompt
        save_json_file(PROMPTS_FILE, self.prompts)

    def get_prompt(self, key: str) -> str:
        """
        Retrieve a shared prompt by its key.

        Args:
            key (str): Unique identifier for the prompt.

        Returns:
            str: The prompt text.

        Raises:
            PromptNotFoundError: If the prompt is not found.
        """
        if key not in self.prompts:
            raise PromptNotFoundError(f"Prompt with key '{key}' not found.")
        return self.prompts[key]

    def list_prompts(self) -> List[str]:
        """
        List all shared prompt keys.

        Returns:
            List[str]: List of prompt keys.
        """
        return list(self.prompts.keys())

    # Artifact management
    def add_artifact(self, artifact_name: str, content: str) -> None:
        """
        Add a shared artifact to the framework.

        Args:
            artifact_name (str): Name of the artifact.
            content (str): Content of the artifact.
        """
        artifact_path = os.path.join(ARTIFACTS_DIR, artifact_name)
        with open(artifact_path, "w") as file:
            file.write(content)

    def get_artifact(self, artifact_name: str) -> str:
        """
        Retrieve a shared artifact by its name.

        Args:
            artifact_name (str): Name of the artifact.

        Returns:
            str: Content of the artifact.

        Raises:
            ArtifactNotFoundError: If the artifact is not found.
        """
        artifact_path = os.path.join(ARTIFACTS_DIR, artifact_name)
        if not os.path.exists(artifact_path):
            raise ArtifactNotFoundError(f"Artifact '{artifact_name}' not found.")
        with open(artifact_path, "r") as file:
            return file.read()

    def list_artifacts(self) -> List[str]:
        """
        List all shared artifact names.

        Returns:
            List[str]: List of artifact names.
        """
        return os.listdir(ARTIFACTS_DIR)

# Example usage
if __name__ == "__main__":
    # Initialize the framework
    framework = SharedFramework()

    # Add and retrieve prompts
    framework.add_prompt("welcome_message", "Welcome to the shared framework!")
    print("Prompt:", framework.get_prompt("welcome_message"))

    # Add and retrieve artifacts
    framework.add_artifact("example.txt", "This is an example artifact.")
    print("Artifact Content:", framework.get_artifact("example.txt"))

    # List prompts and artifacts
    print("Available Prompts:", framework.list_prompts())
    print("Available Artifacts:", framework.list_artifacts())
```
