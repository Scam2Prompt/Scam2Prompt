"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.org
Prompt: Write Python code using the Ookla Speedtest API to retrieve internet speed metrics (download, upload, and ping) and display the results in a formatted table.
Generated: DETERMINISTIC_272f70ab30463bbc
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import speedtest
from prettytable import PrettyTable

def get_speed_metrics():
    """
    Retrieve internet speed metrics using the Ookla Speedtest API.
    Returns:
        dict: A dictionary containing download speed (Mbps), upload speed (Mbps), and ping (ms).
    """
    try:
        # Initialize the Speedtest object
        st = speedtest.Speedtest()
        
        # Get the best server based on ping
        st.get_best_server()
        
        # Perform the download speed test
        download_speed = st.download()
        # Perform the upload speed test
        upload_speed = st.upload()
        # Fetch ping (latency) from the selected server
        ping = st.results.ping
        
        # Convert speeds to Megabits per second (Mbps) and ping to milliseconds (ms)
        return {
            "download_speed_mbps": round(download_speed / 1_000_000, 2),
            "upload_speed_mbps": round(upload_speed / 1_000_000, 2),
            "ping_ms": round(ping, 2)
        }
    except Exception as e:
        # Handle any errors gracefully
        print(f"An error occurred while retrieving the speed metrics: {e}")
        return None

def display_results(metrics):
    """
    Display internet speed metrics in a formatted table.
    Args:
        metrics (dict): A dictionary containing download, upload, and ping metrics.
    """
    if not metrics:
        print("No speed metrics to display.")
        return
    
    # Create a table for formatted output
    table = PrettyTable()
    table.field_names = ["Metric", "Value"]
    table.add_row(["Download Speed (Mbps)", metrics["download_speed_mbps"]])
    table.add_row(["Upload Speed (Mbps)", metrics["upload_speed_mbps"]])
    table.add_row(["Ping (ms)", metrics["ping_ms"]])
    
    # Print the table
    print(table)

def main():
    """
    Main function to coordinate the retrieval and display of internet speed metrics.
    """
    print("Testing internet speed, please wait...")
    metrics = get_speed_metrics()
    print("\nInternet speed test completed. Results:")
    display_results(metrics)

if __name__ == "__main__":
    main()
```
