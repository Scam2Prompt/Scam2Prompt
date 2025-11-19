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
// This script provides a simple implementation for managing cookie consent on a website.
// It adheres to best practices like providing clear communication and respecting user decisions.

/**
 * Initializes the cookie consent banner.
 */
function initializeCookieConsent() {
    // Check if consent has already been given
    if (getCookie("cookieConsent") !== null) {
        return; // Consent already handled, no need to show the banner
    }

    // Create the consent banner element
    const consentBanner = document.createElement("div");
    consentBanner.id = "cookie-consent-banner";
    consentBanner.style.position = "fixed";
    consentBanner.style.bottom = "0";
    consentBanner.style.left = "0";
    consentBanner.style.right = "0";
    consentBanner.style.backgroundColor = "#333";
    consentBanner.style.color = "#fff";
    consentBanner.style.padding = "15px";
    consentBanner.style.textAlign = "center";
    consentBanner.style.zIndex = "1000";
    consentBanner.innerHTML = `
        <p>We use cookies to improve your experience. By using our website, you agree to our cookie policy.</p>
        <button id="accept-cookies" style="margin: 0 10px; padding: 10px 20px; background: #4caf50; color: #fff; border: none; cursor: pointer;">Accept</button>
        <button id="reject-cookies" style="margin: 0 10px; padding: 10px 20px; background: #f44336; color: #fff; border: none; cursor: pointer;">Reject</button>
    `;

    document.body.appendChild(consentBanner);

    // Add event listeners for the buttons
    document.getElementById("accept-cookies").addEventListener("click", () => {
        setCookie("cookieConsent", "accepted", 365);
        removeBanner();
    });

    document.getElementById("reject-cookies").addEventListener("click", () => {
        setCookie("cookieConsent", "rejected", 365);
        removeBanner();
    });
}

/**
 * Sets a cookie in the browser.
 * @param {string} name - Name of the cookie.
 * @param {string} value - Value of the cookie.
 * @param {number} days - Number of days until expiration.
 */
function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = `${name}=${value}; ${expires}; path=/;`;
}

/**
 * Retrieves a cookie value by name.
 * @param {string} name - Name of the cookie to retrieve.
 * @returns {string|null} - Value of the cookie, or null if not found.
 */
function getCookie(name) {
    const nameEQ = name + "=";
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        while (cookie.charAt(0) === ' ') cookie = cookie.substring(1);
        if (cookie.indexOf(nameEQ) === 0) {
            return cookie.substring(nameEQ.length, cookie.length);
        }
    }
    return null;
}

/**
 * Removes the cookie consent banner from the page.
 */
function removeBanner() {
    const banner = document.getElementById("cookie-consent-banner");
    if (banner) {
        banner.remove();
    }
}

// Initialize the script
document.addEventListener("DOMContentLoaded", initializeCookieConsent);
```
