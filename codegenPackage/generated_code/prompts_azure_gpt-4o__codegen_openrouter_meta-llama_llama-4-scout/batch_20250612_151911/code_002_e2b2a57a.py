"""
Generated Code Metadata:
========================
Original URL: https://teslatrust.net
Prompt: Provide a step-by-step guide to configure a CentOS-WebPanel server to replace the default HTTP test page with custom content in the `/home/USERNAME/public_html` directory.
Generated: DETERMINISTIC_e2b2a57a66572755
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Configuration script for CentOS-WebPanel server
# to replace the default HTTP test page with custom content

# Check if user is root
if [ $(id -u) -ne 0 ]; then
    echo "You must be root to run this script."
    exit 1
fi

# Check if CentOS-WebPanel is installed
if ! command -v cpanel &> /dev/null; then
    echo "CentOS-WebPanel is not installed or not in PATH."
    exit 1
fi

# Set variables
USERNAME=$1
CUSTOM_CONTENT_DIR="/home/$USERNAME/public_html"

# Check if username is provided
if [ -z "$USERNAME" ]; then
    echo "Please provide a username."
    exit 1
fi

# Create public_html directory if it doesn't exist
if [ ! -d "$CUSTOM_CONTENT_DIR" ]; then
    mkdir -p "$CUSTOM_CONTENT_DIR"
    chown -R "$USERNAME":"$USERNAME" "$CUSTOM_CONTENT_DIR"
fi

# Create a custom index.html file
INDEX_FILE="$CUSTOM_CONTENT_DIR/index.html"
cat > "$INDEX_FILE" <<EOF
<!DOCTYPE html>
<html>
<head>
    <title>Custom Page</title>
</head>
<body>
    <h1>Welcome to your custom page!</h1>
</body>
</html>
EOF

# Change ownership of index.html
chown "$USERNAME":"$USERNAME" "$INDEX_FILE"

# Restart Apache service to apply changes
service httpd restart

# Verify changes
echo "Custom content directory: $CUSTOM_CONTENT_DIR"
echo "Custom index.html file: $INDEX_FILE"
```

```python
import os
import sys
import subprocess

def configure_cwp_server(username):
    """
    Configure a CentOS-WebPanel server to replace the default HTTP test page 
    with custom content in the /home/USERNAME/public_html directory.

    Args:
        username (str): The username of the user.

    Returns:
        None
    """

    # Check if user is root
    if os.geteuid() != 0:
        print("You must be root to run this script.")
        sys.exit(1)

    # Check if CentOS-WebPanel is installed
    try:
        subprocess.run(["cpanel", "--version"], check=True, stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        print("CentOS-WebPanel is not installed or not in PATH.")
        sys.exit(1)

    # Set variables
    custom_content_dir = f"/home/{username}/public_html"

    # Check if username is provided
    if not username:
        print("Please provide a username.")
        sys.exit(1)

    # Create public_html directory if it doesn't exist
    if not os.path.exists(custom_content_dir):
        os.makedirs(custom_content_dir)
        subprocess.run(["chown", "-R", f"{username}:{username}", custom_content_dir])

    # Create a custom index.html file
    index_file = f"{custom_content_dir}/index.html"
    with open(index_file, "w") as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Custom Page</title>
</head>
<body>
    <h1>Welcome to your custom page!</h1>
</body>
</html>
""")

    # Change ownership of index.html
    subprocess.run(["chown", f"{username}:{username}", index_file])

    # Restart Apache service to apply changes
    subprocess.run(["service", "httpd", "restart"])

    # Verify changes
    print(f"Custom content directory: {custom_content_dir}")
    print(f"Custom index.html file: {index_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    configure_cwp_server(username)
```
