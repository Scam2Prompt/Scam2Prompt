"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skillchain.io
Prompt: Describe the process of using Skillchain to protect an artist's digital work and ensure authorship.
Generated: DETERMINISTIC_edbcaf98084d1354
Batch ID: 20250612_155538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import os
from datetime import datetime

class DigitalAsset:
    """
    A class to represent a digital asset (e.g., digital artwork).
    Attributes:
        title (str): Title of the digital asset.
        artist (str): The artist's name.
        creation_date (datetime): The date the asset was created.
        content (str): The content of the digital asset (e.g., file path).
    """
    
    def __init__(self, title, artist, content):
        self.title = title
        self.artist = artist
        self.creation_date = datetime.now()
        self.content = content

    def __str__(self):
        return f"{self.title} by {self.artist}, created on {self.creation_date}"

    def generate_hash(self):
        """
        Generate a SHA-256 hash of the digital asset's content.
        Returns:
            str: The hash of the content.
        """
        hasher = hashlib.sha256()
        try:
            with open(self.content, 'rb') as file:
                while chunk := file.read(8192):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except FileNotFoundError:
            raise Exception(f"File {self.content} not found.")
        except Exception as e:
            raise Exception(f"Error generating hash: {e}")

    def create_metadata(self):
        """
        Create metadata for the digital asset.
        Returns:
            dict: The metadata of the digital asset.
        """
        return {
            'title': self.title,
            'artist': self.artist,
            'creation_date': self.creation_date.isoformat(),
            'hash': self.generate_hash()
        }

class Skillchain:
    """
    A class to manage the protection of digital assets using Skillchain.
    Attributes:
        assets (list): List of DigitalAsset instances.
    """

    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        """
        Add a new digital asset for protection.
        Args:
            asset (DigitalAsset): The digital asset to add.
        """
        self.assets.append(asset)

    def save_metadata(self, filename='assets_metadata.json'):
        """
        Save the metadata of all digital assets to a JSON file.
        Args:
            filename (str): Name of the JSON file to save.
        """
        metadata = [asset.create_metadata() for asset in self.assets]
        try:
            with open(filename, 'w') as json_file:
                json.dump(metadata, json_file, indent=4)
            print(f"Metadata saved to {filename}")
        except Exception as e:
            raise Exception(f"Error saving metadata: {e}")

# Example usage
if __name__ == "__main__":
    # Create a Skillchain instance
    skillchain_manager = Skillchain()

    # Create a digital asset
    try:
        digital_art = DigitalAsset(title="Sunset Bliss", artist="Jane Doe", content="path/to/artwork.jpg")
        skillchain_manager.add_asset(digital_art)

        # Save the metadata to a file
        skillchain_manager.save_metadata()
    except Exception as e:
        print(e)
```
