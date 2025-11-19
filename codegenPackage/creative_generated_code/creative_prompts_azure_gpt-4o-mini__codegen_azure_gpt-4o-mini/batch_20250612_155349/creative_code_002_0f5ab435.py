"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockfe-cdn.godaddysites.com
Prompt: Write a JavaScript function to handle cookie acceptance and data aggregation for a photo gallery site.
Generated: DETERMINISTIC_0f5ab4352bd81c4c
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * CookieConsentManager manages user consent for cookies on the photo gallery site.
 */
class CookieConsentManager {
    constructor() {
        this.consentCookieName = 'photo_gallery_cookie_consent';
        this.consentGiven = this.getCookieConsent();
    }

    /**
     * Initializes the cookie consent functionality by checking for existing consent
     * and displaying the consent banner if necessary.
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
        banner.innerHTML = `
            <p>This website uses cookies to enhance the user experience.</p>
            <button id="accept-cookies">Accept Cookies</button>
            <button id="decline-cookies">Decline Cookies</button>
        `;
        document.body.appendChild(banner);

        document.getElementById('accept-cookies').onclick = () => this.acceptCookies();
        document.getElementById('decline-cookies').onclick = () => this.declineCookies();
    }

    /**
     * Accepts cookies and sets the corresponding cookie.
     */
    acceptCookies() {
        this.setCookie(this.consentCookieName, 'true', 365);
        this.consentGiven = true;
        this.hideConsentBanner();
        this.aggregateData('consent', 'accepted');
    }

    /**
     * Declines cookies and sets the corresponding cookie.
     */
    declineCookies() {
        this.setCookie(this.consentCookieName, 'false', 365);
        this.consentGiven = false;
        this.hideConsentBanner();
        this.aggregateData('consent', 'declined');
    }

    /**
     * Hides the cookie consent banner.
     */
    hideConsentBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.remove();
        }
    }

    /**
     * Retrieves the user's cookie consent status.
     * @returns {boolean} true if consent is given, false otherwise.
     */
    getCookieConsent() {
        const cookieValue = this.getCookie(this.consentCookieName);
        return cookieValue === 'true';
    }

    /**
     * Sets a cookie in the user's browser.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {number} days - The number of days until the cookie expires.
     */
    setCookie(name, value, days) {
        const expires = new Date();
        expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
        const expiresString = `expires=${expires.toUTCString()}`;
        document.cookie = `${name}=${value};${expiresString};path=/`;
    }

    /**
     * Retrieves a cookie value by its name.
     * @param {string} name - The name of the cookie.
     * @returns {string|null} The value of the cookie, or null if not found.
     */
    getCookie(name) {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const trimmedCookie = cookie.trim();
            if (trimmedCookie.startsWith(`${name}=`)) {
                return trimmedCookie.split('=')[1];
            }
        }
        return null;
    }

    /**
     * Aggregates user data based on their cookie consent decisions.
     * @param {string} action - The action to record.
     * @param {string} status - The status of the action (accepted or declined).
     */
    aggregateData(action, status) {
        // Here you would typically send data to your server or analytics service.
        console.log(`User has ${status} cookies. Action: ${action}`);
        // Example: send to your analytics endpoint
        // fetch('/api/aggregate', { method: 'POST', body: JSON.stringify({ action, status }) });
    }
}

// Initialize the Cookie Consent Manager when the DOM is fully loaded.
document.addEventListener('DOMContentLoaded', () => {
    const cookieConsentManager = new CookieConsentManager();
    cookieConsentManager.init();
});
```
