"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masalaunch.pages.dev
Prompt: Generate code to manage user consent preferences for cookies, including functionality for "Accept All," "Reject All," and "Customize Preferences," as outlined on the Masa website.
Generated: DETERMINISTIC_4c7ca87e0028e9d7
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// cookieConsent.js

// Cookie consent management class
class CookieConsentManager {
    constructor() {
        this.preferences = {
            analytics: false,
            marketing: false,
            necessary: true
        };
        this.consentGiven = false;
        this.init();
    }

    // Initialize consent manager and event listeners
    init() {
        this.loadPreferences();
        this.renderConsentBanner();
        this.bindEvents();
    }

    // Load preferences from local storage
    loadPreferences() {
        const storedPreferences = localStorage.getItem('cookie-consent-preferences');
        if (storedPreferences) {
            this.preferences = JSON.parse(storedPreferences);
            this.consentGiven = storedPreferences.includes("true");
        }
    }

    // Render the cookie consent banner
    renderConsentBanner() {
        const bannerHTML = `
            <div id="cookie-consent-banner" style="position: fixed; bottom: 0; width: 100%; background-color: #fff; border-top: 1px solid #ccc; padding: 10px; z-index: 1000;">
                <p>We use cookies to enhance your experience. 
                    <button id="accept-all">Accept All</button>
                    <button id="reject-all">Reject All</button>
                    <button id="customize">Customize Preferences</button>
                </p>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', bannerHTML);
    }

    // Bind event listeners for buttons
    bindEvents() {
        document.getElementById('accept-all').addEventListener('click', () => this.acceptAll());
        document.getElementById('reject-all').addEventListener('click', () => this.rejectAll());
        document.getElementById('customize').addEventListener('click', () => this.customizePreferences());
    }

    // Accept all cookies and save preferences
    acceptAll() {
        this.preferences = {
            analytics: true,
            marketing: true,
            necessary: true
        };
        this.savePreferences();
        this.hideBanner();
    }

    // Reject all cookies except necessary ones and save preferences
    rejectAll() {
        this.preferences = {
            analytics: false,
            marketing: false,
            necessary: true
        };
        this.savePreferences();
        this.hideBanner();
    }

    // Open a dialog to customize preferences
    customizePreferences() {
        // Implement a modal dialog for customization
        const customizeHTML = `
            <div id="customize-modal" style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #fff; padding: 20px; border: 1px solid #ccc; z-index: 1001;">
                <h3>Customize Your Preferences</h3>
                <label>
                    <input type="checkbox" id="analytics" ${this.preferences.analytics ? 'checked' : ''}/> Analytics
                </label><br/>
                <label>
                    <input type="checkbox" id="marketing" ${this.preferences.marketing ? 'checked' : ''}/> Marketing
                </label><br/>
                <button id="save-preferences">Save Preferences</button>
                <button id="close-modal">Close</button>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', customizeHTML);
        this.bindCustomizationEvents();
    }

    // Bind events for the customization modal
    bindCustomizationEvents() {
        document.getElementById('save-preferences').addEventListener('click', () => this.saveCustomizedPreferences());
        document.getElementById('close-modal').addEventListener('click', () => this.closeModal());
    }

    // Save customized preferences from modal
    saveCustomizedPreferences() {
        this.preferences.analytics = document.getElementById('analytics').checked;
        this.preferences.marketing = document.getElementById('marketing').checked;
        this.savePreferences();
        this.hideBanner();
        this.closeModal();
    }

    // Save preferences to local storage
    savePreferences() {
        try {
            localStorage.setItem('cookie-consent-preferences', JSON.stringify(this.preferences));
        } catch (error) {
            console.error('Error saving preferences to local storage:', error);
        }
    }

    // Hide the cookie consent banner
    hideBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.remove();
        }
    }

    // Close the customization modal
    closeModal() {
        const modal = document.getElementById('customize-modal');
        if (modal) {
            modal.remove();
        }
    }
}

// Instantiate the CookieConsentManager on page load
document.addEventListener('DOMContentLoaded', () => {
    new CookieConsentManager();
});
```
