"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frame.markets
Prompt: Generate a Python script that utilizes the frame.markets library to fetch real-time market data.
Generated: DETERMINISTIC_af8e94c65602c7c3
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script fetches real-time market data using the frame.markets library.
Ensure you have the 'frame.markets' library installed before running this script.
Install it using: pip install frame-markets
"""

import frame.markets as fm
import logging
import sys

# Configure logging to display errors and info
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

def fetch_market_data():
    """
    Fetches real-time market data from the frame.markets library.
    Handles connection errors and prints the retrieved data to the console.
    """
    try:
        # Initialize the client (replace 'YOUR_API_KEY' with your actual API key)
        client = fm.Client(api_key="YOUR_API_KEY")
        
        # Fetch real-time market data (example: S&P 500 index)
        market_data = client.get_real_time_data("SP500")
        
        # Log and display the fetched market data
        logging.info("Successfully fetched market data.")
        print("Market Data:", market_data)

    except fm.AuthenticationError:
        logging.error("Authentication failed. Please check your API key.")
    except fm.ConnectionError:
        logging.error("Failed to connect to the frame.markets server. Please check your network connection.")
    except fm.RequestError as e:
        logging.error(f"An error occurred while fetching market data: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the script.
    """
    logging.info("Starting the market data fetch script...")
    fetch_market_data()
    logging.info("Script execution completed.")

if __name__ == "__main__":
    main()
```

**Note:** Replace `"YOUR_API_KEY"` with your actual API key from the `frame.markets` service. Ensure you have network connectivity and the library properly installed before running the script.
