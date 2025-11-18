"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marufonlinebd.net
Prompt: Suggest a library or tool to test the speed of MARUF ONLINE BD's internet packages, ensuring accurate Mbps measurements.
Generated: DETERMINISTIC_095aa20709f7b24e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script using the `speedtest-cli` library to test internet speed with accurate Mbps measurements:

```python
# Import necessary libraries
import speedtest

def test_internet_speed():
    """
    Function to test the internet speed (download, upload, and ping) 
    using the speedtest-cli library.
    Returns the results in Mbps and ms for ping.
    """
    try:
        # Initialize the Speedtest object
        st = speedtest.Speedtest()

        # Get the best server based on ping
        st.get_best_server()

        # Perform download speed test
        download_speed = st.download() / 1_000_000  # Convert from bits per second to Mbps
        
        # Perform upload speed test
        upload_speed = st.upload() / 1_000_000  # Convert from bits per second to Mbps
        
        # Get ping (latency)
        ping = st.results.ping  # Ping is already in milliseconds (ms)
        
        # Return results as a dictionary
        return {
            'download_speed_mbps': round(download_speed, 2),
            'upload_speed_mbps': round(upload_speed, 2),
            'ping_ms': round(ping, 2)
        }
    
    except Exception as e:
        # Handle any exceptions and provide error feedback
        return {'error': f"Failed to test internet speed: {str(e)}"}

if __name__ == "__main__":
    # Perform the speed test
    results = test_internet_speed()
    
    # Print the results
    if 'error' in results:
        print(results['error'])
    else:
        print(f"Download Speed: {results['download_speed_mbps']} Mbps")
        print(f"Upload Speed: {results['upload_speed_mbps']} Mbps")
        print(f"Ping: {results['ping_ms']} ms")
```

### Requirements:
1. Install the `speedtest-cli` library:
   ```bash
   pip install speedtest-cli
   ```
2. Run the script on a Python environment.
