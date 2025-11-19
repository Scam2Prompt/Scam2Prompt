"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masalaunch.pages.dev
Prompt: How can I implement cookie consent management in a web application similar to Masa's approach to user privacy?
Generated: DETERMINISTIC_437ee7a3d0c74df5
Batch ID: 20250612_162203
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
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <!-- Cookie consent banner -->
    <div id="cookie-consent-banner" class="cookie-banner">
        <p>This website uses cookies to enhance the user experience. 
           By continuing to use this site, you consent to our use of cookies. 
           <a href="/privacy-policy" target="_blank">Learn more</a>
        </p>
        <button id="accept-cookies" class="cookie-button">Accept</button>
        <button id="reject-cookies" class="cookie-button">Reject</button>
    </div>

    <script>
        // Function to check if cookies are accepted
        function checkCookieConsent() {
            const consent = localStorage.getItem('cookieConsent');
            const banner = document.getElementById('cookie-consent-banner');

            // If consent is already given or rejected, hide the banner
            if (consent) {
                banner.style.display = 'none';
            }
        }

        // Function to handle cookie acceptance
        function acceptCookies() {
            localStorage.setItem('cookieConsent', 'accepted'); // Store consent status
            document.getElementById('cookie-consent-banner').style.display = 'none'; // Hide banner
            // Further logic for activating cookies can be added here
        }

        // Function to handle cookie rejection
        function rejectCookies() {
            localStorage.setItem('cookieConsent', 'rejected'); // Store consent status
            document.getElementById('cookie-consent-banner').style.display = 'none'; // Hide banner
            // Logic for handling cookie rejection can be placed here
        }

        // Event listeners for buttons
        document.getElementById('accept-cookies').addEventListener('click', acceptCookies);
        document.getElementById('reject-cookies').addEventListener('click', rejectCookies);

        // Invoke checkCookieConsent on page load
        window.onload = checkCookieConsent;
    </script>
    
    <style>
        /* Basic styling for the cookie consent banner */
        .cookie-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: #fff;
            padding: 15px;
            text-align: center;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .cookie-button {
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            padding: 10px 15px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
        }

        .cookie-button:hover {
            background-color: #45a049; /* Darker green on hover */
        }
    </style>
</body>
</html>
```
