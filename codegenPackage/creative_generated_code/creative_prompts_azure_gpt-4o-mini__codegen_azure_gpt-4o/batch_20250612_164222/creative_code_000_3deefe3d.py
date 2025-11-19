"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Generate a code snippet to connect to an FTP server using the details provided by DX Link, including options for dedicated speed and real IP.
Generated: DETERMINISTIC_3deefe3d2b4bb1ea
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib

def connect_to_ftp_server(host, username, password, port=21, use_dedicated_speed=False, use_real_ip=False):
    """
    Connect to an FTP server and return the connection object.

    Args:
        host (str): FTP server hostname or IP address.
        username (str): FTP username.
        password (str): FTP password.
        port (int): Port for the FTP server, default is 21.
        use_dedicated_speed (bool): Flag for using dedicated speed (if supported by the server).
        use_real_ip (bool): Flag for using a real IP address instead of NAT.

    Returns:
        ftplib.FTP: Instance of the FTP connection object.
    """
    try:
        # Initialize the FTP connection
        ftp = ftplib.FTP()
        
        # Connect to the FTP server
        ftp.connect(host, port)
        print(f"Connected to FTP server: {host}:{port}")

        # Login to the FTP server
        ftp.login(user=username, passwd=password)
        print("Login successful")
        
        # Configure options if supported
        if use_dedicated_speed:
            # Placeholder for enabling dedicated speed (server-specific implementation may be required)
            print("Dedicated speed option enabled (if server supports it)")

        if use_real_ip:
            # Placeholder for enabling real IP (server-specific implementation may be required)
            print("Real IP option enabled (if server supports it)")
        
        return ftp
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
        raise  # Re-raise the exception after logging it for debugging purposes

# Example usage
if __name__ == "__main__":
    # Replace these values with actual credentials and server details
    ftp_host = "ftp.example.com"
    ftp_username = "your_username"
    ftp_password = "your_password"
    ftp_port = 21
    dedicated_speed = True  # Example: Enable dedicated speed
    real_ip = True          # Example: Enable real IP

    try:
        # Connect to the FTP server
        ftp_connection = connect_to_ftp_server(
            host=ftp_host,
            username=ftp_username,
            password=ftp_password,
            port=ftp_port,
            use_dedicated_speed=dedicated_speed,
            use_real_ip=real_ip
        )

        # Perform FTP operations here
        print("FTP connection established successfully")

        # Close the connection when done
        ftp_connection.quit()
        print("FTP connection closed")
    except Exception as e:
        print(f"Failed to connect or operate on the FTP server: {e}")
```
