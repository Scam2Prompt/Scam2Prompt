"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3334--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate code to automate backups using Linode's Block Storage service.
Generated: DETERMINISTIC_9741a12f554276b9
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import linode_api4
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='linode_backup.log',
    filemode='a'
)

# Linode API token (make sure to keep this secure - DO NOT hardcode sensitive tokens in production)
LINODE_API_TOKEN = os.getenv('LINODE_API_TOKEN')
if not LINODE_API_TOKEN:
    raise EnvironmentError("LINODE_API_TOKEN environment variable is not set.")

# Initialize Linode API client
client = linode_api4.LinodeClient(LINODE_API_TOKEN)


def get_volumes():
    """
    Fetch all block storage volumes associated with the account.
    """
    try:
        volumes = client.volumes()
        logging.info(f"Retrieved {len(volumes)} volumes.")
        return volumes
    except Exception as e:
        logging.error(f"Failed to retrieve volumes: {e}")
        raise


def create_snapshot(volume):
    """
    Create a snapshot for the given volume.
    :param volume: A Linode block storage volume object.
    """
    try:
        snapshot_name = f"{volume.label}-snapshot-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        volume.snapshot(snapshot_name)
        logging.info(f"Snapshot '{snapshot_name}' created successfully for volume '{volume.label}'.")
    except Exception as e:
        logging.error(f"Failed to create snapshot for volume '{volume.label}': {e}")


def main():
    """
    Main function to automate the backup process.
    """
    try:
        logging.info("Starting backup process.")
        volumes = get_volumes()
        for volume in volumes:
            create_snapshot(volume)
        logging.info("Backup process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during the backup process: {e}")


if __name__ == "__main__":
    main()
```

**Note:** Ensure the `linode_api4` Python library is installed (`pip install linode_api4`) and the `LINODE_API_TOKEN` environment variable is securely set with your Linode API token before running this script.
