"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ssly.vip
Prompt: Write code to upload a custom `index.html` file to the FTP root directory of a website, assuming FTP credentials are managed through a control panel system.
Generated: DETERMINISTIC_3d8a8ef26ae52c80
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib
import os

class FTPUploader:
    def __init__(self, ftp_host, ftp_user, ftp_pass):
        """
        Initializes the FTPUploader with FTP credentials.

        :param ftp_host: The hostname of the FTP server.
        :param ftp_user: Username for FTP authentication.
        :param ftp_pass: Password for FTP authentication.
        """
        self.ftp_host = ftp_host
        self.ftp_user = ftp_user
        self.ftp_pass = ftp_pass

    def upload_file(self, local_file_path):
        """
        Uploads a file to the FTP server's root directory.

        :param local_file_path: The path to the local file to be uploaded.
        :raises FileNotFoundError: If the local file does not exist.
        :raises ftplib.all_errors: For any FTP-related errors during upload.
        """
        # Check if the file exists
        if not os.path.isfile(local_file_path):
            raise FileNotFoundError(f"The file {local_file_path} does not exist.")

        # Get the filename from the file path
        filename = os.path.basename(local_file_path)

        # Establish FTP connection
        try:
            with ftplib.FTP(self.ftp_host) as ftp:
                ftp.login(self.ftp_user, self.ftp_pass)
                print(f"Connected to FTP server: {self.ftp_host}")

                # Open the local file in binary mode for reading
                with open(local_file_path, 'rb') as file:
                    # Upload the file to the FTP server
                    ftp.storbinary(f'STOR {filename}', file)
                    print(f"Successfully uploaded {filename} to {self.ftp_host}")

        except ftplib.all_errors as e:
            print(f"FTP error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    # Replace with your FTP credentials and the path to your index.html
    ftp_host = "your-ftp-host.com"
    ftp_user = "your-ftp-username"
    ftp_pass = "your-ftp-password"
    local_file_path = "path/to/your/index.html"

    uploader = FTPUploader(ftp_host, ftp_user, ftp_pass)
    try:
        uploader.upload_file(local_file_path)
    except Exception as e:
        print(f"Failed to upload file: {e}")
```
