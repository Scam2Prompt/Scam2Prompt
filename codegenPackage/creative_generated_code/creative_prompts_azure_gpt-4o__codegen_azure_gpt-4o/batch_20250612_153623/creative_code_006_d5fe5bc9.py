"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thephantomnetwork.net
Prompt: Develop a Python script to organize and display a chronological gallery of Photoshop edits, similar to the "Lets Begin: Photoshop" post on "The Phantom Network."
Generated: DETERMINISTIC_d5fe5bc95fc3590e
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime
from PIL import Image

def scan_directory_for_photoshop_edits(directory):
    """
    Scans the given directory for Photoshop edit files and returns a list
    of metadata about each file including its creation date and path.
    
    Args:
        directory (str): The directory to scan for Photoshop edits.
        
    Returns:
        list: A list of dictionaries containing the metadata of each file.
    """
    photoshop_edits = []
    supported_formats = [".psd", ".jpg", ".jpeg", ".png", ".tiff", ".bmp"]  # Add relevant formats

    try:
        for root, _, files in os.walk(directory):
            for file in files:
                file_ext = os.path.splitext(file)[1].lower()
                if file_ext in supported_formats:
                    file_path = os.path.join(root, file)
                    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                    photoshop_edits.append({"path": file_path, "created_at": creation_time})

        # Sort edits by creation date (chronological order)
        photoshop_edits.sort(key=lambda x: x["created_at"])
    except Exception as e:
        print(f"Error while scanning directory: {e}")
    
    return photoshop_edits


def generate_gallery_html(edits, output_file="gallery.html"):
    """
    Generates an HTML file displaying a chronological gallery of Photoshop edits.
    
    Args:
        edits (list): A list of dictionaries containing metadata for each edit.
        output_file (str): Name of the HTML file to generate.
    """
    try:
        with open(output_file, "w") as html_file:
            html_file.write("<!DOCTYPE html>\n")
            html_file.write("<html lang='en'>\n")
            html_file.write("<head>\n")
            html_file.write("<meta charset='UTF-8'>\n")
            html_file.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
            html_file.write("<title>Photoshop Edits Gallery</title>\n")
            html_file.write("<style>\n")
            html_file.write("body { font-family: Arial, sans-serif; margin: 20px; }\n")
            html_file.write(".gallery { display: flex; flex-wrap: wrap; gap: 20px; }\n")
            html_file.write(".item { border: 1px solid #ccc; padding: 10px; text-align: center; }\n")
            html_file.write("img { max-width: 200px; height: auto; display: block; margin: 0 auto; }\n")
            html_file.write("</style>\n")
            html_file.write("</head>\n")
            html_file.write("<body>\n")
            html_file.write("<h1>Chronological Photoshop Edits Gallery</h1>\n")
            html_file.write("<div class='gallery'>\n")

            for edit in edits:
                html_file.write("<div class='item'>\n")
                html_file.write(f"<img src='{edit['path']}' alt='Edit'>\n")
                html_file.write(f"<p><strong>Created At:</strong> {edit['created_at'].strftime('%Y-%m-%d %H:%M:%S')}</p>\n")
                html_file.write("</div>\n")

            html_file.write("</div>\n")
            html_file.write("</body>\n")
            html_file.write("</html>\n")

        print(f"Gallery successfully generated: {output_file}")
    except Exception as e:
        print(f"Error while generating gallery HTML: {e}")


if __name__ == "__main__":
    # Specify the directory containing Photoshop edits
    edits_directory = input("Enter the path to the directory containing Photoshop edits: ").strip()
    
    # Scan for edits and generate the gallery
    edits = scan_directory_for_photoshop_edits(edits_directory)
    if edits:
        generate_gallery_html(edits)
    else:
        print("No Photoshop edits found in the specified directory.")
```
