"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globallinknext.com
Prompt: Create a script to analyze user preferences and manage consent for cookies, similar to the consent management system described on the GlobalLink NEXT website.
Generated: DETERMINISTIC_24a10d55ea84f145
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CookieConsentManager.js
// This script manages user consent for cookies on a website, allowing users to customize their preferences.

class CookieConsentManager {
    constructor() {
        this.consents = {
            essential: false,
            analytics: false,
            marketing: false,
        };
        this.init();
    }

    // Initialize the consent manager
    init() {
        this.loadConsents();
        this.renderConsentBanner();
    }

    // Load stored consent preferences from localStorage
    loadConsents() {
        const storedConsents = localStorage.getItem('cookieConsents');
        if (storedConsents) {
            this.consents = JSON.parse(storedConsents);
        }
    }

    // Render the consent banner and buttons
    renderConsentBanner() {
        // Create banner element
        const banner = document.createElement('div');
        banner.id = 'cookie-consent-banner';
        banner.style.position = 'fixed';
        banner.style.bottom = '10px';
        banner.style.left = '10px';
        banner.style.backgroundColor = '#fff';
        banner.style.border = '1px solid #ccc';
        banner.style.padding = '20px';
        banner.style.zIndex = '1000';

        // Create consent options
        banner.innerHTML = `
            <h3>Cookie Consent</h3>
            <p>We use cookies to enhance your experience. Please manage your preferences:</p>
            <label>
                <input type="checkbox" id="essential" checked disabled /> Essential Cookies (required)
            </label><br>
            <label>
                <input type="checkbox" id="analytics" ${this.consents.analytics ? 'checked' : ''}/> Analytics Cookies
            </label><br>
            <label>
                <input type="checkbox" id="marketing" ${this.consents.marketing ? 'checked' : ''}/> Marketing Cookies
            </label><br>
            <button id="accept">Accept All</button>
            <button id="save">Save Preferences</button>
            <button id="reject">Reject All</button>
        `;

        // Append banner to the body
        document.body.appendChild(banner);

        // Add event listeners to buttons
        document.getElementById('accept').addEventListener('click', () => this.acceptAll());
        document.getElementById('save').addEventListener('click', () => this.savePreferences());
        document.getElementById('reject').addEventListener('click', () => this.rejectAll());
    }

    // Accept all cookies and save preferences
    acceptAll() {
        this.consents.analytics = true;
        this.consents.marketing = true;
        this.saveConsents();
        this.removeBanner();
    }

    // Reject all non-essential cookies and save preferences
    rejectAll() {
        this.consents.analytics = false;
        this.consents.marketing = false;
        this.saveConsents();
        this.removeBanner();
    }

    // Save selected cookie preferences
    savePreferences() {
        this.consents.analytics = document.getElementById('analytics').checked;
        this.consents.marketing = document.getElementById('marketing').checked;
        this.saveConsents();
        this.removeBanner();
    }

    // Save consent preferences to localStorage
    saveConsents() {
        try {
            localStorage.setItem('cookieConsents', JSON.stringify(this.consents));
        } catch (error) {
            console.error('Error saving consent preferences:', error);
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

// Instantiate the CookieConsentManager on page load
document.addEventListener('DOMContentLoaded', () => {
    new CookieConsentManager();
});
```
