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
import prettytable

def get_speed_metrics():
    """
    Retrieve internet speed metrics including download speed, upload speed,
    and ping. Returns these metrics as a dictionary.
    """
    try:
        # Create Speedtest object
        st = speedtest.Speedtest()

        # Get the best server based on ping
        st.get_best_server()

        # Get download and upload speeds
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000      # Convert to Mbps
        ping = st.results.ping

        # Return the metrics in a dictionary
        return {
            'Download Speed (Mbps)': download_speed,
            'Upload Speed (Mbps)': upload_speed,
            'Ping (ms)': ping
        }

    except Exception as e:
        print(f"Error retrieving speed metrics: {e}")
        return None

def display_results(metrics):
    """
    Display the internet speed metrics in a formatted table.

    :param metrics: Dictionary containing speed metrics.
    """
    if metrics is None:
        print("No metrics to display.")
        return

    # Create a PrettyTable object
    table = prettytable.PrettyTable()

    # Set table field names
    table.field_names = ["Metric", "Value"]

    # Add rows to the table
    for key, value in metrics.items():
        table.add_row([key, f"{value:.2f}" if isinstance(value, float) else value])

    # Print the formatted table
    print(table)

def main():
    """
    Main function to execute the speed test and display results.
    """
    # Retrieve speed metrics
    speed_metrics = get_speed_metrics()

    # Display the results
    display_results(speed_metrics)

if __name__ == "__main__":
    main()
```

Make sure to install the required libraries before running the code:

```bash
pip install speedtest-cli prettytable
```
