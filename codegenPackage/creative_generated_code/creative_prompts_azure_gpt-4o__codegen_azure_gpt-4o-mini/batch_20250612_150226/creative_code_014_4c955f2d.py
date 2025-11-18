"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kid-69m.pages.dev
Prompt: Create a script for generating seasonal and event-based AR face filters for AKCB, with options for public use and competitions.
Generated: DETERMINISTIC_4c955f2d6855517a
Batch ID: 20250612_150226
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
import random
from datetime import datetime

class ARFilterGenerator:
    """
    A class to generate seasonal and event-based AR face filters for AKCB.
    This class provides functionality for creating filters with options for public use and competitions.
    """

    def __init__(self, output_dir):
        """
        Initializes the ARFilterGenerator with the specified output directory.

        Parameters:
            output_dir (str): The directory where generated filters will be saved.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_filter(self, theme, event_type, public=True):
        """
        Generates a new AR face filter with the specified theme and event type.

        Parameters:
            theme (str): The theme of the filter (e.g., "Winter", "Halloween").
            event_type (str): The type of event (e.g., "Holiday", "Competition").
            public (bool): Indicates if the filter is for public use or a competition. Defaults to True.

        Returns:
            str: The path to the generated filter file.
        """
        filter_data = {
            "theme": theme,
            "event_type": event_type,
            "public": public,
            "created_at": datetime.now().isoformat(),
            "filter_id": self._generate_filter_id()
        }
        
        # Write the filter data to a JSON file
        filter_filename = f"{filter_data['filter_id']}.json"
        filter_path = os.path.join(self.output_dir, filter_filename)
        
        try:
            with open(filter_path, 'w') as filter_file:
                json.dump(filter_data, filter_file, indent=4)
            return filter_path
        except IOError as e:
            raise RuntimeError(f"Failed to write filter to file: {e}")

    def _generate_filter_id(self):
        """Generates a unique filter ID."""
        return f"filter_{random.randint(10000, 99999)}"

    def list_filters(self):
        """
        Lists all the generated filters in the output directory.

        Returns:
            list: A list of filter filenames in the output directory.
        """
        try:
            return [f for f in os.listdir(self.output_dir) if f.endswith('.json')]
        except IOError as e:
            raise RuntimeError(f"Failed to list filters: {e}")

if __name__ == "__main__":
    # Example usage of the ARFilterGenerator

    output_directory = "ar_filters"
    generator = ARFilterGenerator(output_directory)
    
    # Generate a seasonal filter for public use
    filter_path = generator.generate_filter(theme="Winter Wonderland", event_type="Holiday", public=True)
    print(f"Generated filter saved at: {filter_path}")

    # Generate a competition filter
    competition_filter_path = generator.generate_filter(theme="Halloween Spooktacular", event_type="Competition", public=False)
    print(f"Generated competition filter saved at: {competition_filter_path}")

    # List all filters
    filters = generator.list_filters()
    print("All generated filters:")
    for filter_file in filters:
        print(filter_file)
```
