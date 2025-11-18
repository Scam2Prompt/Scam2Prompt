"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Write a Python script to measure internet speed using DX Link's package specifications, including upload and download speeds as described on their website.
Generated: DETERMINISTIC_e63694ce4484d013
Batch ID: 20250612_151513
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def measure_internet_speed():
    """
    Measures the internet upload and download speeds using the Speedtest library.

    Returns:
        dict: A dictionary containing download and upload speeds in Mbps.
    """
    try:
        # Create a Speedtest object
        st = speedtest.Speedtest()

        # Get the best server based on ping
        logging.info("Finding the best server...")
        st.get_best_server()

        # Measure download speed
        logging.info("Measuring download speed...")
        download_speed = st.download() / 1_000_000  # Convert from bps to Mbps

        # Measure upload speed
        logging.info("Measuring upload speed...")
        upload_speed = st.upload() / 1_000_000  # Convert from bps to Mbps

        # Returning results as a dictionary
        return {
            "download_speed_mbps": round(download_speed, 2),
            "upload_speed_mbps": round(upload_speed, 2)
        }

    except Exception as e:
        logging.error("An error occurred while measuring internet speed: %s", e)
        return {"error": str(e)}

if __name__ == "__main__":
    # Run the speed test and print the results
    results = measure_internet_speed()
    if "error" not in results:
        logging.info("Download Speed: %s Mbps", results["download_speed_mbps"])
        logging.info("Upload Speed: %s Mbps", results["upload_speed_mbps"])
    else:
        logging.error("Failed to measure internet speed: %s", results["error"])
```
