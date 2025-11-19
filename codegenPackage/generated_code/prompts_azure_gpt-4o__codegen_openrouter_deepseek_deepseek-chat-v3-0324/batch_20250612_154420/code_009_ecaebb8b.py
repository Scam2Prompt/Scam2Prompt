"""
Generated Code Metadata:
========================
Original URL: https://linkbonus.net
Prompt: Generate code to back up and restore Nginx Proxy Manager configurations programmatically.
Generated: DETERMINISTIC_ecaebb8b67b88411
Batch ID: 20250612_154420
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
Nginx Proxy Manager Configuration Backup and Restore Tool

This script allows backing up and restoring Nginx Proxy Manager configurations
including SSL certificates, proxy hosts, and other settings.

Usage:
    nginx_proxy_manager_tool.py backup <backup_dir> [--db-password=<password>]
    nginx_proxy_manager_tool.py restore <backup_dir> [--db-password=<password>]
"""

import os
import sys
import shutil
import json
import subprocess
import argparse
from datetime import datetime
from pathlib import Path
import tarfile
import psycopg2
from psycopg2 import sql

# Configuration
DEFAULT_DB_NAME = "npm"
DEFAULT_DB_USER = "npm"
DEFAULT_DB_HOST = "localhost"
DEFAULT_DB_PORT = 5432
BACKUP_FILES = [
    "/app/data/nginx/proxy_hosts",
    "/app/data/nginx/redirection_hosts",
    "/app/data/nginx/dead_hosts",
    "/app/data/nginx/streams",
    "/app/data/nginx/custom",
    "/app/data/letsencrypt",
    "/app/data/ssl"
]

