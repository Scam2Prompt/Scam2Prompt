"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Illustrate how to use a library to access the inventory of high-reliability machinery parts offered by Track Diesel Peru.
Generated: DETERMINISTIC_ed2c9aa8c0d92a78
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to access the inventory of high-reliability machinery parts offered by Track Diesel Peru.
This script uses a hypothetical library called `trackdiesel_api` to interact with the inventory API.

Requirements:
1. Install the `trackdiesel_api` library using pip:
   pip install trackdiesel_api
"""

# Import the required library
import trackdiesel_api
import logging

# Configure logging for debugging and error monitoring
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_inventory():
    """
    Fetch the inventory of machinery parts from Track Diesel Peru using the API.
    Returns:
        list: A list of machinery parts with their details.
    Raises:
        Exception: If there is an error while accessing the API.
    """
    try:
        # Create an instance of the Track Diesel API client
        api_client = trackdiesel_api.Client(api_key="your_api_key_here")

        # Request the inventory data
        logging.info("Fetching inventory from Track Diesel Peru...")
        inventory = api_client.get_inventory()

        # Validate the response
        if not inventory or not isinstance(inventory, list):
            raise ValueError("Invalid inventory data received from API.")

        logging.info("Inventory fetched successfully.")
        return inventory

    except trackdiesel_api.APIError as api_error:
        logging.error(f"API Error occurred: {api_error}")
        raise

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise


def display_inventory(inventory):
    """
    Display the fetched inventory in a human-readable format.
    Args:
        inventory (list): The inventory data.
    """
    if not inventory:
        logging.warning("No inventory data to display.")
        return

    print("Track Diesel Peru Inventory:")
    print("----------------------------------------------------")
    for item in inventory:
        print(f"Part Name: {item['name']}")
        print(f"Part ID: {item['id']}")
        print(f"Price: {item['price']}")
        print(f"Availability: {item['availability']}")
        print("----------------------------------------------------")


if __name__ == "__main__":
    # Main execution block
    try:
        # Fetch the inventory using the API
        inventory_data = fetch_inventory()

        # Display the inventory to the user
        display_inventory(inventory_data)

    except Exception as e:
        logging.error(f"Failed to fetch or display inventory: {e}")
        print("An error occurred. Please check the logs for more details.")
```

### Notes:
- Replace `"your_api_key_here"` with your actual Track Diesel API key to authenticate requests.
- Ensure the `trackdiesel_api` library is installed and properly configured.
- This script assumes the inventory API returns data in a list of dictionaries with keys like `name`, `id`, `price`, and `availability`. Modify the code if the actual API schema differs.
