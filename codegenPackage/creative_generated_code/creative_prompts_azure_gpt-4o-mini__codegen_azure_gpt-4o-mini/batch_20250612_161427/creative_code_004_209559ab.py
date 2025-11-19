"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghozallli.pages.dev
Prompt: Explain how to set cookie preferences in a web app that features NFTs and memecoins, as outlined on Ghozali's site.
Generated: DETERMINISTIC_209559ab45f95458
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Preferences Management for NFT and Memecoin Web Application

// Utility function to set a cookie
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
}

// Utility function to get a cookie by name
function getCookie(name) {
    return document.cookie.split('; ').reduce((r, v) => {
        const parts = v.split('=');
        return parts[0] === name ? decodeURIComponent(parts[1]) : r
    }, '');
}

// Utility function to delete a cookie
function deleteCookie(name) {
    setCookie(name, '', -1);
}

// Function to initialize cookie preferences
function initCookiePreferences() {
    // Check if cookie preferences have already been set
    const cookieConsent = getCookie('cookieConsent');
    
    // If the cookie preference is not set, show consent banner
    if (!cookieConsent) {
        showConsentBanner();
    }
}

// Function to show the cookie consent banner
function showConsentBanner() {
    const banner = document.createElement('div');
    banner.id = 'cookie-banner';
    banner.innerHTML = `
        <p>We use cookies to improve your experience on our site. 
        By clicking "Accept", you consent to our cookie policy.</p>
        <button id="accept-cookies">Accept</button>
        <button id="decline-cookies">Decline</button>
    `;
    document.body.appendChild(banner);
    
    document.getElementById('accept-cookies').onclick = () => {
        setCookie('cookieConsent', 'accepted', 30); // Set cookie for 30 days
        document.body.removeChild(banner); // Remove banner
    };

    document.getElementById('decline-cookies').onclick = () => {
        setCookie('cookieConsent', 'declined', 30); // Set cookie for 30 days
        document.body.removeChild(banner); // Remove banner
    };
}

// Function to check cookie preferences and adjust application behavior
function handleCookiePreferences() {
    const cookieConsent = getCookie('cookieConsent');
    
    if (cookieConsent === 'accepted') {
        // Logic to enable tracking or additional features
        console.log('Cookies accepted: Enabling tracking features.');
    } else if (cookieConsent === 'declined') {
        // Logic to disable tracking or reduce cookie usage
        console.log('Cookies declined: Disabling tracking features.');
    }
}

// Initialize cookie preferences on page load
window.onload = () => {
    try {
        initCookiePreferences();
        handleCookiePreferences();
    } catch (error) {
        console.error('Error initializing cookie preferences:', error);
    }
};
```
