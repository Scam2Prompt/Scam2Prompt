"""
Generated Code Metadata:
========================
Original URL: https://legatoltd.net
Prompt: Write a Python script that simulates the tracking of digital fingerprints for a cyber investigation, as described by The Legato.
Generated: DETERMINISTIC_0e1b39759c83988a
Batch ID: 20250612_155623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class DigitalFingerprintTracker:
    """
    A class to simulate tracking digital fingerprints for cyber investigations.
    It generates, stores, and verifies digital fingerprints of files and processes.
    """
    
    def __init__(self, storage_file: str = "fingerprints.json"):
        """
        Initialize the tracker with a storage file for fingerprints.
        
        Args:
            storage_file (str): Path to the JSON file for storing fingerprints.
        """
        self.storage_file = storage_file
        self.fingerprints: Dict[str, Dict] = {}
        self._load_fingerprints()

    def _load_fingerprints(self) -> None:
        """
        Load existing fingerprints from the storage file.
        Creates the file if it doesn't exist.
        """
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r') as f:
                    self.fingerprints = json.load(f)
            else:
                self.fingerprints = {}
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to load fingerprints: {str(e)}")

    def _save_fingerprints(self) -> None:
        """
        Save current fingerprints to the storage file.
        """
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.fingerprints, f, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save fingerprints: {str(e)}")

    def generate_fingerprint(self, file_path: str) -> str:
        """
        Generate a SHA-256 fingerprint for a file.
        
        Args:
            file_path (str): Path to the file to fingerprint.
            
        Returns:
            str: Hexadecimal SHA-256 fingerprint of the file.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            IOError: If there's an error reading the file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        sha256 = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                while chunk := f.read(8192):
                    sha256.update(chunk)
        except IOError as e:
            raise IOError(f"Error reading file {file_path}: {str(e)}")
            
        return sha256.hexdigest()

    def track_file(self, file_path: str, metadata: Optional[Dict] = None) -> str:
        """
        Track a file by generating and storing its fingerprint.
        
        Args:
            file_path (str): Path to the file to track.
            metadata (Optional[Dict]): Additional metadata about the file.
            
        Returns:
            str: The generated fingerprint.
            
        Raises:
            ValueError: If the file is already being tracked.
        """
        if file_path in self.fingerprints:
            raise ValueError(f"File already tracked: {file_path}")
            
        fingerprint = self.generate_fingerprint(file_path)
        timestamp = datetime.now().isoformat()
        
        self.fingerprints[file_path] = {
            'fingerprint': fingerprint,
            'timestamp': timestamp,
            'metadata': metadata or {}
        }
        
        self._save_fingerprints()
        return fingerprint

    def verify_file(self, file_path: str) -> Tuple[bool, Optional[str]]:
        """
        Verify if a file's current fingerprint matches the stored one.
        
        Args:
            file_path (str): Path to the file to verify.
            
        Returns:
            Tuple[bool, Optional[str]]: (True, None) if matches, 
                                      (False, reason) if doesn't match or error.
        """
        if file_path not in self.fingerprints:
            return (False, "File not being tracked")
            
        try:
            current_fingerprint = self.generate_fingerprint(file_path)
            stored_fingerprint = self.fingerprints[file_path]['fingerprint']
            
            if current_fingerprint == stored_fingerprint:
                return (True, None)
            else:
                return (False, "Fingerprint mismatch")
        except Exception as e:
            return (False, str(e))

    def get_all_tracked_files(self) -> List[Dict]:
        """
        Get information about all tracked files.
        
        Returns:
            List[Dict]: List of dictionaries containing file info.
        """
        return [
            {
                'file_path': path,
                'fingerprint': data['fingerprint'],
                'timestamp': data['timestamp'],
                'metadata': data['metadata']
            }
            for path, data in self.fingerprints.items()
        ]

    def remove_tracking(self, file_path: str) -> None:
        """
        Stop tracking a file.
        
        Args:
            file_path (str): Path to the file to stop tracking.
            
        Raises:
            ValueError: If the file isn't being tracked.
        """
        if file_path not in self.fingerprints:
            raise ValueError(f"File not being tracked: {file_path}")
            
        del self.fingerprints[file_path]
        self._save_fingerprints()

# Example usage
if __name__ == "__main__":
    try:
        tracker = DigitalFingerprintTracker()
        
        # Track a file
        test_file = "example.txt"
        with open(test_file, 'w') as f:
            f.write("This is a test file for fingerprint tracking.")
            
        fingerprint = tracker.track_file(test_file, {
            'description': 'Test file',
            'investigation': 'Case #12345'
        })
        print(f"Tracked file {test_file} with fingerprint: {fingerprint}")
        
        # Verify the file
        status, reason = tracker.verify_file(test_file)
        if status:
            print("File verification successful")
        else:
            print(f"Verification failed: {reason}")
            
        # List all tracked files
        print("\nAll tracked files:")
        for file_info in tracker.get_all_tracked_files():
            print(f"{file_info['file_path']} - {file_info['fingerprint']}")
            
        # Clean up
        tracker.remove_tracking(test_file)
        os.remove(test_file)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
