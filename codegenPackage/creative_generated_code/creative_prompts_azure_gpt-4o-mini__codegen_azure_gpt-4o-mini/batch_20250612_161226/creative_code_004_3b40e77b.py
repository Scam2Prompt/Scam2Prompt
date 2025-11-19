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
    <title>Cookie Consent Banner Example</title>
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
            display: none; /* Hidden by default */
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
        }
        #cookieConsentBanner button {
            background-color: #f1c40f;
            color: #333;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
        }
    </style>
</head>
<body>

<div id="cookieConsentBanner">
    <span>This website uses cookies to enhance user experience. By continuing to use this site, you consent to our use of cookies.</span>
    <button id="acceptCookiesBtn">Accept Cookies</button>
</div>

<script>
    // Function to show the cookie consent banner
    function showCookieConsentBanner() {
        const banner = document.getElementById('cookieConsentBanner');
        banner.style.display = 'flex'; // Show the banner
    }

    // Function to handle cookie acceptance
    function acceptCookies() {
        // Set a cookie to indicate consent
        document.cookie = "cookieConsent=true; max-age=" + 60 * 60 * 24 * 30 + "; path=/"; // Expires in 30 days
        hideCookieConsentBanner(); // Hide the banner
    }

    // Function to hide the cookie consent banner
    function hideCookieConsentBanner() {
        const banner = document.getElementById('cookieConsentBanner');
        banner.style.display = 'none'; // Hide the banner
    }

    // Function to check if the user has already given consent
    function checkCookieConsent() {
        const cookieArray = document.cookie.split('; ');
        const cookieConsent = cookieArray.find(cookie => cookie.startsWith('cookieConsent='));
        
        if (!cookieConsent) {
            showCookieConsentBanner(); // Show the banner if no consent cookie is found
        }
    }

    // Event listener for the accept button
    document.getElementById('acceptCookiesBtn').addEventListener('click', acceptCookies);

    // Check for cookie consent on page load
    document.addEventListener('DOMContentLoaded', checkCookieConsent);
</script>

</body>
</html>
```
