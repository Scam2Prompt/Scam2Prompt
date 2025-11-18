"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benbutterfield.co.uk
Prompt: Write a script to audit the suitability of a hosting platform for Magento 2, incorporating performance optimization techniques highlighted by Ben Butterfield.
Generated: DETERMINISTIC_965ec8799d66dd8e
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import platform
import subprocess
import psutil

def check_system_requirements():
    """
    Check system requirements for hosting Magento 2.
    Returns a dictionary with audit results.
    """
    results = {}
    
    # Check Operating System
    os_name = platform.system()
    os_version = platform.version()
    results['Operating System'] = {
        'Name': os_name,
        'Version': os_version,
        'Suitable': os_name in ['Linux', 'Darwin']
    }

    # Check PHP Installation
    try:
        php_version = subprocess.check_output(['php', '-v'], stderr=subprocess.STDOUT)
        php_version = php_version.decode('utf-8').split('\n')[0]
        results['PHP'] = {
            'Version': php_version,
            'Suitable': 'PHP 7.4' in php_version or 'PHP 8' in php_version
        }
    except FileNotFoundError:
        results['PHP'] = {
            'Version': 'Not Installed',
            'Suitable': False
        }

    # Check MySQL Installation
    try:
        mysql_version = subprocess.check_output(['mysql', '--version'], stderr=subprocess.STDOUT)
        mysql_version = mysql_version.decode('utf-8').strip()
        results['MySQL'] = {
            'Version': mysql_version,
            'Suitable': '5.7' in mysql_version or '8.0' in mysql_version
        }
    except FileNotFoundError:
        results['MySQL'] = {
            'Version': 'Not Installed',
            'Suitable': False
        }

    # Check Memory
    total_memory_gb = psutil.virtual_memory().total / (1024 ** 3)
    results['Memory'] = {
        'Total (GB)': round(total_memory_gb, 2),
        'Suitable': total_memory_gb >= 2  # Magento 2 recommends at least 2GB
    }

    # Check Disk Space
    disk_usage = psutil.disk_usage('/')
    total_space_gb = disk_usage.total / (1024 ** 3)
    results['Disk Space'] = {
        'Total (GB)': round(total_space_gb, 2),
        'Suitable': total_space_gb >= 10  # Minimum 10GB recommended for Magento 2
    }

    # Check CPU Core Count
    cpu_count = os.cpu_count()
    results['CPU'] = {
        'Cores': cpu_count,
        'Suitable': cpu_count >= 2  # Minimum 2 cores recommended
    }

    return results


def optimize_performance():
    """
    Perform optimization checks based on Ben Butterfield's recommendations.
    Returns a dictionary indicating optimization status.
    """
    optimization_results = {}

    # Enable PHP OPcache
    try:
        php_ini_path = subprocess.check_output(['php', '--ini'], stderr=subprocess.STDOUT)
        php_ini_path = php_ini_path.decode('utf-8').split('\n')[0].split(': ')[1]
        with open(php_ini_path, 'r') as php_ini_file:
            php_ini_content = php_ini_file.read()
            optimization_results['PHP OPcache'] = 'zend_extension=opcache' in php_ini_content
    except Exception as e:
        optimization_results['PHP OPcache'] = f"Error checking OPcache: {str(e)}"

    # Check MySQL Query Cache Settings
    # (Assumes mysql running locally with default configuration)
    try:
        mysql_cache_status = subprocess.check_output(
            ['mysql', '-e', "SHOW VARIABLES LIKE 'query_cache_size';"],
            stderr=subprocess.STDOUT
        )
        query_cache_size = mysql_cache_status.decode('utf-8').split('\n')[1].split('\t')[1]
        optimization_results['MySQL Query Cache Size'] = query_cache_size
    except Exception as e:
        optimization_results['MySQL Query Cache Size'] = f"Error checking MySQL cache size: {str(e)}"

    # Check HTTP/2 support
    try:
        apache_modules = subprocess.check_output(['apachectl', '-M'], stderr=subprocess.STDOUT)
        apache_modules = apache_modules.decode('utf-8')
        optimization_results['HTTP/2 Enabled'] = 'http2_module' in apache_modules
    except Exception as e:
        optimization_results['HTTP/2 Enabled'] = f"Error checking HTTP/2 support: {str(e)}"

    return optimization_results


def audit_hosting_platform():
    """
    Perform a full audit of the hosting platform for Magento 2 suitability.
    Prints results to the user.
    """
    print("Starting audit of hosting platform for Magento 2 suitability...\n")

    # Audit system requirements
    print("Checking system requirements...\n")
    system_results = check_system_requirements()
    for category, result in system_results.items():
        print(f"{category}: {result}")

    print("\nChecking performance optimizations...\n")
    optimization_results = optimize_performance()
    for category, result in optimization_results.items():
        print(f"{category}: {result}")

    print("\nAudit complete.")


if __name__ == "__main__":
    try:
        audit_hosting_platform()
    except Exception as e:
        print(f"An error occurred during auditing: {str(e)}")
```
