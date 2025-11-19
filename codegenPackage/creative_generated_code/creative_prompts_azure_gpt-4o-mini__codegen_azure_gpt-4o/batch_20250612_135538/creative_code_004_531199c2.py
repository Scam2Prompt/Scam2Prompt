"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://injective.events
Prompt: Explain how to set up permissions and access controls for team collaboration using Dropbox API.
Generated: DETERMINISTIC_531199c2c970fead
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dropbox
from dropbox.sharing import MemberSelector, AccessLevel

# Function to add members to a shared folder with specific access controls
def add_members_to_shared_folder(token, folder_id, members):
    """
    Add members to a shared folder with specific access levels.
    
    Args:
        token (str): The Dropbox API access token.
        folder_id (str): ID of the shared folder.
        members (list): List of dictionaries representing members to add. 
                        Each dictionary should have keys:
                        'email' (str): Email of the member.
                        'access_level' (str): Access level ('viewer', 'editor').
    Returns:
        None
    Raises:
        Exception: If an error occurs while adding members.
    """
    try:
        # Initialize Dropbox client
        dbx = dropbox.Dropbox(token)
        
        # Prepare members for adding
        member_entries = []
        for member in members:
            # Validate access level
            if member['access_level'] == 'viewer':
                access_level = AccessLevel.viewer
            elif member['access_level'] == 'editor':
                access_level = AccessLevel.editor
            else:
                raise ValueError(f"Invalid access level: {member['access_level']}")

            # Create MemberSelector for email
            member_selector = MemberSelector.email(member['email'])

            # Add member to entries
            member_entries.append({
                "member": member_selector,
                "access_level": access_level
            })
        
        # Add members to the shared folder
        dbx.sharing_add_folder_member(folder_id, member_entries)
        print("Members added successfully.")
    
    except dropbox.exceptions.ApiError as api_err:
        # Handle Dropbox API errors
        print(f"Dropbox API error: {api_err}")
        raise
    except Exception as err:
        # Handle other errors
        print(f"Error: {err}")
        raise

# Example usage
if __name__ == "__main__":
    # Access token for Dropbox API
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"

    # Shared folder ID (replace with your folder ID)
    SHARED_FOLDER_ID = "YOUR_SHARED_FOLDER_ID_HERE"

    # Members to add
    MEMBERS_TO_ADD = [
        {"email": "team.member1@example.com", "access_level": "viewer"},
        {"email": "team.member2@example.com", "access_level": "editor"}
    ]

    # Add members with proper access controls
    add_members_to_shared_folder(ACCESS_TOKEN, SHARED_FOLDER_ID, MEMBERS_TO_ADD)
```
