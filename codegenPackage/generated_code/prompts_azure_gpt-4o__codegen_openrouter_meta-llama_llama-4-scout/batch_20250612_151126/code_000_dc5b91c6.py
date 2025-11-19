"""
Generated Code Metadata:
========================
Original URL: https://elmensajero.e-kraken.net
Prompt: Write a Python script to interact with a CGI-bin directory on a server, using the structure described in the webpage.
Generated: DETERMINISTIC_dc5b91c6ab7051da
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Interact with a CGI-bin directory on a server.

This script provides functions to list, read, and execute CGI scripts in a specified directory.

Usage:
    python cgi_interactor.py [-h] [-d DIRECTORY] [-l] [-r SCRIPT] [-e SCRIPT]

Arguments:
    -h, --help            show this help message and exit
    -d DIRECTORY, --directory DIRECTORY
                          specify the CGI-bin directory
    -l, --list            list available CGI scripts
    -r SCRIPT, --read SCRIPT
                          read and display the content of a CGI script
    -e SCRIPT, --execute SCRIPT
                          execute a CGI script
"""

import os
import argparse
import subprocess

def list_scripts(directory):
    """
    List available CGI scripts in the specified directory.

    Args:
        directory (str): Path to the CGI-bin directory.

    Returns:
        list: List of script names.
    """
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.cgi')]
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return []

def read_script(directory, script_name):
    """
    Read and display the content of a CGI script.

    Args:
        directory (str): Path to the CGI-bin directory.
        script_name (str): Name of the CGI script.

    Returns:
        str: Script content.
    """
    script_path = os.path.join(directory, script_name)
    try:
        with open(script_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Script '{script_name}' not found in directory '{directory}'.")
        return ""

def execute_script(directory, script_name):
    """
    Execute a CGI script.

    Args:
        directory (str): Path to the CGI-bin directory.
        script_name (str): Name of the CGI script.

    Returns:
        str: Script output.
    """
    script_path = os.path.join(directory, script_name)
    try:
        output = subprocess.check_output(['python', script_path], cwd=directory)
        return output.decode('utf-8')
    except FileNotFoundError:
        print(f"Error: Script '{script_name}' not found in directory '{directory}'.")
        return ""
    except subprocess.CalledProcessError as e:
        print(f"Error: Script '{script_name}' returned non-zero exit status {e.returncode}.")
        return ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Interact with a CGI-bin directory.')
    parser.add_argument('-d', '--directory', default='/var/www/cgi-bin', help='CGI-bin directory')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', '--list', action='store_true', help='list available CGI scripts')
    group.add_argument('-r', '--read', help='read and display the content of a CGI script')
    group.add_argument('-e', '--execute', help='execute a CGI script')
    args = parser.parse_args()

    if args.list:
        scripts = list_scripts(args.directory)
        for script in scripts:
            print(script)
    elif args.read:
        print(read_script(args.directory, args.read))
    elif args.execute:
        print(execute_script(args.directory, args.execute))
```
