"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3334--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate code to automate backups using Linode's Block Storage service.
Generated: DETERMINISTIC_9741a12f554276b9
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Linode Block Storage Backup Automation Script

This script automates the process of creating backups for Linode Block Storage volumes.
It uses the Linode API to create snapshots of specified volumes on a scheduled basis.

Requirements:
- Python 3.6+
- linode-api4 package (pip install linode-api4)
- Linode API token with appropriate permissions
"""

import os
import argparse
from datetime import datetime, timedelta
from linode_api4 import LinodeClient, ApiError
import logging
import sys
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('linode_backup.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class LinodeBackupAutomation:
    def __init__(self, api_token: str):
        """
        Initialize the Linode backup client
        
        Args:
            api_token: Linode API token with read/write permissions
        """
        self.client = LinodeClient(api_token)
        self._validate_token()

    def _validate_token(self):
        """Validate the API token by making a test request"""
        try:
            self.client.account()
        except ApiError as e:
            logger.error(f"Failed to authenticate with Linode API: {e}")
            raise

    def list_volumes(self) -> List[str]:
        """List all available block storage volumes"""
        try:
            volumes = self.client.volumes()
            return [vol.label for vol in volumes]
        except ApiError as e:
            logger.error(f"Failed to list volumes: {e}")
            raise

    def create_snapshot(self, volume_label: str, snapshot_label: Optional[str] = None) -> bool:
        """
        Create a snapshot of a specified volume
        
        Args:
            volume_label: Label of the volume to snapshot
            snapshot_label: Optional custom label for the snapshot
            
        Returns:
            bool: True if snapshot was created successfully
        """
        if not snapshot_label:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            snapshot_label = f"{volume_label}-backup-{timestamp}"

        try:
            volume = self.client.volumes(volume_label)[0]
            snapshot = volume.snapshot(snapshot_label)
            logger.info(f"Created snapshot '{snapshot_label}' for volume '{volume_label}'")
            return True
        except IndexError:
            logger.error(f"Volume '{volume_label}' not found")
            return False
        except ApiError as e:
            logger.error(f"Failed to create snapshot for volume '{volume_label}': {e}")
            return False

    def cleanup_snapshots(self, volume_label: str, days_to_keep: int = 30) -> int:
        """
        Delete snapshots older than specified days
        
        Args:
            volume_label: Label of the volume to clean up snapshots for
            days_to_keep: Number of days to retain snapshots
            
        Returns:
            int: Number of snapshots deleted
        """
        try:
            volume = self.client.volumes(volume_label)[0]
            snapshots = volume.snapshots()
            
            cutoff_date = datetime.now() - timedelta(days=days_to_keep)
            deleted_count = 0
            
            for snapshot in snapshots:
                if datetime.strptime(snapshot.created, "%Y-%m-%dT%H:%M:%S") < cutoff_date:
                    snapshot.delete()
                    logger.info(f"Deleted old snapshot '{snapshot.label}' created on {snapshot.created}")
                    deleted_count += 1
            
            return deleted_count
        except IndexError:
            logger.error(f"Volume '{volume_label}' not found")
            return 0
        except ApiError as e:
            logger.error(f"Failed to clean up snapshots for volume '{volume_label}': {e}")
            return 0

def main():
    parser = argparse.ArgumentParser(description="Linode Block Storage Backup Automation")
    parser.add_argument('--api-token', help="Linode API token", required=False)
    parser.add_argument('--volume', help="Volume label to backup", required=True)
    parser.add_argument('--snapshot-label', help="Custom snapshot label", required=False)
    parser.add_argument('--cleanup', action='store_true', help="Enable snapshot cleanup")
    parser.add_argument('--retention-days', type=int, default=30, help="Days to retain snapshots")
    
    args = parser.parse_args()
    
    # Get API token from environment if not provided
    api_token = args.api_token or os.getenv('LINODE_API_TOKEN')
    if not api_token:
        logger.error("Linode API token must be provided via --api-token or LINODE_API_TOKEN environment variable")
        sys.exit(1)
    
    try:
        backup = LinodeBackupAutomation(api_token)
        
        # Create new snapshot
        success = backup.create_snapshot(args.volume, args.snapshot_label)
        if not success:
            sys.exit(1)
        
        # Clean up old snapshots if enabled
        if args.cleanup:
            deleted = backup.cleanup_snapshots(args.volume, args.retention_days)
            logger.info(f"Deleted {deleted} old snapshots")
            
    except Exception as e:
        logger.error(f"Backup operation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
