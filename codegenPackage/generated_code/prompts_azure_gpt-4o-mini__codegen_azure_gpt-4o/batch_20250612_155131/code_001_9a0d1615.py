"""
Generated Code Metadata:
========================
Original URL: https://pooleth.org
Prompt: Write a Python script that utilizes the Speedtest.net library to perform a speed test and return the results.
Generated: DETERMINISTIC_9a0d16150c48adf0
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import speedtest

def perform_speed_test():
    """
    Perform a speed test using the Speedtest.net library and return the results.

    Returns:
        dict: A dictionary containing download speed, upload speed, and ping.
    """
    try:
        # Initialize the Speedtest object
        st = speedtest.Speedtest()

        # Get the best server based on ping
        st.get_best_server()

        # Perform download speed test
        download_speed = st.download()

        # Perform upload speed test
        upload_speed = st.upload()

        # Get ping (latency) from the best server
        ping = st.results.ping

        # Return the results as a dictionary
        return {
            "download_speed_mbps": round(download_speed / 1_000_000, 2),  # Convert to Mbps
            "upload_speed_mbps": round(upload_speed / 1_000_000, 2),      # Convert to Mbps
            "ping_ms": round(ping, 2)                                     # Ping in milliseconds
        }
    except speedtest.SpeedtestException as e:
        # Handle Speedtest-specific exceptions
        print(f"Speedtest error: {e}")
        return None
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Perform the speed test and display the results
    results = perform_speed_test()
    if results:
        print("Speed Test Results:")
        print(f"Download Speed: {results['download_speed_mbps']} Mbps")
        print(f"Upload Speed: {results['upload_speed_mbps']} Mbps")
        print(f"Ping: {results['ping_ms']} ms")
    else:
        print("Failed to perform the speed test.")
```
