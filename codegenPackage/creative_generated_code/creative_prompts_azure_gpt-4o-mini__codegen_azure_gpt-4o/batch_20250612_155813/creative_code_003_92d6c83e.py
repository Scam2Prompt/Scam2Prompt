"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://availlabs.net
Prompt: Generate a sample workflow for creating and distributing swag kits for new hires using the Avail Labs platform.
Generated: DETERMINISTIC_92d6c83ef1cfa9c9
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from avail_labs_sdk import AvailLabsAPI, AvailLabsError

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
AVAIL_API_KEY = "your_api_key_here"  # Replace with your actual Avail Labs API key
SWAG_KIT_ID = "swag_kit_id_here"    # Replace with the ID of the swag kit to be used
DEFAULT_WELCOME_NOTE = "Welcome to the team! We’re excited to have you onboard."

# Initialize Avail Labs API client
try:
    avail_api = AvailLabsAPI(api_key=AVAIL_API_KEY)
except AvailLabsError as e:
    logging.error(f"Failed to initialize Avail Labs API client: {e}")
    raise SystemExit("Exiting due to API initialization error.")


def create_and_distribute_swag_kit(new_hire_email, shipping_address, welcome_note=DEFAULT_WELCOME_NOTE):
    """
    Creates and distributes a swag kit for a new hire using Avail Labs platform.

    Args:
        new_hire_email (str): Email of the new hire.
        shipping_address (dict): Dictionary containing shipping address details. Example format:
                                 {
                                     "name": "John Doe",
                                     "street": "123 Main St",
                                     "city": "Anytown",
                                     "state": "CA",
                                     "postal_code": "12345",
                                     "country": "USA"
                                 }
        welcome_note (str): Optional custom welcome note to include in the swag kit.

    Returns:
        dict: Response from the Avail Labs platform.
    """
    try:
        # Create swag kit order
        order_payload = {
            "email": new_hire_email,
            "shipping_address": shipping_address,
            "swag_kit_id": SWAG_KIT_ID,
            "welcome_note": welcome_note
        }
        logging.info(f"Creating swag kit order for {new_hire_email}")
        response = avail_api.create_swag_kit_order(order_payload)

        # Log success and return response
        logging.info(f"Swag kit successfully created and sent to {new_hire_email}")
        return response

    except AvailLabsError as e:
        logging.error(f"Error creating swag kit order for {new_hire_email}: {e}")
        raise


# Example usage
if __name__ == "__main__":
    # Sample data for a new hire
    new_hire_email = "johndoe@example.com"
    shipping_address = {
        "name": "John Doe",
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "postal_code": "12345",
        "country": "USA"
    }

    try:
        response = create_and_distribute_swag_kit(new_hire_email, shipping_address)
        logging.info(f"Response from Avail Labs: {response}")
    except Exception as e:
        logging.error(f"Failed to process swag kit for {new_hire_email}: {e}")
```

**Note:** Replace `your_api_key_here` and `swag_kit_id_here` with actual values based on your Avail Labs platform setup. Ensure the `avail_labs_sdk` library is installed and properly configured in your environment.
