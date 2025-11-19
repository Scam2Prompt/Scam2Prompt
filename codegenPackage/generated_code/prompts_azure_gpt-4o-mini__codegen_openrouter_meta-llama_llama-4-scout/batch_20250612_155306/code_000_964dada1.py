"""
Generated Code Metadata:
========================
Original URL: https://thg-awardprogram.epizy.com
Prompt: Generate a Python script that utilizes iFastNet's hosting features, including Node.js support and multiple PHP versions.
Generated: DETERMINISTIC_964dada1e3e79bf7
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# iFastNet Hosting Features Script
# ======================================

import os
import subprocess
from typing import Dict

class iFastNetHosting:
    def __init__(self, node_js_path: str, php_versions: Dict[str, str]):
        """
        Initialize iFastNet hosting features.

        Args:
        - node_js_path (str): Path to Node.js executable.
        - php_versions (Dict[str, str]): Dictionary of PHP versions with their paths.
        """
        self.node_js_path = node_js_path
        self.php_versions = php_versions

    def create_node_js_app(self, app_name: str, port: int) -> None:
        """
        Create a new Node.js application.

        Args:
        - app_name (str): Name of the application.
        - port (int): Port number to use.

        Raises:
        - Exception: If Node.js executable is not found.
        """
        try:
            # Create a new directory for the application
            os.mkdir(app_name)
            # Create a basic Node.js application
            with open(os.path.join(app_name, 'app.js'), 'w') as f:
                f.write(f'const http = require("http");\nhttp.createServer((req, res) => {{\n  res.writeHead(200, {{"Content-Type": "text/plain"}});\n  res.end("Hello World\\n");\n}}).listen({port});')
            # Start the Node.js application
            subprocess.Popen([self.node_js_path, os.path.join(app_name, 'app.js')], cwd=app_name)
        except FileNotFoundError:
            raise Exception(f"Node.js executable not found at {self.node_js_path}")

    def switch_php_version(self, version: str, website_path: str) -> None:
        """
        Switch PHP version for a website.

        Args:
        - version (str): PHP version to switch to.
        - website_path (str): Path to the website.

        Raises:
        - ValueError: If the specified PHP version is not supported.
        - Exception: If the PHP version executable is not found.
        """
        if version not in self.php_versions:
            raise ValueError(f"Unsupported PHP version: {version}")
        try:
            # Update the PHP version symlink
            php_path = self.php_versions[version]
            subprocess.run(['ln', '-sf', php_path, os.path.join(website_path, 'php')])
        except FileNotFoundError:
            raise Exception(f"PHP {version} executable not found at {php_path}")

def main():
    # Example usage
    node_js_path = '/usr/bin/node'
    php_versions = {
        '7.4': '/usr/bin/php7.4',
        '8.0': '/usr/bin/php8.0',
        '8.1': '/usr/bin/php8.1'
    }
    hosting = iFastNetHosting(node_js_path, php_versions)

    # Create a new Node.js application
    app_name = 'example-node-app'
    port = 8080
    hosting.create_node_js_app(app_name, port)

    # Switch PHP version for a website
    version = '8.0'
    website_path = '/var/www/example-website'
    hosting.switch_php_version(version, website_path)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
