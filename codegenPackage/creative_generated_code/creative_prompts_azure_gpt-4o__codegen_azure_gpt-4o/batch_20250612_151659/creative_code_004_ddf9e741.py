"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahopefulme.com
Prompt: Write a Python script to automate the management of user-generated content, such as inspirational posts and picture walls, for a platform like HopefulMe.
Generated: DETERMINISTIC_ddf9e74112c5622c
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

# Constants
CONTENT_DIRECTORY = "user_content"  # Directory to store user-generated content
LOG_FILE = "content_log.json"  # File to log content metadata

# Ensure the content directory exists
if not os.path.exists(CONTENT_DIRECTORY):
    os.makedirs(CONTENT_DIRECTORY)

# Function to save a new post
def save_post(username, post_title, post_content):
    """
    Save a user-generated text post to the content directory.

    Parameters:
        username (str): The name of the user creating the post.
        post_title (str): The title of the post.
        post_content (str): The content of the post.

    Returns:
        dict: Metadata about the saved post.
    """
    try:
        # Validate inputs
        if not username or not post_title or not post_content:
            raise ValueError("All inputs (username, post_title, post_content) are required.")

        # Create a timestamp for the post
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Generate a filename for the post
        filename = f"{username}_{timestamp}.txt"
        file_path = os.path.join(CONTENT_DIRECTORY, filename)

        # Save the content to the file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Title: {post_title}\n")
            f.write(f"Date: {timestamp}\n")
            f.write(f"Author: {username}\n\n")
            f.write(post_content)

        # Log the metadata
        metadata = {
            "username": username,
            "post_title": post_title,
            "timestamp": timestamp,
            "file_path": file_path
        }
        log_content_metadata(metadata)

        return metadata
    except Exception as e:
        print(f"Error saving post: {e}")
        return {"error": str(e)}

# Function to upload a picture
def save_picture(username, picture_path):
    """
    Save a user-uploaded picture to the content directory.

    Parameters:
        username (str): The name of the user uploading the picture.
        picture_path (str): The path of the picture to upload.

    Returns:
        dict: Metadata about the saved picture.
    """
    try:
        # Validate inputs
        if not username or not picture_path:
            raise ValueError("Both username and picture_path are required.")

        if not os.path.exists(picture_path):
            raise FileNotFoundError(f"Picture file not found: {picture_path}")

        # Create a timestamp for the picture
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Generate a new filename for the picture
        original_extension = os.path.splitext(picture_path)[1]
        new_filename = f"{username}_{timestamp}{original_extension}"
        new_file_path = os.path.join(CONTENT_DIRECTORY, new_filename)

        # Copy the picture to the content directory
        with open(picture_path, "rb") as src, open(new_file_path, "wb") as dest:
            dest.write(src.read())

        # Log the metadata
        metadata = {
            "username": username,
            "timestamp": timestamp,
            "file_path": new_file_path
        }
        log_content_metadata(metadata)

        return metadata
    except Exception as e:
        print(f"Error saving picture: {e}")
        return {"error": str(e)}

# Function to log content metadata
def log_content_metadata(metadata):
    """
    Log metadata about user-generated content.

    Parameters:
        metadata (dict): Metadata to log.
    """
    try:
        # Read existing log data
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        else:
            logs = []

        # Append the new metadata
        logs.append(metadata)

        # Save the updated log data
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=4)
    except Exception as e:
        print(f"Error logging metadata: {e}")

# Function to display logs
def display_logs():
    """
    Display the logged metadata about user-generated content.
    """
    try:
        if not os.path.exists(LOG_FILE):
            print("No logs found.")
            return

        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
            for log in logs:
                print(json.dumps(log, indent=4))
    except Exception as e:
        print(f"Error displaying logs: {e}")

# Example Usage:
if __name__ == "__main__":
    # Save a post
    post_metadata = save_post("john_doe", "Inspirational Quote", "Believe in yourself and all that you are.")
    print(post_metadata)

    # Save a picture
    picture_metadata = save_picture("john_doe", "example_picture.jpg")  # Replace with an actual picture path
    print(picture_metadata)

    # Display logs
    print("\nContent Logs:")
    display_logs()
```
