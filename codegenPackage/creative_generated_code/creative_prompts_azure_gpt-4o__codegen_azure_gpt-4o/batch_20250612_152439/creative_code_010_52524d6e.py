"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet-app.pages.dev
Prompt: Write a script using Lava SDK to fetch geolocation-based QoS analytics for node providers serving the Optimism blockchain.
Generated: DETERMINISTIC_52524d6e92279d90
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules from the Lava SDK
from lava_sdk import LavaClient, LavaException
import sys

# Function to fetch QoS analytics for node providers serving Optimism blockchain based on geolocation
def fetch_qos_analytics(geolocation='global'):
    """
    Fetch geolocation-based QoS analytics for node providers serving Optimism blockchain.

    Parameters:
        geolocation (str): The geolocation filter for the analytics (default: 'global').
    
    Returns:
        None. Prints the QoS analytics to the console.
    """
    try:
        # Initialize the LavaClient
        lava_client = LavaClient(api_key='your_api_key_here')  # Replace with your actual Lava API key

        # Query QoS analytics for Optimism blockchain with geolocation filter
        qos_analytics = lava_client.get_qos_analytics(
            blockchain='optimism',
            geolocation=geolocation
        )

        # Validate and display results
        if qos_analytics and isinstance(qos_analytics, list):
            print(f"QoS Analytics for Optimism blockchain nodes (Geolocation: {geolocation}):")
            for analytic in qos_analytics:
                print(f"Provider: {analytic['provider']}, Latency: {analytic['latency']}ms, Availability: {analytic['availability']}%")
        else:
            print("No QoS analytics data available for the specified geolocation.")

    except LavaException as e:
        # Handle exceptions from the Lava SDK
        print(f"Error fetching QoS analytics: {str(e)}")
    except Exception as e:
        # Handle general exceptions
        print(f"An unexpected error occurred: {str(e)}")
    finally:
        # Clean up or close resources if needed
        print("Script execution completed.")

# Entry point for the script
if __name__ == "__main__":
    try:
        # Obtain geolocation input from the user (optional)
        geolocation_input = input("Enter geolocation filter (default: 'global'): ").strip()
        geolocation = geolocation_input if geolocation_input else 'global'

        # Fetch and display QoS analytics
        fetch_qos_analytics(geolocation=geolocation)
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
        sys.exit(1)
```

**Note:** Replace `'your_api_key_here'` with your actual Lava API key. Ensure the Lava SDK is installed and properly configured in your environment before running this script. You can install the SDK using `pip install lava-sdk` if required.
