"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pegasus-staging.vercel.app
Prompt: Generate a script to display a custom message for users in restricted regions, similar to the "Usual Interface Restricted region" message on the Pegasus website.
Generated: DETERMINISTIC_f35ef6cf3eed3a6a
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class RegionRestrictionError(Exception):
    """Custom exception for handling region restriction errors."""
    pass

def get_user_region() -> str:
    """
    Simulated function to retrieve the user's region.
    In an actual implementation, this could be replaced with a method
    that retrieves the region from the user's IP address or account settings.
    
    Returns:
        str: The region of the user.
    """
    # For demonstration purposes, let's assume the user is from a restricted region.
    return "RestrictedRegion"

def display_restriction_message(region: str) -> None:
    """
    Displays a custom message to the user based on their region.
    
    Args:
        region (str): The region of the user.
    
    Raises:
        RegionRestrictionError: If the user is from a restricted region.
    """
    # Define restricted regions
    restricted_regions = ["RestrictedRegion", "AnotherRestrictedRegion"]
    
    if region in restricted_regions:
        raise RegionRestrictionError("Access to this content is restricted in your region.")
    else:
        print("Welcome! You have access to all available content.")

def main() -> None:
    """
    Main function to execute the region check and display appropriate messages.
    """
    try:
        # Get the user's region
        user_region = get_user_region()
        
        # Display the restriction message based on the user's region
        display_restriction_message(user_region)

    except RegionRestrictionError as e:
        print(f"Error: {e}")
        print("Please contact support for more information.")
    except Exception as e:
        print("An unexpected error occurred.")
        print(f"Error details: {e}")
        # Log the unexpected error for further investigation
        # In a production scenario, use logging instead of print
        sys.exit(1)  # Exit with an error status

if __name__ == "__main__":
    main()
```
