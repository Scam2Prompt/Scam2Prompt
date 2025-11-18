"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.org
Prompt: Recommend tools or APIs for accessing Speedtest Performance Directory data, and provide example code for extracting server performance metrics.
Generated: DETERMINISTIC_8aca49c143fa3467
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to access Speedtest Performance Directory data
# This script uses the Speedtest.net API (via the "speedtest-cli" library) to fetch server performance metrics.
# Note: Ensure you have installed the `speedtest-cli` library before running the script.

import speedtest

def get_speedtest_metrics():
    """
    Fetches and returns server performance metrics using the Speedtest.net API.

    Returns:
        dict: A dictionary containing download speed, upload speed, and ping.
    """
    try:
        # Initialize Speedtest object
        st = speedtest.Speedtest()

        # Get the best server based on ping
        st.get_best_server()

        # Measure download speed (in bits per second)
        download_speed = st.download()

        # Measure upload speed (in bits per second)
        upload_speed = st.upload()

        # Measure ping (latency in milliseconds)
        ping = st.results.ping

        # Return the results as a dictionary
        return {
            'download_speed': download_speed / 1_000_000,  # Convert to Mbps
            'upload_speed': upload_speed / 1_000_000,      # Convert to Mbps
            'ping': ping                                   # In milliseconds
        }

    except Exception as e:
        # Handle any errors (e.g., no internet connection)
        return {
            'error': f"An error occurred: {str(e)}"
        }

# Example usage
if __name__ == "__main__":
    metrics = get_speedtest_metrics()
    if 'error' in metrics:
        print(f"Error: {metrics['error']}")
    else:
        print(f"Download Speed: {metrics['download_speed']:.2f} Mbps")
        print(f"Upload Speed: {metrics['upload_speed']:.2f} Mbps")
        print(f"Ping: {metrics['ping']:.2f} ms")
```

**Instructions to Run:**
1. Install the `speedtest-cli` Python library if not already installed:
   ```bash
   pip install speedtest-cli
   ```
2. Run the script using Python.
3. The script will output the download speed, upload speed, and ping.

**Production Notes:**
- Ensure proper network permissions if running in a restricted environment.
- Consider logging results to a file or monitoring tool for production use.
