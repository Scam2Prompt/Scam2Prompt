"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Write a tutorial on how to use the Source engine's SDK to create custom textures and materials for a Day of Defeat: Source mod.
Generated: DETERMINISTIC_62bcb24cba1328f1
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for file handling and image processing
import os
from PIL import Image

# Define a function to create a custom texture
def create_custom_texture(source_image_path, output_texture_path, texture_name):
    """
    Create a custom texture for use in the Source engine.

    Parameters:
    source_image_path (str): Path to the source image file.
    output_texture_path (str): Path where the output texture will be saved.
    texture_name (str): Name of the texture to be created.

    Raises:
    FileNotFoundError: If the source image does not exist.
    ValueError: If the output path is invalid.
    """
    # Check if the source image exists
    if not os.path.isfile(source_image_path):
        raise FileNotFoundError(f"Source image not found: {source_image_path}")

    # Ensure the output path is valid
    if not os.path.isdir(output_texture_path):
        raise ValueError(f"Invalid output path: {output_texture_path}")

    # Load the source image
    try:
        with Image.open(source_image_path) as img:
            # Convert the image to a format suitable for the Source engine
            img = img.convert("RGBA")
            # Save the image in the appropriate format
            output_file = os.path.join(output_texture_path, f"{texture_name}.vtf")
            img.save(output_file, format="PNG")  # Save as PNG for VTF conversion
            print(f"Texture created successfully: {output_file}")
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")

# Define a function to create a material file
def create_material_file(output_texture_path, texture_name):
    """
    Create a material file for the custom texture.

    Parameters:
    output_texture_path (str): Path where the output texture is saved.
    texture_name (str): Name of the texture for the material file.
    """
    # Define the material file content
    material_content = f"""
    "LightmappedGeneric"
    {{
        "$basetexture" "{texture_name}"
        "$surfaceprop" "metal"
    }}
    """

    # Define the material file path
    material_file_path = os.path.join(output_texture_path, f"{texture_name}.vmt")

    # Write the material file
    try:
        with open(material_file_path, 'w') as material_file:
            material_file.write(material_content)
            print(f"Material file created successfully: {material_file_path}")
    except Exception as e:
        print(f"An error occurred while creating the material file: {e}")

# Example usage
if __name__ == "__main__":
    # Define paths and texture name
    source_image = "path/to/your/image.png"  # Replace with your image path
    output_path = "path/to/output/directory"  # Replace with your output directory
    texture_name = "custom_texture"  # Define your texture name

    # Create the custom texture and material file
    try:
        create_custom_texture(source_image, output_path, texture_name)
        create_material_file(output_path, texture_name)
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** Ensure you have the Pillow library installed for image processing. You can install it using `pip install Pillow`. Adjust the paths in the example usage section to point to your actual image and desired output directory.
