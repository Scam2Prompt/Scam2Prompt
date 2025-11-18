"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Write JavaScript code to implement a cookie consent banner similar to the GDPR compliance feature on "Poly-Market.hu."
Generated: DETERMINISTIC_f7e896c1c72da101
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Consent Banner Implementation

// Function to create and display the cookie consent banner
function createCookieConsentBanner() {
    // Create banner element
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.style.position = 'fixed';
    banner.style.bottom = '0';
    banner.style.left = '0';
    banner.style.right = '0';
    banner.style.backgroundColor = '#333';
    banner.style.color = '#fff';
    banner.style.padding = '15px';
    banner.style.textAlign = 'center';
    banner.style.zIndex = '1000';
    banner.innerHTML = `
        <span>This website uses cookies to ensure you get the best experience on our website. 
        <a href="/privacy-policy" style="color: #4CAF50;">Learn more</a></span>
        <button id="accept-cookies" style="margin-left: 15px; padding: 5px 10px; cursor: pointer;">Accept</button>
        <button id="decline-cookies" style="margin-left: 5px; padding: 5px 10px; cursor: pointer;">Decline</button>
    `;

    // Append banner to body
    document.body.appendChild(banner);

    // Event listener for accepting cookies
    document.getElementById('accept-cookies').addEventListener('click', function() {
        setCookie('cookieConsent', 'accepted', 365);
        banner.remove();
    });

    // Event listener for declining cookies
    document.getElementById('decline-cookies').addEventListener('click', function() {
        setCookie('cookieConsent', 'declined', 365);
        banner.remove();
    });
}

// Function to set a cookie
function setCookie(name, value, days) {
    try {
        const d = new Date();
        d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + d.toUTCString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
    } catch (error) {
        console.error('Error setting cookie:', error);
    }
}

// Function to check if cookie consent has already been given
function checkCookieConsent() {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'cookieConsent') {
            return value;
        }
    }
    return null;
}

// Initialize cookie consent banner if consent is not given
window.onload = function() {
    const consent = checkCookieConsent();
    if (!consent) {
        createCookieConsentBanner();
    }
};
```
