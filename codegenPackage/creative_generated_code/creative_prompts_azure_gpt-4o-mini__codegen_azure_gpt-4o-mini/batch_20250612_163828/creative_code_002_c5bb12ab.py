"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinneon.com
Prompt: "Generate code for a cookie consent banner that complies with GDPR for a business website."
Generated: DETERMINISTIC_c5bb12ab59e67f12
Batch ID: 20250612_163828
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
        /* Basic styles for the cookie consent banner */
        #cookieConsentBanner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: #fff;
            padding: 15px;
            text-align: center;
            z-index: 1000;
            display: none; /* Hidden by default */
        }
        #cookieConsentBanner button {
            background-color: #f0a500; /* Button color */
            color: #fff;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            margin-left: 10px;
        }
    </style>
</head>
<body>

<div id="cookieConsentBanner">
    <p>
        We use cookies to enhance your experience on our website. 
        By clicking "Accept", you consent to our use of cookies in accordance with our 
        <a href="/privacy-policy" style="color: #f0a500;">Privacy Policy</a>.
    </p>
    <button id="acceptCookies">Accept</button>
    <button id="rejectCookies">Reject</button>
</div>

<script>
    // Function to show the cookie consent banner
    function showCookieConsentBanner() {
        const banner = document.getElementById('cookieConsentBanner');
        banner.style.display = 'block';
    }

    // Function to handle the user's cookie consent decision
    function handleCookieConsent(accepted) {
        if (accepted) {
            // Set a cookie to remember that the user accepted cookies
            document.cookie = "cookieConsent=true; max-age=" + 60 * 60 * 24 * 365 + "; path=/"; // 1 year expiry
        } else {
            // Set a cookie to remember that the user rejected cookies
            document.cookie = "cookieConsent=false; max-age=" + 60 * 60 * 24 * 365 + "; path=/"; // 1 year expiry
        }
        // Hide the cookie consent banner after user action
        document.getElementById('cookieConsentBanner').style.display = 'none';
    }

    // Function to check if the cookie consent has already been given
    function checkCookieConsent() {
        const consentCookie = document.cookie.split('; ').find(row => row.startsWith('cookieConsent='));
        if (!consentCookie) {
            // If no consent cookie, show the banner
            showCookieConsentBanner();
        }
    }

    // Event listeners for button clicks
    document.getElementById('acceptCookies').addEventListener('click', () => {
        handleCookieConsent(true);
    });

    document.getElementById('rejectCookies').addEventListener('click', () => {
        handleCookieConsent(false);
    });

    // Check for cookie consent on page load
    window.onload = checkCookieConsent;
</script>

</body>
</html>
```
