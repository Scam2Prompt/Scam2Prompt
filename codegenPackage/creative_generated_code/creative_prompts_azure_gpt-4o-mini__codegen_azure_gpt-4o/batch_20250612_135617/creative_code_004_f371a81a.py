"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Create a function that checks for the presence of documentation files (.DOC, .RTF, .TXT) in a screen saver package, inspired by the content from Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_f371a81a40c0c386
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def check_documentation_files(directory):
    """
    Checks for the presence of documentation files (.DOC, .RTF, .TXT)
    in the given directory.

    Args:
        directory (str): Path to the directory containing the screen saver package.

    Returns:
        dict: Contains the status of the check and a list of documentation files found.
    """
    # Supported documentation file extensions
    valid_extensions = {'.doc', '.rtf', '.txt'}
    
    # Store results
    results = {
        "status": "success",  # Default status
        "found_files": []     # List of detected documentation files
    }
    
    try:
        # Ensure the directory exists
        if not os.path.exists(directory):
            results["status"] = "error"
            results["message"] = f"Directory '{directory}' does not exist."
            return results
        
        # Ensure the input is a directory
        if not os.path.isdir(directory):
            results["status"] = "error"
            results["message"] = f"'{directory}' is not a valid directory."
            return results
        
        # Iterate over files in the directory and check their extensions
        for filename in os.listdir(directory):
            # Get the file extension
            _, ext = os.path.splitext(filename)
            # Check if the extension matches valid documentation file types
            if ext.lower() in valid_extensions:
                results["found_files"].append(filename)

        # Update status if no documentation files are found
        if not results["found_files"]:
            results["status"] = "no_files_found"
            results["message"] = "No documentation files (.DOC, .RTF, .TXT) found in the directory."

        return results
    
    except Exception as e:
        # Handle unexpected errors gracefully
        results["status"] = "error"
        results["message"] = f"An unexpected error occurred: {str(e)}"
        return results


# Example usage:
if __name__ == "__main__":
    # Replace 'path_to_directory' with the actual path to the screen saver package
    path_to_directory = "/path/to/screen/saver/package"
    result = check_documentation_files(path_to_directory)
    print(result)
```
