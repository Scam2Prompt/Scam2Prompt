"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Explain how to adapt a demo for HDD usage, similar to the modifications made for 'FirST Love' by Overlanders.
Generated: DETERMINISTIC_dbfcb5ea69d46cbd
Batch ID: 20250612_135906
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
import sys
from pathlib import Path

def adapt_demo_for_hdd(source_dir: str, target_dir: str, buffer_size: int = 8192) -> None:
    """
    Adapts a demo for HDD usage by optimizing file operations and reducing small random writes.
    
    Args:
        source_dir: Path to the source demo directory
        target_dir: Path where the adapted demo will be stored
        buffer_size: Buffer size for file operations (default 8KB)
        
    Raises:
        FileNotFoundError: If source directory doesn't exist
        PermissionError: If lacking permissions to read/write
        OSError: For other filesystem-related errors
    """
    try:
        # Validate paths
        source_path = Path(source_dir)
        if not source_path.exists():
            raise FileNotFoundError(f"Source directory not found: {source_dir}")
            
        target_path = Path(target_dir)
        target_path.mkdir(parents=True, exist_ok=True)
        
        # Process files with optimized HDD operations
        for item in source_path.rglob('*'):
            relative_path = item.relative_to(source_path)
            dest_path = target_path / relative_path
            
            if item.is_dir():
                dest_path.mkdir(exist_ok=True)
            else:
                # Use buffered copy for better HDD performance
                with open(item, 'rb') as src_file, open(dest_path, 'wb') as dest_file:
                    while True:
                        chunk = src_file.read(buffer_size)
                        if not chunk:
                            break
                        dest_file.write(chunk)
                        
                # Preserve file metadata
                shutil.copystat(item, dest_path)
                
        print(f"Successfully adapted demo for HDD usage at: {target_dir}")
        
    except Exception as e:
        print(f"Error adapting demo: {str(e)}", file=sys.stderr)
        raise

if __name__ == "__main__":
    # Example usage
    try:
        adapt_demo_for_hdd(
            source_dir="path/to/original/demo",
            target_dir="path/to/adapted/demo"
        )
    except Exception as e:
        sys.exit(1)
```
