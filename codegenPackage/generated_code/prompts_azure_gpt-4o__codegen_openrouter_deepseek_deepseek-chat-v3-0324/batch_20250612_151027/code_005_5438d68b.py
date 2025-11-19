"""
Generated Code Metadata:
========================
Original URL: https://mylovelyplanet.xyz
Prompt: Generate a configuration file for a web hosting control panel using CentOS-WebPanel to manage VPS servers.
Generated: DETERMINISTIC_5438d68b756a2448
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```yaml
# CentOS-WebPanel Configuration File
# This file configures the web hosting control panel for VPS servers

# System Settings
system:
  hostname: "vps.example.com"
  timezone: "UTC"
  admin_email: "admin@example.com"
  language: "en_US.UTF-8"

# Web Server Configuration
webserver:
  type: "nginx_apache"  # Options: apache, nginx, nginx_apache
  php_version: "7.4"    # Supported: 5.6, 7.0, 7.1, 7.2, 7.3, 7.4, 8.0
  apache_port: "8080"
  nginx_port: "80"
  ssl_port: "443"
  mod_security: true
  autoindex: false

# Database Settings
database:
  mysql_version: "5.7"  # Supported: 5.5, 5.6, 5.7, 8.0
  root_password: "secure_password_here"
  remote_access: false
  max_connections: "100"

# DNS Settings
dns:
  enabled: true
  nameserver1: "ns1.example.com"
  nameserver2: "ns2.example.com"
  nameserver_ip1: "192.168.1.1"
  nameserver_ip2: "192.168.1.2"

# Security Settings
security:
  firewall: "csf"       # Options: csf, firewalld, none
  ssh_port: "2222"
  brute_force_protection: true
  fail2ban: true
  mod_evasive: true

# Mail Server Configuration
mail:
  server_type: "exim_dovecot"  # Options: exim, exim_dovecot
  smtp_port: "25"
  smtps_port: "465"
  imap_port: "143"
  imaps_port: "993"
  pop3_port: "110"
  pop3s_port: "995"
  antivirus: "clamav"
  spam_filter: "spamassassin"

# Backup Settings
backup:
  enabled: true
  frequency: "daily"    # Options: daily, weekly, monthly
  retention: "30"       # Days to retain backups
  remote_backup: false
  remote_server: ""
  remote_path: ""
  remote_user: ""
  remote_password: ""

# Monitoring Settings
monitoring:
  enabled: true
  email_alerts: true
  cpu_threshold: "90"
  memory_threshold: "90"
  disk_threshold: "90"

# PHP Settings
php:
  memory_limit: "256M"
  max_execution_time: "300"
  upload_max_filesize: "64M"
  post_max_size: "64M"
  max_input_vars: "1000"
  disable_functions: "exec,passthru,shell_exec,system"

# Logging Settings
logging:
  enabled: true
  log_rotation: "weekly"
  keep_logs: "4"        # Weeks to keep logs
  log_level: "info"     # Options: debug, info, warning, error, critical
```
