"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Write code to upload and organize photos and media files in a genealogy database, referencing the media attachment system described on the Meyer/Seim family website.
Generated: DETERMINISTIC_fce6826baa2e8be2
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# media_uploader.py

import os
import uuid
from datetime import datetime
from typing import Dict, List

class MediaUploader:
    def __init__(self, db_connection, media_dir: str = './media'):
        """
        Initialize the MediaUploader.

        Args:
        - db_connection: A connection object to the genealogy database.
        - media_dir: The directory where media files will be stored.
        """
        self.db_connection = db_connection
        self.media_dir = media_dir

    def upload_media(self, file_path: str, file_type: str, description: str = '') -> int:
        """
        Upload a media file to the server and add it to the database.

        Args:
        - file_path: The path to the media file on the local machine.
        - file_type: The type of media file (e.g., image, video, audio).
        - description: A brief description of the media file.

        Returns:
        - The ID of the newly created media record.
        """
        try:
            # Generate a unique filename for the media file
            file_name = f"{uuid.uuid4()}.{file_type.split('/')[-1]}"

            # Create the media directory if it doesn't exist
            if not os.path.exists(self.media_dir):
                os.makedirs(self.media_dir)

            # Copy the media file to the media directory
            media_file_path = os.path.join(self.media_dir, file_name)
            with open(file_path, 'rb') as src:
                with open(media_file_path, 'wb') as dst:
                    dst.write(src.read())

            # Create a new media record in the database
            media_id = self._create_media_record(file_name, file_type, description)

            return media_id

        except Exception as e:
            print(f"Error uploading media: {e}")
            return None

    def _create_media_record(self, file_name: str, file_type: str, description: str) -> int:
        """
        Create a new media record in the database.

        Args:
        - file_name: The filename of the media file.
        - file_type: The type of media file.
        - description: A brief description of the media file.

        Returns:
        - The ID of the newly created media record.
        """
        cursor = self.db_connection.cursor()
        query = """
            INSERT INTO media (file_name, file_type, description, created_at)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (file_name, file_type, description, datetime.now()))
        self.db_connection.commit()
        return cursor.lastrowid

    def associate_media_with_person(self, media_id: int, person_id: int) -> bool:
        """
        Associate a media file with a person in the database.

        Args:
        - media_id: The ID of the media record.
        - person_id: The ID of the person.

        Returns:
        - True if the association was successful, False otherwise.
        """
        try:
            cursor = self.db_connection.cursor()
            query = """
                INSERT INTO person_media (person_id, media_id)
                VALUES (?, ?)
            """
            cursor.execute(query, (person_id, media_id))
            self.db_connection.commit()
            return True

        except Exception as e:
            print(f"Error associating media with person: {e}")
            return False

def main():
    # Example usage
    db_connection = None  # Replace with your database connection object
    uploader = MediaUploader(db_connection)

    file_path = '/path/to/media/file.jpg'
    file_type = 'image/jpeg'
    description = 'A photo of John Doe'

    media_id = uploader.upload_media(file_path, file_type, description)
    print(f"Media ID: {media_id}")

    person_id = 123  # Replace with the ID of the person
    associated = uploader.associate_media_with_person(media_id, person_id)
    print(f"Associated: {associated}")

if __name__ == '__main__':
    main()
```
