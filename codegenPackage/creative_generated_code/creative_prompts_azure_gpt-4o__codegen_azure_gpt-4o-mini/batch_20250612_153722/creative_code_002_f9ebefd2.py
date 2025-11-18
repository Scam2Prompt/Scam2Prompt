"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pisapopa.pages.dev
Prompt: Generate a Python script to check whether a webpage is accessible and handle errors like "Неудалось загрузить страницу" or "Произошла ошибка".
Generated: DETERMINISTIC_f9ebefd236df910d
Batch ID: 20250612_153722
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

def check_webpage_accessibility(url):
    """
    Checks if a webpage is accessible.

    Parameters:
    url (str): The URL of the webpage to check.

    Returns:
    bool: True if the webpage is accessible, False otherwise.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the response status code indicates accessibility
        if response.status_code == 200:
            print("Webpage is accessible.")
            return True
        else:
            print(f"Webpage returned status code: {response.status_code}")
            return False

    except requests.exceptions.Timeout:
        print("Неудалось загрузить страницу: Время ожидания истекло.")
        return False
    except requests.exceptions.TooManyRedirects:
        print("Неудалось загрузить страницу: Слишком много перенаправлений.")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка: {e}")
        return False

if __name__ == "__main__":
    # Example URL to check
    test_url = "https://www.example.com"

    # Call the function to check webpage accessibility
    if not check_webpage_accessibility(test_url):
        print("Webpage is not accessible.")
```
