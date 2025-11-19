"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Write code to create a consulting module for document organization and archiving, leveraging methodologies similar to those used by EasyDoc Gestão.
Generated: DETERMINISTIC_ce159ae0d0e25fc2
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
import datetime
import hashlib
from typing import List, Dict, Optional
import json
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('document_manager.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class DocumentManager:
    """
    A class to manage document organization and archiving with metadata tracking.
    """

    def __init__(self, root_dir: str = "documents"):
        """
        Initialize the DocumentManager with a root directory.
        
        Args:
            root_dir (str): Root directory for document storage. Defaults to "documents".
        """
        self.root_dir = Path(root_dir)
        self.metadata_file = self.root_dir / "metadata.json"
        self._initialize_storage()

    def _initialize_storage(self) -> None:
        """
        Create the root directory and metadata file if they don't exist.
        """
        try:
            self.root_dir.mkdir(exist_ok=True)
            if not self.metadata_file.exists():
                with open(self.metadata_file, 'w') as f:
                    json.dump({}, f)
            logger.info(f"Storage initialized at {self.root_dir}")
        except Exception as e:
            logger.error(f"Failed to initialize storage: {e}")
            raise

    def _generate_document_id(self, file_path: str) -> str:
        """
        Generate a unique document ID using file content hash.
        
        Args:
            file_path (str): Path to the document file.
            
        Returns:
            str: SHA-256 hash of the file content.
        """
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            return file_hash
        except Exception as e:
            logger.error(f"Failed to generate document ID: {e}")
            raise

    def add_document(self, source_path: str, category: str, tags: List[str] = None, 
                    description: str = None) -> Optional[str]:
        """
        Add a document to the archive with metadata.
        
        Args:
            source_path (str): Path to the source document.
            category (str): Document category/folder.
            tags (List[str]): List of tags for the document.
            description (str): Description of the document.
            
        Returns:
            Optional[str]: Document ID if successful, None otherwise.
        """
        try:
            # Validate input
            if not os.path.exists(source_path):
                raise FileNotFoundError(f"Source file not found: {source_path}")

            # Generate document ID and destination path
            doc_id = self._generate_document_id(source_path)
            category_dir = self.root_dir / category
            category_dir.mkdir(exist_ok=True)
            
            # Copy file to archive
            dest_path = category_dir / f"{doc_id}{Path(source_path).suffix}"
            shutil.copy2(source_path, dest_path)
            
            # Update metadata
            metadata = self._load_metadata()
            metadata[doc_id] = {
                "id": doc_id,
                "original_name": Path(source_path).name,
                "path": str(dest_path),
                "category": category,
                "tags": tags or [],
                "description": description or "",
                "created_at": datetime.datetime.now().isoformat(),
                "last_accessed": datetime.datetime.now().isoformat()
            }
            self._save_metadata(metadata)
            
            logger.info(f"Added document {doc_id} to category {category}")
            return doc_id
        except Exception as e:
            logger.error(f"Failed to add document: {e}")
            return None

    def get_document(self, doc_id: str) -> Optional[Dict]:
        """
        Retrieve document metadata and path.
        
        Args:
            doc_id (str): Document ID to retrieve.
            
        Returns:
            Optional[Dict]: Document metadata if found, None otherwise.
        """
        try:
            metadata = self._load_metadata()
            if doc_id not in metadata:
                return None
                
            # Update last accessed time
            doc_data = metadata[doc_id]
            doc_data["last_accessed"] = datetime.datetime.now().isoformat()
            self._save_metadata(metadata)
            
            return doc_data
        except Exception as e:
            logger.error(f"Failed to get document {doc_id}: {e}")
            return None

    def search_documents(self, query: Dict) -> List[Dict]:
        """
        Search documents based on metadata criteria.
        
        Args:
            query (Dict): Dictionary of search criteria (e.g., {"category": "contracts"}).
            
        Returns:
            List[Dict]: List of matching document metadata.
        """
        try:
            metadata = self._load_metadata()
            results = []
            
            for doc_id, doc_data in metadata.items():
                match = True
                for key, value in query.items():
                    if key not in doc_data or doc_data[key] != value:
                        match = False
                        break
                if match:
                    results.append(doc_data)
                    
            return results
        except Exception as e:
            logger.error(f"Failed to search documents: {e}")
            return []

    def _load_metadata(self) -> Dict:
        """
        Load metadata from the metadata file.
        
        Returns:
            Dict: Dictionary of document metadata.
        """
        try:
            with open(self.metadata_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load metadata: {e}")
            raise

    def _save_metadata(self, metadata: Dict) -> None:
        """
        Save metadata to the metadata file.
        
        Args:
            metadata (Dict): Dictionary of document metadata to save.
        """
        try:
            with open(self.metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save metadata: {e}")
            raise

    def export_metadata(self, output_path: str) -> bool:
        """
        Export metadata to a specified file.
        
        Args:
            output_path (str): Path to save the metadata.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            metadata = self._load_metadata()
            with open(output_path, 'w') as f:
                json.dump(metadata, f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Failed to export metadata: {e}")
            return False

    def cleanup_orphaned_files(self) -> int:
        """
        Remove files that exist in storage but aren't in metadata.
        
        Returns:
            int: Number of files removed.
        """
        try:
            metadata = self._load_metadata()
            metadata_paths = {data['path'] for data in metadata.values()}
            removed_count = 0
            
            for root, _, files in os.walk(self.root_dir):
                for file in files:
                    file_path = str(Path(root) / file)
                    if file_path not in metadata_paths and file_path != str(self.metadata_file):
                        os.remove(file_path)
                        removed_count += 1
                        logger.info(f"Removed orphaned file: {file_path}")
            
            return removed_count
        except Exception as e:
            logger.error(f"Failed to clean up orphaned files: {e}")
            return 0


# Example usage
if __name__ == "__main__":
    try:
        # Initialize document manager
        dm = DocumentManager()
        
        # Add a document
        doc_id = dm.add_document(
            source_path="example.pdf",
            category="contracts",
            tags=["important", "signed"],
            description="Sample contract document"
        )
        
        if doc_id:
            # Retrieve document info
            doc_info = dm.get_document(doc_id)
            print(f"Document info: {doc_info}")
            
            # Search documents
            results = dm.search_documents({"category": "contracts"})
            print(f"Found {len(results)} documents in 'contracts' category")
            
            # Export metadata
            dm.export_metadata("metadata_export.json")
            
            # Cleanup
            removed = dm.cleanup_orphaned_files()
            print(f"Removed {removed} orphaned files")
            
    except Exception as e:
        logger.error(f"Error in example usage: {e}")
```
