"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: "Design a basic CGI-bin directory structure for a personal website and explain its purpose."
Generated: DETERMINISTIC_e0ae9677f3288e61
Batch ID: 20250622_205206
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
Basic CGI-bin directory structure for a personal website.
"""

import os
import sys
from pathlib import Path

def create_cgi_directory_structure(base_path):
    """
    Creates a basic CGI-bin directory structure for a personal website.
    
    Args:
        base_path (str): The root directory where the structure should be created.
    """
    try:
        # Create main directories
        Path(base_path).mkdir(exist_ok=True)
        cgi_bin = Path(base_path) / "cgi-bin"
        cgi_bin.mkdir(exist_ok=True)
        
        # Create subdirectories within cgi-bin
        (cgi_bin / "forms").mkdir(exist_ok=True)
        (cgi_bin / "utilities").mkdir(exist_ok=True)
        (cgi_bin / "api").mkdir(exist_ok=True)
        
        # Create sample CGI scripts
        create_sample_script(cgi_bin / "forms" / "contact.py")
        create_sample_script(cgi_bin / "utilities" / "counter.py")
        create_sample_script(cgi_bin / "api" / "data_handler.py")
        
        # Create configuration file
        create_config_file(base_path)
        
        print(f"CGI directory structure created successfully at {base_path}")
        
    except Exception as e:
        print(f"Error creating directory structure: {e}", file=sys.stderr)
        sys.exit(1)

def create_sample_script(file_path):
    """
    Creates a sample CGI script with basic functionality.
    
    Args:
        file_path (Path): Path to the script file to create.
    """
    content = f"""#!/usr/bin/env python3
# {file_path.name} - Sample CGI script

import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html\\n\\n")
print("<html><head><title>{file_path.stem}</title></head>")
print("<body>")
print("<h1>Sample {file_path.stem} CGI Script</h1>")
print("<p>This is a sample CGI script.</p>")
print("</body></html>")
"""
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        file_path.chmod(0o755)  # Make executable
    except Exception as e:
        print(f"Error creating sample script {file_path}: {e}", file=sys.stderr)
        raise

def create_config_file(base_path):
    """
    Creates a basic configuration file for the CGI setup.
    
    Args:
        base_path (str): The root directory where the config should be created.
    """
    config_path = Path(base_path) / "cgi-bin" / "config.ini"
    content = """[main]
# CGI-bin configuration
debug = true
log_path = /var/log/cgi-bin.log

[permissions]
# Default permissions for CGI scripts
default_mode = 755
"""
    try:
        with open(config_path, 'w') as f:
            f.write(content)
    except Exception as e:
        print(f"Error creating config file: {e}", file=sys.stderr)
        raise

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 setup_cgi.py <base_directory>", file=sys.stderr)
        sys.exit(1)
    
    create_cgi_directory_structure(sys.argv[1])
```
