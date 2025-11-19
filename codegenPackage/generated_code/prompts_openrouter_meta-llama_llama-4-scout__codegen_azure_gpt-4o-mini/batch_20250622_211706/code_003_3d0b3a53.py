"""
Generated Code Metadata:
========================
Original URL: https://11tesorosibericos.com
Prompt: "Create a JavaScript function to implement a cookie consent banner for an e-commerce website, similar to the one on 11tesorosibericos.com."
Generated: DETERMINISTIC_3d0b3a53fccc00d1
Batch ID: 20250622_211706
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
    // Check if the user has already accepted cookies
    if (getCookie('cookieConsent') === 'accepted') {
        return; // Exit if consent has already been given
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
    banner.style.padding = '15px';
    banner.style.textAlign = 'center';
    banner.style.zIndex = '1000';

    // Create the message
    const message = document.createElement('span');
    message.innerText = 'We use cookies to enhance your experience. By continuing to visit this site, you agree to our use of cookies.';
    banner.appendChild(message);

    // Create the accept button
    const acceptButton = document.createElement('button');
    acceptButton.innerText = 'Accept';
    acceptButton.style.marginLeft = '15px';
    acceptButton.style.padding = '10px 20px';
    acceptButton.style.backgroundColor = '#4CAF50';
    acceptButton.style.color = '#fff';
    acceptButton.style.border = 'none';
    acceptButton.style.cursor = 'pointer';

    // Add event listener to the accept button
    acceptButton.addEventListener('click', function() {
        setCookie('cookieConsent', 'accepted', 365); // Set cookie for 1 year
        document.body.removeChild(banner); // Remove the banner
    });

    // Append the button to the banner
    banner.appendChild(acceptButton);

    // Append the banner to the body
    document.body.appendChild(banner);
}

// Function to set a cookie
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 864e5).toUTCString(); // Calculate expiration date
    document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/'; // Set cookie
}

// Function to get a cookie by name
function getCookie(name) {
    return document.cookie.split('; ').reduce((r, c) => {
        const [key, ...v] = c.split('=');
        return key === name ? decodeURIComponent(v.join('=')) : r;
    }, ''); // Return cookie value or empty string
}

// Initialize the cookie consent banner on page load
window.onload = function() {
    createCookieConsentBanner();
};
```
