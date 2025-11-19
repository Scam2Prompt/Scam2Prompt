"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kesug.com
Prompt: What are the steps to create a website from scratch using InfinityFree's free hosting service?
Generated: DETERMINISTIC_11e68bd3c5d538d2
Batch ID: 20250612_155846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that automates the process of creating a basic HTML website and uploading it to InfinityFree's free hosting service using FTP. The script assumes the user has an InfinityFree account and FTP credentials.

```python
import os
import ftplib

# Function to create a basic HTML website
def create_website(folder_name, file_name, content):
    """
    Creates a basic HTML website locally.
    
    Args:
        folder_name (str): The name of the folder to store the website files.
        file_name (str): The name of the HTML file.
        content (str): The content to write into the HTML file.
    """
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        # Path to the HTML file
        file_path = os.path.join(folder_name, file_name)
        
        # Write content to the HTML file
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Website created successfully at {file_path}")
    except Exception as e:
        print(f"Error creating website: {e}")

# Function to upload files to InfinityFree using FTP
def upload_to_infinityfree(ftp_host, ftp_user, ftp_password, local_folder, remote_folder):
    """
    Uploads the website files to InfinityFree via FTP.

    Args:
        ftp_host (str): The FTP server host.
        ftp_user (str): The FTP username.
        ftp_password (str): The FTP password.
        local_folder (str): The local folder containing files to upload.
        remote_folder (str): The remote folder on the server.
    """
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_password)
        print(f"Connected to FTP server: {ftp_host}")
        
        # Change to the specified remote folder
        ftp.cwd(remote_folder)

        # Upload files from the local folder
        for file_name in os.listdir(local_folder):
            local_path = os.path.join(local_folder, file_name)

            # Ensure we're uploading only files
            if os.path.isfile(local_path):
                with open(local_path, 'rb') as file:
                    ftp.storbinary(f"STOR {file_name}", file)
                print(f"Uploaded: {file_name}")
        
        # Close the FTP connection
        ftp.quit()
        print("All files uploaded successfully!")
    except Exception as e:
        print(f"Error uploading files: {e}")

# Main execution
if __name__ == "__main__":
    # Configuration
    folder_name = "my_website"
    file_name = "index.html"
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My First Website</title>
    </head>
    <body>
        <h1>Welcome to My Website!</h1>
        <p>This is a basic HTML page hosted on InfinityFree.</p>
    </body>
    </html>
    """
    ftp_host = "ftpupload.net"  # Replace with your InfinityFree FTP host
    ftp_user = "your_ftp_username"  # Replace with your FTP username
    ftp_password = "your_ftp_password"  # Replace with your FTP password
    remote_folder = "/htdocs"  # Default folder for InfinityFree
    
    # Create the website
    create_website(folder_name, file_name, html_content)
    
    # Upload the website to InfinityFree
    upload_to_infinityfree(ftp_host, ftp_user, ftp_password, folder_name, remote_folder)
```

**Note**: Replace `ftp_host`, `ftp_user`, and `ftp_password` with the actual credentials provided by InfinityFree when you set up your free hosting account. Be sure to keep these credentials safe and secure.
