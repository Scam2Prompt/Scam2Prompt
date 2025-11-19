"""
Generated Code Metadata:
========================
Original URL: https://getgrass.im
Prompt: Create a JavaScript function to implement a cookie consent banner on a website, allowing users to opt-out of tracking, as seen on GetGrass's website.
Generated: DETERMINISTIC_a98febe423c90347
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Cookie Consent Banner Implementation

// Function to create and display the cookie consent banner
function createCookieConsentBanner() {
    // Check if the user has already given consent
    if (getCookie('cookieConsent') === 'true') {
        return; // Consent already given, no need to show the banner
    }

    // Create the banner element
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
    banner.style.zIndex = '1000';

    // Create the message and buttons
    banner.innerHTML = `
        <span>This website uses cookies to enhance the user experience. 
        By clicking "Accept", you consent to our use of cookies. 
        You can opt-out at any time.</span>
        <button id="accept-cookies" style="margin-left: 10px;">Accept</button>
        <button id="decline-cookies" style="margin-left: 10px;">Decline</button>
    `;

    // Append the banner to the body
    document.body.appendChild(banner);

    // Event listener for the accept button
    document.getElementById('accept-cookies').addEventListener('click', function() {
        setCookie('cookieConsent', 'true', 365); // Set consent cookie for 1 year
        document.body.removeChild(banner); // Remove the banner
    });

    // Event listener for the decline button
    document.getElementById('decline-cookies').addEventListener('click', function() {
        setCookie('cookieConsent', 'false', 365); // Set decline cookie for 1 year
        document.body.removeChild(banner); // Remove the banner
    });
}

// Function to set a cookie
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 864e5).toUTCString(); // Calculate expiration date
    document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`; // Set cookie
}

// Function to get a cookie value by name
function getCookie(name) {
    return document.cookie.split('; ').reduce((r, v) => {
        const parts = v.split('=');
        return parts[0] === name ? decodeURIComponent(parts[1]) : r;
    }, ''); // Return cookie value or empty string
}

// Initialize the cookie consent banner on page load
window.onload = function() {
    createCookieConsentBanner(); // Call the function to create the banner
};
```
