"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-lido-7fd.pages.dev
Prompt: Provide a JavaScript snippet to enable cookies for collecting anonymous site visitation data, as described in the "Cookies" section of the webpage.
Generated: DETERMINISTIC_ccab2be62dfef44f
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie consent management for collecting anonymous site visitation data

// Function to set a cookie
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
}

// Function to get a cookie value by its name
function getCookie(name) {
    return document.cookie.split('; ').reduce((r, c) => {
        const [key, ...v] = c.split('=');
        return key === name ? decodeURIComponent(v.join('=')) : r;
    }, '');
}

// Function to check if the user has already accepted cookies
function hasAcceptedCookies() {
    return getCookie('cookieConsent') === 'true';
}

// Function to show the cookie consent banner
function showCookieConsentBanner() {
    const banner = document.createElement('div');
    banner.id = 'cookie-banner';
    banner.innerHTML = `
        <p>This website uses cookies to collect anonymous visitation data. 
        <button id="accept-cookies">I Accept</button>
        <button id="decline-cookies">I Decline</button></p>
    `;
    banner.style.position = 'fixed';
    banner.style.bottom = '0';
    banner.style.width = '100%';
    banner.style.backgroundColor = '#333';
    banner.style.color = '#fff';
    banner.style.textAlign = 'center';
    banner.style.padding = '10px';
    document.body.appendChild(banner);

    // Event listeners for button clicks
    document.getElementById('accept-cookies').addEventListener('click', () => {
        setCookie('cookieConsent', 'true', 30); // Set cookie consent for 30 days
        document.body.removeChild(banner); // Remove banner after consent
    });

    document.getElementById('decline-cookies').addEventListener('click', () => {
        setCookie('cookieConsent', 'false', 30); // Set cookie consent as declined for 30 days
        document.body.removeChild(banner); // Remove banner after decline
    });
}

// Main function to initialize cookie consent management
function initCookieConsent() {
    // Check if cookies have already been accepted
    if (!hasAcceptedCookies()) {
        showCookieConsentBanner(); // Show the banner if no consent has been given
    }
}

// Run the initialization function on page load
document.addEventListener('DOMContentLoaded', initCookieConsent);
```
