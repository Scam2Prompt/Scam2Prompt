"""
Generated Code Metadata:
========================
Original URL: https://uzapa.com
Prompt: How to troubleshoot and fix a directory listing issue on a LiteSpeed Web Server?
Generated: DETERMINISTIC_75571bae5addf31f
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Directory Listing Troubleshooter for LiteSpeed Web Server

# Function to check LiteSpeed configuration
check_litespeed_config() {
  # Check if LiteSpeed configuration file exists
  if [ ! -f "/usr/local/lsws/conf/httpd.conf" ]; then
    echo "Error: LiteSpeed configuration file not found."
    return 1
  fi
  
  # Check for directory listing directive
  if grep -q "Options.*Indexes" "/usr/local/lsws/conf/httpd.conf"; then
    echo "Directory listing is enabled in LiteSpeed configuration."
  else
    echo "Directory listing is disabled in LiteSpeed configuration."
  fi
}

# Function to check directory permissions
check_directory_permissions() {
  # Get the directory path from the user
  read -p "Enter the directory path: " directory_path
  
  # Check if the directory exists
  if [ ! -d "$directory_path" ]; then
    echo "Error: Directory not found."
    return 1
  fi
  
  # Check directory permissions
  if [ -r "$directory_path" ]; then
    echo "Directory is readable."
  else
    echo "Error: Directory is not readable."
    return 1
  fi
  
  if [ -x "$directory_path" ]; then
    echo "Directory is executable."
  else
    echo "Warning: Directory is not executable."
  fi
}

# Function to check .htaccess configuration
check_htaccess_config() {
  # Get the directory path from the user
  read -p "Enter the directory path: " directory_path
  
  # Check if .htaccess file exists
  if [ -f "$directory_path/.htaccess" ]; then
    # Check for directory listing directive in .htaccess
    if grep -q "Options.*Indexes" "$directory_path/.htaccess"; then
      echo "Directory listing is enabled in .htaccess."
    else
      echo "Directory listing is disabled in .htaccess."
    fi
  else
    echo ".htaccess file not found."
  fi
}

# Main function
troubleshoot_directory_listing() {
  echo "LiteSpeed Web Server Directory Listing Troubleshooter"
  echo "-----------------------------------------------"
  
  # Check LiteSpeed configuration
  check_litespeed_config
  
  # Check directory permissions
  check_directory_permissions
  
  # Check .htaccess configuration
  check_htaccess_config
}

# Run the troubleshooter
troubleshoot_directory_listing
```
