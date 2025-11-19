"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestamosklogi.godaddysites.com
Prompt: How do I create a cookie policy for my website that complies with privacy regulations?
Generated: DETERMINISTIC_828f01db5fbfd0e7
Batch ID: 20250612_161035
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
    <title>Cookie Policy</title>
    <style>
        /* Basic styles for the cookie consent banner */
        #cookie-banner {
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
        #cookie-banner button {
            background-color: #ff9800;
            color: #fff;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
            margin-left: 10px;
        }
    </style>
</head>
<body>

<div id="cookie-banner">
    This website uses cookies to ensure you get the best experience on our website. 
    <a href="/cookie-policy" style="color: #ff9800;">Learn more</a>
    <button id="accept-cookies">Accept</button>
</div>

<script>
    // Function to check if cookies have been accepted
    function areCookiesAccepted() {
        return document.cookie.split(';').some((item) => item.trim().startsWith('cookiesAccepted='));
    }

    // Function to show the cookie banner if cookies are not accepted
    function showCookieBanner() {
        if (!areCookiesAccepted()) {
            document.getElementById('cookie-banner').style.display = 'block';
        }
    }

    // Function to set a cookie to remember user's choice
    function setCookie(name, value, days) {
        const d = new Date();
        d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000)); // Set expiration date
        const expires = "expires=" + d.toUTCString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/"; // Set cookie
    }

    // Event listener for the Accept button
    document.getElementById('accept-cookies').addEventListener('click', function() {
        try {
            setCookie('cookiesAccepted', 'true', 30); // Set cookie for 30 days
            document.getElementById('cookie-banner').style.display = 'none'; // Hide banner
        } catch (error) {
            console.error('Error setting cookie:', error); // Log any error
        }
    });

    // Show cookie banner on page load
    window.onload = showCookieBanner;
</script>

</body>
</html>
```
