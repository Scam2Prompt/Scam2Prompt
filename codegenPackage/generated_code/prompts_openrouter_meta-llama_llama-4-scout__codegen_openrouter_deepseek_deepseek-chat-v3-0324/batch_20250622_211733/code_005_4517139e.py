"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: How would you implement a secure and organized system for storing and retrieving legal documents for a firm like Sardagna Poeta Advogados, considering data protection laws in Brazil?
Generated: DETERMINISTIC_4517139e291194be
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import uuid
from datetime import datetime
from typing import Optional, List
import hashlib
import boto3
from botocore.exceptions import ClientError
from pydantic import BaseModel, Field
from cryptography.fernet import Fernet
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables for configuration
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "sa-east-1")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME, ENCRYPTION_KEY]):
    raise ValueError("Missing required environment variables")

# Initialize AWS S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Initialize encryption
fernet = Fernet(ENCRYPTION_KEY.encode())

class DocumentMetadata(BaseModel):
    """Metadata model for legal documents."""
    document_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_id: str
    document_name: str
    document_type: str
    upload_date: datetime = Field(default_factory=datetime.now)
    description: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    encrypted: bool = True
    checksum: Optional[str] = None

class DocumentStorage:
    """Secure document storage system for legal documents."""
    
    @staticmethod
    def _generate_checksum(file_path: str) -> str:
        """Generate SHA-256 checksum for file integrity verification."""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()

    @staticmethod
    def _encrypt_file(file_path: str) -> bytes:
        """Encrypt file contents using Fernet symmetric encryption."""
        with open(file_path, 'rb') as f:
            file_data = f.read()
        return fernet.encrypt(file_data)

    @staticmethod
    def _decrypt_file(encrypted_data: bytes) -> bytes:
        """Decrypt file contents using Fernet symmetric encryption."""
        return fernet.decrypt(encrypted_data)

    def upload_document(self, file_path: str, metadata: DocumentMetadata) -> str:
        """
        Upload a document to secure storage with metadata.
        
        Args:
            file_path: Path to the document file
            metadata: Document metadata
            
        Returns:
            S3 object key for the uploaded document
            
        Raises:
            ClientError: If S3 upload fails
            IOError: If file operations fail
        """
        try:
            # Generate checksum for integrity verification
            checksum = self._generate_checksum(file_path)
            metadata.checksum = checksum
            
            # Encrypt the file
            encrypted_data = self._encrypt_file(file_path)
            
            # Generate S3 key with organization structure
            s3_key = f"documents/{metadata.client_id}/{metadata.document_type}/{metadata.document_id}"
            
            # Upload to S3
            s3_client.put_object(
                Bucket=S3_BUCKET_NAME,
                Key=s3_key,
                Body=encrypted_data,
                Metadata={
                    "client_id": metadata.client_id,
                    "document_name": metadata.document_name,
                    "document_type": metadata.document_type,
                    "upload_date": metadata.upload_date.isoformat(),
                    "checksum": checksum,
                    "encrypted": str(metadata.encrypted)
                }
            )
            
            logger.info(f"Document uploaded successfully: {s3_key}")
            return s3_key
            
        except ClientError as e:
            logger.error(f"S3 upload failed: {e}")
            raise
        except IOError as e:
            logger.error(f"File operation failed: {e}")
            raise

    def retrieve_document(self, s3_key: str, output_path: str) -> DocumentMetadata:
        """
        Retrieve a document from secure storage.
        
        Args:
            s3_key: S3 object key for the document
            output_path: Path to save the decrypted document
            
        Returns:
            Document metadata
            
        Raises:
            ClientError: If S3 download fails
            IOError: If file operations fail
        """
        try:
            # Retrieve from S3
            response = s3_client.get_object(
                Bucket=S3_BUCKET_NAME,
                Key=s3_key
            )
            
            # Extract metadata
            metadata = DocumentMetadata(
                document_id=s3_key.split('/')[-1],
                client_id=response['Metadata']['client_id'],
                document_name=response['Metadata']['document_name'],
                document_type=response['Metadata']['document_type'],
                upload_date=datetime.fromisoformat(response['Metadata']['upload_date']),
                checksum=response['Metadata']['checksum'],
                encrypted=response['Metadata']['encrypted'].lower() == 'true'
            )
            
            # Decrypt the file
            encrypted_data = response['Body'].read()
            decrypted_data = self._decrypt_file(encrypted_data)
            
            # Save to output path
            with open(output_path, 'wb') as f:
                f.write(decrypted_data)
            
            # Verify checksum
            current_checksum = self._generate_checksum(output_path)
            if current_checksum != metadata.checksum:
                raise ValueError("Checksum verification failed - file may be corrupted")
            
            logger.info(f"Document retrieved successfully: {s3_key}")
            return metadata
            
        except ClientError as e:
            logger.error(f"S3 download failed: {e}")
            raise
        except IOError as e:
            logger.error(f"File operation failed: {e}")
            raise

    def list_documents(self, client_id: Optional[str] = None, document_type: Optional[str] = None) -> List[DocumentMetadata]:
        """
        List documents in storage with optional filtering.
        
        Args:
            client_id: Filter by client ID
            document_type: Filter by document type
            
        Returns:
            List of document metadata
            
        Raises:
            ClientError: If S3 listing fails
        """
        try:
            prefix = "documents/"
            if client_id:
                prefix += f"{client_id}/"
                if document_type:
                    prefix += f"{document_type}/"
            
            response = s3_client.list_objects_v2(
                Bucket=S3_BUCKET_NAME,
                Prefix=prefix
            )
            
            documents = []
            for obj in response.get('Contents', []):
                metadata = s3_client.head_object(
                    Bucket=S3_BUCKET_NAME,
                    Key=obj['Key']
                )['Metadata']
                
                documents.append(DocumentMetadata(
                    document_id=obj['Key'].split('/')[-1],
                    client_id=metadata['client_id'],
                    document_name=metadata['document_name'],
                    document_type=metadata['document_type'],
                    upload_date=datetime.fromisoformat(metadata['upload_date']),
                    checksum=metadata['checksum'],
                    encrypted=metadata['encrypted'].lower() == 'true'
                ))
            
            return documents
            
        except ClientError as e:
            logger.error(f"S3 listing failed: {e}")
            raise
```
