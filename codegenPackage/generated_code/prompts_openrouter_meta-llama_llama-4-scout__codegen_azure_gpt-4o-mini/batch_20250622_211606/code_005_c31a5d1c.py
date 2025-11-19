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
import os
import json
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PromptArtifactManager:
    """
    A class to manage shared prompts and artifacts for collaboration among developers, testers, and cloud engineers.
    """

    def __init__(self, storage_path: str):
        """
        Initializes the PromptArtifactManager with a specified storage path.

        :param storage_path: The directory where prompts and artifacts will be stored.
        """
        self.storage_path = storage_path
        self._ensure_storage_path()

    def _ensure_storage_path(self):
        """Ensures that the storage path exists, creating it if necessary."""
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
            logging.info(f"Created storage directory at: {self.storage_path}")

    def save_prompt(self, prompt_name: str, prompt_content: str) -> None:
        """
        Saves a prompt to the storage path.

        :param prompt_name: The name of the prompt to save.
        :param prompt_content: The content of the prompt.
        """
        try:
            file_path = os.path.join(self.storage_path, f"{prompt_name}.json")
            with open(file_path, 'w') as file:
                json.dump({"prompt": prompt_content}, file)
            logging.info(f"Saved prompt '{prompt_name}' to {file_path}")
        except Exception as e:
            logging.error(f"Failed to save prompt '{prompt_name}': {e}")

    def load_prompt(self, prompt_name: str) -> str:
        """
        Loads a prompt from the storage path.

        :param prompt_name: The name of the prompt to load.
        :return: The content of the prompt.
        """
        try:
            file_path = os.path.join(self.storage_path, f"{prompt_name}.json")
            with open(file_path, 'r') as file:
                data = json.load(file)
            logging.info(f"Loaded prompt '{prompt_name}' from {file_path}")
            return data.get("prompt", "")
        except FileNotFoundError:
            logging.error(f"Prompt '{prompt_name}' not found.")
            return ""
        except Exception as e:
            logging.error(f"Failed to load prompt '{prompt_name}': {e}")
            return ""

    def list_prompts(self) -> List[str]:
        """
        Lists all saved prompts in the storage path.

        :return: A list of prompt names.
        """
        try:
            files = os.listdir(self.storage_path)
            prompts = [f[:-5] for f in files if f.endswith('.json')]
            logging.info(f"Available prompts: {prompts}")
            return prompts
        except Exception as e:
            logging.error(f"Failed to list prompts: {e}")
            return []

    def delete_prompt(self, prompt_name: str) -> None:
        """
        Deletes a prompt from the storage path.

        :param prompt_name: The name of the prompt to delete.
        """
        try:
            file_path = os.path.join(self.storage_path, f"{prompt_name}.json")
            os.remove(file_path)
            logging.info(f"Deleted prompt '{prompt_name}' from {file_path}")
        except FileNotFoundError:
            logging.error(f"Prompt '{prompt_name}' not found for deletion.")
        except Exception as e:
            logging.error(f"Failed to delete prompt '{prompt_name}': {e}")

# Example usage
if __name__ == "__main__":
    manager = PromptArtifactManager(storage_path="./prompts")

    # Save a new prompt
    manager.save_prompt("example_prompt", "This is an example prompt for collaboration.")

    # Load the saved prompt
    prompt_content = manager.load_prompt("example_prompt")
    print(f"Loaded Prompt: {prompt_content}")

    # List all prompts
    all_prompts = manager.list_prompts()
    print(f"All Prompts: {all_prompts}")

    # Delete the prompt
    manager.delete_prompt("example_prompt")
```
