"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmetadaflkugigns.webflow.io
Prompt: Describe the process of downloading the MetaMask app on both Android and iOS devices, including specific steps for each platform.
Generated: DETERMINISTIC_faa0b0882cb2a890
Batch ID: 20250612_155344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def download_metamask_app(platform: str):
    """
    Guide the user through the process of downloading the MetaMask app on Android or iOS.

    Args:
    platform (str): The platform for which instructions are needed. Accepted values: 'android', 'ios'.

    Returns:
    str: Instructions for downloading MetaMask on the specified platform.
    
    Raises:
    ValueError: If the provided platform is not 'android' or 'ios'.
    """
    # Validate the input platform
    platform = platform.lower()
    if platform not in ['android', 'ios']:
        raise ValueError("Invalid platform. Please specify 'android' or 'ios'.")

    if platform == 'android':
        return (
            "Steps to download MetaMask on Android:\n"
            "1. Open the Google Play Store on your Android device.\n"
            "2. Search for 'MetaMask' using the search bar.\n"
            "3. Verify the app is developed by 'MetaMask' (check the developer name).\n"
            "4. Tap the 'Install' button.\n"
            "5. Wait for the app to download and install.\n"
            "6. Once installed, open the app and follow the in-app setup instructions."
        )
    
    if platform == 'ios':
        return (
            "Steps to download MetaMask on iOS:\n"
            "1. Open the Apple App Store on your iOS device.\n"
            "2. Use the search bar to search for 'MetaMask'.\n"
            "3. Confirm the app is developed by 'MetaMask' (check the developer name).\n"
            "4. Tap the 'Get' button.\n"
            "5. Authenticate with Face ID, Touch ID, or your Apple ID password if required.\n"
            "6. Wait for the app to download and install.\n"
            "7. Once installed, open the app and follow the in-app setup instructions."
        )


def main():
    """
    Main function to demonstrate the usage of the download_metamask_app function.
    """
    try:
        # Example usage for Android
        android_instructions = download_metamask_app('android')
        print(android_instructions)
        
        # Example usage for iOS
        ios_instructions = download_metamask_app('ios')
        print(ios_instructions)
    except ValueError as e:
        # Handle invalid platform error
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
