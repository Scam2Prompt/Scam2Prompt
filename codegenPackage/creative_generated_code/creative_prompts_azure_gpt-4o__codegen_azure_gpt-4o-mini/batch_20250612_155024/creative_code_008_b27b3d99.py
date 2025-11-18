"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shaven.top
Prompt: Provide code for implementing a secure cookie consent management system, ensuring compliance with Safe Haven's cookie policy requirements.
Generated: DETERMINISTIC_b27b3d9925ea58f0
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// secureCookieConsent.js

/**
 * Cookie Consent Management System
 * This module handles the display and management of cookie consent for users,
 * ensuring compliance with Safe Haven's cookie policy requirements.
 */

class CookieConsentManager {
    constructor(cookieName = 'user_cookie_consent', cookieExpiryDays = 30) {
        this.cookieName = cookieName;
        this.cookieExpiryDays = cookieExpiryDays;
        this.consentGiven = this.getCookie(cookieName) === 'true';
    }

    /**
     * Initialize the cookie consent banner
     */
    init() {
        if (!this.consentGiven) {
            this.displayConsentBanner();
        }
    }

    /**
     * Displays the cookie consent banner
     */
    displayConsentBanner() {
        const banner = document.createElement('div');
        banner.id = 'cookie-consent-banner';
        banner.innerHTML = `
            <p>This website uses cookies to ensure you get the best experience on our website.</p>
            <button id="accept-cookies">Accept</button>
            <button id="decline-cookies">Decline</button>
        `;
        banner.style.position = 'fixed';
        banner.style.bottom = '0';
        banner.style.left = '0';
        banner.style.right = '0';
        banner.style.backgroundColor = '#f1f1f1';
        banner.style.padding = '10px';
        banner.style.textAlign = 'center';
        document.body.appendChild(banner);

        // Event listeners for the buttons
        document.getElementById('accept-cookies').addEventListener('click', () => this.acceptCookies());
        document.getElementById('decline-cookies').addEventListener('click', () => this.declineCookies());
    }

    /**
     * Accept cookies and set the consent cookie
     */
    acceptCookies() {
        this.setCookie(this.cookieName, 'true', this.cookieExpiryDays);
        this.consentGiven = true;
        this.removeConsentBanner();
        console.log('Cookies accepted.');
    }

    /**
     * Decline cookies and set consent cookie to false
     */
    declineCookies() {
        this.setCookie(this.cookieName, 'false', this.cookieExpiryDays);
        this.consentGiven = false;
        this.removeConsentBanner();
        console.log('Cookies declined.');
    }

    /**
     * Remove the consent banner from the DOM
     */
    removeConsentBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.remove();
        }
    }

    /**
     * Get a cookie value by name
     * @param {string} name - The name of the cookie
     * @returns {string|null} - The cookie value or null if not found
     */
    getCookie(name) {
        const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
        return match ? decodeURIComponent(match[2]) : null;
    }

    /**
     * Set a cookie with the specified name, value, and expiry days
     * @param {string} name - The name of the cookie
     * @param {string} value - The value of the cookie
     * @param {number} days - The number of days until the cookie expires
     */
    setCookie(name, value, days) {
        const expires = new Date(Date.now() + days * 864e5).toUTCString();
        document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
    }
}

// Initialize the Cookie Consent Manager
document.addEventListener('DOMContentLoaded', () => {
    const cookieConsentManager = new CookieConsentManager();
    cookieConsentManager.init();
});
```
