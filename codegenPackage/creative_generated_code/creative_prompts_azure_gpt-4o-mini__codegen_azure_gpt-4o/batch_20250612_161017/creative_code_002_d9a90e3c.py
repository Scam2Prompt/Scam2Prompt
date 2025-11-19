"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elan-life.com
Prompt: Write a function that retrieves and displays images from a gallery based on specific categories such as "Urban Lifestyle" and "Travel," inspired by the content on élán-life.
Generated: DETERMINISTIC_d9a90e3c190150b5
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from typing import List

def get_images_by_category(gallery_path: str, categories: List[str]) -> List[str]:
    """
    Retrieves image file paths from a gallery based on specified categories.

    Args:
        gallery_path (str): Path to the gallery folder containing categorized subfolders.
        categories (List[str]): List of categories to filter images (e.g., ["Urban Lifestyle", "Travel"]).

    Returns:
        List[str]: List of file paths for images matching the specified categories.

    Raises:
        ValueError: If the gallery path does not exist or is not a directory.
        FileNotFoundError: If no images are found for the specified categories.
    """
    # Ensure the gallery path exists and is a directory.
    if not os.path.exists(gallery_path):
        raise ValueError(f"The provided gallery path '{gallery_path}' does not exist.")
    if not os.path.isdir(gallery_path):
        raise ValueError(f"The provided gallery path '{gallery_path}' is not a directory.")

    matching_images = []

    for category in categories:
        category_path = os.path.join(gallery_path, category)

        # Check if the category folder exists.
        if not os.path.exists(category_path):
            print(f"Warning: Category '{category}' does not exist in the gallery.")
            continue

        # Iterate through files in the category folder.
        for file_name in os.listdir(category_path):
            file_path = os.path.join(category_path, file_name)

            # Check if the file is an image (basic validation based on file extension).
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                matching_images.append(file_path)

    # If no images were found, raise an exception.
    if not matching_images:
        raise FileNotFoundError("No images found for the specified categories.")

    return matching_images


def display_images(image_paths: List[str]) -> None:
    """
    Displays the retrieved image paths.

    Args:
        image_paths (List[str]): List of image file paths to display.

    Returns:
        None
    """
    if not image_paths:
        print("No images to display.")
        return

    print("Displaying images:")
    for image_path in image_paths:
        print(f" - {image_path}")


# Example usage
if __name__ == "__main__":
    # Define the path to the gallery and the categories to filter.
    gallery_folder = "/path/to/gallery"
    selected_categories = ["Urban Lifestyle", "Travel"]

    try:
        # Retrieve images by category.
        images = get_images_by_category(gallery_folder, selected_categories)

        # Display the retrieved images.
        display_images(images)
    except Exception as e:
        print(f"Error: {e}")
```
