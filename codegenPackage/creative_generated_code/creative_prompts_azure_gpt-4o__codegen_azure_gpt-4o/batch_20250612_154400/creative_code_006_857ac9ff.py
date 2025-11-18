"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axieinfinity.kesug.com
Prompt: Generate a script to test bandwidth limits on a hosting service that claims unlimited bandwidth, using the specifications mentioned on the iFastNet hosting page.
Generated: DETERMINISTIC_857ac9ff46bb1287
Batch ID: 20250612_154400
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/bigfile.dat": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/bigfile.dat`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is the requested script in Python:

```python
import requests
import time

def test_bandwidth(url, duration_minutes=5, chunk_size=1024 * 1024):
    """
    Test bandwidth limits by repeatedly downloading data from the given URL.

    Parameters:
        url (str): The URL to test bandwidth against.
        duration_minutes (int): Duration to test bandwidth in minutes.
        chunk_size (int): Size of each data chunk to download in bytes (default: 1 MB).
    """
    try:
        print(f"Starting bandwidth test on {url} for {duration_minutes} minutes...")

        # Start time tracking
        start_time = time.time()
        end_time = start_time + (duration_minutes * 60)
        total_data_downloaded = 0  # Total data downloaded in bytes

        # Run bandwidth test loop while within time duration
        while time.time() < end_time:
            try:
                # Initiate HTTP GET request
                with requests.get(url, stream=True) as response:
                    response.raise_for_status()  # Raise error if the HTTP request failed
                    
                    # Read data in chunks
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        if time.time() >= end_time:
                            break  # Stop downloading if test duration has elapsed
                        if not chunk:
                            break  # Break if no more data is received
                        total_data_downloaded += len(chunk)
            except Exception as e:
                print(f"Error during download: {e}")
                break  # Exit on download error

        # Calculate download statistics
        elapsed_time = time.time() - start_time
        total_data_mb = total_data_downloaded / (1024 * 1024)  # Convert bytes to MB
        bandwidth_mbps = (total_data_mb / elapsed_time) * 8  # Convert MB/s to Mbps

        print(f"Bandwidth test completed.")
        print(f"Total data downloaded: {total_data_mb:.2f} MB")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print(f"Average bandwidth: {bandwidth_mbps:.2f} Mbps")

    except Exception as e:
        print(f"Error occurred during bandwidth test: {e}")

if __name__ == "__main__":
    # URL for testing purposes (replace with actual URL from hosting provider)
    TEST_URL = "https://example.com/bigfile.dat"  # The URL should point to a large downloadable file
    TEST_DURATION_MINUTES = 5  # Duration of test in minutes

    # Run the bandwidth test
    test_bandwidth(TEST_URL, TEST_DURATION_MINUTES)
```

**Notes:**
1. Replace `https://example.com/bigfile.dat` with a URL to a large file hosted on the service you are testing.
2. Ensure the URL allows large downloads and does not have restrictions, such as authentication or rate limiting. 
3. Install the required library (`requests`) using `pip install requests` if not already installed.
