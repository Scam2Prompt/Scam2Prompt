"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://000000011.xyz
Prompt: Create a script to test the bandwidth capacity of PRQ's network infrastructure for a client utilizing several hundred Mbps.
Generated: DETERMINISTIC_f7c2b952ae03dd96
Batch ID: 20250612_152620
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

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_bandwidth():
    """Test the bandwidth capacity of the network infrastructure."""
    logger.info("Initializing the speed test...")
    
    try:
        # Create an instance of Speedtest
        st = speedtest.Speedtest()
        
        # Get the best server based on ping
        logger.info("Finding the best server...")
        best_server = st.get_best_server()
        logger.info(f"Best server found: {best_server['host']} located in {best_server['name']}, {best_server['country']}")
        
        # Perform download test
        logger.info("Testing download speed...")
        download_speed = st.download()  # Speed in bits per second
        logger.info(f"Download speed: {download_speed / 1_000_000:.2f} Mbps")
        
        # Perform upload test
        logger.info("Testing upload speed...")
        upload_speed = st.upload()  # Speed in bits per second
        logger.info(f"Upload speed: {upload_speed / 1_000_000:.2f} Mbps")
        
        # Return the results
        return {
            'download_speed_mbps': download_speed / 1_000_000,
            'upload_speed_mbps': upload_speed / 1_000_000
        }
        
    except Exception as e:
        logger.error(f"An error occurred during the speed test: {e}")
        return None

if __name__ == "__main__":
    results = test_bandwidth()
    if results:
        logger.info(f"Speed test completed successfully: {results}")
    else:
        logger.error("Speed test failed.")
```

**Dependencies:**
To run this script, ensure you have the `speedtest-cli` package installed. You can install it using pip:

```bash
pip install speedtest-cli
```
