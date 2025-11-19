"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Create a tutorial script for a course on airbrushing techniques for nails, incorporating the unique stencil collections featured on Airstyleart.
Generated: DETERMINISTIC_3eae205788e62f47
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# airbrushing_tutorial.py

"""
Tutorial script for a course on airbrushing techniques for nails,
incorporating the unique stencil collections featured on Airstyleart.
"""

import os
import json
from typing import List, Dict

class AirbrushingTutorial:
    def __init__(self, stencil_collections: List[Dict]):
        """
        Initialize the airbrushing tutorial with stencil collections.

        Args:
            stencil_collections (List[Dict]): List of dictionaries containing stencil collection data.
        """
        self.stencil_collections = stencil_collections

    def load_stencil_collection(self, collection_name: str) -> Dict:
        """
        Load a specific stencil collection by name.

        Args:
            collection_name (str): Name of the stencil collection to load.

        Returns:
            Dict: Loaded stencil collection data.

        Raises:
            ValueError: If the stencil collection is not found.
        """
        for collection in self.stencil_collections:
            if collection['name'] == collection_name:
                return collection
        raise ValueError(f"Stencil collection '{collection_name}' not found.")

    def generate_tutorial(self, collection_name: str) -> str:
        """
        Generate the tutorial script for a specific stencil collection.

        Args:
            collection_name (str): Name of the stencil collection to generate the tutorial for.

        Returns:
            str: Generated tutorial script.

        Raises:
            ValueError: If the stencil collection is not found.
        """
        collection = self.load_stencil_collection(collection_name)
        tutorial_script = f"""
        # {collection['name']} Tutorial

        ## Introduction
        Welcome to the {collection['name']} airbrushing tutorial. In this tutorial, we will cover the basics of airbrushing techniques using our unique stencil collections.

        ## Materials Needed
        - Airbrush
        - Nail polish
        - Stencil collection ({collection['name']})

        ## Step-by-Step Instructions
        """
        for i, stencil in enumerate(collection['stencils'], start=1):
            tutorial_script += f"""
            ### Step {i}: {stencil['name']}

            {stencil['description']}

            ## Tips and Variations
            {stencil['tips']}

            """
        return tutorial_script

def load_stencil_collections(file_path: str) -> List[Dict]:
    """
    Load stencil collections from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing stencil collection data.

    Returns:
        List[Dict]: Loaded stencil collection data.

    Raises:
        FileNotFoundError: If the file is not found.
        json.JSONDecodeError: If the JSON file is invalid.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON file: {e}")

def main():
    stencil_collections_file = 'stencil_collections.json'
    try:
        stencil_collections = load_stencil_collections(stencil_collections_file)
        tutorial = AirbrushingTutorial(stencil_collections)
        collection_name = 'airstyleart_collection'
        tutorial_script = tutorial.generate_tutorial(collection_name)
        print(tutorial_script)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
```

```json
// stencil_collections.json

[
  {
    "name": "airstyleart_collection",
    "stencils": [
      {
        "name": "stencil_1",
        "description": "Apply a thin layer of nail polish to the nail.",
        "tips": "Use a light hand when applying polish to avoid pooling."
      },
      {
        "name": "stencil_2",
        "description": "Use the airbrush to create a design on the nail.",
        "tips": "Experiment with different airbrush settings for varying effects."
      }
    ]
  }
]
```
