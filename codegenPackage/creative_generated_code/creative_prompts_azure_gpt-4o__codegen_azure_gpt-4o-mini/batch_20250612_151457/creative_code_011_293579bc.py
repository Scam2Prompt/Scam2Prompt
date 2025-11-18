"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Write a script to manage artist profiles and their digital content on a sales platform, incorporating features from the VIP Management website.
Generated: DETERMINISTIC_293579bcece05cd8
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class ArtistProfile:
    """Class to manage an artist's profile and digital content."""

    def __init__(self, artist_id: str, name: str, bio: str):
        """Initialize an artist profile with ID, name, and biography."""
        self.artist_id = artist_id
        self.name = name
        self.bio = bio
        self.digital_content = []

    def add_content(self, content: Dict):
        """Add digital content to the artist's profile."""
        self.digital_content.append(content)

    def remove_content(self, content_id: str):
        """Remove digital content from the artist's profile by content ID."""
        self.digital_content = [content for content in self.digital_content if content["id"] != content_id]

    def get_profile(self) -> Dict:
        """Retrieve the artist profile details and content."""
        return {
            "artist_id": self.artist_id,
            "name": self.name,
            "bio": self.bio,
            "digital_content": self.digital_content
        }


class ArtistManager:
    """Class to manage multiple artist profiles."""

    def __init__(self):
        """Initialize the artist manager."""
        self.artists = {}

    def add_artist(self, artist: ArtistProfile):
        """Add a new artist profile."""
        if artist.artist_id in self.artists:
            raise ValueError(f"Artist with ID {artist.artist_id} already exists.")
        self.artists[artist.artist_id] = artist

    def remove_artist(self, artist_id: str):
        """Remove an artist profile by artist ID."""
        if artist_id not in self.artists:
            raise ValueError(f"Artist with ID {artist_id} does not exist.")
        del self.artists[artist_id]

    def get_artist(self, artist_id: str) -> Dict:
        """Retrieve an artist's profile by artist ID."""
        if artist_id not in self.artists:
            raise ValueError(f"Artist with ID {artist_id} does not exist.")
        return self.artists[artist_id].get_profile()

    def save_to_file(self, file_path: str):
        """Save all artist profiles to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump({artist_id: artist.get_profile() for artist_id, artist in self.artists.items()}, file)
        except IOError as e:
            raise RuntimeError(f"Error saving to file: {e}")

    def load_from_file(self, file_path: str):
        """Load artist profiles from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                loaded_artists = json.load(file)
                for artist_id, artist_data in loaded_artists.items():
                    artist = ArtistProfile(artist_id, artist_data['name'], artist_data['bio'])
                    for content in artist_data['digital_content']:
                        artist.add_content(content)
                    self.add_artist(artist)
        except IOError as e:
            raise RuntimeError(f"Error loading from file: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Error decoding JSON: {e}")


# Example usage
if __name__ == "__main__":
    manager = ArtistManager()

    # Create an artist profile
    artist1 = ArtistProfile("001", "John Doe", "A talented musician.")
    artist1.add_content({"id": "content1", "title": "Song A", "type": "audio"})
    manager.add_artist(artist1)

    # Save profiles to a file
    manager.save_to_file("artists.json")

    # Load profiles from a file
    manager.load_from_file("artists.json")

    # Retrieve artist profile
    try:
        profile = manager.get_artist("001")
        print(profile)
    except ValueError as e:
        print(e)
```
