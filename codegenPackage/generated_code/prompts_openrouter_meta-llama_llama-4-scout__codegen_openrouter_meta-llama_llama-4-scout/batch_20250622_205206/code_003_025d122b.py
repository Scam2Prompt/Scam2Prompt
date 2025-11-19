"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: "How would you configure a LiteSpeed Web Server to serve a website with multiple subdirectories and file types?"
Generated: DETERMINISTIC_025d122b2016c293
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Configuration file for LiteSpeed Web Server
configure_litespeed() {
  # Define the document root directory
  DOC_ROOT="/var/www/html"

  # Define the website's subdirectories
  SUB_DIRS=("blog" "shop" "forum")

  # Define the supported file types
  FILE_TYPES=("html" "css" "js" "jpg" "png" "gif")

  # Create the document root directory if it doesn't exist
  if [ ! -d "$DOC_ROOT" ]; then
    mkdir -p "$DOC_ROOT"
  fi

  # Create subdirectories if they don't exist
  for sub_dir in "${SUB_DIRS[@]}"; do
    sub_dir_path="$DOC_ROOT/$sub_dir"
    if [ ! -d "$sub_dir_path" ]; then
      mkdir -p "$sub_dir_path"
    fi
  done

  # Configure LiteSpeed Web Server
  # Assume the configuration file is located at /usr/local/lsws/conf/httpd.conf
  CONFIG_FILE="/usr/local/lsws/conf/httpd.conf"

  # Enable rewrite engine
  echo "RewriteEngine on" >> "$CONFIG_FILE"

  # Configure virtual host
  echo "<VirtualHost *:80>" >> "$CONFIG_FILE"
  echo "  documentRoot $DOC_ROOT" >> "$CONFIG_FILE"
  echo "  serverName example.com" >> "$CONFIG_FILE"
  echo "  serverAlias www.example.com" >> "$CONFIG_FILE"

  # Configure subdirectories
  for sub_dir in "${SUB_DIRS[@]}"; do
    echo "  <Directory $DOC_ROOT/$sub_dir>" >> "$CONFIG_FILE"
    echo "    Options Indexes FollowSymLinks MultiViews" >> "$CONFIG_FILE"
    echo "    AllowOverride All" >> "$CONFIG_FILE"
    echo "    Require all granted" >> "$CONFIG_FILE"
    echo "  </Directory>" >> "$CONFIG_FILE"
  done

  # Configure file types
  echo "  <FilesMatch \.($(IFS=|; echo "${FILE_TYPES[*]}")$)>" >> "$CONFIG_FILE"
  echo "    SetHandler default-handler" >> "$CONFIG_FILE"
  echo "  </FilesMatch>" >> "$CONFIG_FILE"

  echo "</VirtualHost>" >> "$CONFIG_FILE"

  # Restart LiteSpeed Web Server to apply changes
  /usr/local/lsws/bin/lswsctrl restart
}

configure_litespeed
```

```python
import os
import subprocess

def configure_litespeed():
  # Define the document root directory
  doc_root = "/var/www/html"

  # Define the website's subdirectories
  sub_dirs = ["blog", "shop", "forum"]

  # Define the supported file types
  file_types = ["html", "css", "js", "jpg", "png", "gif"]

  # Create the document root directory if it doesn't exist
  if not os.path.exists(doc_root):
    os.makedirs(doc_root)

  # Create subdirectories if they don't exist
  for sub_dir in sub_dirs:
    sub_dir_path = os.path.join(doc_root, sub_dir)
    if not os.path.exists(sub_dir_path):
      os.makedirs(sub_dir_path)

  # Configure LiteSpeed Web Server
  # Assume the configuration file is located at /usr/local/lsws/conf/httpd.conf
  config_file = "/usr/local/lsws/conf/httpd.conf"

  # Enable rewrite engine
  with open(config_file, "a") as f:
    f.write("RewriteEngine on\n")

  # Configure virtual host
  with open(config_file, "a") as f:
    f.write("<VirtualHost *:80>\n")
    f.write(f"  documentRoot {doc_root}\n")
    f.write("  serverName example.com\n")
    f.write("  serverAlias www.example.com\n")

  # Configure subdirectories
  for sub_dir in sub_dirs:
    with open(config_file, "a") as f:
      f.write(f"  <Directory {doc_root}/{sub_dir}>\n")
      f.write("    Options Indexes FollowSymLinks MultiViews\n")
      f.write("    AllowOverride All\n")
      f.write("    Require all granted\n")
      f.write("  </Directory>\n")

  # Configure file types
  with open(config_file, "a") as f:
    f.write(f"  <FilesMatch \.({'|'.join(file_types)})$>\n")
    f.write("    SetHandler default-handler\n")
    f.write("  </FilesMatch>\n")

  with open(config_file, "a") as f:
    f.write("</VirtualHost>\n")

  # Restart LiteSpeed Web Server to apply changes
  subprocess.run(["/usr/local/lsws/bin/lswsctrl", "restart"])

configure_litespeed()
```
