"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.solutions
Prompt: Write a JavaScript function that tracks user consent for cookies, inspired by the cookie policy on celestia.solutions.
Generated: DETERMINISTIC_9b4d0e49e36b00e5
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Cookie Consent Manager
 * This utility manages user consent for cookies, allowing users to accept or decline cookie usage.
 */
class CookieConsentManager {
    constructor() {
        this.cookieName = 'userCookieConsent';
        this.consentGiven = false;
        this.init();
    }

    /**
     * Initializes the cookie consent manager by checking existing consent.
     */
    init() {
        const consent = this.getCookie(this.cookieName);
        if (consent) {
            this.consentGiven = consent === 'true';
        } else {
            this.showConsentBanner();
        }
    }

    /**
     * Shows the cookie consent banner to the user.
     */
    showConsentBanner() {
        const banner = document.createElement('div');
        banner.id = 'cookie-consent-banner';
        banner.innerHTML = `
            <div>
                <p>This website uses cookies to enhance your experience. 
                Do you accept the use of cookies?</p>
                <button id="accept-cookies" class="cookie-button">Accept</button>
                <button id="decline-cookies" class="cookie-button">Decline</button>
            </div>
        `;
        document.body.appendChild(banner);

        document.getElementById('accept-cookies').addEventListener('click', () => this.acceptCookies());
        document.getElementById('decline-cookies').addEventListener('click', () => this.declineCookies());
    }

    /**
     * Accepts cookies and sets the consent cookie.
     */
    acceptCookies() {
        this.setCookie(this.cookieName, 'true', 365);
        this.consentGiven = true;
        this.hideBanner();
    }

    /**
     * Declines cookies and sets the consent cookie.
     */
    declineCookies() {
        this.setCookie(this.cookieName, 'false', 365);
        this.consentGiven = false;
        this.hideBanner();
    }

    /**
     * Hides the cookie consent banner.
     */
    hideBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.remove();
        }
    }

    /**
     * Sets a cookie in the browser.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {number} days - The number of days until the cookie expires.
     */
    setCookie(name, value, days) {
        const expires = new Date(Date.now() + days * 24 * 60 * 60 * 1000).toUTCString();
        document.cookie = `${name}=${value}; expires=${expires}; path=/; SameSite=Lax;`;
    }

    /**
     * Retrieves a cookie by name.
     * @param {string} name - The name of the cookie to retrieve.
     * @returns {string|null} The value of the cookie or null if not found.
     */
    getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }
}

// Initialize the Cookie Consent Manager
document.addEventListener('DOMContentLoaded', () => {
    try {
        new CookieConsentManager();
    } catch (error) {
        console.error('Error initializing Cookie Consent Manager:', error);
    }
});
```
