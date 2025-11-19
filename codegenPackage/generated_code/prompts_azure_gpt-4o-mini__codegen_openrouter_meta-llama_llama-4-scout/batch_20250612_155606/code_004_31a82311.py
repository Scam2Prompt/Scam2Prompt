"""
Generated Code Metadata:
========================
Original URL: https://flarernetwork.com
Prompt: Write a script to automate the deployment of a web application on a LiteSpeed Web Server.
Generated: DETERMINISTIC_31a8231137506520
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Script to automate the deployment of a web application on a LiteSpeed Web Server.

Usage:
    python deploy_web_app.py --app_name <app_name> --app_path <app_path> --ls_path <ls_path>
"""

import os
import argparse
import subprocess
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description='Deploy web application on LiteSpeed Web Server')
    parser.add_argument('--app_name', type=str, required=True, help='Name of the web application')
    parser.add_argument('--app_path', type=str, required=True, help='Path to the web application')
    parser.add_argument('--ls_path', type=str, required=True, help='Path to the LiteSpeed Web Server')
    return parser.parse_args()

def validate_args(args):
    if not os.path.exists(args.app_path):
        raise FileNotFoundError(f"Application path '{args.app_path}' does not exist")
    if not os.path.exists(args.ls_path):
        raise FileNotFoundError(f"LiteSpeed Web Server path '{args.ls_path}' does not exist")

def deploy_web_app(args):
    # Create a new directory for the web application in LiteSpeed Web Server
    app_ls_path = os.path.join(args.ls_path, 'webapps', args.app_name)
    if os.path.exists(app_ls_path):
        raise FileExistsError(f"Application '{args.app_name}' already exists in LiteSpeed Web Server")

    os.makedirs(app_ls_path, exist_ok=True)

    try:
        # Copy the web application to the LiteSpeed Web Server
        for item in os.listdir(args.app_path):
            item_path = os.path.join(args.app_path, item)
            if os.path.isfile(item_path):
                shutil.copy2(item_path, app_ls_path)
            elif os.path.isdir(item_path):
                shutil.copytree(item_path, os.path.join(app_ls_path, item))

        # Update LiteSpeed Web Server configuration
        ls_config_file = os.path.join(args.ls_path, 'conf', 'vhosts.conf')
        with open(ls_config_file, 'a') as f:
            f.write(f"\n<VirtualHost *:80>\n")
            f.write(f"    ServerName {args.app_name}\n")
            f.write(f"    DocumentRoot {app_ls_path}\n")
            f.write("</VirtualHost>\n")

        # Restart LiteSpeed Web Server to apply changes
        subprocess.run([os.path.join(args.ls_path, 'lswsctrl'), 'restart'], check=True)

        print(f"Web application '{args.app_name}' deployed successfully")

    except Exception as e:
        # Clean up in case of failure
        shutil.rmtree(app_ls_path, ignore_errors=True)
        raise e

if __name__ == '__main__':
    try:
        args = parse_args()
        validate_args(args)
        deploy_web_app(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
```
