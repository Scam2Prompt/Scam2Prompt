"""
Generated Code Metadata:
========================
Original URL: https://substantial-eggplant-fast.on-fleek.app
Prompt: Generate a script that automates the process of adding multiple files to IPFS and retrieving their CIDs.
Generated: DETERMINISTIC_1fdfc8020cb564e9
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess

def add_files_to_ipfs(directory_path):
    """
    Adds all files in the specified directory to IPFS and retrieves their CIDs.

    Args:
        directory_path (str): Path to the directory containing files to be added to IPFS.

    Returns:
        dict: A dictionary where keys are file names and values are their corresponding CIDs.
    """
    # Validate the directory path
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path '{directory_path}' is not a valid directory.")

    # Dictionary to store file names and their corresponding CIDs
    file_cid_map = {}

    # Iterate through all files in the directory
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)

        # Skip directories, only process files
        if os.path.isfile(file_path):
            try:
                # Use the `ipfs add` command to add the file to IPFS
                result = subprocess.run(
                    ["ipfs", "add", file_path],
                    capture_output=True,
                    text=True,
                    check=True
                )

                # Parse the output to extract the CID
                output_lines = result.stdout.strip().split("\n")
                last_line = output_lines[-1]
                cid = last_line.split()[1]  # Extract the CID from the output

                # Store the file name and CID in the dictionary
                file_cid_map[file_name] = cid

            except subprocess.CalledProcessError as e:
                # Handle errors from the `ipfs add` command
                print(f"Error adding file '{file_name}' to IPFS: {e.stderr}")
            except IndexError:
                # Handle unexpected output format
                print(f"Unexpected output format while processing file '{file_name}'.")

    return file_cid_map


if __name__ == "__main__":
    # Example usage
    try:
        # Specify the directory containing files to be added to IPFS
        directory = "./files_to_add"

        # Add files to IPFS and retrieve their CIDs
        cids = add_files_to_ipfs(directory)

        # Print the results
        print("Files added to IPFS:")
        for file, cid in cids.items():
            print(f"{file}: {cid}")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```

### Notes:
- Ensure that the `ipfs` command-line tool is installed and properly configured on your system.
- Replace `./files_to_add` with the path to the directory containing the files you want to add to IPFS.
- This script assumes that the IPFS daemon is running locally.
