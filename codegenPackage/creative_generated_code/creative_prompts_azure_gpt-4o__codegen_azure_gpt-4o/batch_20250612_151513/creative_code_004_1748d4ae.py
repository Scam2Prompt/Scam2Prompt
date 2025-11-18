"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Create a script to automate package selection for DX Link users based on their internet usage requirements, including streaming services and upload/download speed needs.
Generated: DETERMINISTIC_1748d4aec09d097b
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define package options
PACKAGES = [
    {
        "name": "Basic Plan",
        "download_speed": 25,  # Mbps
        "upload_speed": 3,    # Mbps
        "streaming_quality": "Standard Definition (SD)",
        "price": 25.00        # USD/month
    },
    {
        "name": "Standard Plan",
        "download_speed": 100, # Mbps
        "upload_speed": 10,    # Mbps
        "streaming_quality": "High Definition (HD)",
        "price": 50.00         # USD/month
    },
    {
        "name": "Premium Plan",
        "download_speed": 300, # Mbps
        "upload_speed": 20,    # Mbps
        "streaming_quality": "Ultra High Definition (4K)",
        "price": 75.00         # USD/month
    }
]

def recommend_package(download_speed_required, upload_speed_required, streaming_quality_required):
    """
    Function to recommend the best package based on user requirements.
    
    Args:
        download_speed_required (int): Minimum required download speed in Mbps.
        upload_speed_required (int): Minimum required upload speed in Mbps.
        streaming_quality_required (str): Desired streaming quality, e.g., SD, HD, 4K.
    
    Returns:
        dict: Recommended package details or an error message if no suitable package is found.
    """
    try:
        for package in PACKAGES:
            if (package["download_speed"] >= download_speed_required and
                package["upload_speed"] >= upload_speed_required and
                package["streaming_quality"] == streaming_quality_required):
                return package

        return {"error": "No suitable package found for the specified requirements."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

def main():
    """
    Main function to interact with the user and automate package selection.
    """
    try:
        # Gather user input
        print("Welcome to DX Link Package Selection Tool!")
        download_speed = int(input("Enter the minimum download speed you require (Mbps): "))
        upload_speed = int(input("Enter the minimum upload speed you require (Mbps): "))
        streaming_quality = input("Enter the desired streaming quality (SD, HD, 4K): ").strip()

        # Validate streaming quality input
        if streaming_quality not in ["Standard Definition (SD)", "High Definition (HD)", "Ultra High Definition (4K)"]:
            print("Invalid streaming quality entered. Please enter SD, HD, or 4K.")
            return

        # Recommend a package based on user input
        recommended_package = recommend_package(download_speed, upload_speed, streaming_quality)

        # Output recommended package
        if "error" in recommended_package:
            print(recommended_package["error"])
        else:
            print("Recommended Package:")
            print(json.dumps(recommended_package, indent=4))
    except ValueError:
        print("Invalid input. Please enter numeric values for download and upload speeds.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
