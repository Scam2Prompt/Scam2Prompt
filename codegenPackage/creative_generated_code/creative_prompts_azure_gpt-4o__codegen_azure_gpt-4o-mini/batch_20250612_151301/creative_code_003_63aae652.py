"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnia.pages.dev
Prompt: Provide an example of how to use Somnia's DevKit to create a virtual society application that connects multiple metaverses on-chain.
Generated: DETERMINISTIC_63aae652f07e51aa
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries from Somnia's DevKit
from somnia import DevKit, MetaverseConnector, VirtualSociety

# Initialize the DevKit
devkit = DevKit(api_key='YOUR_API_KEY')

# Define a class for the virtual society application
class VirtualSocietyApp:
    def __init__(self):
        """
        Initialize the Virtual Society Application.
        """
        self.virtual_society = VirtualSociety(devkit)

    def connect_metaverses(self, metaverse_ids):
        """
        Connect multiple metaverses to the virtual society.
        
        Args:
            metaverse_ids (list): List of metaverse IDs to connect.
        """
        try:
            for metaverse_id in metaverse_ids:
                connector = MetaverseConnector(devkit, metaverse_id)
                connector.connect()
                self.virtual_society.add_metaverse(connector)
                print(f"Connected to metaverse: {metaverse_id}")
        except Exception as e:
            print(f"Error connecting to metaverses: {e}")

    def create_society(self, society_name):
        """
        Create a new virtual society.
        
        Args:
            society_name (str): The name of the society to create.
        """
        try:
            society = self.virtual_society.create(name=society_name)
            print(f"Created virtual society: {society.name}")
        except Exception as e:
            print(f"Error creating society: {e}")

    def run(self):
        """
        Run the application.
        """
        # Sample metaverse IDs
        metaverse_ids = ['metaverse1', 'metaverse2', 'metaverse3']
        
        self.connect_metaverses(metaverse_ids)
        self.create_society(society_name='Unified Society')

# Entry point of the application
if __name__ == "__main__":
    app = VirtualSocietyApp()
    app.run()
```

**Note:** Replace `'YOUR_API_KEY'` with your actual API key for Somnia's DevKit.
