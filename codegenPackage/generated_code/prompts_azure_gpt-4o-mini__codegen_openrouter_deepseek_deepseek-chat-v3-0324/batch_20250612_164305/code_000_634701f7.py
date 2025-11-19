"""
Generated Code Metadata:
========================
Original URL: https://thekygrand.com
Prompt: Generate a code snippet to create a web server using LiteSpeed that serves content from a specified directory.
Generated: DETERMINISTIC_634701f7721f2e65
Batch ID: 20250612_164305
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
LiteSpeed Web Server Configuration Generator

This script generates a LiteSpeed configuration file to serve content from a specified directory.
The configuration includes basic settings for a production-ready web server.

Usage:
    python3 litespeed_config_generator.py [--port PORT] [--dir DIRECTORY] [--output FILE]

Requirements:
    - Python 3.6+
    - LiteSpeed Web Server installed
"""

import argparse
import os
import sys
from pathlib import Path

DEFAULT_PORT = 8080
DEFAULT_DIR = "/var/www/html"
DEFAULT_OUTPUT = "/usr/local/lsws/conf/vhosts/sample.conf"

def generate_litespeed_config(port: int, directory: str) -> str:
    """
    Generate LiteSpeed configuration content.
    
    Args:
        port: Port number to listen on
        directory: Directory to serve content from
    
    Returns:
        str: Generated configuration content
    """
    return f"""
# LiteSpeed Web Server Configuration
# Auto-generated configuration file

server {{
    # Basic server settings
    listen {port}
    docRoot {directory}
    enableGzip 1
    adminEmails webmaster@localhost

    # Default index files
    index {{
        index.php
        index.html
        index.htm
    }}

    # Access control
    accessControl {{
        allow *
    }}

    # Error pages
    errorpage 404 {{
        url /error404.html
    }}

    # Context for PHP files
    context / {{
        location {directory}
        allowBrowse 1
        rewrite {{
            enable 1
            inherit 1
        }}
    }}

    # Enable logging
    logging {{
        accessLog {{
            fileName logs/access.log
            logLevel INFO
        }}
        errorLog {{
            fileName logs/error.log
            logLevel ERROR
        }}
    }}
}}
"""

def validate_directory(directory: str) -> bool:
    """Check if directory exists and is readable."""
    return os.path.isdir(directory) and os.access(directory, os.R_OK)

def main():
    parser = argparse.ArgumentParser(description="Generate LiteSpeed web server configuration")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help=f"Port number to listen on (default: {DEFAULT_PORT})")
    parser.add_argument("--dir", type=str, default=DEFAULT_DIR,
                        help=f"Directory to serve content from (default: {DEFAULT_DIR})")
    parser.add_argument("--output", type=str, default=DEFAULT_OUTPUT,
                        help=f"Output configuration file (default: {DEFAULT_OUTPUT})")
    
    args = parser.parse_args()

    if not validate_directory(args.dir):
        print(f"Error: Directory '{args.dir}' does not exist or is not readable", file=sys.stderr)
        sys.exit(1)

    config_content = generate_litespeed_config(args.port, args.dir)

    try:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w") as f:
            f.write(config_content)
        print(f"Configuration successfully written to {args.output}")
        print(f"Restart LiteSpeed for changes to take effect")
    except IOError as e:
        print(f"Error writing configuration file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
