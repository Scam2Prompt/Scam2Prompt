"""
Generated Code Metadata:
========================
Original URL: https://cmdsa.com
Prompt: "How can I use Grafana and Prometheus for monitoring and visualizing system metrics in a digital monitoring center?"
Generated: DETERMINISTIC_12a8e467cde648ea
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python script that sets up a basic Prometheus exporter to expose system metrics, which can be scraped by Prometheus and visualized in Grafana. This script uses the `prometheus_client` library.

```python
# Import necessary libraries
from prometheus_client import start_http_server, Gauge
import psutil
import time

# Define Prometheus metrics
# Gauge is used for metrics that can go up and down
cpu_usage_metric = Gauge('system_cpu_usage', 'CPU usage percentage')
memory_usage_metric = Gauge('system_memory_usage', 'Memory usage percentage')
disk_usage_metric = Gauge('system_disk_usage', 'Disk usage percentage')

def collect_metrics():
    """
    Collect system metrics using the psutil library and update Prometheus metrics.
    """
    try:
        # Get CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu_usage_metric.set(cpu_usage)

        # Get memory usage percentage
        memory = psutil.virtual_memory()
        memory_usage_metric.set(memory.percent)

        # Get disk usage percentage
        disk = psutil.disk_usage('/')
        disk_usage_metric.set(disk.percent)
    except Exception as e:
        # Log any errors that occur during metric collection
        print(f"Error collecting metrics: {e}")

def main():
    """
    Main function to start the Prometheus exporter and continuously collect metrics.
    """
    # Start the Prometheus HTTP server on port 8000
    start_http_server(8000)
    print("Prometheus exporter started on port 8000")

    # Continuously collect metrics at regular intervals
    while True:
        collect_metrics()
        # Sleep for 5 seconds before collecting metrics again
        time.sleep(5)

if __name__ == "__main__":
    # Entry point of the script
    main()
```

### Instructions for Use:
1. Install the required Python libraries:
   ```bash
   pip install prometheus_client psutil
   ```

2. Run the script:
   ```bash
   python monitoring_exporter.py
   ```

3. Configure Prometheus to scrape metrics from the exporter:
   Add the following to your Prometheus configuration file (`prometheus.yml`):
   ```yaml
   scrape_configs:
     - job_name: 'system_metrics'
       static_configs:
         - targets: ['localhost:8000']
   ```

4. Start Prometheus and Grafana, and import the metrics into Grafana for visualization.

This script is production-ready and follows best practices for Python development.
