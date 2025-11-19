"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomware.net
Prompt: Write a function in JavaScript that handles user consent for cookies, inspired by the cookie usage policy on phantomware.net.
Generated: DETERMINISTIC_034dfb55bc879077
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Cookie Consent Manager for handling user consent regarding cookie usage.
 * Inspired by the cookie usage policy on phantomware.net.
 */
class CookieConsentManager {
    constructor() {
        this.cookieName = 'userConsent';
        this.consentGiven = this.getConsentStatus();
        this.init();
    }

    /**
     * Initializes the cookie consent manager by displaying the consent banner if needed.
     */
    init() {
        if (!this.consentGiven) {
            this.showConsentBanner();
        }
    }

    /**
     * Displays the cookie consent banner to the user.
     */
    showConsentBanner() {
        const banner = document.createElement('div');
        banner.id = 'cookie-consent-banner';
        banner.style.position = 'fixed';
        banner.style.bottom = '0';
        banner.style.left = '0';
        banner.style.right = '0';
        banner.style.backgroundColor = '#333';
        banner.style.color = '#fff';
        banner.style.padding = '10px';
        banner.style.textAlign = 'center';
        banner.innerHTML = `
            <p>This website uses cookies to ensure you get the best experience on our website. 
            <a href="/cookie-policy" style="color: #4caf50;">Learn more</a></p>
            <button id="accept-cookies">I Accept</button>
            <button id="decline-cookies">I Decline</button>
        `;
        document.body.appendChild(banner);

        // Attach event listeners to buttons
        document.getElementById('accept-cookies').addEventListener('click', () => this.acceptCookies());
        document.getElementById('decline-cookies').addEventListener('click', () => this.declineCookies());
    }

    /**
     * Accepts the cookies and sets the consent cookie.
     */
    acceptCookies() {
        this.setConsentCookie(true);
        this.removeConsentBanner();
    }

    /**
     * Declines the cookies and sets the consent cookie accordingly.
     */
    declineCookies() {
        this.setConsentCookie(false);
        this.removeConsentBanner();
    }

    /**
     * Sets the user consent cookie with an expiration of 365 days.
     * @param {boolean} consent - User's consent status.
     */
    setConsentCookie(consent) {
        const expiryDate = new Date();
        expiryDate.setFullYear(expiryDate.getFullYear() + 1);
        const cookieValue = consent ? 'accepted' : 'declined';
        document.cookie = `${this.cookieName}=${cookieValue}; expires=${expiryDate.toUTCString()}; path=/`;
    }

    /**
     * Retrieves the user's consent status from cookies.
     * @returns {boolean|null} - Returns true if consent is given, false if declined, or null if not set.
     */
    getConsentStatus() {
        const cookies = document.cookie.split('; ');
        for (let cookie of cookies) {
            const [name, value] = cookie.split('=');
            if (name === this.cookieName) {
                return value === 'accepted';
            }
        }
        return null; // Consent not set
    }

    /**
     * Removes the consent banner from the DOM.
     */
    removeConsentBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.remove();
        }
    }
}

// Initialize the Cookie Consent Manager
document.addEventListener('DOMContentLoaded', () => new CookieConsentManager());
```
