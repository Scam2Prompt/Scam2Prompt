"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://videtisconsultores.es
Prompt: Provide code to implement a cookie consent management system for a website, following the privacy policy guidelines mentioned on Videtis Consultores' site.
Generated: DETERMINISTIC_60eee6c5e34e9c1c
Batch ID: 20250612_153517
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
    <style>
        /* Styles for the cookie consent banner */
        #cookie-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f8f8f8;
            color: #333;
            padding: 15px;
            text-align: center;
            box-shadow: 0px -2px 5px rgba(0,0,0,0.2);
            display: none;
        }
        #cookie-banner button {
            margin: 0 5px;
            padding: 10px 15px;
            border: none;
            background-color: #007BFF;
            color: white;
            cursor: pointer;
            border-radius: 3px;
        }
        #cookie-banner button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<div id="cookie-banner">
    <p>We use cookies to improve your experience on our website. By clicking "Accept", you consent to the use of cookies. 
       For more information, see our <a href="/privacy-policy" target="_blank">Privacy Policy</a>.</p>
    <button id="accept-cookies">Accept</button>
    <button id="reject-cookies">Reject</button>
</div>

<script>
    /**
     * Utility function to set a cookie
     * @param {string} name - Cookie name
     * @param {string} value - Cookie value
     * @param {number} days - Expiration time in days
     */
    function setCookie(name, value, days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }

    /**
     * Utility function to get a cookie by name
     * @param {string} name - Cookie name
     * @returns {string|null} - Cookie value or null if not found
     */
    function getCookie(name) {
        const nameEQ = name + "=";
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.indexOf(nameEQ) === 0) {
                return cookie.substring(nameEQ.length, cookie.length);
            }
        }
        return null;
    }

    /**
     * Initialize cookie consent banner
     */
    function initCookieConsent() {
        const banner = document.getElementById('cookie-banner');
        
        // Check if user has already made a choice
        const userConsent = getCookie('userConsent');
        if (userConsent) {
            console.log('User consent: ', userConsent);
            return; // Consent already given/rejected; no need to show banner
        }

        // Show cookie consent banner
        banner.style.display = 'block';

        // Handle accept button click
        document.getElementById('accept-cookies').addEventListener('click', function() {
            setCookie('userConsent', 'accepted', 365); // Store consent for 1 year
            banner.style.display = 'none'; // Hide banner
        });

        // Handle reject button click
        document.getElementById('reject-cookies').addEventListener('click', function() {
            setCookie('userConsent', 'rejected', 365); // Store rejection for 1 year
            banner.style.display = 'none'; // Hide banner
        });
    }

    // Initialize the cookie consent banner on page load
    window.onload = initCookieConsent;
</script>

</body>
</html>
```
