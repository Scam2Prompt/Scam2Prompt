"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: "Generate a JavaScript function to track and manage user interactions with a website while respecting cookie consent preferences, specifically for analytics and performance cookies."
Generated: DETERMINISTIC_209ef529f29f11a0
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * CookieConsentTracker - Tracks user interactions while respecting cookie consent preferences.
 * @class
 */
class CookieConsentTracker {
    /**
     * Initializes the tracker with default settings.
     * @param {Object} options - Configuration options.
     * @param {string} options.consentCookieName - Name of the cookie storing consent preferences.
     * @param {number} options.cookieExpiryDays - Number of days until cookies expire.
     */
    constructor(options = {}) {
        this.consentCookieName = options.consentCookieName || 'cookie_consent';
        this.cookieExpiryDays = options.cookieExpiryDays || 30;
        this.initialize();
    }

    /**
     * Initializes the tracker by checking consent and setting up event listeners.
     */
    initialize() {
        this.checkConsent();
        this.setupEventListeners();
    }

    /**
     * Checks if the user has given consent for analytics and performance cookies.
     * @returns {boolean} True if consent is given, false otherwise.
     */
    hasConsent() {
        const consentCookie = this.getCookie(this.consentCookieName);
        if (!consentCookie) return false;

        try {
            const consentData = JSON.parse(consentCookie);
            return consentData.analytics && consentData.performance;
        } catch (e) {
            console.error('Error parsing consent cookie:', e);
            return false;
        }
    }

    /**
     * Sets a cookie with the given name, value, and expiration.
     * @param {string} name - Cookie name.
     * @param {string} value - Cookie value.
     * @param {number} days - Expiration in days.
     */
    setCookie(name, value, days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = `expires=${date.toUTCString()}`;
        document.cookie = `${name}=${value};${expires};path=/;SameSite=Lax`;
    }

    /**
     * Retrieves a cookie by name.
     * @param {string} name - Cookie name.
     * @returns {string|null} Cookie value or null if not found.
     */
    getCookie(name) {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [cookieName, cookieValue] = cookie.trim().split('=');
            if (cookieName === name) {
                return decodeURIComponent(cookieValue);
            }
        }
        return null;
    }

    /**
     * Tracks a user interaction if consent is given.
     * @param {string} eventName - Name of the event to track.
     * @param {Object} eventData - Data associated with the event.
     */
    trackEvent(eventName, eventData = {}) {
        if (!this.hasConsent()) return;

        try {
            // Simulate sending data to analytics service
            console.log('Tracking event:', eventName, eventData);
            // In a real implementation, replace with actual analytics API call
            // e.g., Google Analytics, Segment, etc.
        } catch (e) {
            console.error('Error tracking event:', e);
        }
    }

    /**
     * Sets up event listeners for common user interactions.
     */
    setupEventListeners() {
        if (!this.hasConsent()) return;

        document.addEventListener('click', (e) => {
            this.trackEvent('click', { target: e.target.tagName });
        });

        window.addEventListener('scroll', () => {
            this.trackEvent('scroll', { position: window.scrollY });
        });

        window.addEventListener('load', () => {
            this.trackEvent('page_load', { url: window.location.href });
        });
    }

    /**
     * Updates consent preferences and re-initializes the tracker.
     * @param {Object} consent - Consent preferences.
     * @param {boolean} consent.analytics - Consent for analytics cookies.
     * @param {boolean} consent.performance - Consent for performance cookies.
     */
    updateConsent(consent) {
        try {
            const consentString = JSON.stringify(consent);
            this.setCookie(this.consentCookieName, consentString, this.cookieExpiryDays);
            this.initialize();
        } catch (e) {
            console.error('Error updating consent:', e);
        }
    }
}

// Example usage:
// const tracker = new CookieConsentTracker();
// tracker.updateConsent({ analytics: true, performance: true });
```
