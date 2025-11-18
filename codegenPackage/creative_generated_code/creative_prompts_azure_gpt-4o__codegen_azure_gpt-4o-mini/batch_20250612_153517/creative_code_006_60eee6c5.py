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
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div id="cookie-consent-banner" class="hidden">
        <p>This website uses cookies to ensure you get the best experience on our website. 
        <a href="/privacy-policy" target="_blank">Learn more</a></p>
        <button id="accept-cookies">Accept Cookies</button>
        <button id="decline-cookies">Decline Cookies</button>
    </div>

    <script>
        /**
         * Function to manage cookie consent
         */
        (function () {
            const consentBanner = document.getElementById('cookie-consent-banner');
            const acceptButton = document.getElementById('accept-cookies');
            const declineButton = document.getElementById('decline-cookies');

            // Function to check if the cookie consent has been given
            function checkCookieConsent() {
                return document.cookie.split(';').some((cookie) => {
                    return cookie.trim().startsWith('cookieConsent=');
                });
            }

            // Function to set a cookie
            function setCookie(name, value, days) {
                const expires = new Date(Date.now() + days * 864e5).toUTCString();
                document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
            }

            // Function to show or hide the consent banner
            function toggleConsentBanner() {
                if (checkCookieConsent()) {
                    consentBanner.classList.add('hidden');
                } else {
                    consentBanner.classList.remove('hidden');
                }
            }

            // Event listener for accepting cookies
            acceptButton.addEventListener('click', () => {
                try {
                    setCookie('cookieConsent', 'accepted', 30); // Cookie expires in 30 days
                    toggleConsentBanner(); // Hide the banner
                } catch (error) {
                    console.error('Error setting cookie consent:', error);
                }
            });

            // Event listener for declining cookies
            declineButton.addEventListener('click', () => {
                try {
                    setCookie('cookieConsent', 'declined', 30); // Cookie expires in 30 days
                    toggleConsentBanner(); // Hide the banner
                } catch (error) {
                    console.error('Error setting cookie consent:', error);
                }
            });

            // Initialize the banner visibility on page load
            window.onload = toggleConsentBanner;

        })();
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
}

#cookie-consent-banner {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #f2f2f2;
    padding: 15px;
    text-align: center;
    box-shadow: 0 -2px 5px rgba(0,0,0,0.2);
    z-index: 1000;
}

.hidden {
    display: none; /* Hide element */
}

#cookie-consent-banner button {
    margin: 0 10px;
    padding: 10px 15px;
    border: none;
    background-color: #007bff; /* Primary button color */
    color: #fff;
    cursor: pointer;
}

#cookie-consent-banner button:hover {
    background-color: #0056b3; /* Darken on hover */
}
```
