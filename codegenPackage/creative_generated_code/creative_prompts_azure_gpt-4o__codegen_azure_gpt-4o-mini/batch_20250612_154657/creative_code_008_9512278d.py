"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiotv.infinityfreeapp.com
Prompt: Recommend hosting solutions for deploying a multi-language web application (PHP, Node.js, Python) and write code to test the hosting environment.
Generated: DETERMINISTIC_9512278dc8dcf811
Batch ID: 20250612_154657
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

def check_php_version():
    """Check the PHP version installed on the server."""
    try:
        result = subprocess.run(['php', '-v'], capture_output=True, text=True, check=True)
        print("PHP Version:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error checking PHP version:", e)
        sys.exit(1)

def check_node_version():
    """Check the Node.js version installed on the server."""
    try:
        result = subprocess.run(['node', '-v'], capture_output=True, text=True, check=True)
        print("Node.js Version:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error checking Node.js version:", e)
        sys.exit(1)

def check_python_version():
    """Check the Python version installed on the server."""
    try:
        result = subprocess.run(['python3', '--version'], capture_output=True, text=True, check=True)
        print("Python Version:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error checking Python version:", e)
        sys.exit(1)

def check_web_server():
    """Check if the web server (Apache or Nginx) is running."""
    try:
        result = subprocess.run(['systemctl', 'is-active', '--quiet', 'apache2'], check=True)
        print("Apache is running.")
    except subprocess.CalledProcessError:
        try:
            result = subprocess.run(['systemctl', 'is-active', '--quiet', 'nginx'], check=True)
            print("Nginx is running.")
        except subprocess.CalledProcessError:
            print("No web server (Apache or Nginx) is running.")

def test_hosting_environment():
    """Run all checks for the hosting environment."""
    print("Testing hosting environment...\n")
    check_php_version()
    check_node_version()
    check_python_version()
    check_web_server()

if __name__ == "__main__":
    test_hosting_environment()
```

### Recommended Hosting Solutions
- **Shared Hosting**: Good for small projects (e.g., Bluehost, HostGator).
- **VPS Hosting**: More control and flexibility (e.g., DigitalOcean, Linode).
- **Cloud Hosting**: Scalable and reliable (e.g., AWS, Google Cloud, Azure).
- **Platform as a Service (PaaS)**: Simplifies deployment (e.g., Heroku, Render). 

### Note
Make sure to install PHP, Node.js, and Python on your server and have administrative access to run this testing script.
