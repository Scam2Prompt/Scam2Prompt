"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mahnoorpc.net
Prompt: Develop a script that utilizes VX Search 16.1.24 for data management tasks as mentioned on Mahnoor PC.
Generated: DETERMINISTIC_ae3192317541b2a9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
VX Search Automation Script
This script utilizes VX Search 16.1.24 command-line tools for data management tasks.
Make sure VX Search command-line tools are installed and added to the system PATH before running this script.
"""

import subprocess
import json


def run_vx_search_command(command):
    """
    Executes a VX Search command and returns the output.
    :param command: List containing the VX Search command and its arguments.
    :return: Decoded output from the command or an error message if the command fails.
    """
    try:
        # Run the command using subprocess
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Check if the command was successful
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error executing command: {result.stderr}"
    except Exception as e:
        return f"An exception occurred: {str(e)}"


def create_search_profile(profile_name, directory, file_extension):
    """
    Creates a VX Search search profile for scanning a directory with specific file extensions.
    :param profile_name: Name of the search profile.
    :param directory: Directory to be scanned.
    :param file_extension: File extension filter (e.g., '.txt', '.log').
    :return: Output from the VX Search command or an error message.
    """
    command = [
        "vxsrcli",  # VX Search command-line executable
        "-create",  # Create a new search profile
        profile_name,
        directory,
        f"-extensions:{file_extension}",
    ]
    return run_vx_search_command(command)


def execute_search_profile(profile_name, output_file):
    """
    Executes a VX Search profile and saves the results to a file.
    :param profile_name: Name of the search profile to execute.
    :param output_file: Path to the output file where results will be saved.
    :return: Output from the VX Search command or an error message.
    """
    command = [
        "vxsrcli",  # VX Search command-line executable
        "-execute",  # Execute search profile
        profile_name,
        f"-export:{output_file}",
    ]
    return run_vx_search_command(command)


def parse_results(output_file):
    """
    Parses the JSON results from a VX Search output file.
    :param output_file: Path to the JSON output file.
    :return: Parsed JSON data or an error message.
    """
    try:
        with open(output_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return "Output file not found."
    except json.JSONDecodeError:
        return "Failed to parse JSON data."
    except Exception as e:
        return f"An exception occurred: {str(e)}"


def main():
    """
    Main function to demonstrate VX Search automation.
    """
    profile_name = "example_profile"
    directory = "C:\\example_directory"
    file_extension = ".txt"
    output_file = "results.json"

    # Step 1: Create Search Profile
    print("Creating search profile...")
    create_output = create_search_profile(profile_name, directory, file_extension)
    print(create_output)

    # Step 2: Execute Search Profile
    print("Executing search profile...")
    execute_output = execute_search_profile(profile_name, output_file)
    print(execute_output)

    # Step 3: Parse Results
    print("Parsing results...")
    parsed_results = parse_results(output_file)
    print(parsed_results)


if __name__ == "__main__":
    main()
```

**Notes:**
- Replace `vxsrcli` with the actual executable name if different.
- Ensure VX Search 16.1.24 is installed and accessible via your system PATH.
- Update directory paths and file extensions as required.
- Modify error handling to suit your production environment.
