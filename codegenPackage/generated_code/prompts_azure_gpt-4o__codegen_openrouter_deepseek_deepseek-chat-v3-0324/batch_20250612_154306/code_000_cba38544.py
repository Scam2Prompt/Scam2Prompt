"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Write Python code to integrate a document management system for organizing, digitalizing, and securely storing files, referencing solutions similar to those provided by EasyDoc Gestão.
Generated: DETERMINISTIC_cba3854421668a18
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import uuid
import hashlib
from datetime import datetime
from typing import List, Dict, Optional
import mimetypes
import logging
from pathlib import Path
import json
import zipfile
import tempfile
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DocumentManager:
    """
    A document management system for organizing, digitizing, and securely storing files.
    """
    
    def __init__(self, storage_root: str, encryption_key: Optional[bytes] = None):
        """
        Initialize the DocumentManager.
        
        Args:
            storage_root: Root directory for document storage
            encryption_key: Optional encryption key for secure storage (Fernet key)
        """
        self.storage_root = Path(storage_root)
        self.metadata_file = self.storage_root / "metadata.json"
        self.encryption_key = encryption_key
        
        # Create storage directory if it doesn't exist
        self.storage_root.mkdir(parents=True, exist_ok=True)
        
        # Initialize metadata
        if not self.metadata_file.exists():
            with open(self.metadata_file, 'w') as f:
                json.dump({"documents": {}}, f)
    
    def _load_metadata(self) -> Dict:
        """Load metadata from the metadata file."""
        try:
            with open(self.metadata_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Failed to load metadata: {e}")
            return {"documents": {}}
    
    def _save_metadata(self, metadata: Dict):
        """Save metadata to the metadata file."""
        try:
            with open(self.metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)
        except IOError as e:
            logger.error(f"Failed to save metadata: {e}")
            raise
    
    def _generate_document_id(self) -> str:
        """Generate a unique document ID."""
        return str(uuid.uuid4())
    
    def _get_document_path(self, doc_id: str) -> Path:
        """Get the storage path for a document."""
        return self.storage_root / doc_id
    
    def _encrypt_file(self, input_path: Path, output_path: Path):
        """Encrypt a file using Fernet encryption."""
        if not self.encryption_key:
            shutil.copy(input_path, output_path)
            return
            
        fernet = Fernet(self.encryption_key)
        with open(input_path, 'rb') as f:
            data = f.read()
        
        encrypted_data = fernet.encrypt(data)
        
        with open(output_path, 'wb') as f:
            f.write(encrypted_data)
    
    def _decrypt_file(self, input_path: Path, output_path: Path):
        """Decrypt a file using Fernet encryption."""
        if not self.encryption_key:
            shutil.copy(input_path, output_path)
            return
            
        fernet = Fernet(self.encryption_key)
        with open(input_path, 'rb') as f:
            encrypted_data = f.read()
        
        try:
            decrypted_data = fernet.decrypt(encrypted_data)
        except Exception as e:
            logger.error(f"Decryption failed: {e}")
            raise
        
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash of a file."""
        sha256_hash = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    def upload_document(
        self,
        file_path: str,
        tags: List[str] = None,
        category: str = None,
        description: str = None,
        overwrite: bool = False
    ) -> str:
        """
        Upload a document to the system.
        
        Args:
            file_path: Path to the file to upload
            tags: List of tags for the document
            category: Document category
            description: Document description
            overwrite: Whether to overwrite if document already exists
            
        Returns:
            Document ID of the uploaded file
        """
        source_path = Path(file_path)
        if not source_path.exists():
            raise FileNotFoundError(f"Source file not found: {file_path}")
        
        metadata = self._load_metadata()
        file_hash = self._calculate_file_hash(source_path)
        
        # Check if file already exists
        existing_doc_id = None
        for doc_id, doc_info in metadata["documents"].items():
            if doc_info.get("file_hash") == file_hash:
                existing_doc_id = doc_id
                break
        
        if existing_doc_id and not overwrite:
            logger.info(f"Document already exists with ID: {existing_doc_id}")
            return existing_doc_id
        
        # Generate new document ID
        doc_id = existing_doc_id if existing_doc_id else self._generate_document_id()
        doc_path = self._get_document_path(doc_id)
        
        # Store the file
        try:
            self._encrypt_file(source_path, doc_path)
        except Exception as e:
            logger.error(f"Failed to store document: {e}")
            raise
        
        # Update metadata
        file_type = mimetypes.guess_type(source_path)[0] or "application/octet-stream"
        file_size = os.path.getsize(source_path)
        
        document_info = {
            "original_filename": source_path.name,
            "file_type": file_type,
            "file_size": file_size,
            "file_hash": file_hash,
            "upload_date": datetime.now().isoformat(),
            "tags": tags or [],
            "category": category,
            "description": description,
            "encrypted": bool(self.encryption_key)
        }
        
        metadata["documents"][doc_id] = document_info
        self._save_metadata(metadata)
        
        logger.info(f"Document uploaded with ID: {doc_id}")
        return doc_id
    
    def download_document(self, doc_id: str, output_path: str) -> None:
        """
        Download a document from the system.
        
        Args:
            doc_id: Document ID to download
            output_path: Path to save the downloaded file
        """
        metadata = self._load_metadata()
        if doc_id not in metadata["documents"]:
            raise ValueError(f"Document ID not found: {doc_id}")
        
        doc_path = self._get_document_path(doc_id)
        if not doc_path.exists():
            raise FileNotFoundError(f"Document file not found for ID: {doc_id}")
        
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            self._decrypt_file(doc_path, output_path)
        except Exception as e:
            logger.error(f"Failed to download document: {e}")
            raise
        
        logger.info(f"Document downloaded to: {output_path}")
    
    def delete_document(self, doc_id: str) -> None:
        """
        Delete a document from the system.
        
        Args:
            doc_id: Document ID to delete
        """
        metadata = self._load_metadata()
        if doc_id not in metadata["documents"]:
            raise ValueError(f"Document ID not found: {doc_id}")
        
        doc_path = self._get_document_path(doc_id)
        try:
            if doc_path.exists():
                doc_path.unlink()
            del metadata["documents"][doc_id]
            self._save_metadata(metadata)
            logger.info(f"Document deleted: {doc_id}")
        except Exception as e:
            logger.error(f"Failed to delete document: {e}")
            raise
    
    def get_document_info(self, doc_id: str) -> Dict:
        """
        Get metadata for a document.
        
        Args:
            doc_id: Document ID to query
            
        Returns:
            Dictionary containing document metadata
        """
        metadata = self._load_metadata()
        if doc_id not in metadata["documents"]:
            raise ValueError(f"Document ID not found: {doc_id}")
        
        return metadata["documents"][doc_id]
    
    def search_documents(
        self,
        query: str = None,
        tags: List[str] = None,
        category: str = None,
        date_range: tuple = None
    ) -> List[Dict]:
        """
        Search for documents based on various criteria.
        
        Args:
            query: Text to search in filename or description
            tags: List of tags to match
            category: Category to match
            date_range: Tuple of (start_date, end_date) as datetime objects
            
        Returns:
            List of matching document metadata dictionaries
        """
        metadata = self._load_metadata()
        results = []
        
        for doc_id
