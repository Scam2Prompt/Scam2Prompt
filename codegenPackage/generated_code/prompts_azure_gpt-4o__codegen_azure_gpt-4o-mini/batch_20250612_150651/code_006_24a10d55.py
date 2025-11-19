"""
Generated Code Metadata:
========================
Original URL: https://globallinknext.com
Prompt: Create a script to analyze user preferences and manage consent for cookies, similar to the consent management system described on the GlobalLink NEXT website.
Generated: DETERMINISTIC_24a10d55ea84f145
Batch ID: 20250612_150651
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
        this.consentKey = 'cookieConsent';
        this.consentData = {
            necessary: true,
            preferences: false,
            statistics: false,
            marketing: false,
        };
    }

    // Initialize the consent manager
    init() {
        this.loadConsent();
        this.renderConsentBanner();
    }

    // Load consent data from local storage
    loadConsent() {
        const consent = localStorage.getItem(this.consentKey);
        if (consent) {
            this.consentData = JSON.parse(consent);
        }
    }

    // Render the consent banner
    renderConsentBanner() {
        if (!this.consentData.preferences && !this.consentData.statistics && !this.consentData.marketing) {
            const banner = document.createElement('div');
            banner.id = 'cookie-consent-banner';
            banner.innerHTML = `
                <p>We use cookies to enhance your experience. Please select your preferences:</p>
                <label><input type="checkbox" id="preferences"> Preferences</label>
                <label><input type="checkbox" id="statistics"> Statistics</label>
                <label><input type="checkbox" id="marketing"> Marketing</label>
                <button id="accept-cookies">Accept</button>
                <button id="reject-cookies">Reject</button>
            `;
            document.body.appendChild(banner);

            // Event listeners for buttons
            document.getElementById('accept-cookies').addEventListener('click', () => this.acceptCookies());
            document.getElementById('reject-cookies').addEventListener('click', () => this.rejectCookies());
        }
    }

    // Accept cookies and save preferences
    acceptCookies() {
        this.consentData.preferences = document.getElementById('preferences').checked;
        this.consentData.statistics = document.getElementById('statistics').checked;
        this.consentData.marketing = document.getElementById('marketing').checked;
        this.saveConsent();
        this.removeBanner();
    }

    // Reject cookies and save preferences
    rejectCookies() {
        this.consentData.preferences = false;
        this.consentData.statistics = false;
        this.consentData.marketing = false;
        this.saveConsent();
        this.removeBanner();
    }

    // Save consent data to local storage
    saveConsent() {
        try {
            localStorage.setItem(this.consentKey, JSON.stringify(this.consentData));
        } catch (error) {
            console.error('Error saving consent data:', error);
        }
    }

    // Remove the consent banner from the DOM
    removeBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.remove();
        }
    }
}

// Initialize the Cookie Consent Manager on page load
document.addEventListener('DOMContentLoaded', () => {
    const cookieConsentManager = new CookieConsentManager();
    cookieConsentManager.init();
});
```

This JavaScript code implements a simple cookie consent management system. It allows users to select their cookie preferences and saves their choices in local storage. The code is structured, well-commented, and includes error handling for local storage operations.
