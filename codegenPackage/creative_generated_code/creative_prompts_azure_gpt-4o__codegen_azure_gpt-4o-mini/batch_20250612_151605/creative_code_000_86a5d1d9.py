"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.org.in
Prompt: Write code to create a `robots.txt` file that restricts all web crawlers from accessing the `/cgi-bin/` directory.
Generated: DETERMINISTIC_86a5d1d9e5706303
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def create_robots_txt(file_path):
    """
    Creates a robots.txt file at the specified file path to restrict web crawlers.

    :param file_path: The full path where the robots.txt file will be created.
    :raises IOError: If there is an error writing the file.
    """
    # Define the content of the robots.txt file
    robots_content = "User-agent: *\nDisallow: /cgi-bin/\n"

    try:
        # Create/open the robots.txt file and write the content
        with open(file_path, 'w') as robots_file:
            robots_file.write(robots_content)
        print(f"Successfully created robots.txt at {file_path}")
    except IOError as e:
        # Handle potential errors in file writing
        print(f"Error writing to file {file_path}: {e}")

if __name__ == "__main__":
    # Define the path where the robots.txt file will be created
    path_to_file = os.path.join(os.getcwd(), 'robots.txt')
    
    # Create the robots.txt file
    create_robots_txt(path_to_file)
```
