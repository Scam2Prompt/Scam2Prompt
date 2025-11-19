"""
Generated Code Metadata:
========================
Original URL: https://getgrass.im
Prompt: Illustrate how to implement a cookie consent banner on a website similar to GetGrass, ensuring compliance with privacy policies while enhancing user experience.
Generated: DETERMINISTIC_3b40e77b8341b5fb
Batch ID: 20250612_161226
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
    <title>Cookie Consent Banner Example</title>
    <style>
        /* Basic styles for the cookie consent banner */
        #cookie-consent-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: #fff;
            padding: 15px;
            text-align: center;
            display: none; /* Hidden by default */
            z-index: 1000;
        }
        #cookie-consent-banner button {
            background-color: #f1c40f;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            margin-left: 10px;
        }
    </style>
</head>
<body>

    <div id="cookie-consent-banner">
        <span>This website uses cookies to enhance the user experience. By continuing to browse, you consent to our use of cookies.</span>
        <button id="accept-cookies">Accept</button>
        <button id="decline-cookies">Decline</button>
    </div>

    <script>
        // Function to check if the cookie consent has already been given
        function checkCookieConsent() {
            return document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='));
        }

        // Function to show the cookie consent banner
        function showCookieConsentBanner() {
            const banner = document.getElementById('cookie-consent-banner');
            banner.style.display = 'block';
        }

        // Function to set a cookie
        function setCookie(name, value, days) {
            const expires = new Date(Date.now() + days * 864e5).toUTCString();
            document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
        }

        // Function to handle cookie acceptance
        function acceptCookies() {
            setCookie('cookieConsent', 'accepted', 30); // Store consent for 30 days
            document.getElementById('cookie-consent-banner').style.display = 'none';
        }

        // Function to handle cookie decline
        function declineCookies() {
            setCookie('cookieConsent', 'declined', 30); // Store decline for 30 days
            document.getElementById('cookie-consent-banner').style.display = 'none';
        }

        // Initialize the cookie consent banner
        function initCookieConsent() {
            if (!checkCookieConsent()) {
                showCookieConsentBanner();
            }
        }

        // Event listeners for buttons
        document.getElementById('accept-cookies').addEventListener('click', acceptCookies);
        document.getElementById('decline-cookies').addEventListener('click', declineCookies);

        // Run the initialization function on page load
        window.onload = initCookieConsent;
    </script>

</body>
</html>
```
