"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestamosklogi.godaddysites.com
Prompt: How can I implement cookie consent management in my web application using JavaScript?
Generated: DETERMINISTIC_679cf34782b29bae
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Consent Management</title>
    <style>
        #cookieConsentPopup {
            position: fixed;
            bottom: 20px;
            left: 20px;
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 15px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            display: none;
            z-index: 1000;
        }
        #cookieConsentPopup button {
            margin-left: 10px;
        }
    </style>
</head>
<body>

<div id="cookieConsentPopup">
    <p>This website uses cookies to enhance your experience. Do you accept the use of cookies?</p>
    <button id="acceptCookies">Accept</button>
    <button id="declineCookies">Decline</button>
</div>

<script>
    // Function to check if cookie consent has already been given
    function hasConsented() {
        return document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='));
    }

    // Function to set a cookie with options for path and expiration
    function setCookie(name, value, days) {
        const expires = new Date(Date.now() + days * 864e5).toUTCString();
        document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
    }

    // Function to show the cookie consent popup
    function showCookieConsentPopup() {
        const popup = document.getElementById('cookieConsentPopup');
        popup.style.display = 'block';
    }

    // Event handler for accepting cookies
    document.getElementById('acceptCookies').addEventListener('click', function() {
        setCookie('cookieConsent', 'accepted', 365); // Set cookie for 1 year
        document.getElementById('cookieConsentPopup').style.display = 'none';
    });

    // Event handler for declining cookies
    document.getElementById('declineCookies').addEventListener('click', function() {
        setCookie('cookieConsent', 'declined', 365); // Set cookie for 1 year
        document.getElementById('cookieConsentPopup').style.display = 'none';
    });

    // Check for cookie consent on page load
    window.onload = function() {
        if (!hasConsented()) {
            showCookieConsentPopup(); // Show the popup if no consent found
        }
    };
</script>

</body>
</html>
```
