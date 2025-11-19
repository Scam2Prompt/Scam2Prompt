"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sensibleoptimism.com
Prompt: Generate a code snippet for a simple web application that incorporates cookie consent functionality, similar to what might be found on a site like Sensible Optimism.
Generated: DETERMINISTIC_a544ea990dd3a0bc
Batch ID: 20250612_155457
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
    <title>Cookie Consent Example</title>
    <style>
        /* Styling for the cookie consent banner */
        #cookie-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: #fff;
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 14px;
            z-index: 1000;
        }
        #cookie-banner button {
            background: #007BFF;
            color: #fff;
            border: none;
            padding: 8px 12px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }
        #cookie-banner button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <!-- Main content of the page -->
    <h1>Welcome to Sensible Optimism</h1>
    <p>Enjoy browsing our site.</p>

    <!-- Cookie consent banner -->
    <div id="cookie-banner" style="display: none;">
        <span>We use cookies to improve your experience on our website. By using our site, you consent to cookies.</span>
        <button id="accept-cookies">Accept</button>
    </div>

    <script>
        // Function to check if the user has already accepted cookies
        function hasAcceptedCookies() {
            return document.cookie.split('; ').some(cookie => cookie.trim().startsWith('cookieConsent='));
        }

        // Function to set the cookie indicating user's consent
        function setCookieConsent() {
            const expirationDays = 365; // Cookie validity period (1 year)
            const date = new Date();
            date.setTime(date.getTime() + (expirationDays * 24 * 60 * 60 * 1000));
            document.cookie = `cookieConsent=true; expires=${date.toUTCString()}; path=/`;
        }

        // Function to handle cookie consent acceptance
        function handleAcceptCookies() {
            setCookieConsent();
            document.getElementById('cookie-banner').style.display = 'none';
        }

        // Initialize the cookie banner functionality
        (function initializeCookieBanner() {
            const cookieBanner = document.getElementById('cookie-banner');
            const acceptButton = document.getElementById('accept-cookies');

            // If cookies have not been accepted, show the banner
            if (!hasAcceptedCookies()) {
                cookieBanner.style.display = 'flex';
            }

            // Attach event listener to the "Accept" button
            acceptButton.addEventListener('click', handleAcceptCookies);
        })();
    </script>
</body>
</html>
```
