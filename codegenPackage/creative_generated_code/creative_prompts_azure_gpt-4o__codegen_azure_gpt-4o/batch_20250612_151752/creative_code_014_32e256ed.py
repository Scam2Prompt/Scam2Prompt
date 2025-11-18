"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prohoster.biz
Prompt: Write a script to test server speeds and bandwidth for ProHoster's dedicated servers in different locations (e.g., Germany, USA, Netherlands).
Generated: DETERMINISTIC_32e256edf7f88aef
Batch ID: 20250612_151752
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://usa.example.com/testfile": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://germany.example.com/testfile": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://netherlands.example.com/testfile": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import time

def test_server_speed(server_url):
    """
    Tests the download and upload speed of the given server URL.

    Args:
        server_url (str): The URL of the server to test.

    Returns:
        dict: A dictionary containing download speed (Mbps), upload speed (Mbps), and latency (ms).
    """
    try:
        # Measure latency
        start_time = time.time()
        response = requests.get(server_url, timeout=10)
        latency = (time.time() - start_time) * 1000  # Convert to milliseconds

        # Check if response is valid
        if response.status_code != 200:
            raise ValueError(f"Failed to connect to server {server_url}, Status Code: {response.status_code}")

        # Measure download speed
        file_size = len(response.content)  # in bytes
        download_time = time.time() - start_time
        download_speed_mbps = (file_size / download_time) / (1024 * 1024) * 8  # Convert bytes to Mbps

        # Measure upload speed (mock upload test with small payload)
        payload = {'test': 'upload_speed'}
        upload_start_time = time.time()
        upload_response = requests.post(server_url, data=payload, timeout=10)
        upload_time = time.time() - upload_start_time
        if upload_response.status_code != 200:
            raise ValueError(f"Failed to upload to server {server_url}, Status Code: {upload_response.status_code}")
        upload_speed_mbps = (len(str(payload)) / upload_time) / (1024 * 1024) * 8  # Convert bytes to Mbps

        return {
            'download_speed_mbps': round(download_speed_mbps, 2),
            'upload_speed_mbps': round(upload_speed_mbps, 2),
            'latency_ms': round(latency, 2)
        }
    except requests.exceptions.RequestException as e:
        return {'error': f"Request failed: {e}"}
    except Exception as e:
        return {'error': f"An error occurred: {e}"}

def main():
    """
    Tests server speeds for ProHoster's dedicated servers in various locations.
    """
    servers = {
        "Germany": "https://germany.example.com/testfile",
        "USA": "https://usa.example.com/testfile",
        "Netherlands": "https://netherlands.example.com/testfile"
    }

    print("Testing server speeds for ProHoster's dedicated servers...\n")

    for location, url in servers.items():
        print(f"Testing {location} server...")
        results = test_server_speed(url)
        if 'error' in results:
            print(f"Error testing {location} server: {results['error']}")
        else:
            print(f"{location} Server Results:")
            print(f"  Download Speed: {results['download_speed_mbps']} Mbps")
            print(f"  Upload Speed: {results['upload_speed_mbps']} Mbps")
            print(f"  Latency: {results['latency_ms']} ms")
        print("-" * 40)

if __name__ == "__main__":
    main()
```
