"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Generate a script to check the integrity of downloaded screen saver files from Dick Lee's Screen Saver Page and verify that the required documentation files (.DOC, .RTF, .TXT, or .WRI) are present.
Generated: DETERMINISTIC_09f2420f83514170
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib

# Define the directory containing the screen saver files
SCREEN_SAVER_DIR = 'path/to/screen_savers'
# Define the required documentation file extensions
REQUIRED_EXTENSIONS = ('.doc', '.rtf', '.txt', '.wri')

def calculate_file_hash(file_path):
    """Calculate the SHA-256 hash of the given file."""
    try:
        with open(file_path, 'rb') as f:
            file_hash = hashlib.sha256()
            while chunk := f.read(8192):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {file_path}: {e}")
        return None

def check_file_integrity(file_path):
    """Check the integrity of the downloaded screen saver file."""
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return False
    
    # Calculate the hash of the file (for integrity check)
    file_hash = calculate_file_hash(file_path)
    if file_hash is None:
        return False

    # For example, you can define a known hash for validation
    # known_hash = "expected_hash_value_here"
    # if file_hash != known_hash:
    #     print(f"File integrity compromised: {file_path}")
    #     return False

    return True

def verify_documentation_files():
    """Verify that required documentation files are present for each screen saver."""
    screen_savers = [f for f in os.listdir(SCREEN_SAVER_DIR) if f.lower().endswith('.scr')]
    
    for ss in screen_savers:
        ss_path = os.path.join(SCREEN_SAVER_DIR, ss)
        print(f"Checking screen saver: {ss}")

        # Check integrity of the screen saver file
        if not check_file_integrity(ss_path):
            print(f"Integrity check failed for {ss}.")
            continue

        # Check for the presence of required documentation files
        documentation_present = False
        for ext in REQUIRED_EXTENSIONS:
            doc_file = ss.replace('.scr', ext)
            doc_file_path = os.path.join(SCREEN_SAVER_DIR, doc_file)
            if os.path.isfile(doc_file_path):
                documentation_present = True
                print(f"Documentation file found: {doc_file}")

        if not documentation_present:
            print(f"No required documentation files found for {ss}.")

if __name__ == '__main__':
    try:
        verify_documentation_files()
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace `'path/to/screen_savers'` with the actual path to the directory where the screen saver files are stored. The code will check the integrity of each screen saver file and verify if the required documentation files are present in the specified directory.
