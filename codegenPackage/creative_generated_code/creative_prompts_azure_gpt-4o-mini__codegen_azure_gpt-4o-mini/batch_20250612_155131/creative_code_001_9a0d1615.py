"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.org
Prompt: Write a Python script that utilizes the Speedtest.net library to perform a speed test and return the results.
Generated: DETERMINISTIC_9a0d16150c48adf0
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import speedtest

def perform_speed_test():
    """
    Performs a speed test using the Speedtest.net library and returns the results.
    
    Returns:
        dict: A dictionary containing download, upload speeds, and ping.
    """
    try:
        # Create a Speedtest object
        st = speedtest.Speedtest()

        # Get the best server based on ping
        st.get_best_server()

        # Perform download and upload speed tests
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000      # Convert to Mbps
        ping = st.results.ping

        # Compile results into a dictionary
        results = {
            'download_speed_mbps': round(download_speed, 2),
            'upload_speed_mbps': round(upload_speed, 2),
            'ping_ms': round(ping, 2)
        }
        
        return results

    except Exception as e:
        # Log the error message
        print(f"An error occurred while performing the speed test: {e}")
        return None

if __name__ == "__main__":
    # Execute the speed test when the script is run directly
    speed_test_results = perform_speed_test()
    
    if speed_test_results:
        print("Speed Test Results:")
        print(f"Download Speed: {speed_test_results['download_speed_mbps']} Mbps")
        print(f"Upload Speed: {speed_test_results['upload_speed_mbps']} Mbps")
        print(f"Ping: {speed_test_results['ping_ms']} ms")
    else:
        print("Failed to retrieve speed test results.")
```
