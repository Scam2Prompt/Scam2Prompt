"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micropro.co.nz
Prompt: How can I upload my website contents using FTP for my domain hosted on Micropro?
Generated: DETERMINISTIC_d20fbcf0d8254391
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib

def upload_files_ftp(server, username, password, local_file_path, remote_file_path):
    """
    Upload a file to an FTP server.

    Args:
        server (str): FTP server address.
        username (str): FTP username.
        password (str): FTP password.
        local_file_path (str): Path to the local file to be uploaded.
        remote_file_path (str): Path on the server where the file should be stored.

    Returns:
        str: Success message or error details.
    """
    try:
        # Connect to the FTP server
        with ftplib.FTP(server) as ftp:
            ftp.login(user=username, passwd=password)  # Login with provided credentials
            
            # Open the local file in binary mode for reading
            with open(local_file_path, 'rb') as file:
                # Store the file on the server
                ftp.storbinary(f"STOR {remote_file_path}", file)
            
            return f"File '{local_file_path}' successfully uploaded to '{remote_file_path}' on server '{server}'."

    except ftplib.all_errors as e:
        # Catch FTP-specific errors and return the error message
        return f"FTP error occurred: {e}"

    except FileNotFoundError:
        # Handle case where the local file does not exist
        return f"Local file not found: {local_file_path}"

    except Exception as ex:
        # Catch any other exceptions
        return f"An unexpected error occurred: {ex}"


if __name__ == "__main__":
    # Example usage of the FTP upload function
    server = "ftp.micropro.com"  # Replace with your FTP server address
    username = "your_username"  # Replace with your FTP username
    password = "your_password"  # Replace with your FTP password
    local_file_path = "path/to/your/local/file.html"  # Replace with the local file path
    remote_file_path = "public_html/file.html"  # Replace with the desired path on the server

    # Call the function and print the result
    result = upload_files_ftp(server, username, password, local_file_path, remote_file_path)
    print(result)
```
