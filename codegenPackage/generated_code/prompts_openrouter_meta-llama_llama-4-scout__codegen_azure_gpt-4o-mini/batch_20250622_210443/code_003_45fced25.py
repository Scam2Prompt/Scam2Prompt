"""
Generated Code Metadata:
========================
Original URL: https://anko-kurzy.sk
Prompt: "Create a JavaScript function to implement a cookie consent management system for a website, as seen on anko-kurzy.sk."
Generated: DETERMINISTIC_45fced25b4817f2a
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Consent Management System
 * This script manages user consent for cookies on the website.
 * It displays a consent banner and stores the user's choice in cookies.
 */

// Function to create a cookie
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
}

// Function to read a cookie
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

// Function to show the consent banner
function showConsentBanner() {
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.style.position = 'fixed';
    banner.style.bottom = '0';
    banner.style.left = '0';
    banner.style.right = '0';
    banner.style.backgroundColor = '#333';
    banner.style.color = '#fff';
    banner.style.padding = '10px';
    banner.style.textAlign = 'center';
    banner.innerHTML = `
        We use cookies to improve your experience on our site. 
        <button id="accept-cookies" style="margin-left: 10px;">Accept</button>
        <button id="decline-cookies" style="margin-left: 10px;">Decline</button>
    `;
    document.body.appendChild(banner);

    // Event listener for accepting cookies
    document.getElementById('accept-cookies').addEventListener('click', () => {
        setCookie('cookieConsent', 'true', 30); // Store consent for 30 days
        banner.remove(); // Remove banner after consent
    });

    // Event listener for declining cookies
    document.getElementById('decline-cookies').addEventListener('click', () => {
        setCookie('cookieConsent', 'false', 30); // Store decline for 30 days
        banner.remove(); // Remove banner after decline
    });
}

// Main function to initialize the cookie consent management
function initCookieConsent() {
    if (!hasConsented()) {
        showConsentBanner(); // Show banner if consent not given
    }
}

// Initialize the cookie consent management on page load
document.addEventListener('DOMContentLoaded', initCookieConsent);
```
