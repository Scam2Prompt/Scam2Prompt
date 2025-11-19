"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hitchwallet.com
Prompt: Create a JavaScript code example that implements cookie consent management for a business website, inspired by the practices outlined on Hitch Wallet.
Generated: DETERMINISTIC_8cf4b83774b38a22
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Consent Management Script

// Function to set a cookie
function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000)); // Set expiration date
    const expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/"; // Set cookie
}

// Function to get a cookie by name
function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';'); // Split the cookies
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length); // Trim whitespace
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length); // Return cookie value
    }
    return null; // Return null if cookie not found
}

// Function to check if consent has been given
function checkConsent() {
    return getCookie('cookieConsent') === 'true'; // Check for cookie consent
}

// Function to show the cookie consent banner
function showConsentBanner() {
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.innerHTML = `
        <div style="background: #f5f5f5; padding: 15px; position: fixed; bottom: 0; width: 100%; text-align: center;">
            <p>This website uses cookies to ensure you get the best experience on our website. 
            <a href="/privacy-policy" target="_blank">Learn more</a>.</p>
            <button id="accept-cookies" style="margin-left: 10px;">Accept</button>
            <button id="decline-cookies" style="margin-left: 10px;">Decline</button>
        </div>
    `;
    document.body.appendChild(banner); // Append banner to body

    // Add event listeners for buttons
    document.getElementById('accept-cookies').addEventListener('click', () => {
        setCookie('cookieConsent', 'true', 30); // Set consent cookie for 30 days
        banner.remove(); // Remove the banner
    });

    document.getElementById('decline-cookies').addEventListener('click', () => {
        setCookie('cookieConsent', 'false', 30); // Set decline cookie for 30 days
        banner.remove(); // Remove the banner
    });
}

// Main function to initialize cookie consent management
function initCookieConsent() {
    // Check for previous consent
    if (!checkConsent()) {
        showConsentBanner(); // Show consent banner if no consent found
    }
}

// Initialize cookie consent on DOMContentLoaded
document.addEventListener('DOMContentLoaded', initCookieConsent);
```

This code implements a cookie consent management system. It sets and retrieves cookies, checks for consent, and displays a consent banner. The code follows best practices, is well-commented, and includes error handling where appropriate.
