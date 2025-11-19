"""
Generated Code Metadata:
========================
Original URL: https://celestia.solutions
Prompt: Write a JavaScript function that tracks user consent for cookies, inspired by the cookie policy on celestia.solutions.
Generated: DETERMINISTIC_9b4d0e49e36b00e5
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Consent Manager
 * This module manages user consent for cookies on the website.
 * It displays a consent banner and stores the user's choice in local storage.
 */

class CookieConsentManager {
    constructor() {
        this.consentKey = 'cookieConsent';
        this.consentBannerId = 'cookie-consent-banner';
        this.init();
    }

    /**
     * Initializes the cookie consent manager.
     * Checks for existing consent and displays the banner if necessary.
     */
    init() {
        if (!this.getConsent()) {
            this.showConsentBanner();
        }
    }

    /**
     * Displays the cookie consent banner.
     */
    showConsentBanner() {
        const banner = document.createElement('div');
        banner.id = this.consentBannerId;
        banner.innerHTML = `
            <div style="background: #f8f9fa; padding: 20px; position: fixed; bottom: 0; width: 100%; text-align: center; z-index: 1000;">
                <p>This website uses cookies to enhance the user experience. 
                <a href="/cookie-policy" target="_blank">Learn more</a>.</p>
                <button id="accept-cookies" style="margin-right: 10px;">Accept</button>
                <button id="decline-cookies">Decline</button>
            </div>
        `;
        document.body.appendChild(banner);

        // Event listeners for buttons
        document.getElementById('accept-cookies').addEventListener('click', () => this.setConsent(true));
        document.getElementById('decline-cookies').addEventListener('click', () => this.setConsent(false));
    }

    /**
     * Sets the user's cookie consent choice and hides the banner.
     * @param {boolean} consent - User's consent choice.
     */
    setConsent(consent) {
        try {
            localStorage.setItem(this.consentKey, JSON.stringify(consent));
            this.hideConsentBanner();
        } catch (error) {
            console.error('Error saving cookie consent:', error);
        }
    }

    /**
     * Hides the cookie consent banner.
     */
    hideConsentBanner() {
        const banner = document.getElementById(this.consentBannerId);
        if (banner) {
            banner.remove();
        }
    }

    /**
     * Retrieves the user's cookie consent choice from local storage.
     * @returns {boolean|null} - Returns true if consent is given, false if declined, or null if not set.
     */
    getConsent() {
        try {
            const consent = localStorage.getItem(this.consentKey);
            return consent !== null ? JSON.parse(consent) : null;
        } catch (error) {
            console.error('Error retrieving cookie consent:', error);
            return null;
        }
    }
}

// Instantiate the CookieConsentManager to start tracking user consent
document.addEventListener('DOMContentLoaded', () => {
    new CookieConsentManager();
});
```
