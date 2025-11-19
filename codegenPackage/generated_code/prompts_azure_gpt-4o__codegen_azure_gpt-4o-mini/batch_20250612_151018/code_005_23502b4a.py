"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: Create a debugging script that identifies and resolves "evil byte" issues in markdown or HTML files, as described on the webpage.
Generated: DETERMINISTIC_23502b4a0b79037c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import sys

class EvilByteResolver:
    """
    A class to identify and resolve 'evil byte' issues in markdown or HTML files.
    An 'evil byte' is defined as any byte that is not valid UTF-8.
    """

    def __init__(self, directory):
        """
        Initializes the EvilByteResolver with the directory to scan.

        :param directory: The directory containing markdown or HTML files.
        """
        self.directory = directory

    def find_files(self):
        """
        Finds all markdown and HTML files in the specified directory.

        :return: A list of file paths.
        """
        files = []
        for root, _, filenames in os.walk(self.directory):
            for filename in filenames:
                if filename.endswith(('.md', '.html')):
                    files.append(os.path.join(root, filename))
        return files

    def is_valid_utf8(self, byte_data):
        """
        Checks if the given byte data is valid UTF-8.

        :param byte_data: The byte data to check.
        :return: True if valid UTF-8, False otherwise.
        """
        try:
            byte_data.decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False

    def resolve_evil_bytes(self, file_path):
        """
        Reads a file, identifies evil bytes, and attempts to resolve them.

        :param file_path: The path to the file to process.
        """
        with open(file_path, 'rb') as file:
            content = file.read()

        # Identify evil bytes
        if not self.is_valid_utf8(content):
            print(f"Evil bytes found in file: {file_path}")
            # Attempt to fix by replacing invalid bytes with a placeholder
            fixed_content = self.fix_evil_bytes(content)
            self.write_fixed_file(file_path, fixed_content)

    def fix_evil_bytes(self, byte_data):
        """
        Replaces invalid bytes with a placeholder.

        :param byte_data: The original byte data.
        :return: Fixed byte data with evil bytes replaced.
        """
        # Replace invalid bytes with a placeholder (�)
        return re.sub(b'[^\x00-\x7F]+', b'\xef\xbf\xbd', byte_data)

    def write_fixed_file(self, file_path, fixed_content):
        """
        Writes the fixed content back to the file.

        :param file_path: The path to the file to write.
        :param fixed_content: The fixed byte content to write.
        """
        with open(file_path, 'wb') as file:
            file.write(fixed_content)
        print(f"Fixed file written: {file_path}")

    def run(self):
        """
        Executes the evil byte resolution process.
        """
        try:
            files = self.find_files()
            for file_path in files:
                self.resolve_evil_bytes(file_path)
            print("Evil byte resolution completed.")
        except Exception as e:
            print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evil_byte_resolver.py <directory>", file=sys.stderr)
        sys.exit(1)

    directory = sys.argv[1]
    resolver = EvilByteResolver(directory)
    resolver.run()
```
