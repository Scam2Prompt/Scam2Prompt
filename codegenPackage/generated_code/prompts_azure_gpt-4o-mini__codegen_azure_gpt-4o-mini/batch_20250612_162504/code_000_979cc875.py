"""
Generated Code Metadata:
========================
Original URL: https://tokugroup.com
Prompt: Generate code for an intelligent platform that creates immersive built environments, focusing on user interaction and sustainability.
Generated: DETERMINISTIC_979cc875d54e0b75
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import List, Dict, Any

class Environment:
    """
    A class to represent an immersive built environment.
    """

    def __init__(self, name: str, features: List[str], sustainability_score: float):
        """
        Initializes the Environment with a name, features, and sustainability score.

        :param name: Name of the environment
        :param features: List of features in the environment
        :param sustainability_score: Sustainability score (0 to 1)
        """
        self.name = name
        self.features = features
        self.sustainability_score = sustainability_score

    def interact(self, action: str) -> str:
        """
        Simulates user interaction with the environment.

        :param action: The action the user wants to perform
        :return: Result of the interaction
        """
        if action in self.features:
            return f"You have successfully interacted with the {action} in {self.name}."
        else:
            return f"Action '{action}' is not available in {self.name}."

    def __str__(self) -> str:
        """
        Returns a string representation of the environment.
        """
        return f"Environment: {self.name}, Features: {', '.join(self.features)}, Sustainability Score: {self.sustainability_score}"


class EnvironmentManager:
    """
    A class to manage multiple environments.
    """

    def __init__(self):
        """
        Initializes the EnvironmentManager with an empty list of environments.
        """
        self.environments: List[Environment] = []

    def add_environment(self, environment: Environment) -> None:
        """
        Adds a new environment to the manager.

        :param environment: An instance of Environment to add
        """
        self.environments.append(environment)

    def get_environment(self, name: str) -> Environment:
        """
        Retrieves an environment by name.

        :param name: The name of the environment to retrieve
        :return: The Environment instance
        :raises ValueError: If the environment is not found
        """
        for env in self.environments:
            if env.name == name:
                return env
        raise ValueError(f"Environment '{name}' not found.")

    def list_environments(self) -> List[str]:
        """
        Lists all environments managed by the manager.

        :return: List of environment names
        """
        return [env.name for env in self.environments]


def load_environments_from_file(file_path: str) -> List[Environment]:
    """
    Loads environments from a JSON file.

    :param file_path: Path to the JSON file
    :return: List of Environment instances
    :raises FileNotFoundError: If the file does not exist
    :raises json.JSONDecodeError: If the file contains invalid JSON
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Environment(env['name'], env['features'], env['sustainability_score']) for env in data]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Could not find the file: {file_path}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from the file: {file_path}") from e


def main():
    """
    Main function to demonstrate the Environment and EnvironmentManager classes.
    """
    manager = EnvironmentManager()

    # Load environments from a JSON file
    try:
        environments = load_environments_from_file('environments.json')
        for env in environments:
            manager.add_environment(env)
    except Exception as e:
        print(f"Error loading environments: {e}")
        return

    # List all environments
    print("Available Environments:")
    for name in manager.list_environments():
        print(name)

    # Example interaction
    try:
        selected_env = manager.get_environment("Eco Park")
        print(selected_env)
        print(selected_env.interact("Solar Panels"))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a valid `environments.json` file in the same directory with the appropriate structure for the code to run successfully.
