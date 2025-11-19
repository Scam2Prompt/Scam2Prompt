"""
Generated Code Metadata:
========================
Original URL: https://www.giselabravo.com
Prompt: Develop a script to manage cookie preferences and GDPR compliance for a website, similar to the cookie management system explained on Gisela Bravo's site.
Generated: DETERMINISTIC_7078d9ad04d29318
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieConsentManager.js

class CookieConsentManager {
    constructor() {
        this.cookieName = 'cookieConsent';
        this.consentGiven = false;
        this.init();
    }

    // Initialize the cookie consent manager
    init() {
        this.checkConsent();
        this.renderConsentBanner();
    }

    // Check if consent cookie exists and set consent status
    checkConsent() {
        const consentCookie = this.getCookie(this.cookieName);
        if (consentCookie) {
            this.consentGiven = consentCookie === 'true';
        }
    }

    // Render the cookie consent banner
    renderConsentBanner() {
        if (!this.consentGiven) {
            const banner = document.createElement('div');
            banner.id = 'cookie-consent-banner';
            banner.innerHTML = `
                <p>This website uses cookies to enhance the user experience. 
                <button id="accept-cookies">Accept</button>
                <button id="decline-cookies">Decline</button></p>
            `;
            document.body.appendChild(banner);

            // Event listeners for buttons
            document.getElementById('accept-cookies').addEventListener('click', () => this.acceptCookies());
            document.getElementById('decline-cookies').addEventListener('click', () => this.declineCookies());
        }
    }

    // Accept cookies and set consent cookie
    acceptCookies() {
        this.setCookie(this.cookieName, 'true', 365);
        this.consentGiven = true;
        this.removeBanner();
    }

    // Decline cookies and set consent cookie
    declineCookies() {
        this.setCookie(this.cookieName, 'false', 365);
        this.consentGiven = false;
        this.removeBanner();
    }

    // Remove the consent banner from the DOM
    removeBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.remove();
        }
    }

    // Get a cookie by name
    getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }

    // Set a cookie with a specified name, value, and expiration days
    setCookie(name, value, days) {
        const expires = new Date(Date.now() + days * 864e5).toUTCString();
        document.cookie = `${name}=${value}; expires=${expires}; path=/`;
    }
}

// Instantiate the CookieConsentManager on page load
document.addEventListener('DOMContentLoaded', () => {
    try {
        new CookieConsentManager();
    } catch (error) {
        console.error('Error initializing CookieConsentManager:', error);
    }
});
```

This code provides a simple cookie consent management system that complies with GDPR requirements. It allows users to accept or decline cookies and stores their preferences in a cookie. The implementation includes error handling and follows best practices for JavaScript development.
