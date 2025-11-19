"""
Generated Code Metadata:
========================
Original URL: https://arweave.ar
Prompt: Can you provide an example of how to implement the ans104UnbundleFilter in a project using Arweave's supported manifest versions?
Generated: DETERMINISTIC_6d1a54ab7b90aff6
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

def ans104_unbundle_filter(manifest_path, supported_versions):
    """
    Filters an ANS-104 manifest file to ensure it uses supported versions.

    Args:
        manifest_path (str): Path to the ANS-104 manifest file.
        supported_versions (list): List of supported manifest versions.

    Returns:
        dict: Filtered manifest data if valid, None otherwise.
    """
    try:
        # Ensure the manifest file exists
        if not os.path.exists(manifest_path):
            raise FileNotFoundError(f"Manifest file not found: {manifest_path}")

        # Load the manifest file
        with open(manifest_path, 'r') as file:
            manifest_data = json.load(file)

        # Validate the manifest structure
        if 'version' not in manifest_data:
            raise ValueError("Manifest file is missing the 'version' field.")

        # Check if the manifest version is supported
        manifest_version = manifest_data['version']
        if manifest_version not in supported_versions:
            raise ValueError(f"Unsupported manifest version: {manifest_version}")

        # Return the valid manifest data
        return manifest_data

    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        # Log the error and return None
        print(f"Error processing manifest file: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define the path to the manifest file and supported versions
    manifest_file_path = "path/to/manifest.json"
    supported_manifest_versions = ["0.1", "0.2", "1.0"]

    # Filter the manifest file
    filtered_manifest = ans104_unbundle_filter(manifest_file_path, supported_manifest_versions)

    if filtered_manifest:
        print("Valid manifest file:")
        print(json.dumps(filtered_manifest, indent=4))
    else:
        print("Manifest file is invalid or unsupported.")
```
