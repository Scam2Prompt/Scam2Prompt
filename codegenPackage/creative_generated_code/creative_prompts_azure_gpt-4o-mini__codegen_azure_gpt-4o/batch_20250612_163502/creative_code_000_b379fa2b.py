"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tangganglife.pages.dev
Prompt: Generate a code snippet to create a guild using the Guild SDK as described on the Tang Gang website.
Generated: DETERMINISTIC_b379fa2bfc87c12d
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary modules from the Guild SDK
from guild_sdk import GuildClient, GuildCreationError

# Function to create a guild using the Guild SDK
def create_guild(api_key, guild_name, description, is_public):
    """
    Creates a guild using the Guild SDK.

    Args:
        api_key (str): API key for authentication with the Guild SDK.
        guild_name (str): Desired name for the guild.
        description (str): A brief description of the guild.
        is_public (bool): Indicates whether the guild is public or private.

    Returns:
        dict: Details of the created guild if successful.
    """
    # Initialize the Guild SDK client with the provided API key
    client = GuildClient(api_key=api_key)

    try:
        # Attempt to create the guild with the given parameters
        guild_details = client.create_guild(
            name=guild_name,
            description=description,
            public=is_public
        )

        # Return the details of the successfully created guild
        return {
            "status": "success",
            "guild": guild_details
        }
    except GuildCreationError as e:
        # Handle errors related to guild creation
        return {
            "status": "error",
            "message": f"Guild creation failed: {str(e)}"
        }
    except Exception as e:
        # Handle any other unforeseen errors
        return {
            "status": "error",
            "message": f"An unexpected error occurred: {str(e)}"
        }

# Example usage
if __name__ == "__main__":
    # Replace these placeholder values with real data
    API_KEY = "your_api_key_here"
    GUILD_NAME = "Tang Gang Guild"
    DESCRIPTION = "A guild for Tang Gang members to collaborate and grow."
    IS_PUBLIC = True

    # Create the guild and print the result
    result = create_guild(API_KEY, GUILD_NAME, DESCRIPTION, IS_PUBLIC)
    print(result)
```
