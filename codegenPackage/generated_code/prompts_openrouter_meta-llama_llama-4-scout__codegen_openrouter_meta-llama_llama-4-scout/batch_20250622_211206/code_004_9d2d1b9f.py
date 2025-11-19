"""
Generated Code Metadata:
========================
Original URL: https://consejodigitalmx.com
Prompt: Develop a Python script to monitor and report on the last modified dates of files on a server, similar to the information displayed on this webpage.
Generated: DETERMINISTIC_9d2d1b9fc6433b90
Batch ID: 20250622_211206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
import argparse

def get_last_modified_dates(directory):
    """
    Retrieves the last modified dates of files in a given directory.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        dict: A dictionary where the keys are file names and the values are the last modified dates.
    """
    try:
        files = os.listdir(directory)
        last_modified_dates = {}

        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                timestamp = os.path.getmtime(file_path)
                last_modified_date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                last_modified_dates[file] = last_modified_date

        return last_modified_dates

    except FileNotFoundError:
        print(f"Error: The directory '{directory}' was not found.")
        return {}
    except PermissionError:
        print(f"Error: Permission denied to access the directory '{directory}'.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def report_last_modified_dates(last_modified_dates, output_file=None):
    """
    Reports the last modified dates of files.

    Args:
        last_modified_dates (dict): A dictionary where the keys are file names and the values are the last modified dates.
        output_file (str, optional): The path to the output file. Defaults to None.
    """
    if output_file:
        try:
            with open(output_file, 'w') as f:
                for file, last_modified_date in last_modified_dates.items():
                    f.write(f"{file}: {last_modified_date}\n")
            print(f"Report saved to {output_file}")
        except Exception as e:
            print(f"Error writing to output file: {e}")
    else:
        for file, last_modified_date in last_modified_dates.items():
            print(f"{file}: {last_modified_date}")

def main():
    parser = argparse.ArgumentParser(description='Monitor and report on the last modified dates of files on a server.')
    parser.add_argument('directory', help='the directory to scan')
    parser.add_argument('-o', '--output', help='the output file')
    args = parser.parse_args()

    last_modified_dates = get_last_modified_dates(args.directory)
    report_last_modified_dates(last_modified_dates, args.output)

if __name__ == "__main__":
    main()
```
