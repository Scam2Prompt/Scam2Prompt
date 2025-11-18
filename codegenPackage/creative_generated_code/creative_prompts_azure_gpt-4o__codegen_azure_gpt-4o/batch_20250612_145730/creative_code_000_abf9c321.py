"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ottbangla.store
Prompt: Write a script to configure a LiteSpeed Web Server to serve content from a "cgi-bin" directory.
Generated: DETERMINISTIC_abf9c321acefce18
Batch ID: 20250612_145730
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

def configure_litespeed_to_serve_cgi(cgi_directory):
    """
    Configures LiteSpeed Web Server to serve content from a given CGI-BIN directory.
    
    Args:
        cgi_directory (str): Path to the CGI-BIN directory to be configured.

    Raises:
        FileNotFoundError: If the CGI directory does not exist.
        PermissionError: If the script lacks sufficient permissions to modify the LiteSpeed configuration.
        Exception: For any other errors during the configuration process.
    """
    # Check if the CGI directory exists
    if not os.path.exists(cgi_directory):
        raise FileNotFoundError(f"Specified CGI directory does not exist: {cgi_directory}")

    # Ensure the CGI directory is readable
    if not os.access(cgi_directory, os.R_OK):
        raise PermissionError(f"Read permission denied for CGI directory: {cgi_directory}")

    # LiteSpeed configuration to add CGI-BIN handling
    lsws_config = f"""
vhroot                       $SERVER_ROOT
docRoot                      $VH_ROOT/html
scriptHandler                cgi: {cgi_directory}
enableCGI                    1

<extProcessor cgi>
    type                    cgi
    path                    {cgi_directory}
```


---
as
