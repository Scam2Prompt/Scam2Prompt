"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ishiba.org
Prompt: Write a code snippet that demonstrates how to handle cookie consent management in a web application, similar to the approach used by Instituto Shibata Barbosa.
Generated: DETERMINISTIC_f788a916568c80ad
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Cookie Consent Management Code
 * This script handles cookie consent banner display and user preferences for a web application.
 * It ensures compliance with cookie regulations (e.g., GDPR).
 */

// Immediately Invoked Function Expression (IIFE) to avoid polluting global scope
(function () {
    // Constants
    const COOKIE_NAME = 'cookieConsent';
    const COOKIE_EXPIRATION_DAYS = 365;
    const COOKIE_BANNER_ID = 'cookie-banner';
    const ACCEPT_BUTTON_ID = 'accept-cookies';
    const REJECT_BUTTON_ID = 'reject-cookies';

    /**
     * Utility: Set a cookie with a specified name, value, and expiration days.
     * @param {string} name - The cookie name.
     * @param {string} value - The cookie value.
     * @param {number} days - Number of days until the cookie expires.
     */
    function setCookie(name, value, days) {
        const date = new Date();
        date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
        document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`;
    }

    /**
     * Utility: Get the value of a specified cookie by name.
     * @param {string} name - The cookie name.
     * @returns {string|null} - The cookie value, or null if not found.
     */
    function getCookie(name) {
        const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
        return match ? match[2] : null;
    }

    /**
     * Show the cookie consent banner.
     */
    function showCookieBanner() {
        const banner = document.getElementById(COOKIE_BANNER_ID);
        if (banner) {
            banner.style.display = 'block';
        }
    }

    /**
     * Hide the cookie consent banner.
     */
    function hideCookieBanner() {
        const banner = document.getElementById(COOKIE_BANNER_ID);
        if (banner) {
            banner.style.display = 'none';
        }
    }

    /**
     * Handle the user's consent decision for cookies.
     * @param {boolean} consent - True if the user accepts cookies; false otherwise.
     */
    function handleCookieConsent(consent) {
        setCookie(COOKIE_NAME, consent ? 'accepted' : 'rejected', COOKIE_EXPIRATION_DAYS);
        hideCookieBanner();
        console.log(`Cookie consent: ${consent ? 'Accepted' : 'Rejected'}`);
    }

    /**
     * Initialization: Check the user's cookie consent status and show banner if necessary.
     */
    function initCookieConsent() {
        const consent = getCookie(COOKIE_NAME);
        if (!consent) {
            // Show banner only if consent is not yet given
            showCookieBanner();
        }
    }

    // Event listeners for consent buttons
    document.addEventListener('DOMContentLoaded', () => {
        const acceptButton = document.getElementById(ACCEPT_BUTTON_ID);
        const rejectButton = document.getElementById(REJECT_BUTTON_ID);

        if (acceptButton) {
            acceptButton.addEventListener('click', () => handleCookieConsent(true));
        }

        if (rejectButton) {
            rejectButton.addEventListener('click', () => handleCookieConsent(false));
        }

        // Initialize cookie consent logic
        initCookieConsent();
    });
})();
```

```html
<!-- HTML code for the cookie consent banner -->
<div id="cookie-banner" style="display: none; position: fixed; bottom: 0; width: 100%; background: #f8f9fa; padding: 10px; text-align: center; border-top: 1px solid #ddd;">
    <p>We use cookies to improve your experience. Do you accept?</p>
    <button id="accept-cookies" style="margin-right: 10px;">Accept</button>
    <button id="reject-cookies">Reject</button>
</div>
```
