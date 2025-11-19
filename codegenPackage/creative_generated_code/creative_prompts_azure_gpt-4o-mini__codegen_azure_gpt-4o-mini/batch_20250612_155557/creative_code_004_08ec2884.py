"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pandana.vip
Prompt: Write a script that utilizes the cURL command to check the status of a webpage and returns whether it is accessible or not.
Generated: DETERMINISTIC_08ec288471fead17
Batch ID: 20250612_155557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys

def check_webpage_status(url):
    """
    Checks the status of a webpage using cURL command.

    Args:
        url (str): The URL of the webpage to check.

    Returns:
        bool: True if the webpage is accessible (HTTP status 200), False otherwise.
    """
    try:
        # Execute the cURL command to fetch the HTTP status code
        response = subprocess.run(
            ['curl', '-o', '/dev/null', '-s', '-w', '%{http_code}', url],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Decode the response and convert to an integer
        http_status = int(response.stdout.decode('utf-8'))

        # Check if the status code is 200 (OK)
        if http_status == 200:
            print(f"The webpage '{url}' is accessible.")
            return True
        else:
            print(f"The webpage '{url}' is not accessible. HTTP Status Code: {http_status}")
            return False

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while checking the webpage: {e.stderr.decode('utf-8')}")
        return False
    except ValueError as e:
        print(f"Error processing the HTTP status code: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_webpage_status.py <url>")
        sys.exit(1)

    webpage_url = sys.argv[1]
    check_webpage_status(webpage_url)
```
