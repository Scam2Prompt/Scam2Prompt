"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-masafinance.pages.dev
Prompt: Generate a code snippet that enables basic functionalities of a website while respecting user cookie consent, as seen in Masa's implementation.
Generated: DETERMINISTIC_a534e93990eda6b7
Batch ID: 20250612_162207
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
        /* Basic styles for the cookie consent banner */
        #cookie-consent {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: #fff;
            padding: 15px;
            display: none; /* Hidden by default */
            z-index: 1000;
            text-align: center;
        }
        #cookie-consent button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div id="cookie-consent">
        <p>We use cookies to enhance your experience. By continuing to visit this site you agree to our use of cookies.</p>
        <button id="accept-cookies">Accept</button>
    </div>

    <script>
        // Function to check if the user has already accepted cookies
        function hasUserConsented() {
            return document.cookie.split(';').some((item) => item.trim().startsWith('cookies_accepted='));
        }

        // Function to display the cookie consent banner
        function displayCookieConsent() {
            const consentBanner = document.getElementById('cookie-consent');
            consentBanner.style.display = 'block';
        }

        // Function to handle user cookie consent
        function handleCookieConsent() {
            // Set a cookie to remember the user's consent for 1 year
            const expires = new Date(Date.now() + 365 * 24 * 60 * 60 * 1000).toUTCString();
            document.cookie = `cookies_accepted=true; expires=${expires}; path=/`;

            // Hide the consent banner after acceptance
            document.getElementById('cookie-consent').style.display = 'none';
        }

        // Event listener for the "Accept" button
        document.getElementById('accept-cookies').addEventListener('click', handleCookieConsent);

        // Check for cookie consent on page load
        window.onload = function() {
            if (!hasUserConsented()) {
                displayCookieConsent();
            }
        };
    </script>

</body>
</html>
```
