"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: Write code to integrate cloud security features into a video surveillance system, ensuring secure storage and remote access, as described by Ray-Z Entreprise.
Generated: DETERMINISTIC_9c79175830d3a064
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import boto3
from botocore.exceptions import ClientError
from cryptography.fernet import Fernet
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CloudSecurityManager:
    """
    Manages cloud security features for video surveillance system including:
    - Secure storage in AWS S3
    - Encryption/Decryption of video files
    - Secure access control
    """
    
    def __init__(self, aws_access_key, aws_secret_key, bucket_name, encryption_key=None):
        """
        Initialize the CloudSecurityManager with AWS credentials and bucket name.
        
        Args:
            aws_access_key (str): AWS access key ID
            aws_secret_key (str): AWS secret access key
            bucket_name (str): S3 bucket name
            encryption_key (bytes, optional): Fernet encryption key. Generates one if None.
        """
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_key
        )
        
        if encryption_key is None:
            self.encryption_key = Fernet.generate_key()
        else:
            self.encryption_key = encryption_key
        self.cipher_suite = Fernet(self.encryption_key)
        
    def encrypt_file(self, file_path):
        """
        Encrypt a file using Fernet symmetric encryption.
        
        Args:
            file_path (str): Path to the file to encrypt
            
        Returns:
            bytes: Encrypted data
        """
        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()
            encrypted_data = self.cipher_suite.encrypt(file_data)
            return encrypted_data
        except Exception as e:
            logger.error(f"Error encrypting file {file_path}: {str(e)}")
            raise
            
    def decrypt_file(self, encrypted_data, output_path):
        """
        Decrypt a file and save to specified path.
        
        Args:
            encrypted_data (bytes): Encrypted data to decrypt
            output_path (str): Path to save decrypted file
        """
        try:
            decrypted_data = self.cipher_suite.decrypt(encrypted_data)
            with open(output_path, 'wb') as file:
                file.write(decrypted_data)
        except Exception as e:
            logger.error(f"Error decrypting file to {output_path}: {str(e)}")
            raise
            
    def upload_to_s3(self, file_path, s3_key=None):
        """
        Encrypt and upload a file to S3 with proper access controls.
        
        Args:
            file_path (str): Path to the file to upload
            s3_key (str, optional): S3 object key. Uses filename if None.
            
        Returns:
            str: S3 object key of uploaded file
        """
        try:
            if s3_key is None:
                s3_key = os.path.basename(file_path)
                
            # Add timestamp to prevent overwrites
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            s3_key = f"{timestamp}_{s3_key}"
            
            encrypted_data = self.encrypt_file(file_path)
            
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=s3_key,
                Body=encrypted_data,
                ServerSideEncryption='AES256',
                ACL='private'
            )
            
            logger.info(f"Successfully uploaded {file_path} to S3 as {s3_key}")
            return s3_key
        except ClientError as e:
            logger.error(f"AWS Client Error uploading {file_path}: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error uploading {file_path}: {str(e)}")
            raise
            
    def download_from_s3(self, s3_key, output_path):
        """
        Download and decrypt a file from S3.
        
        Args:
            s3_key (str): S3 object key to download
            output_path (str): Path to save decrypted file
        """
        try:
            response = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key=s3_key
            )
            encrypted_data = response['Body'].read()
            self.decrypt_file(encrypted_data, output_path)
            logger.info(f"Successfully downloaded and decrypted {s3_key} to {output_path}")
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                logger.error(f"File {s3_key} not found in S3")
            else:
                logger.error(f"AWS Client Error downloading {s3_key}: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error downloading {s3_key}: {str(e)}")
            raise
            
    def generate_presigned_url(self, s3_key, expiration=3600):
        """
        Generate a presigned URL for secure temporary access to a file.
        
        Args:
            s3_key (str): S3 object key
            expiration (int): URL expiration time in seconds (default 1 hour)
            
        Returns:
            str: Presigned URL
        """
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': self.bucket_name,
                    'Key': s3_key
                },
                ExpiresIn=expiration
            )
            return url
        except ClientError as e:
            logger.error(f"Error generating presigned URL for {s3_key}: {str(e)}")
            raise
            
    def verify_file_integrity(self, original_path, downloaded_path):
        """
        Verify file integrity by comparing SHA-256 hashes.
        
        Args:
            original_path (str): Path to original file
            downloaded_path (str): Path to downloaded file
            
        Returns:
            bool: True if files match, False otherwise
        """
        try:
            def calculate_hash(filepath):
                sha256_hash = hashlib.sha256()
                with open(filepath, 'rb') as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)
                return sha256_hash.hexdigest()
                
            original_hash = calculate_hash(original_path)
            downloaded_hash = calculate_hash(downloaded_path)
            
            if original_hash == downloaded_hash:
                logger.info("File integrity verified - hashes match")
                return True
            else:
                logger.warning("File integrity check failed - hashes don't match")
                return False
        except Exception as e:
            logger.error(f"Error verifying file integrity: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your AWS credentials and bucket name
        security_manager = CloudSecurityManager(
            aws_access_key="YOUR_AWS_ACCESS_KEY",
            aws_secret_key="YOUR_AWS_SECRET_KEY",
            bucket_name="your-bucket-name"
        )
        
        # Example file operations
        test_file = "test_video.mp4"
        encrypted_file = "encrypted_video.mp4"
        downloaded_file = "downloaded_video.mp4"
        
        # Upload a file
        s3_key = security_manager.upload_to_s3(test_file)
        
        # Generate a presigned URL
        presigned_url = security_manager.generate_presigned_url(s3_key)
        print(f"Presigned URL: {presigned_url}")
        
        # Download the file
        security_manager.download_from_s3(s3_key, downloaded_file)
        
        # Verify integrity
        security_manager.verify_file_integrity(test_file, downloaded_file)
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
```
