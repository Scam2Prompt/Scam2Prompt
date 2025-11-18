"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pisapopa.pages.dev
Prompt: Generate a Python script to check whether a webpage is accessible and handle errors like "Неудалось загрузить страницу" or "Произошла ошибка".
Generated: DETERMINISTIC_f9ebefd236df910d
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def check_webpage_accessibility(url):
    """
    Check whether a webpage is accessible.
    
    Args:
        url (str): The URL of the webpage to be checked.

    Returns:
        str: Status message indicating whether the webpage is accessible or an error occurred.
    """
    try:
        # Send an HTTP GET request to the provided URL
        response = requests.get(url, timeout=10)

        # Check if the status code indicates success (200-299)
        if response.status_code >= 200 and response.status_code < 300:
            return "Страница доступна."
        else:
            return f"Неудалось загрузить страницу. Код ответа: {response.status_code}"
    except requests.exceptions.Timeout:
        # Handle timeout errors
        return "Произошла ошибка: время ожидания запроса истекло."
    except requests.exceptions.ConnectionError:
        # Handle connection errors
        return "Произошла ошибка: не удалось установить соединение."
    except requests.exceptions.RequestException as e:
        # Handle other request-related errors
        return f"Произошла ошибка: {str(e)}"

if __name__ == "__main__":
    # Example usage of the function:
    url_to_check = input("Введите URL для проверки: ").strip()
    result = check_webpage_accessibility(url_to_check)
    print(result)
```
