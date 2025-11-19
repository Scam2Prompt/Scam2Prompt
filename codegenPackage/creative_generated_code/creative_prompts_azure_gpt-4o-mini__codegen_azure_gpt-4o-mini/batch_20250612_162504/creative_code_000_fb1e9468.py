"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opeansea.godaddysites.com
Prompt: Generate a code snippet for a web application that uses cookies to enhance user experience, similar to the approach mentioned on the Opean Sea website.
Generated: DETERMINISTIC_fb1e94688515b578
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie management utility functions
const CookieUtil = {
    // Set a cookie with a specified name, value, and expiration days
    setCookie: function(name, value, days) {
        const expires = days ? `; expires=${new Date(Date.now() + days * 864e5).toUTCString()}` : '';
        document.cookie = `${encodeURIComponent(name)}=${encodeURIComponent(value)}${expires}; path=/`;
    },

    // Get the value of a cookie by name
    getCookie: function(name) {
        return document.cookie.split('; ').reduce((acc, cookie) => {
            const [key, val] = cookie.split('=');
            return key === encodeURIComponent(name) ? decodeURIComponent(val) : acc;
        }, null);
    },

    // Delete a cookie by name
    deleteCookie: function(name) {
        this.setCookie(name, '', -1);
    }
};

// Function to check if a user has previously accepted cookies
function checkCookieConsent() {
    const consent = CookieUtil.getCookie('cookieConsent');
    if (consent) {
        // User has already accepted cookies
        console.log('User has consented to cookies.');
    } else {
        // Prompt the user for cookie consent
        showConsentBanner();
    }
}

// Function to show the cookie consent banner
function showConsentBanner() {
    // Create a banner element
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.innerHTML = `
        <p>This website uses cookies to enhance user experience. 
           <button id="accept-cookies">Accept</button>
           <button id="decline-cookies">Decline</button>
        </p>`;
    document.body.appendChild(banner);

    // Event listener for accepting cookies
    document.getElementById('accept-cookies').addEventListener('click', () => {
        CookieUtil.setCookie('cookieConsent', 'accepted', 30); // Set cookie for 30 days
        banner.remove(); // Remove the banner
        console.log('Cookies accepted.');
    });

    // Event listener for declining cookies
    document.getElementById('decline-cookies').addEventListener('click', () => {
        CookieUtil.setCookie('cookieConsent', 'declined', 30); // Set cookie for 30 days
        banner.remove(); // Remove the banner
        console.log('Cookies declined.');
    });
}

// Initialize cookie consent check on page load
window.onload = function() {
    try {
        checkCookieConsent();
    } catch (error) {
        console.error('Error checking cookie consent:', error);
    }
};
```
