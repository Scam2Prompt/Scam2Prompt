"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-crypto.yivesites.com
Prompt: Write JavaScript code to create a cookie consent banner that complies with the cookie policy described on the Apelbet website, including options for personal, technical, and third-party cookies.
Generated: DETERMINISTIC_750b0afe88357777
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Consent Banner Implementation

// Function to create and show the cookie consent banner
function createCookieConsentBanner() {
    // Check if consent has already been given
    if (getCookie('cookie_consent')) return;

    // Create banner element
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.style.position = 'fixed';
    banner.style.bottom = '20px';
    banner.style.left = '50%';
    banner.style.transform = 'translateX(-50%)';
    banner.style.backgroundColor = '#333';
    banner.style.color = '#fff';
    banner.style.padding = '20px';
    banner.style.borderRadius = '5px';
    banner.style.zIndex = '1000';
    banner.innerHTML = `
        <p>This website uses cookies to ensure you get the best experience. 
        We use personal, technical, and third-party cookies.</p>
        <button id="accept-all">Accept All</button>
        <button id="accept-technical">Accept Technical Cookies</button>
        <button id="reject-all">Reject All</button>
        <button id="preferences">Preferences</button>
    `;

    // Append banner to the body
    document.body.appendChild(banner);

    // Event listeners for each button
    document.getElementById('accept-all').addEventListener('click', () => {
        setCookie('cookie_consent', 'all', 365);
        banner.remove();
    });

    document.getElementById('accept-technical').addEventListener('click', () => {
        setCookie('cookie_consent', 'technical', 365);
        banner.remove();
    });

    document.getElementById('reject-all').addEventListener('click', () => {
        setCookie('cookie_consent', 'none', 365);
        banner.remove();
    });

    document.getElementById('preferences').addEventListener('click', () => {
        // Placeholder for preferences modal
        alert('Opening preferences modal...'); // Replace with actual modal implementation
    });
}

// Function to set a cookie
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
}

// Function to get a cookie by name
function getCookie(name) {
    return document.cookie.split('; ').reduce((r, c) => {
        const [key, val] = c.split('=');
        return key === name ? decodeURIComponent(val) : r;
    }, '');
}

// Call the function to create the cookie consent banner when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', createCookieConsentBanner);
```
