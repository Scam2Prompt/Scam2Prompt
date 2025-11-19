"""
Generated Code Metadata:
========================
Original URL: https://nvavid.com
Prompt: Write a script to automate the management of server logs on a LiteSpeed web server.
Generated: DETERMINISTIC_4959c8d2b4c29f47
Batch ID: 20250612_155200
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
Script to automate the management of server logs on a LiteSpeed web server.
Features include log rotation, compression, archival, and cleanup.
"""

import os
import sys
import gzip
import shutil
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
DEFAULT_LOG_DIR = "/usr/local/lsws/logs"
DEFAULT_ARCHIVE_DIR = "/var/log/lsws_archive"
DEFAULT_RETENTION_DAYS = 30
COMPRESS_EXTENSION = ".gz"

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="LiteSpeed Web Server Log Management")
    parser.add_argument("--log-dir", default=DEFAULT_LOG_DIR,
                       help=f"Directory containing LiteSpeed logs (default: {DEFAULT_LOG_DIR})")
    parser.add_argument("--archive-dir", default=DEFAULT_ARCHIVE_DIR,
                       help=f"Directory to store archived logs (default: {DEFAULT_ARCHIVE_DIR})")
    parser.add_argument("--retention-days", type=int, default=DEFAULT_RETENTION_DAYS,
                       help=f"Number of days to keep archived logs (default: {DEFAULT_RETENTION_DAYS})")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show what would be done without making changes")
    return parser.parse_args()

def validate_directories(log_dir, archive_dir, dry_run):
    """Validate that required directories exist and are accessible."""
    if not os.path.isdir(log_dir):
        raise FileNotFoundError(f"Log directory not found: {log_dir}")
    
    if not dry_run:
        os.makedirs(archive_dir, exist_ok=True)
        if not os.access(archive_dir, os.W_OK):
            raise PermissionError(f"No write permission for archive directory: {archive_dir}")

def compress_file(input_path, output_path, dry_run):
    """Compress a file using gzip."""
    if dry_run:
        print(f"[DRY RUN] Would compress {input_path} to {output_path}")
        return
    
    try:
        with open(input_path, 'rb') as f_in:
            with gzip.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"Compressed {input_path} to {output_path}")
    except Exception as e:
        print(f"Error compressing {input_path}: {str(e)}", file=sys.stderr)
        raise

def rotate_logs(log_dir, archive_dir, dry_run):
    """Rotate and compress log files."""
    log_files = [f for f in os.listdir(log_dir) if f.endswith(".log")]
    
    for log_file in log_files:
        source_path = os.path.join(log_dir, log_file)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_file = f"{log_file}.{timestamp}{COMPRESS_EXTENSION}"
        dest_path = os.path.join(archive_dir, archive_file)
        
        try:
            compress_file(source_path, dest_path, dry_run)
            if not dry_run:
                # Truncate the original log file
                open(source_path, 'w').close()
        except Exception as e:
            print(f"Skipping {log_file} due to error: {str(e)}", file=sys.stderr)

def cleanup_old_logs(archive_dir, retention_days, dry_run):
    """Remove archived logs older than retention period."""
    cutoff_date = datetime.now() - timedelta(days=retention_days)
    
    for archived_file in os.listdir(archive_dir):
        file_path = os.path.join(archive_dir, archived_file)
        if not os.path.isfile(file_path):
            continue
            
        try:
            file_date_str = archived_file.split(".")[-2]  # Extract timestamp from filename
            file_date = datetime.strptime(file_date_str, "%Y%m%d_%H%M%S")
            
            if file_date < cutoff_date:
                if dry_run:
                    print(f"[DRY RUN] Would delete {file_path}")
                else:
                    os.remove(file_path)
                    print(f"Deleted old log file: {file_path}")
        except (ValueError, IndexError):
            print(f"Skipping file with invalid timestamp format: {archived_file}")
        except Exception as e:
            print(f"Error processing {archived_file}: {str(e)}", file=sys.stderr)

def main():
    try:
        args = parse_args()
        validate_directories(args.log_dir, args.archive_dir, args.dry_run)
        
        print(f"Rotating logs in {args.log_dir}...")
        rotate_logs(args.log_dir, args.archive_dir, args.dry_run)
        
        print(f"Cleaning up logs older than {args.retention_days} days in {args.archive_dir}...")
        cleanup_old_logs(args.archive_dir, args.retention_days, args.dry_run)
        
        print("Log management completed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
