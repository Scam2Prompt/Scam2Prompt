"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthinsuranceshop.ie
Prompt: Write JavaScript code to display a cookie consent banner on a website, with options to accept all cookies or manage consent for categories like "Performance" and "Advertisement," as described on the Health Insurance Shop site.
Generated: DETERMINISTIC_72ebfd385ce674f8
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CookieConsent.js

// Function to create and display the cookie consent banner
function createCookieConsentBanner() {
    // Check if the consent has already been given
    if (getCookie('cookieConsent')) return;

    // Create banner element
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.style.position = 'fixed';
    banner.style.bottom = '0';
    banner.style.left = '0';
    banner.style.right = '0';
    banner.style.backgroundColor = '#333';
    banner.style.color = '#fff';
    banner.style.padding = '10px';
    banner.style.zIndex = '1000';
    banner.innerHTML = `
        <p>We use cookies to enhance your experience. By clicking "Accept All", you agree to our use of cookies.</p>
        <button id="accept-all" style="margin-right: 10px;">Accept All</button>
        <button id="manage-consent">Manage Consent</button>
    `;

    // Append the banner to the body
    document.body.appendChild(banner);

    // Add event listeners for the buttons
    document.getElementById('accept-all').onclick = () => {
        setCookie('cookieConsent', 'accepted', 30);
        banner.remove();
    };

    document.getElementById('manage-consent').onclick = () => {
        manageCookieCategories();
    };
}

// Function to manage cookie categories
function manageCookieCategories() {
    const categoryModal = document.createElement('div');
    categoryModal.id = 'cookie-category-modal';
    categoryModal.style.position = 'fixed';
    categoryModal.style.top = '50%';
    categoryModal.style.left = '50%';
    categoryModal.style.transform = 'translate(-50%, -50%)';
    categoryModal.style.backgroundColor = '#fff';
    categoryModal.style.padding = '20px';
    categoryModal.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    categoryModal.style.zIndex = '1001';
    categoryModal.innerHTML = `
        <h3>Manage Cookie Consent</h3>
        <label>
            <input type="checkbox" id="performance-cookies" /> Performance Cookies
        </label><br />
        <label>
            <input type="checkbox" id="advertisement-cookies" /> Advertisement Cookies
        </label><br />
        <button id="save-consent">Save Preferences</button>
        <button id="close-modal">Close</button>
    `;

    // Append the modal to the body
    document.body.appendChild(categoryModal);

    // Load previously saved preferences
    loadCookiePreferences();

    // Event listeners for buttons in the modal
    document.getElementById('save-consent').onclick = () => {
        const performanceAccepted = document.getElementById('performance-cookies').checked;
        const advertisementAccepted = document.getElementById('advertisement-cookies').checked;
        setCookie('performanceCookies', performanceAccepted, 30);
        setCookie('advertisementCookies', advertisementAccepted, 30);
        categoryModal.remove();
    };

    document.getElementById('close-modal').onclick = () => {
        categoryModal.remove();
    };
}

// Function to set a cookie
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
}

// Function to get a cookie value
function getCookie(name) {
    return document.cookie.split('; ').reduce((r, current) => {
        const [key, val] = current.split('=');
        return key === name ? decodeURIComponent(val) : r;
    }, '');
}

// Function to load cookie preferences
function loadCookiePreferences() {
    const performanceAccepted = getCookie('performanceCookies') === 'true';
    const advertisementAccepted = getCookie('advertisementCookies') === 'true';

    document.getElementById('performance-cookies').checked = performanceAccepted;
    document.getElementById('advertisement-cookies').checked = advertisementAccepted;
}

// Initialize the cookie consent banner on page load
window.onload = createCookieConsentBanner;
```

**Note**: Include the JavaScript file in your HTML to utilize this cookie consent banner functionality.
