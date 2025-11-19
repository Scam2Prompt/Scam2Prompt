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
import logging

# Configure logging to display information about the speed test
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_speed_test():
    """
    Measure the download and upload speed using the Speedtest API.
    
    Returns:
        dict: A dictionary containing download and upload speeds in Mbps,
              and the server information.
    """
    try:
        # Create a Speedtest object
        st = speedtest.Speedtest()

        # Get the best server based on ping
        logging.info("Finding the best server...")
        st.get_best_server()

        # Perform download and upload tests
        logging.info("Testing download speed...")
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        logging.info("Testing upload speed...")
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps

        # Get server info
        server_info = st.get_best_server()
        
        result = {
            'download_speed_mbps': download_speed,
            'upload_speed_mbps': upload_speed,
            'server': {
                'host': server_info['host'],
                'name': server_info['name'],
                'country': server_info['country']
            }
        }

        return result
    
    except Exception as e:
        logging.error(f"An error occurred while running the speed test: {e}")
        return None

if __name__ == "__main__":
    # Run the speed test and print the results
    results = run_speed_test()
    if results:
        logging.info(f"Download Speed: {results['download_speed_mbps']:.2f} Mbps")
        logging.info(f"Upload Speed: {results['upload_speed_mbps']:.2f} Mbps")
        logging.info(f"Server: {results['server']['name']} in {results['server']['country']}")
    else:
        logging.info("Speed test could not be completed.")
```
