"""
Generated Code Metadata:
========================
Original URL: https://thephantomnetwork.net
Prompt: Develop a Python script to organize and display a chronological gallery of Photoshop edits, similar to the "Lets Begin: Photoshop" post on "The Phantom Network."
Generated: DETERMINISTIC_d5fe5bc95fc3590e
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import glob
from datetime import datetime
from PIL import Image
import exifread
import argparse
import sys

class PhotoshopGallery:
    """
    A class to organize and display a chronological gallery of Photoshop edits.
    """

    def __init__(self, input_dir, output_dir=None):
        """
        Initialize the gallery with input and optional output directories.
        
        Args:
            input_dir (str): Path to the directory containing Photoshop files.
            output_dir (str, optional): Path to save organized files. Defaults to input_dir.
        """
        self.input_dir = input_dir
        self.output_dir = output_dir if output_dir else input_dir
        self.supported_extensions = ('.psd', '.tif', '.tiff', '.jpg', '.jpeg', '.png')

    def _get_creation_date(self, file_path):
        """
        Get the creation date of a file using EXIF data or file metadata.
        
        Args:
            file_path (str): Path to the file.
            
        Returns:
            datetime: Creation date of the file.
            
        Raises:
            ValueError: If no creation date can be determined.
        """
        try:
            # Try to get EXIF data for image files
            if file_path.lower().endswith(('.jpg', '.jpeg', '.tif', '.tiff')):
                with open(file_path, 'rb') as f:
                    tags = exifread.process_file(f, stop_tag='DateTimeOriginal')
                    if 'EXIF DateTimeOriginal' in tags:
                        date_str = str(tags['EXIF DateTimeOriginal'])
                        return datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
            
            # Fall back to file system creation time
            timestamp = os.path.getmtime(file_path)
            return datetime.fromtimestamp(timestamp)
            
        except Exception as e:
            raise ValueError(f"Could not determine creation date for {file_path}: {str(e)}")

    def _organize_files(self):
        """
        Organize files chronologically by creation date.
        
        Returns:
            list: Sorted list of tuples (datetime, file_path).
        """
        files = []
        for ext in self.supported_extensions:
            files.extend(glob.glob(os.path.join(self.input_dir, f'*{ext}')))
        
        dated_files = []
        for file_path in files:
            try:
                date = self._get_creation_date(file_path)
                dated_files.append((date, file_path))
            except ValueError as e:
                print(f"Warning: {e}")
                continue
                
        # Sort by date
        dated_files.sort(key=lambda x: x[0])
        return dated_files

    def generate_gallery(self, output_html=None):
        """
        Generate an HTML gallery of the organized files.
        
        Args:
            output_html (str, optional): Path to save HTML file. Defaults to 'gallery.html'.
        """
        if output_html is None:
            output_html = os.path.join(self.output_dir, 'gallery.html')
            
        dated_files = self._organize_files()
        
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Photoshop Edits Gallery</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
                .item { border: 1px solid #ddd; padding: 10px; border-radius: 5px; }
                .item img { max-width: 100%; height: auto; }
                .date { color: #666; font-size: 0.9em; }
            </style>
        </head>
        <body>
            <h1>Photoshop Edits Gallery</h1>
            <div class="gallery">
        """
        
        for date, file_path in dated_files:
            filename = os.path.basename(file_path)
            html_content += f"""
                <div class="item">
                    <h3>{filename}</h3>
                    <img src="{file_path}" alt="{filename}">
                    <p class="date">{date.strftime('%Y-%m-%d %H:%M:%S')}</p>
                </div>
            """
            
        html_content += """
            </div>
        </body>
        </html>
        """
        
        try:
            with open(output_html, 'w') as f:
                f.write(html_content)
            print(f"Gallery generated successfully at {output_html}")
        except IOError as e:
            print(f"Error writing HTML file: {e}")

def main():
    parser = argparse.ArgumentParser(description='Organize and display a chronological gallery of Photoshop edits.')
    parser.add_argument('input_dir', help='Directory containing Photoshop files')
    parser.add_argument('--output_dir', help='Output directory for organized files (optional)')
    parser.add_argument('--html', help='Output HTML file path (optional)')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.input_dir):
        print(f"Error: Input directory {args.input_dir} does not exist.")
        sys.exit(1)
        
    if args.output_dir and not os.path.exists(args.output_dir):
        try:
            os.makedirs(args.output_dir)
        except OSError as e:
            print(f"Error creating output directory: {e}")
            sys.exit(1)
    
    gallery = PhotoshopGallery(args.input_dir, args.output_dir)
    gallery.generate_gallery(args.html)

if __name__ == '__main__':
    main()
```
