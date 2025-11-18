"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Write Python code to detect malware distributed via polyglot files, as described in Blue Training Academy's article on cybersecurity threats. Include techniques for identifying StrRAT and Ratty remote access Trojans.
Generated: DETERMINISTIC_ef72aca41ef0a946
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import os
import hashlib

def scan_file_for_malware(file_path):
    """
    Scans a given file for indicators of malware such as StrRAT and Ratty remote access Trojans.
    
    Parameters:
        file_path (str): Path to the file to be scanned.

    Returns:
        dict: A dictionary containing the scan results.
    """
    scan_results = {
        "file_path": file_path,
        "is_malicious": False,
        "detected_malware": [],
    }

    try:
        # Read the file content
        with open(file_path, 'rb') as file:
            file_content = file.read()

        # Calculate file hash for signature-based detection
        file_hash = hashlib.md5(file_content).hexdigest()

        # Known malware hashes (example hashes for StrRAT and Ratty - replace with actual database)
        known_hashes = {
            "StrRAT": ["d41d8cd98f00b204e9800998ecf8427e"],  # Replace with real hash
            "Ratty": ["0cc175b9c0f1b6a831c399e269772661"],  # Replace with real hash
        }

        # Check if file hash matches any known malware hash
        for malware_name, hashes in known_hashes.items():
            if file_hash in hashes:
                scan_results["is_malicious"] = True
                scan_results["detected_malware"].append(malware_name)

        # Perform heuristic analysis
        # Example: Look for StrRAT/Ratty specific patterns in file content
        strrat_pattern = b"authHOST=[^&]+&refId=[^&]+&data="  # Replace with real pattern
        ratty_pattern = b"RAT_CLIENT_START"  # Replace with real pattern

        if re.search(strrat_pattern, file_content):
            scan_results["is_malicious"] = True
            scan_results["detected_malware"].append("StrRAT")

        if re.search(ratty_pattern, file_content):
            scan_results["is_malicious"] = True
            scan_results["detected_malware"].append("Ratty")

    except FileNotFoundError:
        scan_results["error"] = "File not found. Please provide a valid file path."
    except IOError:
        scan_results["error"] = "Unable to read file due to I/O error."
    except Exception as e:
        scan_results["error"] = f"An unexpected error occurred: {e}"

    return scan_results


def scan_directory_for_malware(directory_path):
    """
    Scans all files in a given directory for malware.

    Parameters:
        directory_path (str): Path to the directory to be scanned.

    Returns:
        list: A list of dictionaries containing scan results for each file.
    """
    scan_results_list = []

    try:
        # Iterate over all files in the directory
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)

                # Scan each file for malware
                scan_results = scan_file_for_malware(file_path)
                scan_results_list.append(scan_results)

    except FileNotFoundError:
        print("Directory not found. Please provide a valid directory path.")
    except IOError:
        print("Unable to read directory due to I/O error.")
    except Exception as e:
        print(f"An unexpected error occurred while scanning the directory: {e}")

    return scan_results_list


if __name__ == "__main__":
    # Example usage
    directory_to_scan = input("Enter the path to the directory you want to scan: ")
    results = scan_directory_for_malware(directory_to_scan)

    # Print a summary of the scan results
    for result in results:
        print(f"File: {result['file_path']}")
        if result.get("error"):
            print(f"Error: {result['error']}")
        elif result['is_malicious']:
            print(f"Status: Malicious")
            print(f"Detected Malware: {', '.join(result['detected_malware'])}")
        else:
            print("Status: Clean")
        print("-" * 50)
```
