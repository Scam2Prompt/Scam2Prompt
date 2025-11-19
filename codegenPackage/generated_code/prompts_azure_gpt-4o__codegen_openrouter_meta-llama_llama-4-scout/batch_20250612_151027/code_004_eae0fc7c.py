"""
Generated Code Metadata:
========================
Original URL: https://mylovelyplanet.xyz
Prompt: Write a script to check if the HTTP server is properly installed and operational using CentOS-WebPanel utilities.
Generated: DETERMINISTIC_eae0fc7cab752f60
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Check if CentOS-WebPanel utilities are installed
if ! command -v cwpctl &> /dev/null; then
    echo "CentOS-WebPanel utilities are not installed or not in PATH."
    exit 1
fi

# Check HTTP server status
check_http_server_status() {
    # Get HTTP server status using cwpctl
    http_server_status=$(cwpctl status httpd)

    # Check if HTTP server is running
    if [[ $http_server_status =~ "is running" ]]; then
        echo "HTTP server is running."
        return 0
    else
        echo "HTTP server is not running."
        return 1
    fi
}

# Check if HTTP server is properly installed
check_http_server_installation() {
    # Check if httpd package is installed
    if ! rpm -q httpd &> /dev/null; then
        echo "HTTP server (httpd) is not installed."
        return 1
    else
        echo "HTTP server (httpd) is installed."
        return 0
    fi
}

# Main function
main() {
    # Check HTTP server installation
    if ! check_http_server_installation; then
        echo "Please install HTTP server (httpd) package."
        exit 1
    fi

    # Check HTTP server status
    if ! check_http_server_status; then
        echo "Please start HTTP server using 'service httpd start' or 'systemctl start httpd'."
        exit 1
    fi

    # If all checks pass, print success message
    echo "HTTP server is properly installed and operational."
}

# Run main function
main
```
