"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hope-exchange.com
Prompt: Write a code snippet to create a cookie consent banner for a website, inspired by the cookie policy mentioned on Hope Exchange.
Generated: DETERMINISTIC_a253bb09d3da5f26
Batch ID: 20250612_160526
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
        /* Basic styling for the cookie consent banner */
        #cookie-consent-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: #fff;
            padding: 15px;
            display: none; /* Initially hidden */
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
        }
        #cookie-consent-banner button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
            border-radius: 5px;
        }
        #cookie-consent-banner button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

<div id="cookie-consent-banner">
    <span>This website uses cookies to enhance the user experience. By continuing to use this site, you consent to our cookie policy.</span>
    <button id="accept-cookies">Accept</button>
</div>

<script>
    // Function to check if the cookie consent has already been given
    function hasCookieConsent() {
        return document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='));
    }

    // Function to set the cookie consent
    function setCookieConsent() {
        const expires = new Date();
        expires.setFullYear(expires.getFullYear() + 1); // Cookie expires in 1 year
        document.cookie = `cookieConsent=true; expires=${expires.toUTCString()}; path=/`;
    }

    // Function to display the cookie consent banner
    function showCookieConsentBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        banner.style.display = 'flex'; // Show banner
    }

    // Event listener for the accept button
    document.getElementById('accept-cookies').addEventListener('click', function() {
        setCookieConsent(); // Set consent cookie
        document.getElementById('cookie-consent-banner').style.display = 'none'; // Hide banner
    });

    // Check for cookie consent on page load
    window.onload = function() {
        if (!hasCookieConsent()) {
            showCookieConsentBanner(); // Show banner if consent not given
        }
    };
</script>

</body>
</html>
```
