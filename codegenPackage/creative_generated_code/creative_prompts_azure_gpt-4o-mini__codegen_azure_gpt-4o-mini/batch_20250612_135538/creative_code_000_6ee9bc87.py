"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.solutions
Prompt: Generate code to implement a cookie consent feature for a website, similar to the one described on celestia.solutions.
Generated: DETERMINISTIC_6ee9bc874d99672c
Batch ID: 20250612_135538
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
        /* Basic styling for the cookie consent banner */
        #cookie-consent-banner {
            position: fixed;
            bottom: 20px;
            left: 20px;
            right: 20px;
            background-color: #f1f1f1;
            padding: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            display: none; /* Initially hidden */
            z-index: 1000;
        }
        #cookie-consent-banner button {
            margin-left: 10px;
        }
    </style>
</head>
<body>

<div id="cookie-consent-banner">
    <span>This website uses cookies to ensure you get the best experience on our website.</span>
    <button id="accept-cookies">Accept</button>
    <button id="reject-cookies">Reject</button>
</div>

<script>
    // Function to check for cookie consent
    function checkCookieConsent() {
        // Retrieve the cookie consent status from localStorage
        return localStorage.getItem('cookieConsent') === 'true';
    }

    // Function to show the cookie consent banner
    function showConsentBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        banner.style.display = 'block'; // Show the banner
    }

    // Function to handle cookie acceptance
    function acceptCookies() {
        // Set the cookie consent status in localStorage
        localStorage.setItem('cookieConsent', 'true');
        hideConsentBanner();
    }

    // Function to handle cookie rejection
    function rejectCookies() {
        // Set the cookie consent status in localStorage
        localStorage.setItem('cookieConsent', 'false');
        hideConsentBanner();
    }

    // Function to hide the cookie consent banner
    function hideConsentBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        banner.style.display = 'none'; // Hide the banner
    }

    // Initialize the cookie consent feature
    function initCookieConsent() {
        // Check if consent has already been given
        if (!checkCookieConsent()) {
            showConsentBanner(); // Show the banner if consent is not given
        }
        
        // Add event listeners to the buttons
        document.getElementById('accept-cookies').addEventListener('click', acceptCookies);
        document.getElementById('reject-cookies').addEventListener('click', rejectCookies);
    }

    // Run the initialization function on page load
    window.onload = initCookieConsent;

</script>

</body>
</html>
```
