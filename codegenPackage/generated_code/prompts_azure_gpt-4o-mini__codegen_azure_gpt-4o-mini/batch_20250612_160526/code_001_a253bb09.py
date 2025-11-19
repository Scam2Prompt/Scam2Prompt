"""
Generated Code Metadata:
========================
Original URL: https://hope-exchange.com
Prompt: Write a code snippet to create a cookie consent banner for a website, inspired by the cookie policy mentioned on Hope Exchange.
Generated: DETERMINISTIC_a253bb09d3da5f26
Batch ID: 20250612_160526
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
            padding: 10px 20px;
            cursor: pointer;
            margin-left: 10px;
        }
    </style>
</head>
<body>

<div id="cookieConsentBanner">
    <span>This website uses cookies to ensure you get the best experience on our website. 
    <a href="/cookie-policy" style="color: #f1c40f;">Learn more</a></span>
    <button id="acceptCookies">Accept</button>
</div>

<script>
    // Function to check if the cookie consent has already been given
    function checkCookieConsent() {
        return document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='));
    }

    // Function to show the cookie consent banner
    function showCookieConsentBanner() {
        const banner = document.getElementById('cookieConsentBanner');
        banner.style.display = 'block';
    }

    // Function to set a cookie for consent
    function setCookieConsent() {
        const expirationDays = 365; // Cookie expiration time in days
        const date = new Date();
        date.setTime(date.getTime() + (expirationDays * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        document.cookie = "cookieConsent=true;" + expires + ";path=/"; // Set the cookie
    }

    // Event listener for the accept button
    document.getElementById('acceptCookies').addEventListener('click', function() {
        setCookieConsent(); // Set the cookie consent
        document.getElementById('cookieConsentBanner').style.display = 'none'; // Hide the banner
    });

    // Check for cookie consent on page load
    window.onload = function() {
        if (!checkCookieConsent()) {
            showCookieConsentBanner(); // Show the banner if consent not given
        }
    };
</script>

</body>
</html>
```
