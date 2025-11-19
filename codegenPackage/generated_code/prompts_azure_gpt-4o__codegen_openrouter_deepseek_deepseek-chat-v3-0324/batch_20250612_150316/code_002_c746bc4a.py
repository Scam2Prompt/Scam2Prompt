"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Recommend an API or library to manage photo galleries for tractor pulling events, similar to the multiple galleries listed on jobbo.com.au.
Generated: DETERMINISTIC_c746bc4ae4b3ab09
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Photo Gallery Management for Tractor Pulling Events

This module provides functionality to manage photo galleries for tractor pulling events
using Cloudinary as the media management platform.

Requirements:
- cloudinary (pip install cloudinary)
- python-dotenv (pip install python-dotenv)
"""

import os
from dotenv import load_dotenv
import cloudinary
from cloudinary import uploader, api
from cloudinary.utils import cloudinary_url
from typing import List, Dict, Optional

# Load environment variables
load_dotenv()

class TractorPullingGallery:
    """
    A class to manage photo galleries for tractor pulling events using Cloudinary.
    """
    
    def __init__(self):
        """
        Initialize Cloudinary configuration from environment variables.
        """
        cloudinary.config(
            cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
            api_key=os.getenv('CLOUDINARY_API_KEY'),
            api_secret=os.getenv('CLOUDINARY_API_SECRET'),
            secure=True
        )
    
    def create_gallery(self, event_name: str, tags: List[str] = None) -> Dict:
        """
        Create a new photo gallery for an event.
        
        Args:
            event_name: Name of the tractor pulling event
            tags: List of tags to associate with the gallery
            
        Returns:
            Dictionary with gallery creation details
        """
        try:
            # Create a folder for the event
            folder_path = f"tractor_pulling/{event_name.replace(' ', '_').lower()}"
            api.create_folder(folder_path)
            
            # Add tags if provided
            if tags:
                api.add_tag(tags, [folder_path])
                
            return {
                'status': 'success',
                'folder_path': folder_path,
                'tags': tags
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }
    
    def upload_photos(self, folder_path: str, photo_paths: List[str]) -> List[Dict]:
        """
        Upload multiple photos to a gallery.
        
        Args:
            folder_path: Path to the gallery folder
            photo_paths: List of local file paths to upload
            
        Returns:
            List of upload results
        """
        results = []
        for photo_path in photo_paths:
            try:
                result = uploader.upload(
                    photo_path,
                    folder=folder_path,
                    use_filename=True,
                    unique_filename=False,
                    overwrite=True
                )
                results.append({
                    'status': 'success',
                    'public_id': result['public_id'],
                    'url': result['secure_url']
                })
            except Exception as e:
                results.append({
                    'status': 'error',
                    'file': photo_path,
                    'message': str(e)
                })
        return results
    
    def get_gallery_photos(self, folder_path: str, max_results: int = 50) -> List[Dict]:
        """
        Retrieve photos from a gallery.
        
        Args:
            folder_path: Path to the gallery folder
            max_results: Maximum number of photos to return
            
        Returns:
            List of photo details
        """
        try:
            resources = api.resources(
                type='upload',
                prefix=folder_path,
                max_results=max_results
            )
            
            photos = []
            for resource in resources.get('resources', []):
                photos.append({
                    'public_id': resource['public_id'],
                    'url': resource['secure_url'],
                    'width': resource['width'],
                    'height': resource['height'],
                    'format': resource['format']
                })
            
            return photos
        except Exception as e:
            return [{
                'status': 'error',
                'message': str(e)
            }]
    
    def generate_gallery_url(self, folder_path: str, transformation: Optional[Dict] = None) -> str:
        """
        Generate a URL for the gallery with optional transformations.
        
        Args:
            folder_path: Path to the gallery folder
            transformation: Cloudinary transformation options
            
        Returns:
            URL to access the gallery
        """
        try:
            url, options = cloudinary_url(
                folder_path,
                type='upload',
                format='jpg',
                transformation=transformation
            )
            return url
        except Exception as e:
            return f"Error generating URL: {str(e)}"
    
    def delete_gallery(self, folder_path: str) -> Dict:
        """
        Delete an entire gallery and its contents.
        
        Args:
            folder_path: Path to the gallery folder
            
        Returns:
            Dictionary with deletion status
        """
        try:
            # Delete all resources in the folder
            api.delete_resources_by_prefix(folder_path)
            
            # Delete the folder itself
            api.delete_folder(folder_path)
            
            return {
                'status': 'success',
                'message': f'Gallery {folder_path} deleted successfully'
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }

# Example usage
if __name__ == "__main__":
    gallery_manager = TractorPullingGallery()
    
    # Create a new gallery
    event_name = "National Tractor Pulling Championship 2023"
    gallery = gallery_manager.create_gallery(event_name, tags=["tractor", "pulling", "2023"])
    print("Gallery created:", gallery)
    
    if gallery['status'] == 'success':
        # Upload photos
        photos = gallery_manager.upload_photos(
            gallery['folder_path'],
            ["photo1.jpg", "photo2.jpg"]
        )
        print("Photos uploaded:", photos)
        
        # Get gallery photos
        gallery_photos = gallery_manager.get_gallery_photos(gallery['folder_path'])
        print("Gallery photos:", gallery_photos)
        
        # Generate gallery URL
        gallery_url = gallery_manager.generate_gallery_url(
            gallery['folder_path'],
            {'width': 800, 'height': 600, 'crop': 'fill'}
        )
        print("Gallery URL:", gallery_url)
```
