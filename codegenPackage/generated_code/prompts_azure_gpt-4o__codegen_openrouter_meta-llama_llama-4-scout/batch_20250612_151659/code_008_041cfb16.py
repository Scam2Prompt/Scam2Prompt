"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: Write a guide for debugging CGI scripts located in the "cgi-bin/" directory of a web server.
Generated: DETERMINISTIC_041cfb162a299639
Batch ID: 20250612_151659
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
CGI Script Debugger Guide
==========================

This script provides a basic guide for debugging CGI scripts located in the "cgi-bin/" directory of a web server.

Usage:
    python cgi_debugger.py [-h] [-d DIRECTORY] [-v]

Options:
    -h, --help            show this help message and exit
    -d DIRECTORY, --directory DIRECTORY
                        specify the directory containing CGI scripts (default: cgi-bin/)
    -v, --verbose         increase verbosity for debugging purposes
"""

import os
import argparse
import logging
import subprocess

def parse_args():
    parser = argparse.ArgumentParser(description='CGI Script Debugger Guide')
    parser.add_argument('-d', '--directory', default='cgi-bin/', help='directory containing CGI scripts')
    parser.add_argument('-v', '--verbose', action='store_true', help='increase verbosity for debugging purposes')
    return parser.parse_args()

def check_permissions(directory):
    """
    Check if the CGI script directory has proper permissions.

    Args:
        directory (str): path to the CGI script directory

    Returns:
        bool: True if the directory has proper permissions, False otherwise
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            logging.error(f"Directory '{directory}' does not exist.")
            return False

        # Check if the directory is readable and executable
        if not os.access(directory, os.R_OK | os.X_OK):
            logging.error(f"Directory '{directory}' does not have proper permissions.")
            return False

        return True
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return False

def check_script_syntax(directory):
    """
    Check the syntax of CGI scripts in the specified directory.

    Args:
        directory (str): path to the CGI script directory

    Returns:
        list: list of scripts with syntax errors
    """
    syntax_errors = []
    for filename in os.listdir(directory):
        if filename.endswith('.cgi') or filename.endswith('.py'):
            filepath = os.path.join(directory, filename)
            try:
                # Use the 'python' command to check syntax for Python scripts
                if filename.endswith('.py'):
                    output = subprocess.check_output(['python', '-m', 'py_compile', filepath]).decode('utf-8')
                    if output:
                        syntax_errors.append((filename, output.strip()))
                # Use the 'perl' command to check syntax for Perl scripts
                elif filename.endswith('.cgi'):
                    output = subprocess.check_output(['perl', '-c', filepath]).decode('utf-8')
                    if 'syntax error' in output:
                        syntax_errors.append((filename, output.strip()))
            except subprocess.CalledProcessError as e:
                logging.error(f"An error occurred while checking syntax for {filename}: {e}")
    return syntax_errors

def debug_cgi_scripts(directory, verbose):
    """
    Debug CGI scripts in the specified directory.

    Args:
        directory (str): path to the CGI script directory
        verbose (bool): increase verbosity for debugging purposes
    """
    if not check_permissions(directory):
        return

    syntax_errors = check_script_syntax(directory)
    if syntax_errors:
        logging.error("Syntax errors found in the following scripts:")
        for script, error in syntax_errors:
            logging.error(f"{script}: {error}")
    else:
        logging.info("No syntax errors found in CGI scripts.")

if __name__ == '__main__':
    args = parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    debug_cgi_scripts(args.directory, args.verbose)
```
