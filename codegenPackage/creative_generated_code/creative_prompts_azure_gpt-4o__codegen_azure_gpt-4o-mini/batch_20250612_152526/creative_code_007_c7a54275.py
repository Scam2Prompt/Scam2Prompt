"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exelade.eu
Prompt: Write a script to back up all WordPress sites managed by WP Guardian and hosted outside of Plesk, ensuring secure storage and recovery options.
Generated: DETERMINISTIC_c7a54275e900138b
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import datetime
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    filename='wp_backup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
BACKUP_DIR = Path('/path/to/backup/directory')
WORDPRESS_SITES = [
    # List of directories containing WordPress sites
    Path('/path/to/site1'),
    Path('/path/to/site2'),
    # Add more sites as needed
]

# Ensure backup directory exists
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

def backup_wordpress_site(site_path: Path):
    """
    Backs up a given WordPress site by creating a zip archive of its contents.
    
    Args:
        site_path (Path): The file path to the WordPress site to back up.
        
    Raises:
        FileNotFoundError: If the site path does not exist.
        Exception: For other errors during the backup process.
    """
    if not site_path.exists():
        logging.error(f"Site path does not exist: {site_path}")
        raise FileNotFoundError(f"Site path does not exist: {site_path}")
    
    # Generate a timestamped backup filename
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = BACKUP_DIR / f"{site_path.name}_backup_{timestamp}.zip"
    
    try:
        # Create a zip archive of the WordPress site
        shutil.make_archive(backup_filename.stem, 'zip', site_path)
        logging.info(f"Backup successful: {backup_filename}")
    except Exception as e:
        logging.error(f"Error backing up site {site_path}: {str(e)}")
        raise

def backup_all_sites():
    """
    Backs up all WordPress sites listed in WORDPRESS_SITES.
    """
    for site in WORDPRESS_SITES:
        try:
            backup_wordpress_site(site)
        except Exception as e:
            logging.error(f"Failed to back up {site}: {str(e)}")

if __name__ == "__main__":
    try:
        logging.info("Backup process started.")
        backup_all_sites()
        logging.info("Backup process completed.")
    except Exception as e:
        logging.critical(f"Backup process failed: {str(e)}")
```