class NPMBackupRestore:
    def __init__(self, db_password=None):
        self.db_password = db_password
        self.backup_dir = None
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def validate_backup_dir(self, backup_dir):
        """Validate backup directory exists and is writable"""
        backup_path = Path(backup_dir)
        if not backup_path.exists():
            backup_path.mkdir(parents=True, exist_ok=True)
        if not os.access(backup_dir, os.W_OK):
            raise PermissionError(f"No write permissions for directory: {backup_dir}")
        return backup_path

    def backup_database(self, backup_path):
        """Backup PostgreSQL database to SQL file"""
        db_backup_file = backup_path / f"npm_db_{self.timestamp}.sql"
        
        try:
            conn = psycopg2.connect(
                dbname=DEFAULT_DB_NAME,
                user=DEFAULT_DB_USER,
                password=self.db_password,
                host=DEFAULT_DB_HOST,
                port=DEFAULT_DB_PORT
            )
            
            with conn.cursor() as cursor:
                with open(db_backup_file, 'w') as f:
                    cursor.copy_expert(
                        sql.SQL("COPY (SELECT * FROM {}) TO STDOUT").format(
                            sql.Identifier('proxy_hosts')
                        ), f
                    )
            
            conn.close()
            return db_backup_file
        except psycopg2.Error as e:
            raise Exception(f"Database backup failed: {e}")

    def backup_files(self, backup_path):
        """Backup configuration files"""
        files_backup = backup_path / f"npm_files_{self.timestamp}.tar.gz"
        
        try:
            with tarfile.open(files_backup, "w:gz") as tar:
                for item in BACKUP_FILES:
                    if os.path.exists(item):
                        tar.add(item, arcname=os.path.basename(item))
            return files_backup
        except Exception as e:
            raise Exception(f"File backup failed: {e}")

    def backup(self, backup_dir):
        """Perform complete backup of Nginx Proxy Manager"""
        try:
            backup_path = self.validate_backup_dir(backup_dir)
            print(f"Starting backup to {backup_path}")
            
            # Backup database
            db_backup = self.backup_database(backup_path)
            print(f"Database backup created: {db_backup}")
            
            # Backup files
            files_backup = self.backup_files(backup_path)
            print(f"Files backup created: {files_backup}")
            
            # Create metadata
            metadata = {
                "timestamp": self.timestamp,
                "version": self.get_npm_version(),
                "backup_type": "full",
                "files": {
                    "database": str(db_backup),
                    "config_files": str(files_backup)
                }
            }
            
            metadata_file = backup_path / f"npm_metadata_{self.timestamp}.json"
            with open(metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            print("Backup completed successfully")
            return True
        except Exception as e:
            print(f"Backup failed: {str(e)}", file=sys.stderr)
            return False

    def restore_database(self, backup_file):
        """Restore PostgreSQL database from backup"""
        try:
            conn = psycopg2.connect(
                dbname=DEFAULT_DB_NAME,
                user=DEFAULT_DB_USER,
                password=self.db_password,
                host=DEFAULT_DB_HOST,
                port=DEFAULT_DB_PORT
            )
            
            # Truncate tables before restore
            with conn.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE proxy_hosts CASCADE")
            
            # Restore data
            with conn.cursor() as cursor:
                with open(backup_file, 'r') as f:
                    cursor.copy_expert(
                        sql.SQL("COPY {} FROM STDIN").format(
                            sql.Identifier('proxy_hosts')
                        ), f
                    )
            
            conn.commit()
            conn.close()
            return True
        except psycopg2.Error as e:
            raise Exception(f"Database restore failed: {e}")

    def restore_files(self, backup_file):
        """Restore configuration files from backup"""
        try:
            # Extract files to temporary location first
            temp_dir = Path("/tmp/npm_restore_temp")
            if temp_dir.exists():
                shutil.rmtree(temp_dir)
            temp_dir.mkdir()
            
            with tarfile.open(backup_file, "r:gz") as tar:
                tar.extractall(path=temp_dir)
            
            # Copy files to their original locations
            for item in BACKUP_FILES:
                src = temp_dir / os.path.basename(item)
                if src.exists():
                    if os.path.exists(item):
                        if os.path.isdir(item):
                            shutil.rmtree(item)
                        else:
                            os.remove(item)
                    shutil.move(str(src), item)
            
            shutil.rmtree(temp_dir)
            return True
        except Exception as e:
            raise Exception(f"File restore failed: {e}")

    def restore(self, backup_dir):
        """Perform complete restore of Nginx Proxy Manager"""
        try:
            backup_path = Path(backup_dir)
            if not backup_path.exists():
                raise FileNotFoundError(f"Backup directory not found: {backup_dir}")
            
            # Find the latest backup
            metadata_files = sorted(backup_path.glob("npm_metadata_*.json"), reverse=True)
            if not metadata_files:
                raise FileNotFoundError("No backup metadata files found")
            
            with open(metadata_files[0]) as f:
                metadata = json.load(f)
            
            print(f"Restoring backup from {metadata['timestamp']}")
            
            # Restore database
            db_backup = backup_path / metadata['files']['database']
            if not db_backup.exists():
                raise FileNotFoundError(f"Database backup file not found: {db_backup}")
            
            self.restore_database(db_backup)
            print("Database restored successfully")
            
            # Restore files
            files_backup = backup_path / metadata['files']['config_files']
            if not files_backup.exists():
                raise FileNotFoundError(f"Files backup not found: {files_backup}")
            
            self.restore_files(files_backup)
            print("Configuration files restored successfully")
            
            # Restart Nginx Proxy Manager
            self.restart_npm()
            print("Nginx Proxy Manager restarted")
            
            print("Restore completed successfully")
            return True
        except Exception as e:
            print(f"Restore failed: {str(e)}", file=sys.stderr)
            return False

    def get_npm_version(self):
        """Get Nginx Proxy Manager version"""
        try:
            result = subprocess.run(["npm", "--version"], capture_output=True, text=True)
            return result.stdout.strip()
        except:
            return "unknown"

    def restart_npm(self):
        """Restart Nginx Proxy Manager service"""
        try:
            subprocess.run(["systemctl", "restart", "nginx-proxy-manager"], check=True)
        except subprocess.CalledProcessError:
            print("Warning: Could not restart Nginx Proxy Manager service", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Nginx Proxy Manager Backup and Restore Tool")
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Create a backup')
    backup_parser.add_argument('backup_dir', help='Directory to store backup files')
    backup_parser.add_argument('--db-password', help='PostgreSQL database password')
    
    # Restore command
    restore_parser = subparsers.add_parser('restore', help='Restore from backup')
    restore_
