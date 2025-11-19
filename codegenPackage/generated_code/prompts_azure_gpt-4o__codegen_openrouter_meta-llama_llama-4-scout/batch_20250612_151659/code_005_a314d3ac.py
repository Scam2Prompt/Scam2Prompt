"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: Generate a Bash script to automate the creation and setup of a "cgi-bin/" directory with proper permissions and sample CGI scripts.
Generated: DETERMINISTIC_a314d3acde6fa09c
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Define constants for directory and script names
CGI_BIN_DIR="cgi-bin"
SAMPLE_SCRIPT_1="hello_world.cgi"
SAMPLE_SCRIPT_2="echo_params.cgi"

# Function to create cgi-bin directory with proper permissions
create_cgi_bin_dir() {
  # Create the cgi-bin directory if it doesn't exist
  if [ ! -d "$CGI_BIN_DIR" ]; then
    mkdir "$CGI_BIN_DIR"
    echo "Created $CGI_BIN_DIR directory"
  fi
  
  # Set proper permissions for the cgi-bin directory
  chmod 755 "$CGI_BIN_DIR"
  echo "Set permissions for $CGI_BIN_DIR to 755"
}

# Function to create sample CGI scripts
create_sample_scripts() {
  # Create sample script 1: hello_world.cgi
  cat > "$CGI_BIN_DIR/$SAMPLE_SCRIPT_1" <<EOF
#!/bin/bash
echo "Content-type: text/plain"
echo ""
echo "Hello, World!"
EOF
  chmod 755 "$CGI_BIN_DIR/$SAMPLE_SCRIPT_1"
  echo "Created $SAMPLE_SCRIPT_1 script"

  # Create sample script 2: echo_params.cgi
  cat > "$CGI_BIN_DIR/$SAMPLE_SCRIPT_2" <<EOF
#!/bin/bash
echo "Content-type: text/plain"
echo ""
echo "Request Method: \$REQUEST_METHOD"
echo "Query String: \$QUERY_STRING"
EOF
  chmod 755 "$CGI_BIN_DIR/$SAMPLE_SCRIPT_2"
  echo "Created $SAMPLE_SCRIPT_2 script"
}

# Main function
main() {
  # Create cgi-bin directory and set permissions
  create_cgi_bin_dir
  
  # Create sample CGI scripts
  create_sample_scripts
  
  echo "cgi-bin directory and sample scripts setup complete"
}

# Run the main function
main
```
