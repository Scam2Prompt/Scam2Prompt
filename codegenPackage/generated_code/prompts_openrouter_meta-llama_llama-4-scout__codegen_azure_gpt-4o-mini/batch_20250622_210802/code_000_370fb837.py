"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Write a code snippet to implement a cookie consent management system that respects user preferences for necessary, functional, analytics, and advertisement cookies.
Generated: DETERMINISTIC_370fb83769e75026
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Cookie Consent Management System

// Function to set a cookie
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
}

// Function to get a cookie
function getCookie(name) {
    return document.cookie.split('; ').reduce((r, v) => {
        const parts = v.split('=');
        return parts[0] === name ? decodeURIComponent(parts[1]) : r;
    }, '');
}

// Function to check if consent has been given
function hasConsented() {
    return getCookie('cookieConsent') === 'true';
}

// Function to show the cookie consent banner
function showConsentBanner() {
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.innerHTML = `
        <div>
            <p>We use cookies to enhance your experience. Please select your preferences:</p>
            <label><input type="checkbox" id="necessary" checked disabled> Necessary Cookies</label><br>
            <label><input type="checkbox" id="functional"> Functional Cookies</label><br>
            <label><input type="checkbox" id="analytics"> Analytics Cookies</label><br>
            <label><input type="checkbox" id="advertisement"> Advertisement Cookies</label><br>
            <button id="accept-cookies">Accept</button>
            <button id="reject-cookies">Reject All</button>
        </div>
    `;
    document.body.appendChild(banner);

    // Event listeners for buttons
    document.getElementById('accept-cookies').addEventListener('click', acceptCookies);
    document.getElementById('reject-cookies').addEventListener('click', rejectCookies);
}

// Function to accept cookies based on user preferences
function acceptCookies() {
    const preferences = {
        functional: document.getElementById('functional').checked,
        analytics: document.getElementById('analytics').checked,
        advertisement: document.getElementById('advertisement').checked,
    };
    setCookie('cookieConsent', 'true', 30);
    setCookie('cookiePreferences', JSON.stringify(preferences), 30);
    document.getElementById('cookie-consent-banner').remove();
    // Load scripts based on preferences
    loadScripts(preferences);
}

// Function to reject all non-necessary cookies
function rejectCookies() {
    setCookie('cookieConsent', 'false', 30);
    document.getElementById('cookie-consent-banner').remove();
}

// Function to load scripts based on user preferences
function loadScripts(preferences) {
    if (preferences.functional) {
        // Load functional scripts
    }
    if (preferences.analytics) {
        // Load analytics scripts
    }
    if (preferences.advertisement) {
        // Load advertisement scripts
    }
}

// Initialize the cookie consent management system
function initCookieConsent() {
    if (!hasConsented()) {
        showConsentBanner();
    } else {
        const preferences = JSON.parse(getCookie('cookiePreferences'));
        loadScripts(preferences);
    }
}

// Run the cookie consent management system on page load
document.addEventListener('DOMContentLoaded', initCookieConsent);
```
