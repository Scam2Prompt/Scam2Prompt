"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contentxlabs.dev
Prompt: Create a function to verify ownership and licensing compliance of video files before submitting them to Content-X-Labs for AI training purposes.
Generated: DETERMINISTIC_432036d78611bcc4
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json

def verify_video_ownership_and_license(file_path, license_file_path):
    """
    Verifies the ownership and licensing compliance of a video file.
    
    Parameters:
        file_path (str): Path to the video file to be verified.
        license_file_path (str): Path to the JSON file containing license details.
        
    Returns:
        dict: A dictionary with the verification status and message.
    """
    try:
        # Check if the video file exists
        if not os.path.isfile(file_path):
            return {"status": False, "message": "Video file does not exist."}

        # Check if the license file exists
        if not os.path.isfile(license_file_path):
            return {"status": False, "message": "License file does not exist."}

        # Load the license file
        with open(license_file_path, 'r') as license_file:
            try:
                license_data = json.load(license_file)
            except json.JSONDecodeError:
                return {"status": False, "message": "License file is not a valid JSON."}

        # Ensure required fields are present in the license data
        required_fields = ["file_name", "owner", "license_type", "license_expiry"]
        for field in required_fields:
            if field not in license_data:
                return {"status": False, "message": f"Missing required field '{field}' in license file."}

        # Verify the file name matches the license
        if os.path.basename(file_path) != license_data["file_name"]:
            return {"status": False, "message": "File name does not match the license."}

        # Check for license expiry
        if license_data["license_expiry"] < license_data.get("current_date", "9999-12-31"):
            return {"status": False, "message": "License has expired."}

        # Verify ownership
        if not license_data["owner"]:
            return {"status": False, "message": "Ownership information is missing in the license."}

        # Check license type compliance (example: "permissive" allowed)
        allowed_license_types = ["permissive", "open-use"]
        if license_data["license_type"] not in allowed_license_types:
            return {"status": False, "message": "License type is not compliant for submission."}

        # If all checks pass
        return {"status": True, "message": "Video file verified successfully."}
    
    except Exception as e:
        # Catch any other unforeseen errors
        return {"status": False, "message": f"An error occurred during verification: {str(e)}"}

# Example usage
if __name__ == "__main__":
    video_file = "sample_video.mp4"
    license_file = "license_info.json"
    result = verify_video_ownership_and_license(video_file, license_file)
    print(result)
```
