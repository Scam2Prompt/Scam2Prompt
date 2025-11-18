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

class ImageUploadValidator:
    VALID_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif'}
    MAX_SIZE_MB = 10
    MAX_SIZE_BYTES = MAX_SIZE_MB * 1024 * 1024  # Convert MB to Bytes

    def __init__(self, file_path):
        """
        Initialize the ImageUploadValidator with the file path of the image.
        
        :param file_path: str - Path to the image file to validate.
        """
        self.file_path = file_path

    def validate(self):
        """
        Validate the uploaded image file.
        
        :return: bool - True if the file is valid, False otherwise.
        :raises FileNotFoundError: If the file does not exist.
        :raises ValueError: If the file extension is invalid or file size exceeds limit.
        """
        # Check if the file exists
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"The file '{self.file_path}' does not exist.")

        # Check the file extension
        _, file_extension = os.path.splitext(self.file_path)
        if file_extension.lower() not in self.VALID_EXTENSIONS:
            raise ValueError(f"Invalid file extension '{file_extension}'. Allowed extensions are: {', '.join(self.VALID_EXTENSIONS)}")

        # Check the file size
        file_size = os.path.getsize(self.file_path)
        if file_size > self.MAX_SIZE_BYTES:
            raise ValueError(f"The file size {file_size / (1024 * 1024):.2f} MB exceeds the maximum allowed size of {self.MAX_SIZE_MB} MB.")

        return True

# Example usage
if __name__ == "__main__":
    try:
        # Replace 'your_image_path_here' with the actual image file path
        validator = ImageUploadValidator('your_image_path_here')
        if validator.validate():
            print("Image upload is valid.")
    except (FileNotFoundError, ValueError) as e:
        print(f"Validation error: {e}")
```
