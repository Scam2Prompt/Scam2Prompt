"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-masafinance.pages.dev
Prompt: Write a JavaScript function to customize cookie consent preferences based on user interactions, inspired by the Masa Finance cookie policy.
Generated: DETERMINISTIC_053107b8d974a997
Batch ID: 20250612_162207
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
 * This module handles user interactions for cookie consent preferences.
 */

// CookieConsentManager class definition
class CookieConsentManager {
    constructor() {
        this.cookieName = 'user_cookie_consent';
        this.consentData = this.getConsentData();
        this.init();
    }

    /**
     * Initializes the consent manager by creating UI elements
     * and setting up event listeners
     */
    init() {
        this.createConsentBanner();
        this.setupEventListeners();
    }

    /**
     * Creates the cookie consent banner and appends it to the body
     */
    createConsentBanner() {
        const banner = document.createElement('div');
        banner.id = 'cookie-consent-banner';
        banner.innerHTML = `
            <p>We use cookies to improve your experience. 
               <a href="/cookie-policy" target="_blank">Learn more</a>.
            </p>
            <button id="accept-cookies">Accept All</button>
            <button id="customize-cookies">Customize</button>
            <button id="reject-cookies">Reject All</button>
        `;
        document.body.appendChild(banner);

        // Check for existing consent data
        if (this.consentData) {
            this.updateBannerVisibility(false);
        }
    }

    /**
     * Sets up event listeners for the buttons in the consent banner
     */
    setupEventListeners() {
        document.getElementById('accept-cookies').addEventListener('click', () => {
            this.setConsent(true);
        });
        
        document.getElementById('customize-cookies').addEventListener('click', () => {
            this.openCustomizationModal();
        });

        document.getElementById('reject-cookies').addEventListener('click', () => {
            this.setConsent(false);
        });
    }

    /**
     * Opens a modal for customizing cookie preferences
     */
    openCustomizationModal() {
        // Implementation of the customization UI can be added here
        alert('Customization modal opened (to be implemented)');
    }

    /**
     * Sets the consent preferences and saves them to cookies
     * @param {boolean} consent - User consent decision
     */
    setConsent(consent) {
        const preference = consent ? 'accepted' : 'rejected';
        this.saveConsentData({ preference });
        this.updateBannerVisibility(false);
        console.log(`User has ${preference} cookie consent`);
    }

    /**
     * Saves the consent data to a cookie
     * @param {Object} consentData - The consent data object
     */
    saveConsentData(consentData) {
        const expires = new Date();
        expires.setFullYear(expires.getFullYear() + 1); // 1 year expiration
        document.cookie = `${this.cookieName}=${JSON.stringify(consentData)};expires=${expires.toUTCString()};path=/`;
    }

    /**
     * Retrieves the consent data from cookies
     * @returns {Object|null} - The consent data object or null if not found
     */
    getConsentData() {
        const cookieArr = document.cookie.split(';');
        for (let cookie of cookieArr) {
            const [name, value] = cookie.trim().split('=');
            if (name === this.cookieName) {
                return JSON.parse(value);
            }
        }
        return null;
    }

    /**
     * Updates the visibility of the consent banner
     * @param {boolean} isVisible - Determines if the banner should be visible
     */
    updateBannerVisibility(isVisible) {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.style.display = isVisible ? 'block' : 'none';
        }
    }
}

// Instantiate the CookieConsentManager when the document is ready
document.addEventListener('DOMContentLoaded', () => {
    try {
        new CookieConsentManager();
    } catch (error) {
        console.error('Error initializing CookieConsentManager:', error);
    }
});
```
