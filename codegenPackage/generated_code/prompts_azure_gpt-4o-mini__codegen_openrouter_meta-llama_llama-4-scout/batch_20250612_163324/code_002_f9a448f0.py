"""
Generated Code Metadata:
========================
Original URL: https://meghbd.com
Prompt: Write a Python script to automate the backup of a website hosted on a Linux server with RAID protected disk.
Generated: DETERMINISTIC_f9a448f0df4fb7e8
Batch ID: 20250612_163324
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
Website Backup Script

Automates the backup of a website hosted on a Linux server with RAID protected disk.

Usage:
    python website_backup.py [-h] [-c CONFIG_FILE]

Arguments:
    -h, --help            show this help message and exit
    -c CONFIG_FILE, --config CONFIG_FILE
                        path to configuration file

Author:
    [Your Name]
"""

import argparse
import os
import shutil
import datetime
import tarfile
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_args():
    parser = argparse.ArgumentParser(description='Website Backup Script')
    parser.add_argument('-c', '--config', help='path to configuration file', required=True)
    return parser.parse_args()

def load_config(config_file):
    try:
        with open(config_file, 'r') as f:
            config = {
                'website_root': f.readline().strip(),
                'backup_dir': f.readline().strip(),
                'exclude': f.read().splitlines()
            }
            return config
    except FileNotFoundError:
        logging.error(f"Configuration file '{config_file}' not found.")
        exit(1)

def create_backup_dir(backup_dir):
    try:
        os.makedirs(backup_dir, exist_ok=True)
    except OSError as e:
        logging.error(f"Failed to create backup directory: {e}")
        exit(1)

def backup_website(config):
    website_root = config['website_root']
    backup_dir = config['backup_dir']
    exclude = config['exclude']

    # Create timestamped backup file
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f"website_backup_{timestamp}.tar.gz"

    try:
        with tarfile.open(os.path.join(backup_dir, backup_file), 'w:gz', compresslevel=9) as tar:
            tar.add(website_root, arcdata=None, recursive=True, exclude=exclude)
        logging.info(f"Backup created: {backup_file}")
    except tarfile.TarError as e:
        logging.error(f"Failed to create backup: {e}")
        exit(1)

def cleanup_old_backups(backup_dir, keep_last=7):
    try:
        backups = [f for f in os.listdir(backup_dir) if f.startswith('website_backup_') and f.endswith('.tar.gz')]
        backups.sort()
        for backup in backups[:-keep_last]:
            os.remove(os.path.join(backup_dir, backup))
            logging.info(f"Removed old backup: {backup}")
    except Exception as e:
        logging.error(f"Failed to clean up old backups: {e}")

def main():
    args = parse_args()
    config = load_config(args.config)
    create_backup_dir(config['backup_dir'])
    backup_website(config)
    cleanup_old_backups(config['backup_dir'])

if __name__ == '__main__':
    main()
```

**Config File Format:**
```
/path/to/website/root
/path/to/backup/directory
/path/to/exclude1
/path/to/exclude2
...
```

**Example Usage:**

1. Create a configuration file `config.txt` with the above format.
2. Run the script: `python website_backup.py -c config.txt`
