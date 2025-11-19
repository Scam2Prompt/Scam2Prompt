"""
Generated Code Metadata:
========================
Original URL: https://ledger22.com
Prompt: Write a Python script to handle cookie consent and data aggregation for a website, inspired by ledger22.com's cookie policy.
Generated: DETERMINISTIC_0b04054975a1620f
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from flask import Flask, request, make_response, jsonify
from typing import Dict, Optional, Union

app = Flask(__name__)

# Configuration for cookie settings
COOKIE_NAME = "user_consent"
COOKIE_EXPIRY_DAYS = 365
COOKIE_SECURE = True  # Set to False if not using HTTPS
COOKIE_HTTPONLY = True
COOKIE_SAMESITE = "Lax"

# Default consent settings
DEFAULT_CONSENT = {
    "necessary": True,  # Necessary cookies cannot be disabled
    "analytics": False,
    "marketing": False,
    "preferences": False,
    "consent_date": None
}

class CookieConsent:
    """
    Handles cookie consent management and data aggregation.
    """
    
    @staticmethod
    def get_consent(request) -> Dict[str, Union[bool, str]]:
        """
        Retrieves the user's cookie consent preferences from the cookie.
        
        Args:
            request: The Flask request object
            
        Returns:
            dict: The user's consent preferences
        """
        consent_cookie = request.cookies.get(COOKIE_NAME)
        if consent_cookie:
            try:
                consent_data = json.loads(consent_cookie)
                # Validate the consent data structure
                if all(key in consent_data for key in DEFAULT_CONSENT.keys()):
                    return consent_data
            except json.JSONDecodeError:
                pass
        return DEFAULT_CONSENT.copy()

    @staticmethod
    def set_consent(response, consent_data: Dict[str, Union[bool, str]]) -> None:
        """
        Sets the user's cookie consent preferences in the response cookie.
        
        Args:
            response: The Flask response object
            consent_data: The user's consent preferences
        """
        # Ensure necessary cookies are always enabled
        consent_data["necessary"] = True
        consent_data["consent_date"] = datetime.utcnow().isoformat()
        
        response.set_cookie(
            key=COOKIE_NAME,
            value=json.dumps(consent_data),
            max_age=COOKIE_EXPIRY_DAYS * 24 * 60 * 60,
            secure=COOKIE_SECURE,
            httponly=COOKIE_HTTPONLY,
            samesite=COOKIE_SAMESITE
        )

    @staticmethod
    def should_track(request, category: str) -> bool:
        """
        Checks if tracking is allowed for a given category.
        
        Args:
            request: The Flask request object
            category: The tracking category (e.g., 'analytics')
            
        Returns:
            bool: True if tracking is allowed, False otherwise
        """
        if category not in DEFAULT_CONSENT:
            raise ValueError(f"Invalid tracking category: {category}")
            
        consent = CookieConsent.get_consent(request)
        return consent.get(category, False)

@app.route('/api/consent', methods=['GET', 'POST'])
def handle_consent():
    """
    Handles consent preferences submission and retrieval.
    """
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"}), 400
                
            # Validate the incoming data
            valid_categories = [k for k in DEFAULT_CONSENT.keys() if k != "necessary" and k != "consent_date"]
            for category in data:
                if category not in valid_categories:
                    return jsonify({"error": f"Invalid category: {category}"}), 400
                if not isinstance(data[category], bool):
                    return jsonify({"error": f"Invalid value for {category}"}), 400
            
            # Merge with default consent
            consent_data = DEFAULT_CONSENT.copy()
            consent_data.update(data)
            
            response = jsonify({"status": "success"})
            CookieConsent.set_consent(response, consent_data)
            return response
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
    elif request.method == 'GET':
        consent_data = CookieConsent.get_consent(request)
        return jsonify(consent_data)

@app.route('/api/track', methods=['POST'])
def track_event():
    """
    Handles tracking events based on user consent.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        category = data.get("category")
        if not category:
            return jsonify({"error": "Category is required"}), 400
            
        if not CookieConsent.should_track(request, category):
            return jsonify({"error": "Consent not given for this category"}), 403
            
        # Here you would typically process the tracking data
        # For example: log to database, send to analytics service, etc.
        # This is just a placeholder for the actual implementation
        print(f"Tracking event for {category}: {data.get('event')}")
        
        return jsonify({"status": "success"})
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
