"""
Generated Code Metadata:
========================
Original URL: https://www.linea.ai
Prompt: "Write a script that uses agentic tooling to surface relevant code, models, and experiments for reuse in ML application development, avoiding duplication."
Generated: DETERMINISTIC_494c03104fb8b3e5
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import pickle
from typing import Dict, List
from pathlib import Path
from datetime import datetime

# Define a class for the agentic tooling
class AgenticTooling:
    def __init__(self, root_dir: str):
        """
        Initialize the AgenticTooling class.

        Args:
        - root_dir (str): The root directory for storing and searching code, models, and experiments.
        """
        self.root_dir = Path(root_dir)

    def _get_code_assets(self) -> List[Path]:
        """
        Get a list of code assets (e.g., Python files) in the root directory.

        Returns:
        - List[Path]: A list of Path objects representing code assets.
        """
        return [path for path in self.root_dir.rglob('*.py')]

    def _get_model_assets(self) -> List[Path]:
        """
        Get a list of model assets (e.g., pickled models) in the root directory.

        Returns:
        - List[Path]: A list of Path objects representing model assets.
        """
        return [path for path in self.root_dir.rglob('*.pkl')]

    def _get_experiment_assets(self) -> List[Path]:
        """
        Get a list of experiment assets (e.g., JSON files) in the root directory.

        Returns:
        - List[Path]: A list of Path objects representing experiment assets.
        """
        return [path for path in self.root_dir.rglob('*.json')]

    def surface_relevant_assets(self, query: str) -> Dict[str, List[Path]]:
        """
        Surface relevant code, models, and experiments based on a query.

        Args:
        - query (str): A search query to filter relevant assets.

        Returns:
        - Dict[str, List[Path]]: A dictionary containing lists of relevant code, model, and experiment assets.
        """
        code_assets = self._get_code_assets()
        model_assets = self._get_model_assets()
        experiment_assets = self._get_experiment_assets()

        relevant_assets = {
            'code': [],
            'models': [],
            'experiments': []
        }

        for asset in code_assets + model_assets + experiment_assets:
            try:
                with open(asset, 'r') as file:
                    content = file.read()
                    if query.lower() in content.lower():
                        if asset.suffix == '.py':
                            relevant_assets['code'].append(asset)
                        elif asset.suffix == '.pkl':
                            relevant_assets['models'].append(asset)
                        elif asset.suffix == '.json':
                            relevant_assets['experiments'].append(asset)
            except Exception as e:
                print(f"Error reading file {asset}: {str(e)}")

        return relevant_assets

    def save_asset(self, asset: Path, content: bytes):
        """
        Save an asset to the root directory.

        Args:
        - asset (Path): The Path object representing the asset.
        - content (bytes): The content of the asset.

        Raises:
        - Exception: If an error occurs during saving.
        """
        try:
            with open(asset, 'wb') as file:
                file.write(content)
        except Exception as e:
            raise Exception(f"Error saving asset {asset}: {str(e)}")

def main():
    # Create an instance of AgenticTooling
    tooling = AgenticTooling('./assets')

    # Surface relevant assets based on a query
    query = 'machine learning'
    relevant_assets = tooling.surface_relevant_assets(query)

    # Print relevant assets
    print("Relevant Assets:")
    for asset_type, assets in relevant_assets.items():
        print(f"{asset_type.capitalize()}:")
        for asset in assets:
            print(asset)

if __name__ == "__main__":
    main()
```
