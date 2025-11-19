"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.org
Prompt: Write a Python script that utilizes the Speedtest.net library to perform a speed test and return the results.
Generated: DETERMINISTIC_9a0d16150c48adf0
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to perform internet speed tests using the Speedtest.net library.
This script measures download speed, upload speed, and ping, and outputs the results.
"""

import speedtest

def perform_speed_test():
    """
    Function to perform a speed test using the Speedtest.net library.
    Returns:
        dict: A dictionary containing download speed (Mbps), upload speed (Mbps), and ping (ms).
    """
    try:
        # Create a Speedtest object
        st = speedtest.Speedtest()
        
        # Get the list of servers and choose the best one
        st.get_servers()
        st.get_best_server()

        # Perform download, upload, and ping tests
        download_speed = st.download() / 1_000_000  # Convert from bits to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert from bits to Mbps
        ping = st.results.ping  # Ping in ms

        # Return the speed test results
        return {
            'Download Speed (Mbps)': round(download_speed, 2),
            'Upload Speed (Mbps)': round(upload_speed, 2),
            'Ping (ms)': round(ping, 2)
        }
    except speedtest.SpeedtestException as e:
        # Handle errors from the Speedtest library
        print(f"Error performing speed test: {e}")
        return None
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to perform a speed test and display the results.
    """
    print("Performing Internet Speed Test...")
    results = perform_speed_test()
    
    if results:
        print("\nSpeed Test Results:")
        for key, value in results.items():
            print(f"{key}: {value}")
    else:
        print("Speed test failed. Please check your internet connection and try again.")

if __name__ == "__main__":
    main()
```
