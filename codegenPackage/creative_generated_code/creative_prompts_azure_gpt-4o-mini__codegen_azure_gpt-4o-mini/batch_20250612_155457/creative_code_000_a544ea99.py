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
        /* Basic styles for the cookie consent banner */
        #cookieConsent {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: #fff;
            padding: 15px;
            text-align: center;
            display: none; /* Hidden by default */
        }
        #cookieConsent button {
            margin-left: 15px;
            padding: 5px 10px;
            background-color: #f1f1f1;
            color: #333;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    
    <div id="cookieConsent">
        This website uses cookies to ensure you get the best experience on our website.
        <button id="acceptCookies">Got it!</button>
    </div>

    <script>
        /**
         * Function to check if the cookie consent has already been given.
         * @returns {boolean} True if cookie consent is already given, false otherwise.
         */
        function hasGivenCookieConsent() {
            return document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='));
        }

        /**
         * Function to show the cookie consent banner if consent isn't given.
         */
        function showCookieConsentBanner() {
            if (!hasGivenCookieConsent()) {
                document.getElementById('cookieConsent').style.display = 'block';
            }
        }

        /**
         * Function to handle cookie consent acceptance.
         */
        function acceptCookieConsent() {
            // Set a cookie to remember the user's choice for 365 days
            const expirationDate = new Date();
            expirationDate.setFullYear(expirationDate.getFullYear() + 1);
            document.cookie = `cookieConsent=true; expires=${expirationDate.toUTCString()}; path=/`;
            document.getElementById('cookieConsent').style.display = 'none';
        }

        // Add event listener to the accept button
        document.getElementById('acceptCookies').addEventListener('click', acceptCookieConsent);

        // Show the cookie consent banner on page load
        window.onload = showCookieConsentBanner;

    </script>
</body>
</html>
```
