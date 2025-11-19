"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Construct a library that helps users manage their business licenses and incorporation documents, inspired by the offerings of Hispanic Services.
Generated: DETERMINISTIC_276e55aaaa0994cf
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from typing import Dict, List, Optional, Union
from pathlib import Path

class DocumentManager:
    """
    A library to manage business licenses and incorporation documents.
    Provides functionalities to add, update, delete, and retrieve documents.
    """

    def __init__(self, storage_dir: str = "documents"):
        """
        Initialize the DocumentManager with a storage directory.
        
        Args:
            storage_dir (str): Directory to store document data. Defaults to "documents".
        """
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(exist_ok=True)
        self.metadata_file = self.storage_dir / "metadata.json"
        
        # Initialize metadata if it doesn't exist
        if not self.metadata_file.exists():
            with open(self.metadata_file, "w") as f:
                json.dump({"documents": {}}, f)

    def _load_metadata(self) -> Dict:
        """Load metadata from the metadata file."""
        try:
            with open(self.metadata_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load metadata: {e}")

    def _save_metadata(self, metadata: Dict) -> None:
        """Save metadata to the metadata file."""
        try:
            with open(self.metadata_file, "w") as f:
                json.dump(metadata, f, indent=2)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to save metadata: {e}")

    def add_document(
        self,
        document_id: str,
        document_type: str,
        document_name: str,
        content: Union[str, bytes],
        expiration_date: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> None:
        """
        Add a new document to the manager.
        
        Args:
            document_id (str): Unique identifier for the document.
            document_type (str): Type of document (e.g., "license", "incorporation").
            document_name (str): Name of the document.
            content (Union[str, bytes]): Content of the document (text or binary).
            expiration_date (Optional[str]): Expiration date in YYYY-MM-DD format. Defaults to None.
            tags (Optional[List[str]]): List of tags for the document. Defaults to None.
        
        Raises:
            ValueError: If document_id already exists or invalid expiration_date.
        """
        metadata = self._load_metadata()
        
        if document_id in metadata["documents"]:
            raise ValueError(f"Document with ID {document_id} already exists.")
        
        if expiration_date:
            try:
                datetime.strptime(expiration_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Invalid expiration_date format. Use YYYY-MM-DD.")
        
        # Save document content
        document_path = self.storage_dir / f"{document_id}.dat"
        try:
            if isinstance(content, str):
                with open(document_path, "w") as f:
                    f.write(content)
            else:
                with open(document_path, "wb") as f:
                    f.write(content)
        except IOError as e:
            raise RuntimeError(f"Failed to save document content: {e}")
        
        # Update metadata
        metadata["documents"][document_id] = {
            "type": document_type,
            "name": document_name,
            "path": str(document_path),
            "expiration_date": expiration_date,
            "tags": tags or [],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }
        
        self._save_metadata(metadata)

    def get_document(self, document_id: str) -> Dict:
        """
        Retrieve a document's metadata and content.
        
        Args:
            document_id (str): ID of the document to retrieve.
        
        Returns:
            Dict: Document metadata and content.
        
        Raises:
            ValueError: If document_id does not exist.
        """
        metadata = self._load_metadata()
        
        if document_id not in metadata["documents"]:
            raise ValueError(f"Document with ID {document_id} does not exist.")
        
        doc_meta = metadata["documents"][document_id]
        document_path = Path(doc_meta["path"])
        
        try:
            if doc_meta["type"] in ["license", "incorporation"]:  # Assume text
                with open(document_path, "r") as f:
                    content = f.read()
            else:  # Assume binary
                with open(document_path, "rb") as f:
                    content = f.read()
        except IOError as e:
            raise RuntimeError(f"Failed to read document content: {e}")
        
        return {
            "metadata": doc_meta,
            "content": content,
        }

    def update_document(
        self,
        document_id: str,
        content: Optional[Union[str, bytes]] = None,
        expiration_date: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> None:
        """
        Update a document's content or metadata.
        
        Args:
            document_id (str): ID of the document to update.
            content (Optional[Union[str, bytes]]): New content. Defaults to None.
            expiration_date (Optional[str]): New expiration date. Defaults to None.
            tags (Optional[List[str]]): New tags. Defaults to None.
        
        Raises:
            ValueError: If document_id does not exist or invalid expiration_date.
        """
        metadata = self._load_metadata()
        
        if document_id not in metadata["documents"]:
            raise ValueError(f"Document with ID {document_id} does not exist.")
        
        if expiration_date:
            try:
                datetime.strptime(expiration_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Invalid expiration_date format. Use YYYY-MM-DD.")
        
        doc_meta = metadata["documents"][document_id]
        
        # Update content if provided
        if content is not None:
            document_path = Path(doc_meta["path"])
            try:
                if isinstance(content, str):
                    with open(document_path, "w") as f:
                        f.write(content)
                else:
                    with open(document_path, "wb") as f:
                        f.write(content)
            except IOError as e:
                raise RuntimeError(f"Failed to update document content: {e}")
        
        # Update metadata
        if expiration_date:
            doc_meta["expiration_date"] = expiration_date
        if tags is not None:
            doc_meta["tags"] = tags
        doc_meta["updated_at"] = datetime.now().isoformat()
        
        self._save_metadata(metadata)

    def delete_document(self, document_id: str) -> None:
        """
        Delete a document and its metadata.
        
        Args:
            document_id (str): ID of the document to delete.
        
        Raises:
            ValueError: If document_id does not exist.
            RuntimeError: If deletion fails.
        """
        metadata = self._load_metadata()
        
        if document_id not in metadata["documents"]:
            raise ValueError(f"Document with ID {document_id} does not exist.")
        
        doc_meta = metadata["documents"][document_id]
        document_path = Path(doc_meta["path"])
        
        try:
            document_path.unlink()
        except IOError as e:
            raise RuntimeError(f"Failed to delete document content: {e}")
        
        # Update metadata
        del metadata["documents"][document_id]
        self._save_metadata(metadata)

    def list_documents(
        self,
        document_type: Optional[str] = None,
        expired: Optional[bool] = None,
        tag: Optional[str] = None,
    ) -> List[Dict]:
        """
        List documents filtered by optional criteria.
        
        Args:
            document_type (Optional[str]): Filter by document type. Defaults to None.
            expired (Optional[bool]): Filter by expiration status. Defaults to None.
            tag (Optional[str]): Filter by tag. Defaults to None.
        
        Returns:
            List[Dict]: List of document metadata matching the criteria.
        """
        metadata = self._load_metadata()
        documents = []
        
        for doc_id, doc_meta in metadata["documents"].items():
            include = True
            
            if document_type and doc_meta["type"] != document_type:
                include = False
            
            if expired is not None and doc_meta["expiration_date"]:
                exp_date = datetime.strptime(doc_meta["expiration_date"], "%Y-%m-%d")
                is_expired = exp_date < datetime.now()
                if expired != is_expired:
                    include = False
            
            if tag and tag not in doc_meta.get("tags", []):
                include = False
            
            if include:
                documents.append({"id": doc_id, **doc_meta})
        
        return documents

    def get_expiring_documents(self, days_threshold: int = 30) -> List[Dict]:
