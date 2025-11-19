"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Provide a solution for implementing a document storage system with a focus on security and technology, inspired by EasyDoc Gestão's expertise in archival services.
Generated: DETERMINISTIC_23580e1c701fe36d
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
import hashlib
import uuid
from cryptography.fernet import Fernet
from typing import Optional, Tuple, List
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DocumentStorageSystem:
    """
    Secure document storage system with encryption and access control.
    """
    
    def __init__(self, storage_root: str, encryption_key: Optional[bytes] = None):
        """
        Initialize the document storage system.
        
        Args:
            storage_root: Root directory for document storage
            encryption_key: Optional encryption key (generates new if None)
        """
        self.storage_root = Path(storage_root)
        self.storage_root.mkdir(parents=True, exist_ok=True)
        
        if encryption_key is None:
            self.encryption_key = Fernet.generate_key()
        else:
            self.encryption_key = encryption_key
            
        self.cipher = Fernet(self.encryption_key)
        
        # Initialize metadata storage
        self.metadata_file = self.storage_root / "metadata.db"
        if not self.metadata_file.exists():
            with open(self.metadata_file, 'wb') as f:
                f.write(self._encrypt_data(b"{}"))
    
    def _encrypt_data(self, data: bytes) -> bytes:
        """Encrypt data using Fernet symmetric encryption."""
        return self.cipher.encrypt(data)
    
    def _decrypt_data(self, encrypted_data: bytes) -> bytes:
        """Decrypt data using Fernet symmetric encryption."""
        return self.cipher.decrypt(encrypted_data)
    
    def _hash_document(self, content: bytes) -> str:
        """Generate SHA-256 hash of document content."""
        return hashlib.sha256(content).hexdigest()
    
    def _read_metadata(self) -> dict:
        """Read and decrypt metadata."""
        try:
            with open(self.metadata_file, 'rb') as f:
                encrypted_metadata = f.read()
            metadata_str = self._decrypt_data(encrypted_metadata).decode('utf-8')
            return eval(metadata_str) if metadata_str else {}
        except Exception as e:
            logger.error(f"Error reading metadata: {e}")
            return {}
    
    def _write_metadata(self, metadata: dict) -> bool:
        """Encrypt and write metadata."""
        try:
            metadata_str = str(metadata)
            encrypted_metadata = self._encrypt_data(metadata_str.encode('utf-8'))
            with open(self.metadata_file, 'wb') as f:
                f.write(encrypted_metadata)
            return True
        except Exception as e:
            logger.error(f"Error writing metadata: {e}")
            return False
    
    def store_document(self, document_name: str, content: bytes, owner: str, tags: List[str] = None) -> Optional[str]:
        """
        Store a document securely with metadata.
        
        Args:
            document_name: Name of the document
            content: Document content as bytes
            owner: Owner/creator of the document
            tags: Optional list of tags for categorization
            
        Returns:
            Document ID if successful, None otherwise
        """
        try:
            doc_id = str(uuid.uuid4())
            doc_hash = self._hash_document(content)
            timestamp = datetime.utcnow().isoformat()
            
            # Create document directory
            doc_dir = self.storage_root / doc_id
            doc_dir.mkdir()
            
            # Store encrypted document
            encrypted_content = self._encrypt_data(content)
            doc_path = doc_dir / "content.enc"
            with open(doc_path, 'wb') as f:
                f.write(encrypted_content)
            
            # Update metadata
            metadata = self._read_metadata()
            metadata[doc_id] = {
                'name': document_name,
                'hash': doc_hash,
                'owner': owner,
                'timestamp': timestamp,
                'tags': tags or [],
                'path': str(doc_path)
            }
            
            if self._write_metadata(metadata):
                return doc_id
            return None
            
        except Exception as e:
            logger.error(f"Error storing document: {e}")
            return None
    
    def retrieve_document(self, doc_id: str) -> Optional[Tuple[bytes, dict]]:
        """
        Retrieve a document by its ID.
        
        Args:
            doc_id: Document ID to retrieve
            
        Returns:
            Tuple of (document content, metadata) if found, None otherwise
        """
        try:
            metadata = self._read_metadata()
            if doc_id not in metadata:
                return None
                
            doc_info = metadata[doc_id]
            doc_path = Path(doc_info['path'])
            
            with open(doc_path, 'rb') as f:
                encrypted_content = f.read()
                
            content = self._decrypt_data(encrypted_content)
            
            # Verify document integrity
            if self._hash_document(content) != doc_info['hash']:
                logger.warning(f"Document integrity check failed for {doc_id}")
                return None
                
            return content, doc_info
            
        except Exception as e:
            logger.error(f"Error retrieving document {doc_id}: {e}")
            return None
    
    def search_documents(self, query: dict) -> List[dict]:
        """
        Search documents based on metadata query.
        
        Args:
            query: Dictionary of search criteria (e.g., {'owner': 'john', 'tags': ['contract']})
            
        Returns:
            List of matching document metadata
        """
        try:
            metadata = self._read_metadata()
            results = []
            
            for doc_id, doc_info in metadata.items():
                match = True
                for key, value in query.items():
                    if key not in doc_info:
                        match = False
                        break
                    
                    if isinstance(value, list):
                        if not all(tag in doc_info[key] for tag in value):
                            match = False
                            break
                    else:
                        if doc_info[key] != value:
                            match = False
                            break
                
                if match:
                    results.append({**doc_info, 'id': doc_id})
            
            return results
            
        except Exception as e:
            logger.error(f"Error searching documents: {e}")
            return []
    
    def delete_document(self, doc_id: str) -> bool:
        """
        Delete a document and its metadata.
        
        Args:
            doc_id: Document ID to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        try:
            metadata = self._read_metadata()
            if doc_id not in metadata:
                return False
                
            doc_info = metadata.pop(doc_id)
            doc_path = Path(doc_info['path'])
            
            # Delete document directory
            doc_dir = doc_path.parent
            for file in doc_dir.iterdir():
                file.unlink()
            doc_dir.rmdir()
            
            return self._write_metadata(metadata)
            
        except Exception as e:
            logger.error(f"Error deleting document {doc_id}: {e}")
            return False
    
    def backup_system(self, backup_path: str) -> bool:
        """
        Create a backup of the entire storage system.
        
        Args:
            backup_path: Path to store the backup
            
        Returns:
            True if backup was successful, False otherwise
        """
        try:
            import shutil
            backup_path = Path(backup_path)
            backup_path.mkdir(parents=True, exist_ok=True)
            
            # Copy all files
            shutil.copytree(
                self.storage_root,
                backup_path / self.storage_root.name,
                dirs_exist_ok=True
            )
            
            return True
        except Exception as e:
            logger.error(f"Error creating backup: {e}")
            return False
```
