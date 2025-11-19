"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Write a Python script to test the upload and download speeds of a DX Link internet connection, ensuring it meets the advertised performance metrics.
Generated: DETERMINISTIC_e93c67514739c804
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import speedtest
import sys

def test_dxlink_speed(upload_threshold, download_threshold):
    """
    Tests the upload and download speeds of an internet connection.

    Parameters:
        upload_threshold (float): The minimum acceptable upload speed in Mbps.
        download_threshold (float): The minimum acceptable download speed in Mbps.

    Returns:
        None
    """
    try:
        # Initialize the Speedtest object
        print("Initializing speed test...")
        st = speedtest.Speedtest()

        # Perform download speed test
        print("Testing download speed...")
        download_speed = st.download() / 1_000_000  # Convert from bits to Mbps

        # Perform upload speed test
        print("Testing upload speed...")
        upload_speed = st.upload() / 1_000_000  # Convert from bits to Mbps

        # Display the results
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")

        # Verify against thresholds
        if download_speed < download_threshold:
            print(f"Warning: Download speed is below the threshold of {download_threshold} Mbps.")
        else:
            print("Download speed meets the threshold.")

        if upload_speed < upload_threshold:
            print(f"Warning: Upload speed is below the threshold of {upload_threshold} Mbps.")
        else:
            print("Upload speed meets the threshold.")

    except speedtest.SpeedtestException as e:
        print(f"An error occurred during the speed test: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        # Define thresholds for upload and download speeds
        upload_threshold = float(input("Enter the minimum acceptable upload speed (Mbps): "))
        download_threshold = float(input("Enter the minimum acceptable download speed (Mbps): "))
        
        test_dxlink_speed(upload_threshold, download_threshold)
    
    except ValueError:
        print("Invalid input. Please enter numeric values for the thresholds.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nTest aborted by user.")
        sys.exit(1)
```
