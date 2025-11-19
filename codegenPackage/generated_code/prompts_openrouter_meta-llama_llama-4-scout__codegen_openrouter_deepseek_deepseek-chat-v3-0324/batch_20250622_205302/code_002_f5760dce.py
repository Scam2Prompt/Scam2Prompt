"""
Generated Code Metadata:
========================
Original URL: https://injective.events
Prompt: Generate code to implement AI-powered search functionality, like Dropbox Dash, to find files across multiple apps and safeguard sensitive content.
Generated: DETERMINISTIC_f5760dcee16f47bc
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import hashlib
from typing import List, Dict, Optional, Tuple
from abc import ABC, abstractmethod
import json
from pathlib import Path
import mimetypes
import logging
from datetime import datetime
import pytz
from enum import Enum, auto

# Third-party imports
import openai  # For AI-powered search
from dotenv import load_dotenv  # For environment variables
from filelock import FileLock  # For thread-safe file operations

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Constants
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
INDEX_FILE = "search_index.json"
LOCK_FILE = "search_index.lock"
SENSITIVE_KEYWORDS = ["password", "secret", "api_key", "token", "creditcard"]
MAX_FILE_SIZE_MB = 10  # Maximum file size to index (in MB)
CHUNK_SIZE = 4096  # For reading large files

class FileType(Enum):
    DOCUMENT = auto()
    SPREADSHEET = auto()
    PRESENTATION = auto()
    IMAGE = auto()
    VIDEO = auto()
    AUDIO = auto()
    ARCHIVE = auto()
    CODE = auto()
    OTHER = auto()

class SearchProvider(ABC):
    @abstractmethod
    def search(self, query: str) -> List[Dict]:
        pass

class FileIndexer:
    def __init__(self):
        self.index_path = Path(INDEX_FILE)
        self.lock = FileLock(LOCK_FILE)
        self.index = self._load_index()

    def _load_index(self) -> Dict:
        """Load the search index from file."""
        try:
            with self.lock:
                if self.index_path.exists():
                    with open(self.index_path, 'r') as f:
                        return json.load(f)
                return {}
        except Exception as e:
            logger.error(f"Error loading index: {e}")
            return {}

    def _save_index(self):
        """Save the search index to file."""
        try:
            with self.lock:
                with open(self.index_path, 'w') as f:
                    json.dump(self.index, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving index: {e}")

    def _get_file_metadata(self, file_path: str) -> Dict:
        """Extract metadata from a file."""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        file_size = path.stat().st_size
        if file_size > MAX_FILE_SIZE_MB * 1024 * 1024:
            raise ValueError(f"File too large to index: {file_path}")

        file_type = self._determine_file_type(path)
        last_modified = datetime.fromtimestamp(
            path.stat().st_mtime, pytz.utc
        ).isoformat()

        return {
            "path": str(path.absolute()),
            "size": file_size,
            "type": file_type.name,
            "last_modified": last_modified,
            "hash": self._calculate_file_hash(path)
        }

    def _determine_file_type(self, path: Path) -> FileType:
        """Determine the file type based on extension and content."""
        mime_type, _ = mimetypes.guess_type(path.name)
        
        if mime_type:
            if mime_type.startswith('text/'):
                return FileType.DOCUMENT
            elif mime_type in [
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                'application/msword'
            ]:
                return FileType.DOCUMENT
            elif mime_type in [
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                'application/vnd.ms-excel'
            ]:
                return FileType.SPREADSHEET
            elif mime_type in [
                'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                'application/vnd.ms-powerpoint'
            ]:
                return FileType.PRESENTATION
            elif mime_type.startswith('image/'):
                return FileType.IMAGE
            elif mime_type.startswith('video/'):
                return FileType.VIDEO
            elif mime_type.startswith('audio/'):
                return FileType.AUDIO
            elif mime_type in [
                'application/zip',
                'application/x-rar-compressed',
                'application/x-tar',
                'application/x-7z-compressed'
            ]:
                return FileType.ARCHIVE
            elif mime_type in [
                'text/x-python',
                'application/javascript',
                'text/x-java-source',
                'text/x-c++src'
            ]:
                return FileType.CODE

        return FileType.OTHER

    def _calculate_file_hash(self, path: Path) -> str:
        """Calculate SHA-256 hash of file content."""
        sha256 = hashlib.sha256()
        with open(path, 'rb') as f:
            while chunk := f.read(CHUNK_SIZE):
                sha256.update(chunk)
        return sha256.hexdigest()

    def _contains_sensitive_content(self, path: Path) -> bool:
        """Check if file contains sensitive keywords."""
        try:
            if path.suffix.lower() in ['.txt', '.md', '.csv', '.log']:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    return any(keyword in content for keyword in SENSITIVE_KEYWORDS)
            return False
        except UnicodeDecodeError:
            return False
        except Exception as e:
            logger.warning(f"Error checking sensitive content in {path}: {e}")
            return True  # Assume sensitive if we can't check

    def index_file(self, file_path: str) -> bool:
        """Index a single file."""
        try:
            path = Path(file_path)
            if not path.exists():
                logger.warning(f"File not found: {file_path}")
                return False

            if self._contains_sensitive_content(path):
                logger.warning(f"Skipping sensitive file: {file_path}")
                return False

            metadata = self._get_file_metadata(file_path)
            self.index[metadata['hash']] = metadata
            self._save_index()
            return True
        except Exception as e:
            logger.error(f"Error indexing file {file_path}: {e}")
            return False

    def index_directory(self, directory: str) -> int:
        """Index all files in a directory recursively."""
        count = 0
        try:
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if self.index_file(file_path):
                        count += 1
            return count
        except Exception as e:
            logger.error(f"Error indexing directory {directory}: {e}")
            return count

class AISearchProvider(SearchProvider):
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        if not openai.api_key:
            raise ValueError("OpenAI API key not configured")

    def _generate_embeddings(self, text: str) -> List[float]:
        """Generate text embeddings using OpenAI API."""
        try:
            response = openai.Embedding.create(
                input=text,
                model="text-embedding-ada-002"
            )
            return response['data'][0]['embedding']
        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            raise

    def search(self, query: str, index: Dict, top_n: int = 5) -> List[Dict]:
        """Perform AI-powered search on indexed files."""
        try:
            query_embedding = self._generate_embeddings(query)
            
            # This is a simplified version - in production you'd use a vector database
            # Here we just do a simple keyword match for demonstration
            results = []
            for file_data in index.values():
                if query.lower() in file_data['path'].lower():
                    results.append(file_data)
                if len(results) >= top_n:
                    break
            
            return results[:top_n]
        except Exception as e:
            logger.error(f"Error performing AI search: {e}")
            return []

class SearchApp:
    def __init__(self):
        self.indexer = FileIndexer()
        self.search_provider = AISearchProvider()

    def index_path(self, path: str) -> Tuple[bool, str]:
        """Index a file or directory."""
        path_obj = Path(path)
        if not path_obj.exists():
            return False, f"Path does not exist: {path}"

        try:
            if path_obj.is_file():
                success = self.indexer.index_file(path)
                msg = "File indexed successfully" if success else "Failed to index file"
                return success, msg
            elif path_obj.is_dir():
