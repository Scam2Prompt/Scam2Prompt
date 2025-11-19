"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Create a code example that demonstrates how to use cookies for analytics purposes while respecting user consent preferences, as discussed in the context of the Masa application.
Generated: DETERMINISTIC_3ec8715a6068d497
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// analytics.js - Cookie-based analytics with user consent

/**
 * Checks if user has given consent for analytics cookies
 * @returns {boolean} True if consent is given, false otherwise
 */
function hasConsent() {
    return document.cookie
        .split('; ')
        .some(cookie => cookie.trim().startsWith('analytics_consent=true'));
}

/**
 * Sets the analytics consent cookie
 * @param {boolean} consent - User's consent preference
 * @param {number} days - Cookie expiration in days
 */
function setConsentCookie(consent, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `analytics_consent=${consent}; ${expires}; path=/; SameSite=Lax`;
}

/**
 * Tracks an analytics event if consent is given
 * @param {string} eventName - Name of the event to track
 * @param {Object} eventData - Additional event data
 */
function trackEvent(eventName, eventData = {}) {
    if (!hasConsent()) {
        console.log('Analytics tracking skipped - no user consent');
        return;
    }

    try {
        // Simulate sending data to analytics service
        const payload = {
            event: eventName,
            data: eventData,
            timestamp: new Date().toISOString(),
            userAgent: navigator.userAgent
        };

        console.log('Analytics event tracked:', payload);
        // In a real implementation, you would send this to your analytics backend
        // Example: fetch('/analytics', { method: 'POST', body: JSON.stringify(payload) });
    } catch (error) {
        console.error('Error tracking analytics event:', error);
    }
}

/**
 * Initializes analytics tracking based on user consent
 */
function initAnalytics() {
    // Check for existing consent
    if (hasConsent()) {
        trackEvent('page_view', { path: window.location.pathname });
        window.addEventListener('click', handleClickEvents);
    }
}

/**
 * Handles click events for analytics
 * @param {Event} event - The click event
 */
function handleClickEvents(event) {
    const target = event.target.closest('[data-track]');
    if (target) {
        const eventName = target.getAttribute('data-track');
        const eventData = {
            element: target.tagName,
            id: target.id || null,
            class: target.className || null
        };
        trackEvent(eventName, eventData);
    }
}

// Example UI for consent management
document.addEventListener('DOMContentLoaded', () => {
    const consentBanner = document.getElementById('cookie-consent-banner');
    const acceptBtn = document.getElementById('accept-cookies');
    const rejectBtn = document.getElementById('reject-cookies');

    if (!hasConsent() && consentBanner) {
        consentBanner.style.display = 'block';
    }

    if (acceptBtn) {
        acceptBtn.addEventListener('click', () => {
            setConsentCookie(true, 365);
            consentBanner.style.display = 'none';
            initAnalytics();
        });
    }

    if (rejectBtn) {
        rejectBtn.addEventListener('click', () => {
            setConsentCookie(false, 365);
            consentBanner.style.display = 'none';
        });
    }
});

// Initialize analytics if consent exists
initAnalytics();
```
