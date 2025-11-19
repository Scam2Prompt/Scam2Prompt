"""
Generated Code Metadata:
========================
Original URL: https://sigr.io
Prompt: Create a sample project demonstrating SIGR.IO's functionality for code version management.
Generated: DETERMINISTIC_09c15736dabe7054
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
SIGR.IO Code Version Management Demo

This script demonstrates basic functionality for code version management
using SIGR.IO's approach. It includes features for:
- Tracking code changes
- Managing versions
- Reverting changes
- Comparing versions
"""

import os
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class CodeVersionManager:
    """
    A simple code version management system inspired by SIGR.IO's approach.
    """
    
    def __init__(self, repo_path: str = "."):
        """
        Initialize the version manager with a repository path.
        
        Args:
            repo_path: Path to the code repository (defaults to current directory)
        """
        self.repo_path = os.path.abspath(repo_path)
        self.versions_dir = os.path.join(self.repo_path, ".sigrio_versions")
        self.current_version = 0
        self.version_history = []
        
        # Initialize version directory if it doesn't exist
        if not os.path.exists(self.versions_dir):
            os.makedirs(self.versions_dir)
            self._save_metadata()
    
    def _get_file_hash(self, file_path: str) -> str:
        """
        Calculate SHA-256 hash of a file's content.
        
        Args:
            file_path: Path to the file
            
        Returns:
            SHA-256 hash string
        """
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    def _scan_files(self) -> Dict[str, str]:
        """
        Scan all files in the repository and calculate their hashes.
        
        Returns:
            Dictionary mapping file paths to their hashes
        """
        file_hashes = {}
        for root, _, files in os.walk(self.repo_path):
            # Skip version directory
            if root.startswith(self.versions_dir):
                continue
                
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, self.repo_path)
                file_hashes[relative_path] = self._get_file_hash(file_path)
        return file_hashes
    
    def _save_metadata(self) -> None:
        """
        Save version metadata to disk.
        """
        metadata = {
            "current_version": self.current_version,
            "version_history": self.version_history
        }
        
        with open(os.path.join(self.versions_dir, "metadata.json"), 'w') as f:
            json.dump(metadata, f, indent=2)
    
    def _load_metadata(self) -> None:
        """
        Load version metadata from disk.
        """
        metadata_path = os.path.join(self.versions_dir, "metadata.json")
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
                self.current_version = metadata["current_version"]
                self.version_history = metadata["version_history"]
    
    def create_version(self, message: str = "") -> int:
        """
        Create a new version snapshot of the current code state.
        
        Args:
            message: Description of changes in this version
            
        Returns:
            Version number of the created snapshot
        """
        # Get current file states
        file_hashes = self._scan_files()
        
        # Create version entry
        version = {
            "version": self.current_version + 1,
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "files": file_hashes
        }
        
        # Save version data
        version_file = os.path.join(self.versions_dir, f"version_{version['version']}.json")
        with open(version_file, 'w') as f:
            json.dump(version, f, indent=2)
        
        # Update metadata
        self.current_version = version['version']
        self.version_history.append({
            "version": version['version'],
            "timestamp": version['timestamp'],
            "message": message
        })
        self._save_metadata()
        
        return self.current_version
    
    def get_version(self, version_num: int) -> Optional[Dict]:
        """
        Retrieve information about a specific version.
        
        Args:
            version_num: Version number to retrieve
            
        Returns:
            Version data dictionary or None if not found
        """
        version_file = os.path.join(self.versions_dir, f"version_{version_num}.json")
        if not os.path.exists(version_file):
            return None
            
        with open(version_file, 'r') as f:
            return json.load(f)
    
    def list_versions(self) -> List[Dict]:
        """
        List all available versions.
        
        Returns:
            List of version metadata dictionaries
        """
        return self.version_history.copy()
    
    def compare_versions(self, version_a: int, version_b: int) -> Dict[str, List[str]]:
        """
        Compare files between two versions.
        
        Args:
            version_a: First version number
            version_b: Second version number
            
        Returns:
            Dictionary with:
            - 'added': Files added between versions
            - 'removed': Files removed between versions
            - 'modified': Files modified between versions
        """
        version_a_data = self.get_version(version_a)
        version_b_data = self.get_version(version_b)
        
        if not version_a_data or not version_b_data:
            raise ValueError("One or both versions not found")
        
        files_a = set(version_a_data['files'].keys())
        files_b = set(version_b_data['files'].keys())
        
        result = {
            'added': list(files_b - files_a),
            'removed': list(files_a - files_b),
            'modified': []
        }
        
        common_files = files_a & files_b
        for file in common_files:
            if version_a_data['files'][file] != version_b_data['files'][file]:
                result['modified'].append(file)
                
        return result
    
    def revert_to_version(self, version_num: int) -> bool:
        """
        Revert the codebase to a specific version.
        
        Args:
            version_num: Version number to revert to
            
        Returns:
            True if successful, False otherwise
        """
        version_data = self.get_version(version_num)
        if not version_data:
            return False
            
        # Get current files for comparison
        current_files = self._scan_files()
        
        # Revert files
        for file_path, file_hash in version_data['files'].items():
            abs_path = os.path.join(self.repo_path, file_path)
            
            # Find the version where this file was last modified
            source_version = self._find_file_version(file_path, file_hash, version_num)
            if not source_version:
                continue
                
            source_file = os.path.join(self.versions_dir, f"file_{source_version}_{file_path.replace('/', '_')}")
            
            # Copy file content back
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
            with open(source_file, 'rb') as src, open(abs_path, 'wb') as dst:
                dst.write(src.read())
        
        # Remove files that don't exist in target version
        for file_path in set(current_files.keys()) - set(version_data['files'].keys()):
            abs_path = os.path.join(self.repo_path, file_path)
            if os.path.exists(abs_path):
                os.remove(abs_path)
        
        # Update current version
        self.current_version = version_num
        self._save_metadata()
        
        return True
    
    def _find_file_version(self, file_path: str, target_hash: str, max_version: int) -> Optional[int]:
        """
        Find the most recent version where a file had the target hash.
        
        Args:
            file_path: Path to the file
            target_hash: Hash to match
            max_version: Maximum version to search
            
        Returns:
            Version number where the file last matched the hash, or None
        """
        for version in range(max_version, 0, -1):
            version_data = self.get_version(version)
            if not version_data:
                continue
                
            if file_path in version_data['files'] and version_data['files'][file_path] == target_hash:
                return version
                
        return None

def main():
    """Demonstrate the version management functionality."""
    print("SIGR.IO Code Version Management Demo")
    print("-----------------------------------\n")
    
    # Initialize version manager
    manager = CodeVersionManager()
    
    # Create initial version
    print("Creating initial version...")
    v1 = manager.create_version("Initial version")
    print(f"Created version {v1}\n")
    
    # Simulate making changes
    print("Simulating code changes...")
    with open("example.py", "w") as f:
        f.write("print('Hello, World!')")
    
    # Create second version
    print("Creating second version...")
    v2 = manager.create_version("Added example.py")
    print(f"Created version {v2}\n")
    
    # List versions
    print("Version history:")
    for version in manager.list_versions():
        print
