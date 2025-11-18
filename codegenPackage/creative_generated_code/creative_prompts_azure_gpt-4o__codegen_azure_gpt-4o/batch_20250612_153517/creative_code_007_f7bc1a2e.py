"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://65c141af32b05a11818b2704--delicate-wisp-a6ee1d.netlify.app
Prompt: Provide a code example for using Matrica to authenticate users and retrieve their selected blockchain network.
Generated: DETERMINISTIC_f7bc1a2e96b2d584
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code that demonstrates user authentication and retrieval of blockchain network selection using Matrica SDK for Python:

```python
import matrica_sdk
from matrica_sdk.exceptions import MatricaAuthError, MatricaAPIError

# Configure Matrica SDK
API_KEY = "your-api-key-here"  # Replace with your Matrica API key
matrica = matrica_sdk.Matrica(api_key=API_KEY)

def authenticate_and_get_network(user_id):
    """
    Authenticate a user and retrieve their selected blockchain network.

    Args:
        user_id (str): The unique ID of the user.

    Returns:
        str: The name of the selected blockchain network, or None if not set.
    """
    try:
        # Authenticate the user
        user = matrica.authenticate(user_id)
        
        if user.is_authenticated:
            print(f"User {user_id} authenticated successfully.")
            
            # Retrieve user's selected blockchain network
            selected_network = user.get_selected_network()
            
            if selected_network:
                print(f"User {user_id} has selected the blockchain network: {selected_network}.")
                return selected_network
            else:
                print(f"User {user_id} has not selected a blockchain network yet.")
                return None
        else:
            print(f"User {user_id} failed to authenticate.")
            return None

    except MatricaAuthError as auth_error:
        print(f"Authentication error for user {user_id}: {auth_error}")
        return None
    except MatricaAPIError as api_error:
        print(f"API error encountered: {api_error}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example user ID (replace with actual user ID from your system)
    example_user_id = "user123"

    # Authenticate the user and retrieve the selected network
    blockchain_network = authenticate_and_get_network(example_user_id)

    # Output the result
    if blockchain_network:
        print(f"Blockchain network selected by user {example_user_id}: {blockchain_network}")
    else:
        print(f"No blockchain network selected by user {example_user_id}.")
```

**Note:**
- Replace `"your-api-key-here"` with your Matrica API key.
- Replace `example_user_id` with a valid user ID from your system.
- Ensure you have installed and configured the Matrica SDK properly (`pip install matrica-sdk`).
