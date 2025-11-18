"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ggeminiloginx.godaddysites.com
Prompt: Write JavaScript code to display a cookie consent banner for a login page, similar to the functionality described on the Gemiṇi: Loℊin site.
Generated: DETERMINISTIC_69aeed4d54490d0d
Batch ID: 20250612_154436
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
    <title>Login Page</title>
    <style>
        /* Basic styles for the cookie consent banner */
        #cookie-consent-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            text-align: center;
            display: none; /* Initially hidden */
            z-index: 1000;
        }
        #cookie-consent-banner button {
            background-color: #721c24;
            color: white;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div id="cookie-consent-banner">
        This site uses cookies to improve your experience. 
        <button id="accept-cookies">Accept Cookies</button>
    </div>

    <script>
        // Function to check if cookies have been accepted
        function checkCookieConsent() {
            return document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='));
        }

        // Function to show the cookie consent banner
        function showCookieBanner() {
            const banner = document.getElementById('cookie-consent-banner');
            banner.style.display = 'block';
        }

        // Function to handle cookie acceptance
        function acceptCookies() {
            // Set a cookie to remember the user's consent
            const expirationDate = new Date();
            expirationDate.setFullYear(expirationDate.getFullYear() + 1); // Cookie expires in 1 year
            document.cookie = `cookieConsent=true; expires=${expirationDate.toUTCString()}; path=/`;
            const banner = document.getElementById('cookie-consent-banner');
            banner.style.display = 'none'; // Hide banner after acceptance
        }

        // Initialize cookie consent banner
        function initCookieConsent() {
            try {
                if (!checkCookieConsent()) {
                    showCookieBanner(); // Show banner if no consent
                }
                document.getElementById('accept-cookies').addEventListener('click', acceptCookies);
            } catch (error) {
                console.error('Error initializing cookie consent:', error);
            }
        }

        // Execute initialization on DOMContentLoaded
        document.addEventListener('DOMContentLoaded', initCookieConsent);
    </script>
</body>
</html>
```
