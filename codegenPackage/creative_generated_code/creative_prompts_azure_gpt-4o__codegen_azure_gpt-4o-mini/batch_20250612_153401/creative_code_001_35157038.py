"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Recommend a JavaScript library or API for managing consent preferences, similar to the cookie management system described on Masa's website.
Generated: DETERMINISTIC_35157038e3befbf4
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ConsentManager - A lightweight JavaScript library for managing user consent preferences.
 * 
 * This library allows you to set, get, and manage user consent for cookies and other tracking technologies.
 * It provides an interface to display a consent banner and store preferences in local storage.
 * 
 * Usage:
 * 1. Include this script in your HTML.
 * 2. Initialize the ConsentManager and customize the options.
 * 
 * Example:
 * const consentManager = new ConsentManager({
 *     bannerText: "We use cookies to enhance your experience. Do you consent to the use of cookies?",
 *     acceptText: "Accept",
 *     declineText: "Decline",
 * });
 * consentManager.init();
 */

class ConsentManager {
    constructor(options) {
        // Validate and set options
        this.options = {
            bannerText: options.bannerText || "This website uses cookies to ensure you get the best experience.",
            acceptText: options.acceptText || "Accept",
            declineText: options.declineText || "Decline",
        };

        this.storageKey = 'userConsent';
    }

    /**
     * Initialize the consent manager
     * Displays the consent banner if consent has not been given yet.
     */
    init() {
        if (!this.getConsent()) {
            this.showBanner();
        }
    }

    /**
     * Show the consent banner
     */
    showBanner() {
        const banner = document.createElement('div');
        banner.id = 'consent-banner';
        banner.style.position = 'fixed';
        banner.style.bottom = '0';
        banner.style.width = '100%';
        banner.style.backgroundColor = '#f9f9f9';
        banner.style.padding = '20px';
        banner.style.textAlign = 'center';
        banner.style.boxShadow = '0 -2px 5px rgba(0, 0, 0, 0.1)';
        
        banner.innerHTML = `
            <p>${this.options.bannerText}</p>
            <button id="accept-cookies">${this.options.acceptText}</button>
            <button id="decline-cookies">${this.options.declineText}</button>
        `;

        document.body.appendChild(banner);

        // Add event listeners for buttons
        document.getElementById('accept-cookies').addEventListener('click', () => this.handleConsent(true));
        document.getElementById('decline-cookies').addEventListener('click', () => this.handleConsent(false));
    }

    /**
     * Handle user's consent response
     * @param {boolean} consent - true if user accepts, false if declines
     */
    handleConsent(consent) {
        this.setConsent(consent);
        this.removeBanner();
    }

    /**
     * Set user consent to local storage
     * @param {boolean} consent - User's consent preference
     */
    setConsent(consent) {
        try {
            localStorage.setItem(this.storageKey, JSON.stringify({ consent }));
        } catch (error) {
            console.error('Error saving consent preference:', error);
        }
    }

    /**
     * Get user consent from local storage
     * @returns {boolean|null} - Returns true if consent is given, false if declined, null if not set
     */
    getConsent() {
        try {
            const consentData = localStorage.getItem(this.storageKey);
            return consentData ? JSON.parse(consentData).consent : null;
        } catch (error) {
            console.error('Error retrieving consent preference:', error);
            return null;
        }
    }

    /**
     * Remove the consent banner from the DOM
     */
    removeBanner() {
        const banner = document.getElementById('consent-banner');
        if (banner) {
            banner.remove();
        }
    }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
    const consentManager = new ConsentManager({
        bannerText: "We use cookies to enhance your experience. Do you consent to the use of cookies?",
        acceptText: "Accept",
        declineText: "Decline",
    });
    consentManager.init();
});
```
