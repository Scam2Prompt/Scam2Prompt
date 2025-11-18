"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prohoster.biz
Prompt: Write a script to test server speeds and bandwidth for ProHoster's dedicated servers in different locations (e.g., Germany, USA, Netherlands).
Generated: DETERMINISTIC_32e256edf7f88aef
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import speedtest
import logging
import time

# Configure logging
logging.basicConfig(filename='server_speed_test.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define a list of server locations (country codes)
SERVER_LOCATIONS = {
    "Germany": "DE",
    "USA": "US",
    "Netherlands": "NL"
}

def test_server_speed(location_code):
    """
    Tests the download and upload speeds to the specified server location.
    
    :param location_code: The country code of the server location.
    :return: A dictionary with download and upload speeds.
    """
    try:
        st = speedtest.Speedtest()
        st.get_best_server()  # Get the best server based on ping

        # Set the server to the specified location
        st.get_servers([location_code])
        best_server = st.get_best_server()
        
        # Conduct the speed test
        logging.info(f"Testing server in {best_server['sponsor']} located in {best_server['country']}")
        download_speed = st.download()  # Download speed in bits per second
        upload_speed = st.upload()  # Upload speed in bits per second

        # Convert speeds to Mbps for easier understanding
        download_speed_mbps = download_speed / 1_000_000
        upload_speed_mbps = upload_speed / 1_000_000

        return {
            "location": best_server['country'],
            "download_speed_mbps": download_speed_mbps,
            "upload_speed_mbps": upload_speed_mbps
        }
        
    except Exception as e:
        logging.error(f"Error testing server speed for location {location_code}: {e}")
        return None

def main():
    """
    Main function to run speed tests for defined server locations.
    """
    results = []

    for location, code in SERVER_LOCATIONS.items():
        logging.info(f"Starting speed test for {location}...")
        result = test_server_speed(code)
        if result:
            results.append(result)
            logging.info(f"Results for {location}: {result}")
        time.sleep(5)  # Pause between tests to avoid server overload

    logging.info("All speed tests completed.")
    print("Speed test results:", results)

if __name__ == "__main__":
    main()
```
