"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-nft-fraction-frontend.vercel.app
Prompt: Write a function to validate image uploads (PNG, JPG, GIF up to 10MB) for an NFT fractionalizer built on Solana Devnet.
Generated: DETERMINISTIC_4409a7c78b2b8b4b
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def validate_image_upload(file_path: str) -> bool:
    """
    Validates an image upload for an NFT fractionalizer built on Solana Devnet.
    
    Args:
        file_path (str): The file path to the image being uploaded.

    Returns:
        bool: True if the image is valid, False otherwise.
    """
    # Allowed file extensions
    allowed_extensions = {"png", "jpg", "jpeg", "gif"}
    # Maximum file size in bytes (10MB)
    max_file_size = 10 * 1024 * 1024

    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print("Error: File does not exist.")
            return False

        # Get the file extension
        file_extension = os.path.splitext(file_path)[1].lower().strip(".")
        if file_extension not in allowed_extensions:
            print(f"Error: Invalid file type '{file_extension}'. Allowed types are {', '.join(allowed_extensions)}.")
            return False

        # Check the file size
        file_size = os.path.getsize(file_path)
        if file_size > max_file_size:
            print(f"Error: File size exceeds the limit of 10MB. Current size: {file_size / (1024 * 1024):.2f}MB.")
            return False

        # Validation passed
        print("Image upload validated successfully.")
        return True

    except Exception as e:
        # Handle unexpected errors
        print(f"Error: An unexpected error occurred during validation. Details: {str(e)}")
        return False

# Example usage
# file_path = "path/to/your/image.png"
# is_valid = validate_image_upload(file_path)
# print(f"Is the image valid? {is_valid}")
```
