"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.org
Prompt: How can I use the Speedtest API to measure broadband speed programmatically?
Generated: DETERMINISTIC_3f787ed130c364f3
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

def test_internet_speed():
    """
    Measure broadband speed using the Speedtest API.
    Returns download speed, upload speed, and ping as a dictionary.
    """
    try:
        # Initialize the Speedtest instance
        st = speedtest.Speedtest()

        # Fetch the best server based on ping and location
        st.get_best_server()

        # Measure download speed (in bits per second)
        download_speed = st.download()

        # Measure upload speed (in bits per second)
        upload_speed = st.upload()

        # Measure ping (in milliseconds)
        ping_result = st.results.ping

        # Convert speeds from bits per second to Mbps for readability
        results = {
            "download_speed_mbps": round(download_speed / 1_000_000, 2),
            "upload_speed_mbps": round(upload_speed / 1_000_000, 2),
            "ping_ms": ping_result
        }

        return results

    except Exception as e:
        # Handle any errors that occur during the speed test
        return {"error": str(e)}

if __name__ == "__main__":
    # Perform the speed test and display the results
    speed_results = test_internet_speed()
    if "error" in speed_results:
        print(f"Error: {speed_results['error']}")
    else:
        print(f"Download Speed: {speed_results['download_speed_mbps']} Mbps")
        print(f"Upload Speed: {speed_results['upload_speed_mbps']} Mbps")
        print(f"Ping: {speed_results['ping_ms']} ms")
```

**Dependencies**:
1. Ensure you have the `speedtest-cli` Python library installed. Install it using:
   ```bash
   pip install speedtest-cli
   ```
