"""
Generated Code Metadata:
========================
Original URL: https://elisium.it
Prompt: Write a script in Python to detect changes in an "Index of /" directory listing by comparing the last modified dates of files between two visits.
Generated: DETERMINISTIC_463d049b2782f4ec
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from bs4 import BeautifulSoup
import datetime
import hashlib
import json
import argparse

def fetch_directory_listing(url):
    """
    Fetch the directory listing from the given URL.

    Args:
        url (str): The URL of the directory listing.

    Returns:
        list: A list of dictionaries containing file information.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching directory listing: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    files = []
    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) > 4:
            name = cols[1].a.text
            modified = cols[3].text.strip()
            files.append({
                'name': name,
                'modified': modified
            })
    return files

def parse_modified_date(modified_str):
    """
    Parse the modified date string from the directory listing.

    Args:
        modified_str (str): The modified date string.

    Returns:
        datetime.datetime: The parsed datetime object.
    """
    date_formats = ['%a %b %d %H:%M:%S.%f %Y', '%a %b %d %H:%M:%S %Y']
    for date_format in date_formats:
        try:
            return datetime.datetime.strptime(modified_str, date_format)
        except ValueError:
            pass
    return None

def save_state(files, state_file):
    """
    Save the current state of the directory listing.

    Args:
        files (list): The list of files.
        state_file (str): The file to save the state to.
    """
    state = []
    for file in files:
        file_state = {
            'name': file['name'],
            'modified': file['modified']
        }
        state.append(file_state)
    with open(state_file, 'w') as f:
        json.dump(state, f, indent=4)

def load_state(state_file):
    """
    Load the previous state of the directory listing.

    Args:
        state_file (str): The file to load the state from.

    Returns:
        list: The list of files from the previous state.
    """
    try:
        with open(state_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def compare_states(current_state, previous_state):
    """
    Compare the current and previous states of the directory listing.

    Args:
        current_state (list): The current state.
        previous_state (list): The previous state.

    Returns:
        list: A list of changes.
    """
    changes = []
    current_state_dict = {file['name']: file for file in current_state}
    previous_state_dict = {file['name']: file for file in previous_state}

    for file_name, file_state in current_state_dict.items():
        if file_name not in previous_state_dict:
            changes.append({
                'type': 'added',
                'file': file_state
            })
        else:
            previous_file_state = previous_state_dict[file_name]
            if file_state['modified'] != previous_file_state['modified']:
                changes.append({
                    'type': 'modified',
                    'file': file_state
                })

    for file_name, file_state in previous_state_dict.items():
        if file_name not in current_state_dict:
            changes.append({
                'type': 'removed',
                'file': file_state
            })
    return changes

def main():
    parser = argparse.ArgumentParser(description='Detect changes in an "Index of /" directory listing')
    parser.add_argument('url', help='The URL of the directory listing')
    parser.add_argument('--state_file', default='state.json', help='The file to save and load the state')
    args = parser.parse_args()

    current_state = fetch_directory_listing(args.url)
    previous_state = load_state(args.state_file)

    changes = compare_states(current_state, previous_state)
    if changes:
        print("Changes detected:")
        for change in changes:
            print(f"{change['type']}: {change['file']['name']} (Modified: {change['file']['modified']})")
    else:
        print("No changes detected.")

    save_state(current_state, args.state_file)

if __name__ == "__main__":
    main()
```
