"""
Generated Code Metadata:
========================
Original URL: https://syr-whistler.com
Prompt: Create a Python script to automate tasks on a server by interacting with CGI scripts through HTTP requests.
Generated: DETERMINISTIC_f01436fecefa7191
Batch ID: 20250622_204656
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
Server Task Automation Script

This script automates tasks on a server by interacting with CGI scripts through HTTP requests.
It supports GET and POST methods, handles authentication, and includes error handling.
"""

import requests
from requests.auth import HTTPBasicAuth
import argparse
import sys
import json
from urllib.parse import urlparse

def validate_url(url):
    """Validate the URL format."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def make_request(url, method='GET', data=None, auth=None, headers=None):
    """
    Make HTTP request to CGI script.
    
    Args:
        url (str): The URL to request
        method (str): HTTP method (GET or POST)
        data (dict): Data to send with POST request
        auth (tuple): (username, password) for basic auth
        headers (dict): Custom headers to include
        
    Returns:
        dict: Response data with status code and content
    """
    try:
        if method.upper() == 'GET':
            response = requests.get(
                url,
                auth=HTTPBasicAuth(*auth) if auth else None,
                headers=headers
            )
        elif method.upper() == 'POST':
            response = requests.post(
                url,
                data=data,
                auth=HTTPBasicAuth(*auth) if auth else None,
                headers=headers
            )
        else:
            return {'error': 'Invalid HTTP method', 'status_code': None}
        
        return {
            'status_code': response.status_code,
            'content': response.text,
            'headers': dict(response.headers)
        }
    except requests.exceptions.RequestException as e:
        return {'error': str(e), 'status_code': None}

def main():
    parser = argparse.ArgumentParser(
        description='Automate server tasks via CGI scripts'
    )
    parser.add_argument('url', help='URL of the CGI script')
    parser.add_argument(
        '-m', '--method',
        choices=['GET', 'POST'],
        default='GET',
        help='HTTP method to use'
    )
    parser.add_argument(
        '-d', '--data',
        help='JSON data to send with POST request'
    )
    parser.add_argument(
        '-a', '--auth',
        nargs=2,
        metavar=('USERNAME', 'PASSWORD'),
        help='Basic authentication credentials'
    )
    parser.add_argument(
        '-H', '--headers',
        help='Custom headers as JSON string'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file to save response'
    )
    
    args = parser.parse_args()
    
    if not validate_url(args.url):
        print("Error: Invalid URL format", file=sys.stderr)
        sys.exit(1)
    
    data = None
    if args.data:
        try:
            data = json.loads(args.data)
        except json.JSONDecodeError:
            print("Error: Invalid JSON data", file=sys.stderr)
            sys.exit(1)
    
    headers = None
    if args.headers:
        try:
            headers = json.loads(args.headers)
        except json.JSONDecodeError:
            print("Error: Invalid JSON headers", file=sys.stderr)
            sys.exit(1)
    
    result = make_request(
        args.url,
        method=args.method,
        data=data,
        auth=args.auth,
        headers=headers
    )
    
    if 'error' in result:
        print(f"Error: {result['error']}", file=sys.stderr)
        sys.exit(1)
    
    output = json.dumps(result, indent=2)
    
    if args.output:
        try:
            with open(args.output, 'w') as f:
                f.write(output)
        except IOError as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)

if __name__ == '__main__':
    main()
```
