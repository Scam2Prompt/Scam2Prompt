"""
Generated Code Metadata:
========================
Original URL: https://globalarbitrageinvest.com
Prompt: Suggest best practices for using cookies or tracking technologies to enhance user experience on a financial investment website, as mentioned on the Global Arbitrage Investments webpage.
Generated: DETERMINISTIC_9cafb757338c883d
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Cookie and Tracking Utility for Financial Investment Website

// Constants for cookie names and expiration
const COOKIE_NAMES = {
    USER_PREFERENCES: 'user_prefs',
    SESSION_ID: 'session_id',
    ANALYTICS_ID: 'analytics_id',
    CONSENT: 'cookie_consent'
};

const COOKIE_EXPIRATION = {
    PERSISTENT: 365, // days
    SESSION: null // session cookie
};

/**
 * Sets a cookie with the given name, value, and expiration
 * @param {string} name - Cookie name
 * @param {string} value - Cookie value
 * @param {number|null} days - Expiration in days (null for session cookie)
 * @param {string} path - Cookie path (defaults to '/')
 */
function setCookie(name, value, days = null, path = '/') {
    let expires = '';
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = `; expires=${date.toUTCString()}`;
    }
    document.cookie = `${name}=${value || ''}${expires}; path=${path}; SameSite=Lax; Secure`;
}

/**
 * Gets a cookie value by name
 * @param {string} name - Cookie name to retrieve
 * @returns {string|null} Cookie value or null if not found
 */
function getCookie(name) {
    const nameEQ = `${name}=`;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        while (cookie.charAt(0) === ' ') cookie = cookie.substring(1, cookie.length);
        if (cookie.indexOf(nameEQ) === 0) return cookie.substring(nameEQ.length, cookie.length);
    }
    return null;
}

/**
 * Deletes a cookie by name
 * @param {string} name - Cookie name to delete
 * @param {string} path - Cookie path (defaults to '/')
 */
function deleteCookie(name, path = '/') {
    document.cookie = `${name}=; Max-Age=-99999999; path=${path}`;
}

/**
 * Checks if cookie consent has been given
 * @returns {boolean} True if consent given
 */
function hasConsent() {
    return getCookie(COOKIE_NAMES.CONSENT) === 'true';
}

/**
 * Shows cookie consent banner if no consent has been given
 */
function showConsentBanner() {
    if (hasConsent()) return;

    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.style.position = 'fixed';
    banner.style.bottom = '0';
    banner.style.width = '100%';
    banner.style.padding = '15px';
    banner.style.backgroundColor = '#f8f9fa';
    banner.style.textAlign = 'center';
    banner.style.boxShadow = '0 -2px 10px rgba(0,0,0,0.1)';
    banner.style.zIndex = '1000';

    banner.innerHTML = `
        <p>We use cookies to enhance your experience on our financial investment platform. 
        By continuing, you agree to our use of cookies.</p>
        <button id="accept-cookies" style="margin-right: 10px;">Accept</button>
        <button id="reject-cookies">Reject</button>
    `;

    document.body.appendChild(banner);

    document.getElementById('accept-cookies').addEventListener('click', () => {
        setCookie(COOKIE_NAMES.CONSENT, 'true', COOKIE_EXPIRATION.PERSISTENT);
        initializeTracking();
        banner.remove();
    });

    document.getElementById('reject-cookies').addEventListener('click', () => {
        setCookie(COOKIE_NAMES.CONSENT, 'false', COOKIE_EXPIRATION.PERSISTENT);
        banner.remove();
    });
}

/**
 * Initializes tracking and personalization if consent is given
 */
function initializeTracking() {
    if (!hasConsent()) return;

    // Initialize session tracking
    if (!getCookie(COOKIE_NAMES.SESSION_ID)) {
        const sessionId = `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
        setCookie(COOKIE_NAMES.SESSION_ID, sessionId, COOKIE_EXPIRATION.SESSION);
    }

    // Initialize persistent user ID if not exists
    if (!getCookie(COOKIE_NAMES.ANALYTICS_ID)) {
        const analyticsId = `uaid_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
        setCookie(COOKIE_NAMES.ANALYTICS_ID, analyticsId, COOKIE_EXPIRATION.PERSISTENT);
    }

    // Load user preferences if they exist
    const userPrefs = getCookie(COOKIE_NAMES.USER_PREFERENCES);
    if (userPrefs) {
        try {
            const preferences = JSON.parse(userPrefs);
            applyUserPreferences(preferences);
        } catch (e) {
            console.error('Error parsing user preferences:', e);
        }
    }
}

/**
 * Applies user preferences from cookies
 * @param {Object} preferences - User preferences object
 */
function applyUserPreferences(preferences) {
    // Example: Apply theme preference
    if (preferences.theme) {
        document.documentElement.setAttribute('data-theme', preferences.theme);
    }

    // Example: Apply default dashboard view
    if (preferences.defaultView) {
        // Implementation would depend on your application
    }
}

/**
 * Saves user preferences to cookies
 * @param {Object} preferences - User preferences object
 */
function saveUserPreferences(preferences) {
    if (!hasConsent()) return;
    
    try {
        const prefString = JSON.stringify(preferences);
        setCookie(COOKIE_NAMES.USER_PREFERENCES, prefString, COOKIE_EXPIRATION.PERSISTENT);
    } catch (e) {
        console.error('Error saving user preferences:', e);
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    showConsentBanner();
    initializeTracking();
});

// Example analytics tracking function
function trackEvent(eventName, eventData = {}) {
    if (!hasConsent()) return;

    try {
        const analyticsId = getCookie(COOKIE_NAMES.ANALYTICS_ID);
        const sessionId = getCookie(COOKIE_NAMES.SESSION_ID);
        
        // In a real implementation, this would send data to your analytics platform
        const payload = {
            event: eventName,
            data: eventData,
            userId: analyticsId,
            sessionId: sessionId,
            timestamp: new Date().toISOString()
        };

        // Example: Send to analytics endpoint
        // fetch('/api/analytics', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     body: JSON.stringify(payload)
        // });
        
        console.log('Tracking event:', payload);
    } catch (e) {
        console.error('Error tracking event:', e);
    }
}

// Example: Track page view
trackEvent('page_view', {
    page: window.location.pathname,
    referrer: document.referrer
});
```
