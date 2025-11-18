"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Create a Python script to organize and generate labels for school supplies, including options for pencil labels and personal item tags, inspired by Labelmystuff.com.
Generated: DETERMINISTIC_92fffaa959d5b701
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
from PIL import Image, ImageDraw, ImageFont

# Constants for label dimensions and fonts
LABEL_WIDTH = 300
LABEL_HEIGHT = 100
FONT_PATH = "arial.ttf"  # Ensure you have an appropriate font file
FONT_SIZE = 20
OUTPUT_DIR = "labels"

# Error messages
ERROR_FONT_NOT_FOUND = "Error: Font file not found. Ensure the font path is correct."

def create_label(item_name, owner_name, output_file):
    """
    Creates a label for a school supply item and saves it as an image.
    
    Parameters:
        item_name (str): The name of the school supply (e.g., "Pencil").
        owner_name (str): The name of the owner.
        output_file (str): Location to save the generated label image.
    """
    try:
        # Initialize the image and drawing context
        image = Image.new("RGB", (LABEL_WIDTH, LABEL_HEIGHT), "white")
        draw = ImageDraw.Draw(image)
        
        # Load the font
        try:
            font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        except IOError:
            raise FileNotFoundError(ERROR_FONT_NOT_FOUND)
        
        # Text to display
        text = f"{item_name}\n{owner_name}"
        
        # Calculate text position to center it
        text_width, text_height = draw.multiline_textsize(text, font=font)
        x = (LABEL_WIDTH - text_width) // 2
        y = (LABEL_HEIGHT - text_height) // 2
        
        # Draw the text onto the label
        draw.multiline_text((x, y), text, fill="black", font=font, align="center")
        
        # Save the label to the specified file
        image.save(output_file)
        print(f"Label created: {output_file}")
    except Exception as e:
        print(f"Error creating label: {e}")


def generate_labels_from_csv(csv_file):
    """
    Reads a CSV file containing school supply items and owner names, and generates labels.
    
    Parameters:
        csv_file (str): Path to the CSV file.
        
    CSV Format:
        item_name,owner_name
        Pencil,John Doe
        Notebook,Jane Smith
    """
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.")
        return
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    try:
        # Read the CSV file
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item_name = row.get("item_name", "").strip()
                owner_name = row.get("owner_name", "").strip()
                
                if not item_name or not owner_name:
                    print("Error: Missing 'item_name' or 'owner_name' in CSV row. Skipping...")
                    continue
                
                # Generate output file name
                output_file = os.path.join(OUTPUT_DIR, f"{item_name}_{owner_name}.png")
                
                # Create the label
                create_label(item_name, owner_name, output_file)
    except Exception as e:
        print(f"Error processing CSV file: {e}")


if __name__ == "__main__":
    # Example usage
    print("Welcome to Label Generator!")
    csv_file = input("Enter the path to your CSV file: ").strip()
    generate_labels_from_csv(csv_file)
```
