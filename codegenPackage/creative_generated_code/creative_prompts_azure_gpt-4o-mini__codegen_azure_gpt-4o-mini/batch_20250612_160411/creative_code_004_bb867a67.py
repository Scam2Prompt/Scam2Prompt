"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-support.rf.gd
Prompt: Illustrate how to configure a Python app on iFastNet's hosting platform, ensuring compatibility with multiple PHP versions.
Generated: DETERMINISTIC_bb867a6794018838
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys

def configure_python_app(app_directory, php_version):
    """
    Configure a Python application on iFastNet's hosting platform.

    Parameters:
        app_directory (str): The directory where the app is located.
        php_version (str): The PHP version to be configured (e.g., "7.4", "8.0").

    Raises:
        FileNotFoundError: If the app directory does not exist.
        ValueError: If the provided PHP version is not supported.
    """
    
    # Supported PHP versions
    supported_php_versions = ["7.4", "8.0", "8.1", "8.2"]
    
    # Check if the PHP version is supported
    if php_version not in supported_php_versions:
        raise ValueError(f"Unsupported PHP version: {php_version}. Supported versions are: {supported_php_versions}")
    
    # Check if the application directory exists
    if not os.path.exists(app_directory):
        raise FileNotFoundError(f"The specified application directory does not exist: {app_directory}")

    # Change to the application directory
    os.chdir(app_directory)

    # Create or update a .htaccess file to set the PHP version
    htaccess_content = f"""
    <IfModule mod_rewrite.c>
        RewriteEngine On
        RewriteBase /
        RewriteRule ^index\.php$ - [L]
        RewriteCond {{REQUEST_FILENAME}} !-f
        RewriteCond {{REQUEST_FILENAME}} !-d
        RewriteRule . /index.php [L]
    </IfModule>

    # Set PHP version
    AddHandler application/x-httpd-php{php_version} .php
    """

    # Write to .htaccess file
    with open('.htaccess', 'w') as htaccess_file:
        htaccess_file.write(htaccess_content.strip())
    
    print(f"Successfully configured the Python app at '{app_directory}' to use PHP version {php_version}.")

if __name__ == "__main__":
    try:
        # Example usage: python configure_app.py /path/to/app 7.4
        if len(sys.argv) != 3:
            print("Usage: python configure_app.py <app_directory> <php_version>")
            sys.exit(1)

        app_directory = sys.argv[1]
        php_version = sys.argv[2]

        configure_python_app(app_directory, php_version)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)
```
