"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Create a function to duplicate inspection reports, optionally excluding photos, as described in the BeSoft App Vistoria documentation.
Generated: DETERMINISTIC_0ef27f6b97485667
Batch ID: 20250612_152924
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
from typing import Dict, Any, Optional
import json
from datetime import datetime

def duplicate_inspection_report(
    original_report_path: str,
    new_report_path: str,
    exclude_photos: bool = False,
    metadata_updates: Optional[Dict[str, Any]] = None
) -> bool:
    """
    Duplicates an inspection report, optionally excluding photos and updating metadata.
    
    Args:
        original_report_path: Path to the original report directory
        new_report_path: Path where the new report will be created
        exclude_photos: If True, photos won't be copied to the new report
        metadata_updates: Dictionary of metadata fields to update in the new report
        
    Returns:
        bool: True if duplication was successful, False otherwise
        
    Raises:
        FileNotFoundError: If original report doesn't exist
        PermissionError: If lacking permissions to read/write files
        ValueError: If paths are invalid or metadata is malformed
    """
    try:
        # Validate paths
        if not os.path.isdir(original_report_path):
            raise FileNotFoundError(f"Original report directory not found: {original_report_path}")
            
        if os.path.exists(new_report_path):
            raise FileExistsError(f"Target report path already exists: {new_report_path}")
            
        # Create new report directory structure
        os.makedirs(new_report_path)
        
        # Copy all files except photos if excluded
        for item in os.listdir(original_report_path):
            original_item_path = os.path.join(original_report_path, item)
            new_item_path = os.path.join(new_report_path, item)
            
            if exclude_photos and item.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                continue
                
            if os.path.isfile(original_item_path):
                shutil.copy2(original_item_path, new_item_path)
            elif os.path.isdir(original_item_path):
                shutil.copytree(original_item_path, new_item_path)
        
        # Update metadata if provided
        metadata_path = os.path.join(new_report_path, 'metadata.json')
        if os.path.exists(metadata_path) and metadata_updates:
            with open(metadata_path, 'r+', encoding='utf-8') as f:
                metadata = json.load(f)
                
                # Apply updates
                metadata.update(metadata_updates)
                
                # Update timestamp
                metadata['last_modified'] = datetime.utcnow().isoformat() + 'Z'
                
                # Write back to file
                f.seek(0)
                json.dump(metadata, f, indent=2, ensure_ascii=False)
                f.truncate()
                
        return True
        
    except Exception as e:
        # Clean up partially created report if something went wrong
        if os.path.exists(new_report_path):
            shutil.rmtree(new_report_path, ignore_errors=True)
        raise
```
