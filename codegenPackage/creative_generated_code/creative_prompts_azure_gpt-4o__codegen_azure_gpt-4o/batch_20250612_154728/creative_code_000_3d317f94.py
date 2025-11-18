"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gngm.clck.hk
Prompt: Write Python code to automate the process of retrieving a device ID using the `check_id_verification` command, as described on the GMGN platform. Ensure the code copies the ID to the clipboard.
Generated: DETERMINISTIC_3d317f943fc9cc6b
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import pyperclip


def get_device_id():
    """
    Retrieve the device ID using the `check_id_verification` command and copy it to the clipboard.

    Returns:
        str: The device ID retrieved from the command.
    Raises:
        RuntimeError: If the command fails or the output is invalid.
    """
    try:
        # Execute the `check_id_verification` command
        result = subprocess.run(
            ["check_id_verification"],  # Command to retrieve the device ID
            capture_output=True,        # Capture stdout and stderr
            text=True,                  # Decode output as text
            check=True                  # Raise exception for non-zero exit codes
        )

        # Extract the device ID from the command output
        device_id = result.stdout.strip()  # Ensure we remove any trailing whitespace

        if not device_id:
            # Raise an error if the output is empty or invalid
            raise RuntimeError("Failed to retrieve a valid device ID. Command output was empty.")

        # Copy the device ID to the clipboard using pyperclip
        pyperclip.copy(device_id)

        # Return the retrieved device ID
        return device_id

    except subprocess.CalledProcessError as e:
        # Handle errors from the `subprocess.run` execution
        raise RuntimeError(f"Command execution failed with error: {e.stderr.strip()}") from e
    except Exception as e:
        # Handle any other unforeseen errors
        raise RuntimeError(f"An unexpected error occurred: {str(e)}") from e


if __name__ == "__main__":
    try:
        # Call the function and notify the user
        device_id = get_device_id()
        print(f"Device ID successfully retrieved and copied to clipboard: {device_id}")
    except RuntimeError as error:
        # Print error message for the user
        print(f"Error: {error}")
```
