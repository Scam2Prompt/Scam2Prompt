"""
Generated Code Metadata:
========================
Original URL: https://syr-whistler.com
Prompt: How can I secure a CGI directory on my server to prevent unauthorized access, considering best practices for permissions and authentication?
Generated: DETERMINISTIC_1cc90c7255024d89
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Securing CGI Directory with Authentication and Authorization**
===========================================================

### Directory Structure

Assuming the following directory structure:
```markdown
/cgi-bin/
|---- cgi_script.py
|---- .htaccess
|---- .htpasswd
```

### .htaccess
```bash
# .htaccess
AuthType Basic
AuthName "Restricted Area"
AuthUserFile /path/to/cgi-bin/.htpasswd

Require valid-user

# Options -Indexes
# Options -ExecCGI
# AddHandler cgi-bin .cgi .pl .plx .ppl .cgi-bin .pl
```

### .htpasswd Generation Script (Python)
```python
import hashlib
import os
import getpass

def generate_htpasswd(username, password, filepath='.htpasswd'):
    """Generate .htpasswd file entry."""
    # Hash password with SHA-1
    hashed_password = hashlib.sha1(password.encode()).hexdigest()
    # Write to .htpasswd file
    with open(filepath, 'a') as f:
        f.write(f"{username}:{hashed_password}\n")

def main():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    
    if password == confirm_password:
        generate_htpasswd(username, password)
        print("User created successfully.")
    else:
        print("Passwords do not match.")

if __name__ == "__main__":
    main()
```

### CGI Script with Authentication Check (Python)
```python
#!/usr/bin/env python3
import os
import sys
import subprocess
from http import HTTPStatus

# Define allowed users and their passwords (ideally use a database or secure storage)
ALLOWED_USERS = {
    'user1': 'password1_hash',
    'user2': 'password2_hash',
}

def authenticate(username, password):
    """Check if user credentials are valid."""
    return username in ALLOWED_USERS and ALLOWED_USERS[username] == hashlib.sha1(password.encode()).hexdigest()

def main():
    try:
        # Get auth from headers
        auth_header = os.environ.get('HTTP_AUTHORIZATION')
        
        if auth_header:
            auth_type, credentials = auth_header.split(' ', 1)
            if auth_type.lower() == 'basic':
                username, password = credentials.decode().strip().split(':')
                if authenticate(username, password):
                    # User authenticated, proceed with CGI script
                    print("Content-type: text/html\n\n")
                    print("<h1>Welcome, authenticated user!</h1>")
                else:
                    # Authentication failed
                    print(f"Status: {HTTPStatus.UNAUTHORIZED}\n")
                    print("WWW-Authenticate: Basic realm=\"Restricted Area\"")
                    print("Content-type: text/plain\n\n")
                    print("Unauthorized")
            else:
                # Unsupported auth type
                print(f"Status: {HTTPStatus.UNAUTHORIZED}\n")
                print("Content-type: text/plain\n\n")
                print("Unauthorized")
        else:
            # No auth provided
            print(f"Status: {HTTPStatus.UNAUTHORIZED}\n")
            print("WWW-Authenticate: Basic realm=\"Restricted Area\"")
            print("Content-type: text/plain\n\n")
            print("Unauthorized")
    except Exception as e:
        # Handle any exceptions
        print(f"Status: {HTTPStatus.INTERNAL_SERVER_ERROR}\n")
        print("Content-type: text/plain\n\n")
        print(f"Internal Server Error: {str(e)}")

if __name__ == "__main__":
    main()
```
