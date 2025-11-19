"""
Generated Code Metadata:
========================
Original URL: https://geteasycrypto.com
Prompt: What are the steps to configure the HTTP server test page on CentOS-WebPanel.com, and how can I customize the index.html file?
Generated: DETERMINISTIC_1c523d7763767696
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to configure the HTTP server test page on CentOS-WebPanel.com
# and customize the index.html file.

# Exit immediately if a command exits with a non-zero status
set -e

# Function to install Apache if not already installed
install_apache() {
  echo "Checking if Apache is installed..."
  if ! command -v httpd &> /dev/null; then
    echo "Apache not found. Installing Apache..."
    yum install -y httpd
    echo "Apache installed successfully."
  else
    echo "Apache is already installed."
  fi
}

# Function to start and enable Apache service
start_apache() {
  echo "Starting Apache service..."
  systemctl start httpd
  systemctl enable httpd
  echo "Apache service started and enabled."
}

# Function to configure the HTTP server test page
configure_test_page() {
  echo "Configuring HTTP server test page..."
  local test_page_dir="/var/www/html"
  local test_page_file="${test_page_dir}/index.html"

  # Ensure the directory exists
  mkdir -p "$test_page_dir"

  # Create a default index.html file
  cat > "$test_page_file" <<EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Page</title>
</head>
<body>
    <h1>Welcome to the CentOS-WebPanel HTTP Server Test Page</h1>
    <p>This is the default test page. Customize it as needed.</p>
</body>
</html>
EOF

  echo "Test page configured at $test_page_file."
}

# Function to customize the index.html file
customize_index_html() {
  echo "Customizing index.html file..."
  local test_page_file="/var/www/html/index.html"

  # Check if the file exists
  if [[ -f "$test_page_file" ]]; then
    # Append custom content to the index.html file
    cat >> "$test_page_file" <<EOF
<!-- Custom content added -->
<footer>
    <p>Customized by CentOS-WebPanel.com</p>
</footer>
EOF
    echo "index.html file customized successfully."
  else
    echo "Error: index.html file not found. Ensure the test page is configured first."
    exit 1
  fi
}

# Main script execution
echo "Starting HTTP server configuration script..."

install_apache
start_apache
configure_test_page
customize_index_html

echo "HTTP server test page configured and customized successfully."
```

To run this script:
1. Save it as `configure_http_server.sh`.
2. Make it executable: `chmod +x configure_http_server.sh`.
3. Run it with root privileges: `sudo ./configure_http_server.sh`.
