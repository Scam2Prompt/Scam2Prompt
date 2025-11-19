"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: "Generate a Python script for media selection and management in event planning for brand activations in South Africa."
Generated: DETERMINISTIC_dd00810efff255d2
Batch ID: 20250622_212309
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
import csv
from datetime import datetime
from typing import List, Dict, Optional

class MediaItem:
    """Represents a media item for event planning."""
    
    def __init__(self, name: str, media_type: str, duration: float, file_path: str):
        """
        Initialize a MediaItem.
        
        Args:
            name: Name of the media item
            media_type: Type of media (e.g., 'video', 'image', 'audio')
            duration: Duration in seconds (0 for non-video/audio)
            file_path: Path to the media file
        """
        self.name = name
        self.media_type = media_type
        self.duration = duration
        self.file_path = file_path
        self.last_modified = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert MediaItem to dictionary for serialization."""
        return {
            'name': self.name,
            'media_type': self.media_type,
            'duration': self.duration,
            'file_path': self.file_path,
            'last_modified': self.last_modified.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'MediaItem':
        """Create MediaItem from dictionary."""
        return cls(
            name=data['name'],
            media_type=data['media_type'],
            duration=data['duration'],
            file_path=data['file_path']
        )

class MediaLibrary:
    """Manages a collection of media items for event planning."""
    
    def __init__(self, library_path: str = 'media_library.json'):
        """
        Initialize the MediaLibrary.
        
        Args:
            library_path: Path to the JSON file storing the library
        """
        self.library_path = library_path
        self.media_items: Dict[str, MediaItem] = {}
        self.load_library()
    
    def add_media(self, media_item: MediaItem) -> None:
        """Add a media item to the library."""
        if media_item.name in self.media_items:
            raise ValueError(f"Media item '{media_item.name}' already exists")
        self.media_items[media_item.name] = media_item
        self.save_library()
    
    def remove_media(self, name: str) -> None:
        """Remove a media item from the library."""
        if name not in self.media_items:
            raise ValueError(f"Media item '{name}' not found")
        del self.media_items[name]
        self.save_library()
    
    def get_media(self, name: str) -> Optional[MediaItem]:
        """Get a media item by name."""
        return self.media_items.get(name)
    
    def list_media(self, media_type: Optional[str] = None) -> List[MediaItem]:
        """List all media items, optionally filtered by type."""
        if media_type:
            return [item for item in self.media_items.values() if item.media_type == media_type]
        return list(self.media_items.values())
    
    def load_library(self) -> None:
        """Load the media library from file."""
        if not os.path.exists(self.library_path):
            return
        
        try:
            with open(self.library_path, 'r') as f:
                data = json.load(f)
                for item_data in data.values():
                    media_item = MediaItem.from_dict(item_data)
                    media_item.last_modified = datetime.fromisoformat(item_data['last_modified'])
                    self.media_items[media_item.name] = media_item
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            raise RuntimeError(f"Error loading media library: {str(e)}")
    
    def save_library(self) -> None:
        """Save the media library to file."""
        data = {name: item.to_dict() for name, item in self.media_items.items()}
        try:
            with open(self.library_path, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            raise RuntimeError(f"Error saving media library: {str(e)}")

class EventPlanner:
    """Manages media selection for brand activation events in South Africa."""
    
    def __init__(self, media_library: MediaLibrary):
        """
        Initialize the EventPlanner.
        
        Args:
            media_library: MediaLibrary instance to use
        """
        self.library = media_library
        self.south_african_regions = [
            'Gauteng', 'Western Cape', 'KwaZulu-Natal', 
            'Eastern Cape', 'Limpopo', 'Mpumalanga',
            'North West', 'Free State', 'Northern Cape'
        ]
    
    def create_playlist(self, event_name: str, media_names: List[str]) -> Dict:
        """
        Create a playlist for an event.
        
        Args:
            event_name: Name of the event
            media_names: List of media item names to include
            
        Returns:
            Dictionary containing playlist details
        """
        playlist = {
            'event_name': event_name,
            'created_at': datetime.now().isoformat(),
            'media_items': [],
            'total_duration': 0.0
        }
        
        for name in media_names:
            media_item = self.library.get_media(name)
            if not media_item:
                raise ValueError(f"Media item '{name}' not found in library")
            playlist['media_items'].append(media_item.to_dict())
            playlist['total_duration'] += media_item.duration
        
        return playlist
    
    def export_playlist_csv(self, playlist: Dict, output_path: str) -> None:
        """
        Export a playlist to CSV format.
        
        Args:
            playlist: Playlist dictionary
            output_path: Path to save the CSV file
        """
        try:
            with open(output_path, 'w', newline='') as csvfile:
                fieldnames = ['event_name', 'media_name', 'media_type', 'duration', 'file_path']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for item in playlist['media_items']:
                    writer.writerow({
                        'event_name': playlist['event_name'],
                        'media_name': item['name'],
                        'media_type': item['media_type'],
                        'duration': item['duration'],
                        'file_path': item['file_path']
                    })
        except IOError as e:
            raise RuntimeError(f"Error exporting playlist to CSV: {str(e)}")

def main():
    """Main function to demonstrate usage."""
    try:
        # Initialize media library
        library = MediaLibrary()
        
        # Add some sample media
        sample_video = MediaItem(
            name="Brand_Intro_Video",
            media_type="video",
            duration=30.5,
            file_path="/media/videos/brand_intro.mp4"
        )
        library.add_media(sample_video)
        
        sample_image = MediaItem(
            name="Logo_Display",
            media_type="image",
            duration=0,
            file_path="/media/images/logo.png"
        )
        library.add_media(sample_image)
        
        # Initialize event planner
        planner = EventPlanner(library)
        
        # Create a playlist
        playlist = planner.create_playlist(
            event_name="Johannesburg_Launch",
            media_names=["Brand_Intro_Video", "Logo_Display"]
        )
        
        # Export playlist
        planner.export_playlist_csv(playlist, "johannesburg_launch_playlist.csv")
        print("Playlist created and exported successfully.")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
