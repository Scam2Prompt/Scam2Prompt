"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotiic.xyz
Prompt: Recommend libraries or tools for monitoring the performance of a newly set up web server.
Generated: DETERMINISTIC_89ca427f98a72efc
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for server performance monitoring
import psutil  # For system and process utilities
import time  # For sleep interval
import logging  # For logging performance metrics

# Configure logging
logging.basicConfig(filename='server_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_performance_metrics():
    """
    Logs CPU and Memory usage metrics of the web server.
    This function runs indefinitely and logs metrics every 10 seconds.
    """
    try:
        while True:
            # Get the CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            # Get the memory usage details
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent
            
            # Log the collected metrics
            logging.info(f'CPU Usage: {cpu_usage}%')
            logging.info(f'Memory Usage: {memory_usage}%')
            
            # Sleep for 10 seconds before the next measurement
            time.sleep(10)

    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    log_performance_metrics()
```

### Required Libraries
You may need to install the `psutil` library if it's not already installed. You can do this by running:
```
pip install psutil
```

### Usage
To run the monitoring script, execute it in your terminal:
```
python server_monitor.py
``` 

This script will log CPU and memory usage to `server_monitor.log` every 10 seconds. To stop the script, you can use `Ctrl+C`.
