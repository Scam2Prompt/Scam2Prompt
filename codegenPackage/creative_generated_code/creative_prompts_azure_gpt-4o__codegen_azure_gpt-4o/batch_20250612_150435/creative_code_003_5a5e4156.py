"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooledether.io
Prompt: Write a Python function to upload an image to a Blogger blog post using the Blogger API, ensuring the image is stored securely.
Generated: DETERMINISTIC_5a5e415639f9c501
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import mimetypes
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials


def upload_image_to_blogger(blog_id, image_path, access_token):
    """
    Uploads an image to a Blogger blog post using the Blogger API.

    Parameters:
        blog_id (str): The ID of the blog where the image will be uploaded.
        image_path (str): The local file path to the image.
        access_token (str): OAuth 2.0 access token with Blogger API permissions.

    Returns:
        dict: The API response containing details about the uploaded image.
    """
    # Validate the image file
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found at: {image_path}")
    
    file_type, _ = mimetypes.guess_type(image_path)
    if not file_type or not file_type.startswith("image/"):
        raise ValueError(f"Invalid file type for image: {file_type}")

    try:
        # Authenticate using the provided access token
        credentials = Credentials(token=access_token)
        blogger_service = build("blogger", "v3", credentials=credentials)

        # Upload the image using MediaFileUpload
        media = MediaFileUpload(image_path, mimetype=file_type, resumable=True)
        response = blogger_service.media().insert(blogId=blog_id, media_body=media).execute()

        return response  # Return the API response containing image details

    except HttpError as e:
        # Handle HTTP errors from the API
        error_message = f"HTTP error occurred: {e.status_code} - {e.reason}"
        raise RuntimeError(error_message) from e
    except Exception as e:
        # Handle any other unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {str(e)}") from e


# Example usage:
# Ensure you have a valid OAuth 2.0 access token before calling this function.
# blog_id = "your-blog-id"
# image_path = "path/to/your/image.jpg"
# access_token = "your-oauth-access-token"
# response = upload_image_to_blogger(blog_id, image_path, access_token)
# print("Image uploaded successfully:", response)
```
