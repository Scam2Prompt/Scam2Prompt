"""
Generated Code Metadata:
========================
Original URL: https://metamausklogiixy.godaddysites.com
Prompt: Provide a step-by-step guide to setting up a cookie consent banner for a website, similar to the one described on Metamausklogiixy.
Generated: DETERMINISTIC_c8a81f52b1814e3a
Batch ID: 20250612_150227
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
    <title>Cookie Consent Banner</title>
    <style>
        /* Basic styles for the cookie consent banner */
        #cookieConsentBanner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: white;
            padding: 15px;
            text-align: center;
            display: none; /* Initially hidden */
            z-index: 1000;
        }
        #cookieConsentBanner button {
            background-color: #f1c40f;
            border: none;
            color: black;
            padding: 10px 20px;
            cursor: pointer;
            margin-left: 10px;
        }
    </style>
</head>
<body>

    <div id="cookieConsentBanner">
        This website uses cookies to ensure you get the best experience on our website. 
        <a href="/privacy-policy" style="color: #f1c40f;">Learn more</a>
        <button id="acceptCookies">Accept</button>
        <button id="declineCookies">Decline</button>
    </div>

    <script>
        // Function to check if the cookie consent has been given
        function checkCookieConsent() {
            return document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='));
        }

        // Function to show the cookie consent banner
        function showCookieConsentBanner() {
            const banner = document.getElementById('cookieConsentBanner');
            banner.style.display = 'block';
        }

        // Function to set a cookie
        function setCookie(name, value, days) {
            const expires = new Date(Date.now() + days * 864e5).toUTCString();
            document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
        }

        // Function to handle cookie acceptance
        function acceptCookies() {
            setCookie('cookieConsent', 'accepted', 30); // Set cookie for 30 days
            document.getElementById('cookieConsentBanner').style.display = 'none'; // Hide banner
        }

        // Function to handle cookie decline
        function declineCookies() {
            setCookie('cookieConsent', 'declined', 30); // Set cookie for 30 days
            document.getElementById('cookieConsentBanner').style.display = 'none'; // Hide banner
        }

        // Initialize the cookie consent banner
        function initCookieConsent() {
            if (!checkCookieConsent()) {
                showCookieConsentBanner(); // Show banner if consent not given
            }
        }

        // Event listeners for buttons
        document.getElementById('acceptCookies').addEventListener('click', acceptCookies);
        document.getElementById('declineCookies').addEventListener('click', declineCookies);

        // Run the initialization function on page load
        window.onload = initCookieConsent;
    </script>

</body>
</html>
```
