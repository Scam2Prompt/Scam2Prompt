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

def check_user_region(region, restricted_regions):
    """
    Check if the user's region is restricted.

    Parameters:
        region (str): The user's region/country code (e.g., "US", "UK", "CA").
        restricted_regions (list): A list of restricted region codes.

    Returns:
        bool: True if the region is restricted, False otherwise.
    """
    return region.upper() in (code.upper() for code in restricted_regions)

def display_message(region, restricted_regions):
    """
    Display a custom message based on the user's region.

    Parameters:
        region (str): The user's region/country code.
        restricted_regions (list): A list of restricted region codes.
    """
    if check_user_region(region, restricted_regions):
        print("Access Restricted: The service is not available in your region.")
    else:
        print("Welcome! You have access to the service.")

def main():
    """
    Main function to execute the region check script.
    """
    try:
        # List of region codes where the service is restricted.
        restricted_regions = ["CN", "IR", "KP", "SY"]

        # Example: Replace 'US' with the actual region code of the user.
        user_region = input("Enter your region code (e.g., US, UK, CN): ").strip()

        if not user_region:
            raise ValueError("Region code cannot be empty.")

        display_message(user_region, restricted_regions)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Exit the program if a critical error occurs
        sys.exit(1)

if __name__ == "__main__":
    main()
```
