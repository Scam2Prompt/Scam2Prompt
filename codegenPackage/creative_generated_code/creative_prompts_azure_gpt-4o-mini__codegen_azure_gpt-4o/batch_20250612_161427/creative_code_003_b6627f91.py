"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniapt.space
Prompt: What are the common causes of a 500 Internal Server Error, and how can I resolve them for an Apache server setup like uniapt.space?
Generated: DETERMINISTIC_b6627f9128cbb09f
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python script to troubleshoot common causes of a `500 Internal Server Error` for an Apache server:

```python
import os
import subprocess

def check_apache_error_logs(log_path="/var/log/apache2/error.log"):
    """
    Check Apache error logs for issues.
    :param log_path: Path to the Apache error log file.
    """
    try:
        if os.path.exists(log_path):
            print(f"Reading error logs from: {log_path}\n")
            with open(log_path, 'r') as log_file:
                lines = log_file.readlines()
                recent_logs = lines[-50:]  # Fetch last 50 log lines
                for line in recent_logs:
                    print(line.strip())
        else:
            print(f"Error log file not found at: {log_path}")
    except Exception as e:
        print(f"An error occurred while reading logs: {e}")


def check_file_permissions(site_path="/var/www/uniapt.space"):
    """
    Check file permissions in the site directory.
    :param site_path: Path to the site directory.
    """
    try:
        if os.path.exists(site_path):
            print(f"Checking file permissions in: {site_path}\n")
            for root, dirs, files in os.walk(site_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    permissions = oct(os.stat(file_path).st_mode)[-3:]
                    print(f"{file_path} - Permissions: {permissions}")
                    if permissions not in ['644', '755']:
                        print(f"Warning: {file_path} has potential incorrect permissions.")
        else:
            print(f"Site path not found: {site_path}")
    except Exception as e:
        print(f"An error occurred while checking file permissions: {e}")


def check_apache_configuration(config_path="/etc/apache2/apache2.conf"):
    """
    Check Apache configuration file for syntax errors.
    :param config_path: Path to the Apache configuration file.
    """
    try:
        print("Checking Apache configuration for syntax errors...\n")
        result = subprocess.run(["apachectl", "configtest"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Apache configuration is valid.")
        else:
            print("Apache configuration has issues:")
            print(result.stderr)
    except FileNotFoundError:
        print("Apachectl command not found. Ensure Apache is installed.")
    except Exception as e:
        print(f"An error occurred while checking Apache configuration: {e}")


def restart_apache_service():
    """
    Restart the Apache service to apply changes.
    """
    try:
        print("Restarting Apache service...\n")
        result = subprocess.run(["systemctl", "restart", "apache2"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Apache service restarted successfully.")
        else:
            print("Failed to restart Apache service:")
            print(result.stderr)
    except FileNotFoundError:
        print("Systemctl command not found. Ensure systemd is installed.")
    except Exception as e:
        print(f"An error occurred while restarting the Apache service: {e}")


if __name__ == "__main__":
    print("Diagnosing 500 Internal Server Error...\n")
    check_apache_error_logs()
    check_file_permissions()
    check_apache_configuration()
    restart_apache_service()
```

### Key Points:
1. **Error Logs**: Fetches the last 50 lines of Apache's error logs for debugging.
2. **Permissions**: Checks file permissions in the site directory.
3. **Configuration Check**: Runs `apachectl configtest` to verify the Apache configuration syntax.
4. **Service Restart**: Restarts Apache to apply changes.

Ensure proper permissions to run this script (`sudo` may be required for certain operations). This script is production-ready but should be executed in a testing/staging environment before applying changes to production.
