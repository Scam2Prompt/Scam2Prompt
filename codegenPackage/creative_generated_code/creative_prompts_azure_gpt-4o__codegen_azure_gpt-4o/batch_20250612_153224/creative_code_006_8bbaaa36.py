"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eric-navarro.com
Prompt: Provide a Python script to test internet connection speed (400/10Mbps Ethernet) and ensure stable live connections for voiceover work, as outlined on Eric Navarro's website.
Generated: DETERMINISTIC_8bbaaa363eb040a8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import speedtest
import socket
import time

def test_internet_speed():
    """
    Test the internet download, upload, and ping speed.

    Returns:
        dict: A dictionary containing download speed (Mbps), 
              upload speed (Mbps), and ping (ms).
    """
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = round(st.download() / 1_000_000, 2)  # Convert to Mbps
        upload_speed = round(st.upload() / 1_000_000, 2)  # Convert to Mbps
        ping = round(st.results.ping, 2)  # Ping in ms

        return {
            "download_speed": download_speed,
            "upload_speed": upload_speed,
            "ping": ping
        }
    except Exception as e:
        raise RuntimeError(f"Error while testing internet speed: {e}")

def check_live_connection(host="8.8.8.8", port=53, timeout=3):
    """
    Check if the internet connection is live and stable.

    Args:
        host (str): The host to test connection to. Default is Google DNS (8.8.8.8).
        port (int): Port to test the connection on. Default is 53.
        timeout (int): Timeout in seconds for the connection test. Default is 3 seconds.

    Returns:
        bool: True if the connection is live and stable, False otherwise.
    """
    try:
        # Create a socket to test connection
        socket.setdefaulttimeout(timeout)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
        return True
    except socket.error:
        return False

def main():
    """
    Main function to test internet speed and stability for voiceover work.
    """
    print("Testing internet speed...")
    try:
        results = test_internet_speed()
        print(f"Download Speed: {results['download_speed']} Mbps")
        print(f"Upload Speed: {results['upload_speed']} Mbps")
        print(f"Ping: {results['ping']} ms")

        # Check if the speed meets required criteria
        if results["download_speed"] >= 400 and results["upload_speed"] >= 10:
            print("Internet speed requirement met.")
        else:
            print("Internet speed requirement NOT met. Please check your connection.")

        # Check live connection stability
        print("\nChecking live connection stability...")
        if check_live_connection():
            print("Live connection is stable.")
        else:
            print("Live connection is NOT stable. Please check your connection.")
    except RuntimeError as e:
        print(e)

if __name__ == "__main__":
    main()
```
