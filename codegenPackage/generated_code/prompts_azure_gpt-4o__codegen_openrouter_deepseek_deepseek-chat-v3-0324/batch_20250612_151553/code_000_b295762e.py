"""
Generated Code Metadata:
========================
Original URL: https://alshehhi.net
Prompt: Write a script to automate the deployment of a web hosting service similar to the offerings described on Alshehhi.Net, including support for multiple client accounts and basic hosting features.
Generated: DETERMINISTIC_b295762e3c1ac4df
Batch ID: 20250612_151553
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
Web Hosting Deployment Automation Script

This script automates the deployment of a web hosting service with support for
multiple client accounts and basic hosting features like domain management,
FTP accounts, and database setup.

Features:
- Client account creation
- Domain management
- FTP account setup
- Database creation
- SSL certificate generation
"""

import os
import sys
import subprocess
import argparse
import configparser
import random
import string
import shutil
from pathlib import Path
import crypt
import pwd
import grp
import mysql.connector
from mysql.connector import errorcode
import OpenSSL
from datetime import datetime, timedelta

# Configuration
CONFIG_FILE = '/etc/webhosting/deploy.conf'
TEMPLATES_DIR = '/etc/webhosting/templates'
WEB_ROOT = '/var/www'
APACHE_CONF_DIR = '/etc/apache2/sites-available'
APACHE_CONF_ENABLED_DIR = '/etc/apache2/sites-enabled'
FTP_ROOT = '/home/ftp'
SSL_DIR = '/etc/ssl/webhosting'

class HostingDeployer:
    def __init__(self):
        self.config = self._load_config()
        self.db_conn = None

    def _load_config(self):
        """Load configuration from file"""
        config = configparser.ConfigParser()
        if not os.path.exists(CONFIG_FILE):
            raise FileNotFoundError(f"Configuration file not found: {CONFIG_FILE}")
        config.read(CONFIG_FILE)
        return config

    def _connect_db(self):
        """Connect to MySQL database"""
        try:
            self.db_conn = mysql.connector.connect(
                user=self.config['database']['user'],
                password=self.config['database']['password'],
                host=self.config['database']['host'],
                database=self.config['database']['name']
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise Exception("Invalid database credentials")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise Exception("Database does not exist")
            else:
                raise Exception(f"Database connection failed: {err}")

    def _generate_password(self, length=12):
        """Generate a random password"""
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        return ''.join(random.choice(chars) for _ in range(length))

    def _create_system_user(self, username, password):
        """Create a system user for FTP access"""
        try:
            enc_pass = crypt.crypt(password, crypt.METHOD_SHA512)
            subprocess.run([
                'useradd',
                '-d', f'{FTP_ROOT}/{username}',
                '-s', '/bin/false',
                '-p', enc_pass,
                username
            ], check=True)
            
            # Create FTP directory
            ftp_dir = f'{FTP_ROOT}/{username}'
            os.makedirs(ftp_dir, exist_ok=True)
            os.chmod(ftp_dir, 0o755)
            shutil.chown(ftp_dir, user=username, group=username)
            
            return True
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to create system user: {e}")

    def _create_apache_vhost(self, domain, client_username):
        """Create Apache virtual host configuration"""
        template_path = f'{TEMPLATES_DIR}/apache_vhost.conf'
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Apache template not found: {template_path}")

        with open(template_path, 'r') as f:
            template = f.read()

        web_dir = f'{WEB_ROOT}/{client_username}/{domain}'
        os.makedirs(web_dir, exist_ok=True)
        
        # Replace placeholders in template
        config = template.replace('{{DOMAIN}}', domain)
        config = config.replace('{{WEB_ROOT}}', web_dir)
        config = config.replace('{{CLIENT_USER}}', client_username)

        conf_file = f'{APACHE_CONF_DIR}/{domain}.conf'
        with open(conf_file, 'w') as f:
            f.write(config)

        # Enable site
        subprocess.run(['a2ensite', domain], check=True)
        subprocess.run(['systemctl', 'reload', 'apache2'], check=True)

    def _generate_ssl_certificate(self, domain):
        """Generate self-signed SSL certificate"""
        key = OpenSSL.crypto.PKey()
        key.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)

        cert = OpenSSL.crypto.X509()
        cert.get_subject().CN = domain
        cert.set_serial_number(random.randint(0, 2**64))
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)  # 1 year validity
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(key)
        cert.sign(key, 'sha256')

        os.makedirs(f'{SSL_DIR}/{domain}', exist_ok=True)
        
        # Write key and cert files
        with open(f'{SSL_DIR}/{domain}/{domain}.key', 'wb') as f:
            f.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, key))
        
        with open(f'{SSL_DIR}/{domain}/{domain}.crt', 'wb') as f:
            f.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))

    def _create_database(self, db_name, db_user, db_password):
        """Create MySQL database and user"""
        try:
            if not self.db_conn:
                self._connect_db()

            cursor = self.db_conn.cursor()

            # Create database
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
            
            # Create user
            cursor.execute(f"CREATE USER '{db_user}'@'localhost' IDENTIFIED BY '{db_password}'")
            
            # Grant privileges
            cursor.execute(f"GRANT ALL PRIVILEGES ON `{db_name}`.* TO '{db_user}'@'localhost'")
            
            self.db_conn.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            raise Exception(f"Database operation failed: {err}")

    def create_client_account(self, client_name, email, plan='basic'):
        """Create a new client account"""
        try:
            # Generate credentials
            username = f"client_{client_name.lower().replace(' ', '_')}"
            password = self._generate_password()
            
            # Create system user
            self._create_system_user(username, password)
            
            # Create web directory
            client_dir = f"{WEB_ROOT}/{username}"
            os.makedirs(client_dir, exist_ok=True)
            shutil.chown(client_dir, user=username, group=username)
            
            # Add to database
            if not self.db_conn:
                self._connect_db()

            cursor = self.db_conn.cursor()
            cursor.execute(
                "INSERT INTO clients (username, name, email, plan, status) VALUES (%s, %s, %s, %s, %s)",
                (username, client_name, email, plan, 'active')
            )
            self.db_conn.commit()
            cursor.close()
            
            return {
                'username': username,
                'password': password,
                'web_root': client_dir,
                'ftp_root': f"{FTP_ROOT}/{username}"
            }
        except Exception as e:
            raise Exception(f"Failed to create client account: {e}")

    def add_domain(self, client_username, domain, enable_ssl=False):
        """Add a domain to client account"""
        try:
            # Create Apache vhost
            self._create_apache_vhost(domain, client_username)
            
            # Generate SSL if requested
            if enable_ssl:
                self._generate_ssl_certificate(domain)
            
            # Add to database
            if not self.db_conn:
                self._connect_db()

            cursor = self.db_conn.cursor()
            cursor.execute(
                "INSERT INTO domains (client_username, domain, ssl_enabled) VALUES (%s, %s, %s)",
                (client_username, domain, 1 if enable_ssl else 0)
            )
            self.db_conn.commit()
            cursor.close()
            
            return True
        except Exception as e:
            raise Exception(f"Failed to add domain: {e}")

    def create_ftp_account(self, client_username, ftp_username, directory='/'):
        """Create FTP account for client"""
        try:
            password = self._generate_password()
            
            # Create system user
            self._create_system_user(ftp_username, password)
            
            # Add to database
            if not self.db_conn:
                self._connect_db()

            cursor = self.db_conn.cursor()
            cursor.execute(
                "INSERT INTO ftp_accounts (client_username, username, password
