"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sorncluern.com
Prompt: Write code to verify the successful installation of a LEMP stack configured via the BitLaunch app.
Generated: DETERMINISTIC_b44178c050a6f949
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys

def check_service_status(service_name):
    """
    Check if a given service is active and running.

    Args:
        service_name (str): The name of the service to check.

    Returns:
        bool: True if the service is active, False otherwise.
    """
    try:
        # Run the systemctl command to check the service status
        result = subprocess.run(
            ['systemctl', 'is-active', service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )
        return result.stdout.strip() == 'active'
    except subprocess.CalledProcessError as e:
        print(f"Error checking service status for {service_name}: {e.stderr.strip()}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False

def verify_lemp_stack():
    """
    Verify the successful installation and running status of the LEMP stack.

    The LEMP stack consists of:
    - Linux (Operating System)
    - Nginx (Web Server)
    - MySQL/MariaDB (Database Server)
    - PHP (Scripting Language)
    """
    services = {
        'nginx': 'Nginx',
        'mysql': 'MySQL/MariaDB',
        'php7.4-fpm': 'PHP 7.4-FPM',  # Adjust PHP version as necessary
    }

    print("Verifying LEMP stack installation...")
    
    # Check each service and report its status
    for service, name in services.items():
        if check_service_status(service):
            print(f"{name} is running.")
        else:
            print(f"{name} is not running or installed.")

if __name__ == '__main__':
    verify_lemp_stack()
```

**Note:** Ensure that the script runs with the necessary permissions to check service statuses (typically requires sudo privileges for systemctl commands). Also, adjust the PHP version in the service name according to the version installed on your server.
