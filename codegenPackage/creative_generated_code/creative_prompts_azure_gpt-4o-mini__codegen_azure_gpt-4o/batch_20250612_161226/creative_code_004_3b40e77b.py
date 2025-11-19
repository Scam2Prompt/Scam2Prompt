"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getgrass.im
Prompt: Illustrate how to implement a cookie consent banner on a website similar to GetGrass, ensuring compliance with privacy policies while enhancing user experience.
Generated: DETERMINISTIC_3b40e77b8341b5fb
Batch ID: 20250612_161226
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
    <title>Cookie Consent Banner</title>
    <style>
        /* Style for the cookie banner */
        #cookie-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #303030;
            color: #ffffff;
            padding: 15px;
            box-shadow: 0 -1px 5px rgba(0, 0, 0, 0.2);
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
        }

        #cookie-banner p {
            margin: 0;
            font-size: 14px;
            line-height: 1.5;
        }

        #cookie-banner button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
            font-size: 14px;
            transition: background-color 0.3s;
        }

        #cookie-banner button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <!-- Cookie Consent Banner -->
    <div id="cookie-banner" style="display: none;">
        <p>
            We use cookies to enhance your experience on our website. By continuing, you agree to our 
            <a href="/privacy-policy" style="color: #4CAF50; text-decoration: underline;">Privacy Policy</a>.
        </p>
        <button id="accept-cookies">Accept</button>
    </div>

    <script>
        /**
         * Function to check if the cookie consent has already been given.
         * @returns {boolean} True if consent has been given, false otherwise.
         */
        function hasAcceptedCookies() {
            return document.cookie.split(';').some((cookie) => cookie.trim().startsWith('cookie-consent=accepted'));
        }

        /**
         * Function to save the user's cookie consent.
         */
        function saveCookieConsent() {
            // Set a cookie with a 1-year expiration
            const expirationDate = new Date();
            expirationDate.setFullYear(expirationDate.getFullYear() + 1);
            document.cookie = `cookie-consent=accepted; expires=${expirationDate.toUTCString()}; path=/;`;
        }

        /**
         * Function to hide the cookie banner.
         */
        function hideCookieBanner() {
            const cookieBanner = document.getElementById('cookie-banner');
            cookieBanner.style.display = 'none';
        }

        /**
         * Function to initialize the cookie consent banner.
         */
        function initializeCookieBanner() {
            if (!hasAcceptedCookies()) {
                // Show the banner if the user has not accepted cookies
                const cookieBanner = document.getElementById('cookie-banner');
                cookieBanner.style.display = 'flex';

                // Add click event listener to the accept button
                const acceptButton = document.getElementById('accept-cookies');
                acceptButton.addEventListener('click', () => {
                    saveCookieConsent();
                    hideCookieBanner();
                });
            }
        }

        // Initialize the cookie banner on page load
        window.addEventListener('load', initializeCookieBanner);
    </script>
</body>
</html>
```
