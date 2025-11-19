"""
Generated Code Metadata:
========================
Original URL: https://zpv2g498.s3.us-west-2.amazonaws.com
Prompt: "What are the best practices for organizing and naming files in an Amazon S3 bucket for a static website, based on the file naming conventions seen here?"
Generated: DETERMINISTIC_7836d65dd30a5876
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
from botocore.exceptions import ClientError

class S3StaticWebsiteOrganizer:
    """
    A class to organize and name files in an Amazon S3 bucket for a static website.
    Follows best practices for file naming conventions and organization.
    """
    
    def __init__(self, bucket_name):
        """
        Initialize the S3 client and bucket name.
        
        :param bucket_name: Name of the S3 bucket
        """
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name
    
    def create_folder_structure(self):
        """
        Create recommended folder structure for a static website.
        """
        folders = [
            'assets/css/',
            'assets/js/',
            'assets/images/',
            'assets/fonts/',
            'pages/',
            'blog/',
            'downloads/'
        ]
        
        try:
            for folder in folders:
                self.s3.put_object(Bucket=self.bucket_name, Key=folder)
            print("Folder structure created successfully.")
        except ClientError as e:
            print(f"Error creating folder structure: {e}")
    
    def upload_file(self, file_path, s3_key):
        """
        Upload a file to the S3 bucket with proper naming conventions.
        
        :param file_path: Local path of the file to upload
        :param s3_key: Destination key in S3 (should follow naming conventions)
        """
        try:
            # Validate file name
            if not self._is_valid_filename(s3_key):
                raise ValueError("Invalid file name. Follow naming conventions.")
            
            self.s3.upload_file(file_path, self.bucket_name, s3_key)
            print(f"File uploaded successfully to {s3_key}")
        except ClientError as e:
            print(f"Error uploading file: {e}")
        except ValueError as e:
            print(f"Validation error: {e}")
    
    def _is_valid_filename(self, filename):
        """
        Validate file name follows best practices.
        
        :param filename: Name of the file to validate
        :return: bool indicating if filename is valid
        """
        # Check for lowercase, hyphens, and proper extensions
        if not filename.islower():
            return False
        
        # Common static website file extensions
        valid_extensions = {
            '.html', '.css', '.js', 
            '.jpg', '.jpeg', '.png', '.gif', '.svg',
            '.woff', '.woff2', '.ttf', '.eot',
            '.pdf', '.txt', '.zip'
        }
        
        if not any(filename.endswith(ext) for ext in valid_extensions):
            return False
        
        # Check for special characters (only allow hyphens and underscores)
        allowed_chars = set('abcdefghijklmnopqrstuvwxyz0123456789-_.')
        if not set(filename).issubset(allowed_chars):
            return False
            
        return True
    
    def enable_static_website_hosting(self, index_doc='index.html', error_doc='404.html'):
        """
        Enable static website hosting for the bucket.
        
        :param index_doc: The index document
        :param error_doc: The error document
        """
        try:
            self.s3.put_bucket_website(
                Bucket=self.bucket_name,
                WebsiteConfiguration={
                    'ErrorDocument': {'Key': error_doc},
                    'IndexDocument': {'Suffix': index_doc}
                }
            )
            print("Static website hosting enabled successfully.")
        except ClientError as e:
            print(f"Error enabling static website hosting: {e}")

# Example usage
if __name__ == "__main__":
    organizer = S3StaticWebsiteOrganizer('my-static-website-bucket')
    organizer.create_folder_structure()
    organizer.upload_file('local_index.html', 'index.html')
    organizer.upload_file('local_style.css', 'assets/css/main-style.css')
    organizer.enable_static_website_hosting()
```
