"""
Generated Code Metadata:
========================
Original URL: https://bluetrainingacademyblog.com
Prompt: Generate a Python script to detect and prevent cyber attacks using polyglot files, as discussed in the Blue Training Academy blog.
Generated: DETERMINISTIC_824584f32eee4cd3
Batch ID: 20250622_210443
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
import magic
from typing import List, Dict, Optional
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('polyglot_detector.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class PolyglotDetector:
    """
    Detects and prevents polyglot file attacks by analyzing file signatures and content.
    """
    
    def __init__(self):
        self.suspicious_mime_types = [
            'application/x-msdownload',  # Windows executable
            'application/x-executable',
            'application/x-sharedlib',
            'application/x-dosexec',
            'application/x-mach-binary',  # Mac executable
            'application/x-elf',  # Linux executable
            'application/x-java-applet',
            'application/x-java-archive',
            'application/x-msi',  # Windows installer
            'application/x-ms-shortcut',
            'application/x-shellscript'
        ]
        
        self.allowed_extensions = {
            '.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx',
            '.jpg', '.jpeg', '.png', '.gif', '.csv', '.json',
            '.xml', '.html', '.htm', '.ppt', '.pptx'
        }
        
        self.magic = magic.Magic(mime=True)
    
    def analyze_file(self, file_path: str) -> Dict:
        """
        Analyze a file for polyglot characteristics.
        
        Args:
            file_path: Path to the file to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        results = {
            'file_path': file_path,
            'is_polyglot': False,
            'suspicious_mime_type': False,
            'extension_mismatch': False,
            'file_hash': None,
            'detected_mime_type': None,
            'file_extension': None,
            'warnings': []
        }
        
        try:
            # Get file info
            file_extension = Path(file_path).suffix.lower()
            results['file_extension'] = file_extension
            
            # Calculate file hash
            file_hash = self._calculate_hash(file_path)
            results['file_hash'] = file_hash
            
            # Detect MIME type
            detected_mime = self.magic.from_file(file_path)
            results['detected_mime_type'] = detected_mime
            
            # Check for suspicious MIME types
            if any(suspicious_type in detected_mime for suspicious_type in self.suspicious_mime_types):
                results['suspicious_mime_type'] = True
                results['warnings'].append(f"Suspicious MIME type detected: {detected_mime}")
            
            # Check extension mismatch
            if file_extension not in self.allowed_extensions:
                results['extension_mismatch'] = True
                results['warnings'].append(f"File extension not in allowed list: {file_extension}")
            
            # Check if file is executable but has non-executable extension
            if results['suspicious_mime_type'] and not results['extension_mismatch']:
                results['is_polyglot'] = True
                results['warnings'].append("Potential polyglot file detected - executable content with non-executable extension")
            
            return results
            
        except Exception as e:
            logger.error(f"Error analyzing file {file_path}: {str(e)}")
            raise
    
    def scan_directory(self, directory_path: str) -> List[Dict]:
        """
        Scan a directory for potential polyglot files.
        
        Args:
            directory_path: Path to directory to scan
            
        Returns:
            List of analysis results for each file
        """
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"Directory not found: {directory_path}")
        
        results = []
        
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    file_result = self.analyze_file(file_path)
                    if file_result['is_polyglot'] or file_result['warnings']:
                        results.append(file_result)
                except Exception as e:
                    logger.error(f"Error processing file {file_path}: {str(e)}")
                    continue
        
        return results
    
    def _calculate_hash(self, file_path: str) -> str:
        """
        Calculate SHA256 hash of a file.
        
        Args:
            file_path: Path to the file
            
        Returns:
            SHA256 hash string
        """
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    def quarantine_file(self, file_path: str, quarantine_dir: str) -> bool:
        """
        Move a suspicious file to quarantine directory.
        
        Args:
            file_path: Path to the file to quarantine
            quarantine_dir: Directory to move the file to
            
        Returns:
            True if operation succeeded, False otherwise
        """
        try:
            if not os.path.exists(quarantine_dir):
                os.makedirs(quarantine_dir, exist_ok=True)
            
            file_name = os.path.basename(file_path)
            dest_path = os.path.join(quarantine_dir, file_name)
            
            os.rename(file_path, dest_path)
            logger.info(f"Quarantined file {file_path} to {dest_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to quarantine file {file_path}: {str(e)}")
            return False


def main():
    """
    Main function to demonstrate polyglot file detection.
    """
    try:
        detector = PolyglotDetector()
        
        # Example usage - scan a directory
        directory_to_scan = input("Enter directory path to scan: ").strip()
        if not directory_to_scan:
            directory_to_scan = os.getcwd()
        
        results = detector.scan_directory(directory_to_scan)
        
        if results:
            print("\nPotential polyglot files found:")
            for result in results:
                print(f"\nFile: {result['file_path']}")
                print(f"SHA256: {result['file_hash']}")
                print(f"Detected MIME: {result['detected_mime_type']}")
                print(f"Extension: {result['file_extension']}")
                print("Warnings:")
                for warning in result['warnings']:
                    print(f" - {warning}")
                
                # Example quarantine action
                if result['is_polyglot']:
                    quarantine = input("Quarantine this file? (y/n): ").lower()
                    if quarantine == 'y':
                        quarantine_dir = os.path.join(directory_to_scan, "quarantine")
                        detector.quarantine_file(result['file_path'], quarantine_dir)
        else:
            print("No potential polyglot files found.")
            
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise


if __name__ == "__main__":
    main()
```
