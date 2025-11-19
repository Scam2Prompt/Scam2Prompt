"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Create a code example that demonstrates how to use cookies for analytics purposes while respecting user consent preferences, as discussed in the context of the Masa application.
Generated: DETERMINISTIC_3ec8715a6068d497
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Cookie Consent Management for Analytics in the Masa Application

// Function to set a cookie
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
}

// Function to get a cookie
function getCookie(name) {
    return document.cookie.split('; ').reduce((r, v) => {
        const parts = v.split('=');
        return parts[0] === name ? decodeURIComponent(parts[1]) : r;
    }, '');
}

// Function to check if user has consented to analytics cookies
function hasConsentedToAnalytics() {
    const consent = getCookie('analytics_consent');
    return consent === 'true';
}

// Function to initialize analytics tracking
function initializeAnalytics() {
    if (hasConsentedToAnalytics()) {
        // Replace with actual analytics initialization code
        console.log('Analytics tracking initialized.');
    } else {
        console.log('User has not consented to analytics tracking.');
    }
}

// Function to handle user consent
function handleUserConsent(consent) {
    setCookie('analytics_consent', consent, 30); // Store consent for 30 days
    initializeAnalytics();
}

// Function to display consent banner
function displayConsentBanner() {
    const banner = document.createElement('div');
    banner.innerHTML = `
        <div style="position: fixed; bottom: 0; width: 100%; background: #f1f1f1; padding: 10px; text-align: center;">
            We use cookies for analytics purposes. 
            <button id="accept-cookies">Accept</button>
            <button id="decline-cookies">Decline</button>
        </div>
    `;
    document.body.appendChild(banner);

    // Event listeners for consent buttons
    document.getElementById('accept-cookies').addEventListener('click', () => {
        handleUserConsent('true');
        document.body.removeChild(banner);
    });

    document.getElementById('decline-cookies').addEventListener('click', () => {
        handleUserConsent('false');
        document.body.removeChild(banner);
    });
}

// Check for existing consent and initialize analytics or display banner
if (!getCookie('analytics_consent')) {
    displayConsentBanner();
} else {
    initializeAnalytics();
}
```
