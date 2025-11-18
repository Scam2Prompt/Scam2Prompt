"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Write a script to integrate cookie consent management into an e-commerce website, referencing the detailed cookie policy implementation on ActiveSport.cz.
Generated: DETERMINISTIC_3ca24325c04bead3
Batch ID: 20250612_152739
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
    <title>E-Commerce Cookie Consent Management</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS for styling -->
</head>
<body>

    <!-- Cookie Consent Banner -->
    <div id="cookieConsentBanner" class="cookie-consent-banner" style="display: none;">
        <p>This website uses cookies to ensure you get the best experience on our website. 
            <a href="cookie-policy.html">Learn more</a>
        </p>
        <button id="acceptCookies">Accept</button>
        <button id="declineCookies">Decline</button>
    </div>

    <script>
        // Function to check if cookies are accepted
        function checkCookieConsent() {
            // Retrieve cookie consent status from local storage
            const consentStatus = localStorage.getItem('cookieConsent');
            if (consentStatus === null) {
                // If consent status is not set, show the cookie consent banner
                document.getElementById('cookieConsentBanner').style.display = 'block';
            } else {
                // If consent is already given, you can load necessary scripts or settings
                console.log(`Cookie consent already given: ${consentStatus}`);
            }
        }

        // Function to handle cookie acceptance
        function acceptCookies() {
            localStorage.setItem('cookieConsent', 'accepted');
            document.getElementById('cookieConsentBanner').style.display = 'none';
            // Load analytic scripts or other functionalities that require consent
            console.log("Cookies accepted. Loading functionalities...");
        }

        // Function to handle cookie decline
        function declineCookies() {
            localStorage.setItem('cookieConsent', 'declined');
            document.getElementById('cookieConsentBanner').style.display = 'none';
            // Disable cookies for analytics or tracking
            console.log("Cookies declined. Tracking scripts will be disabled.");
        }

        // Event listeners for button clicks
        document.getElementById('acceptCookies').addEventListener('click', acceptCookies);
        document.getElementById('declineCookies').addEventListener('click', declineCookies);

        // Initialize cookie consent check on page load
        window.onload = checkCookieConsent;

    </script>

</body>
</html>
```

### styles.css
```css
/* Styles for the cookie consent banner */
.cookie-consent-banner {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #333;
    color: white;
    padding: 15px;
    text-align: center;
    z-index: 1000;
}

.cookie-consent-banner button {
    margin-left: 10px;
    padding: 5px 10px;
    background-color: #28a745;
    color: white;
    border: none;
    cursor: pointer;
}

.cookie-consent-banner button:hover {
    background-color: #218838;
}
```

### Note
- Ensure to create a `cookie-policy.html` page that outlines your cookie policy in detail as referenced.
- Adjust the analytics loading script based on your specific requirements after the user accepts cookies.
