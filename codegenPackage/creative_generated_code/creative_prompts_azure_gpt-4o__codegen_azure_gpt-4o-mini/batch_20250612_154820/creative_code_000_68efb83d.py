"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthinsuranceshop.ie
Prompt: Write code to implement cookie consent management similar to the GDPR Cookie Consent plugin described on the Health Insurance Shop website, including categories like "Analytics," "Functional," and "Necessary."
Generated: DETERMINISTIC_68efb83d4aeed834
Batch ID: 20250612_154820
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
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="cookie-consent-banner" class="cookie-consent-banner">
        <h2>Cookie Consent</h2>
        <p>We use cookies to enhance your experience. Please select your cookie preferences:</p>
        
        <div class="cookie-category">
            <label>
                <input type="checkbox" id="necessary-cookies" checked disabled>
                Necessary Cookies (Always Active)
            </label>
        </div>
        
        <div class="cookie-category">
            <label>
                <input type="checkbox" id="functional-cookies">
                Functional Cookies
            </label>
        </div>

        <div class="cookie-category">
            <label>
                <input type="checkbox" id="analytics-cookies">
                Analytics Cookies
            </label>
        </div>

        <button id="accept-cookies">Accept All</button>
        <button id="reject-cookies">Reject All</button>
        <button id="save-preferences">Save Preferences</button>
    </div>

    <script>
        // Function to initialize the cookie consent banner
        function initCookieConsent() {
            // Check if consent has already been given
            if (getCookie('cookie_consent')) {
                document.getElementById('cookie-consent-banner').style.display = 'none';
            } else {
                document.getElementById('cookie-consent-banner').style.display = 'block';
            }

            // Event listeners for buttons
            document.getElementById('accept-cookies').addEventListener('click', acceptAllCookies);
            document.getElementById('reject-cookies').addEventListener('click', rejectAllCookies);
            document.getElementById('save-preferences').addEventListener('click', saveCookiePreferences);
        }

        // Accept all cookies and set the consent cookie
        function acceptAllCookies() {
            setCookie('cookie_consent', 'accepted', 30);
            document.getElementById('cookie-consent-banner').style.display = 'none';
            // Load all scripts here if required
        }

        // Reject all cookies and set the consent cookie
        function rejectAllCookies() {
            setCookie('cookie_consent', 'rejected', 30);
            document.getElementById('cookie-consent-banner').style.display = 'none';
        }

        // Save user preferences and set the consent cookie
        function saveCookiePreferences() {
            const preferences = {
                functional: document.getElementById('functional-cookies').checked,
                analytics: document.getElementById('analytics-cookies').checked,
            };
            setCookie('cookie_consent', JSON.stringify(preferences), 30);
            document.getElementById('cookie-consent-banner').style.display = 'none';
            // Load scripts based on preferences
        }

        // Function to set a cookie
        function setCookie(name, value, days) {
            const expires = new Date(Date.now() + days * 864e5).toUTCString();
            document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
        }

        // Function to get a cookie value by name
        function getCookie(name) {
            return document.cookie.split('; ').reduce((r, c) => {
                const [key, v] = c.split('=');
                return key === name ? decodeURIComponent(v) : r;
            }, '');
        }

        // Initialize cookie consent management on page load
        window.onload = initCookieConsent;
    </script>
    <style>
        /* Basic styles for the cookie consent banner */
        .cookie-consent-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #f8f9fa;
            padding: 20px;
            border-top: 1px solid #ccc;
            display: none;
            z-index: 1000;
        }
        .cookie-category {
            margin-bottom: 10px;
        }
    </style>
</body>
</html>
```
