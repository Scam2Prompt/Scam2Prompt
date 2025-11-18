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

def create_robots_txt(file_path="robots.txt"):
    """
    Creates a robots.txt file that restricts all web crawlers 
    from accessing the /cgi-bin/ directory.
    """
    try:
        # Define the content for the robots.txt file
        robots_content = """User-agent: *
Disallow: /cgi-bin/
"""

        # Write the content to the specified file
        with open(file_path, "w") as file:
            file.write(robots_content)

        print(f"robots.txt file successfully created at: {os.path.abspath(file_path)}")
    except Exception as e:
        # Handle any errors during the file write process
        print(f"An error occurred while creating the robots.txt file: {e}")

# Call the function to create the robots.txt file
create_robots_txt()
```
