"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.giselabravo.com
Prompt: Develop a script to manage cookie preferences and GDPR compliance for a website, similar to the cookie management system explained on Gisela Bravo's site.
Generated: DETERMINISTIC_7078d9ad04d29318
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CookieConsentManager.js

class CookieConsentManager {
    constructor() {
        this.consentKey = 'cookie_consent';
        this.categories = {
            essential: 'essential',
            analytics: 'analytics',
            marketing: 'marketing'
        };
        this.init();
    }

    /**
     * Initializes the cookie consent manager by checking existing consent.
     */
    init() {
        this.checkConsent();
        this.renderBanner();
    }

    /**
     * Checks if cookie consent has already been granted or denied.
     */
    checkConsent() {
        const consent = this.getCookie(this.consentKey);
        if (consent) {
            this.processExistingConsent(consent);
        }
    }

    /**
     * Processes existing consent settings.
     * 
     * @param {string} consent - The stored consent value.
     */
    processExistingConsent(consent) {
        const consentData = JSON.parse(consent);
        this.applyConsent(consentData);
    }

    /**
     * Applies consent settings based on user preferences.
     * 
     * @param {object} consentData - The user consent data.
     */
    applyConsent(consentData) {
        if (consentData[this.categories.analytics]) {
            this.loadAnalyticsScripts();
        }
        if (consentData[this.categories.marketing]) {
            this.loadMarketingScripts();
        }
    }

    /**
     * Renders the cookie consent banner.
     */
    renderBanner() {
        const banner = document.createElement('div');
        banner.innerHTML = this.getBannerHTML();
        document.body.appendChild(banner);
        this.addBannerEvents();
    }

    /**
     * Returns the HTML for the consent banner.
     * 
     * @returns {string} HTML string for the cookie consent banner.
     */
    getBannerHTML() {
        return `
            <div id="cookie-banner" style="background-color: #f1f1f1; padding: 20px; position: fixed; bottom: 0; width: 100%; z-index: 1000;">
                <p>This website uses cookies to enhance your experience. 
                <button id="accept-all">Accept All</button>
                <button id="accept-necessary">Accept Necessary</button>
                <button id="customize">Customize</button>
                </p>
            </div>`;
    }

    /**
     * Adds event listeners to the banner buttons.
     */
    addBannerEvents() {
        document.getElementById('accept-all').addEventListener('click', () => this.acceptAll());
        document.getElementById('accept-necessary').addEventListener('click', () => this.acceptNecessary());
        document.getElementById('customize').addEventListener('click', () => this.showCustomizationOptions());
    }

    /**
     * Accepts all cookie categories and saves consent.
     */
    acceptAll() {
        const consentData = {
            [this.categories.essential]: true,
            [this.categories.analytics]: true,
            [this.categories.marketing]: true
        };
        this.saveConsent(consentData);
        this.hideBanner();
        this.loadAnalyticsScripts();
        this.loadMarketingScripts();
    }

    /**
     * Accepts only necessary cookies and saves consent.
     */
    acceptNecessary() {
        const consentData = {
            [this.categories.essential]: true,
            [this.categories.analytics]: false,
            [this.categories.marketing]: false
        };
        this.saveConsent(consentData);
        this.hideBanner();
    }

    /**
     * Shows customization options for cookie preferences.
     */
    showCustomizationOptions() {
        // Here, implement a modal or prompt for customizing cookie preferences
        alert("Customization options are not yet implemented.");
    }

    /**
     * Hides the cookie consent banner.
     */
    hideBanner() {
        const banner = document.getElementById('cookie-banner');
        if (banner) {
            banner.style.display = 'none';
        }
    }

    /**
     * Saves user consent in a cookie.
     * 
     * @param {object} consentData - The user consent data to save.
     */
    saveConsent(consentData) {
        const consentJson = JSON.stringify(consentData);
        this.setCookie(this.consentKey, consentJson, 365);
    }

    /**
     * Loads analytics scripts if consent is granted.
     */
    loadAnalyticsScripts() {
        // Load analytics scripts here
        console.log("Analytics scripts loaded.");
    }

    /**
     * Loads marketing scripts if consent is granted.
     */
    loadMarketingScripts() {
        // Load marketing scripts here
        console.log("Marketing scripts loaded.");
    }

    /**
     * Sets a cookie with the given name, value, and expiration days.
     * 
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {number} days - The number of days until expiration.
     */
    setCookie(name, value, days) {
        let expires = "";
        if (days) {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/";
    }

    /**
     * Retrieves the value of a specific cookie by its name.
     * 
     * @param {string} name - The name of the cookie.
     * @returns {string|null} - The cookie value or null if not found.
     */
    getCookie(name) {
        const nameEQ = name + "=";
        const ca = document.cookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }
}

// Instantiate the CookieConsentManager when the script loads
document.addEventListener('DOMContentLoaded', () => {
    new CookieConsentManager();
});
```
