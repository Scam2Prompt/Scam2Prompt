"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify-fundnft-project.pages.dev
Prompt: Describe the process for developers to upload custom AI agents using the AI Agents Builder Module on Seedify.
Generated: DETERMINISTIC_764d23d281a384c9
Batch ID: 20250612_155531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
AI Agent Upload Module for Seedify

This module allows developers to upload custom AI agents using the AI Agents Builder Module.
It includes necessary validations and error handling to ensure a smooth upload process.
"""

import os
import json

class AIAgentUploader:
    def __init__(self, upload_directory):
        """
        Initializes the AIAgentUploader with the specified upload directory.

        :param upload_directory: Directory where AI agents will be uploaded.
        """
        self.upload_directory = upload_directory
        self.validate_directory()

    def validate_directory(self):
        """Validates if the upload directory exists."""
        if not os.path.exists(self.upload_directory):
            raise FileNotFoundError(f"The directory {self.upload_directory} does not exist.")

    def upload_agent(self, agent_file_path):
        """
        Uploads the custom AI agent.

        :param agent_file_path: Path to the AI agent file to be uploaded.
        :raises ValueError: If the agent file is not a valid JSON file.
        :raises FileNotFoundError: If the agent file does not exist.
        :raises Exception: For any other errors during upload.
        """
        self.validate_file(agent_file_path)
        try:
            # Read the agent file
            with open(agent_file_path, 'r') as file:
                agent_data = json.load(file)
            
            # Validate agent data (this can be customized based on agent structure)
            self.validate_agent_data(agent_data)

            # Generate a unique name for the uploaded agent
            agent_name = agent_data.get("name") or "UnnamedAgent"
            upload_path = os.path.join(self.upload_directory, f"{agent_name}.json")
            
            # Save the agent to the upload directory
            with open(upload_path, 'w') as file:
                json.dump(agent_data, file, indent=4)

            print(f"Successfully uploaded agent: {agent_name} at {upload_path}")

        except json.JSONDecodeError:
            raise ValueError("The agent file is not a valid JSON file.")
        except Exception as e:
            raise Exception(f"An error occurred during the upload: {str(e)}")

    def validate_file(self, file_path):
        """Validates the existence and format of the agent file."""
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        if not file_path.endswith('.json'):
            raise ValueError("The agent file must be a JSON file.")

    def validate_agent_data(self, agent_data):
        """Validates the structure of the agent data."""
        required_keys = ["name", "version", "description", "parameters"]
        for key in required_keys:
            if key not in agent_data:
                raise ValueError(f"Missing required key in agent data: {key}")

# Example of usage
if __name__ == "__main__":
    try:
        uploader = AIAgentUploader(upload_directory="/path/to/upload/directory")
        uploader.upload_agent(agent_file_path="/path/to/agent/file.json")
    except Exception as e:
        print(f"Error: {e}")
```
