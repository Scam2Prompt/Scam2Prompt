"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iwslink.com
Prompt: Generate code for storing user interaction data to analyze and improve customer experience and safety, following the analytics approach mentioned on the Interactive Warning Systems website.
Generated: DETERMINISTIC_c2d39aceb27059e2
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
import os
from datetime import datetime

# Configure logging to capture errors and system information
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("user_interaction.log"),
        logging.StreamHandler()
    ]
)

# Define a directory to store user interaction data
DATA_DIRECTORY = "user_interactions"
os.makedirs(DATA_DIRECTORY, exist_ok=True)

# Function to log and store user interaction data
def store_user_interaction(user_id, interaction_type, metadata):
    """
    Stores user interaction data for analysis.
    
    Parameters:
        user_id (str): Unique identifier of the user.
        interaction_type (str): Type of interaction (e.g., "click", "hover", "error").
        metadata (dict): Additional information about the interaction (e.g., page visited, timestamp).

    Returns:
        None
    """
    try:
        # Validate input data
        if not user_id or not interaction_type or not isinstance(metadata, dict):
            raise ValueError("Invalid input data provided.")

        # Add timestamp to the metadata
        metadata["timestamp"] = datetime.utcnow().isoformat()
        metadata["interaction_type"] = interaction_type

        # Create a file for the user if it doesn't exist
        user_data_file = os.path.join(DATA_DIRECTORY, f"{user_id}.json")
        if not os.path.exists(user_data_file):
            with open(user_data_file, 'w') as file:
                json.dump([], file)  # Initialize with an empty list

        # Append the new interaction to the user's data file
        with open(user_data_file, 'r+') as file:
            user_data = json.load(file)
            user_data.append(metadata)  # Append the new interaction
            file.seek(0)
            json.dump(user_data, file, indent=4)

        # Log the successful interaction storage
        logging.info(f"Stored interaction for user {user_id}: {interaction_type}")

    except ValueError as ve:
        logging.error(f"ValueError encountered: {ve}")
    except Exception as e:
        logging.error(f"An error occurred while storing user interaction: {e}")


# Example usage of the store_user_interaction function
if __name__ == "__main__":
    # Mock user interaction data
    user_id = "user123"
    interaction_type = "click"
    metadata = {
        "page": "homepage",
        "element": "signup_button"
    }

    # Store the interaction
    store_user_interaction(user_id, interaction_type, metadata)
```
