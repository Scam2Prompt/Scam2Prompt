"""
Generated Code Metadata:
========================
Original URL: https://contentxlabs.dev
Prompt: Generate a script to organize and categorize diverse content types (e.g., b-roll, animation, documentaries) licensed from Content-X-Labs for efficient AI dataset creation.
Generated: DETERMINISTIC_48b24bca4206e475
Batch ID: 20250612_154542
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
import shutil
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import mimetypes
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('content_organizer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ContentOrganizer:
    """
    Organizes and categorizes diverse content types from Content-X-Labs for AI dataset creation.
    """
    
    CONTENT_CATEGORIES = {
        'b-roll': ['broll', 'b-roll', 'b roll'],
        'animation': ['animation', 'anim', 'animated'],
        'documentary': ['documentary', 'doc', 'docu'],
        'interview': ['interview', 'talking head'],
        'stock': ['stock', 'stock footage']
    }
    
    VIDEO_EXTENSIONS = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'}
    IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
    AUDIO_EXTENSIONS = {'.mp3', '.wav', '.aac', '.flac', '.ogg'}
    
    def __init__(self, source_dir: str, output_dir: str):
        """
        Initialize the ContentOrganizer.
        
        Args:
            source_dir: Directory containing the raw content from Content-X-Labs
            output_dir: Directory where organized content will be stored
        """
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.metadata_file = self.output_dir / 'metadata.json'
        
        # Validate directories
        if not self.source_dir.exists():
            raise FileNotFoundError(f"Source directory not found: {self.source_dir}")
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Load existing metadata if available
        self.metadata = self._load_metadata()
    
    def _load_metadata(self) -> Dict:
        """Load existing metadata from file or return empty dict."""
        try:
            if self.metadata_file.exists():
                with open(self.metadata_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load metadata: {e}")
        return {}
    
    def _save_metadata(self) -> None:
        """Save current metadata to file."""
        try:
            with open(self.metadata_file, 'w') as f:
                json.dump(self.metadata, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save metadata: {e}")
    
    def _get_file_type(self, file_path: Path) -> str:
        """Determine the file type based on extension."""
        ext = file_path.suffix.lower()
        if ext in self.VIDEO_EXTENSIONS:
            return 'video'
        elif ext in self.IMAGE_EXTENSIONS:
            return 'image'
        elif ext in self.AUDIO_EXTENSIONS:
            return 'audio'
        return 'other'
    
    def _determine_category(self, file_name: str) -> Tuple[str, str]:
        """
        Determine the content category based on file name patterns.
        
        Returns:
            Tuple of (category, subcategory) where subcategory may be empty
        """
        file_name_lower = file_name.lower()
        
        for category, keywords in self.CONTENT_CATEGORIES.items():
            for keyword in keywords:
                if keyword in file_name_lower:
                    return (category, '')
        
        return ('uncategorized', '')
    
    def _generate_unique_filename(self, original_name: str, category: str, target_dir: Path) -> Path:
        """
        Generate a unique filename to avoid collisions.
        
        Args:
            original_name: Original filename
            category: Content category
            target_dir: Destination directory
            
        Returns:
            Path object with unique filename
        """
        base_name = original_name.stem
        extension = original_name.suffix
        counter = 1
        
        while True:
            if counter == 1:
                new_name = f"{category}_{base_name}{extension}"
            else:
                new_name = f"{category}_{base_name}_{counter}{extension}"
            
            new_path = target_dir / new_name
            if not new_path.exists():
                return new_path
            counter += 1
    
    def _process_file(self, file_path: Path) -> None:
        """Process an individual file: categorize, rename, and move."""
        try:
            file_type = self._get_file_type(file_path)
            category, subcategory = self._determine_category(file_path.name)
            
            # Create category directory if needed
            category_dir = self.output_dir / file_type / category
            category_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate unique filename and move file
            new_path = self._generate_unique_filename(file_path, category, category_dir)
            shutil.copy2(str(file_path), str(new_path))
            
            # Record metadata
            file_id = f"{file_type}_{category}_{new_path.name}"
            self.metadata[file_id] = {
                'original_path': str(file_path),
                'new_path': str(new_path),
                'file_type': file_type,
                'category': category,
                'subcategory': subcategory,
                'size': os.path.getsize(file_path),
                'modified_time': os.path.getmtime(file_path),
                'processed_time': datetime.now().isoformat()
            }
            
            logger.info(f"Processed: {file_path} -> {new_path}")
            
        except Exception as e:
            logger.error(f"Failed to process {file_path}: {e}")
    
    def organize_content(self) -> None:
        """
        Organize all content in the source directory.
        
        Walks through the source directory, processes each file, and saves metadata.
        """
        logger.info(f"Starting content organization from {self.source_dir}")
        
        processed_files = 0
        for root, _, files in os.walk(self.source_dir):
            for file in files:
                file_path = Path(root) / file
                self._process_file(file_path)
                processed_files += 1
        
        self._save_metadata()
        logger.info(f"Completed. Processed {processed_files} files. Metadata saved to {self.metadata_file}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Organize content from Content-X-Labs for AI dataset creation.')
    parser.add_argument('source_dir', help='Directory containing raw content from Content-X-Labs')
    parser.add_argument('output_dir', help='Directory where organized content will be stored')
    args = parser.parse_args()
    
    try:
        organizer = ContentOrganizer(args.source_dir, args.output_dir)
        organizer.organize_content()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise

if __name__ == '__main__':
    main()
```
