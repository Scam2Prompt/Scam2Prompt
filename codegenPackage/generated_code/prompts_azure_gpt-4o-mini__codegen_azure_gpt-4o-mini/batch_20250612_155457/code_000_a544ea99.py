"""
Generated Code Metadata:
========================
Original URL: https://sensibleoptimism.com
Prompt: Generate a code snippet for a simple web application that incorporates cookie consent functionality, similar to what might be found on a site like Sensible Optimism.
Generated: DETERMINISTIC_a544ea990dd3a0bc
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Consent Example</title>
    <style>
        /* Basic styles for the cookie consent banner */
        #cookie-consent-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: white;
            padding: 15px;
            text-align: center;
            display: none; /* Hidden by default */
            z-index: 1000;
        }
        #cookie-consent-banner button {
            margin-left: 10px;
            padding: 5px 10px;
            background-color: #f1c40f;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div id="cookie-consent-banner">
        This website uses cookies to ensure you get the best experience on our website.
        <button id="accept-cookies">Accept</button>
        <button id="decline-cookies">Decline</button>
    </div>

    <script>
        // Function to check if the cookie consent has already been given
        function checkCookieConsent() {
            return document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='));
        }

        // Function to set a cookie
        function setCookie(name, value, days) {
            const expires = new Date(Date.now() + days * 864e5).toUTCString();
            document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
        }

        // Function to show the cookie consent banner
        function showCookieConsentBanner() {
            const banner = document.getElementById('cookie-consent-banner');
            banner.style.display = 'block';
        }

        // Event listener for accepting cookies
        document.getElementById('accept-cookies').addEventListener('click', function() {
            setCookie('cookieConsent', 'accepted', 30); // Set cookie for 30 days
            document.getElementById('cookie-consent-banner').style.display = 'none'; // Hide banner
        });

        // Event listener for declining cookies
        document.getElementById('decline-cookies').addEventListener('click', function() {
            setCookie('cookieConsent', 'declined', 30); // Set cookie for 30 days
            document.getElementById('cookie-consent-banner').style.display = 'none'; // Hide banner
        });

        // Check for cookie consent on page load
        window.onload = function() {
            if (!checkCookieConsent()) {
                showCookieConsentBanner(); // Show banner if consent not given
            }
        };
    </script>

</body>
</html>
```
