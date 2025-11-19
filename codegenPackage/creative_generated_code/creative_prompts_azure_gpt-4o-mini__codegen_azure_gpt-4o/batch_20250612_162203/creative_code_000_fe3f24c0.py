"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Write a Python script that uses cookies to manage user consent preferences for a web application, similar to the functionality described on the Masa website.
Generated: DETERMINISTIC_fe3f24c0b5b1ce4d
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

# Key for consent preferences stored in cookies
COOKIE_NAME = "user_consent_preferences"


def get_consent_preferences():
    """
    Retrieves user consent preferences from cookies.
    :return: A dictionary representing consent preferences or None if not set.
    """
    cookie_value = request.cookies.get(COOKIE_NAME)
    if cookie_value:
        try:
            # Parse cookie value as JSON
            return jsonify(cookie_value)
        EXceptjson.JSONDecode
    return None


@app.route


```
