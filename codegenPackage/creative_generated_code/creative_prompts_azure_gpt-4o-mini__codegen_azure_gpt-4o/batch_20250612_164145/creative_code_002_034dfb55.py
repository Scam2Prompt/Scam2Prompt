"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomware.net
Prompt: Write a function in JavaScript that handles user consent for cookies, inspired by the cookie usage policy on phantomware.net.
Generated: DETERMINISTIC_034dfb55bc879077
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Handles user consent for cookies.
 * Displays a cookie consent banner, stores user preference, and applies choices accordingly.
 */

// Immediately invoked function to manage cookie consent
(function manageCookieConsent() {
    // HTML for the cookie consent banner
    const bannerHTML = `
        <div id="cookie-banner" style="position: fixed; bottom: 0; left: 0; right: 0; background: #333; color: #fff; padding: 15px; text-align: center; z-index: 1000;">
            <p style="margin: 0;">We use cookies to enhance your experience. By continuing to visit this site, you accept our cookie policy. 
                <a href="/cookie-policy" style="color: #00f; text-decoration: underline;">Learn More</a>
            </p>
            <button id="accept-cookies" style="margin: 10px; padding: 8px 15px; border: none; background: #4caf50; color: #fff; cursor: pointer;">Accept</button>
            <button id="reject-cookies" style="margin: 10px; padding: 8px 15px; border: none; background: #f44336; color: #fff; cursor: pointer;">Reject</button>
        </div>
    `;

    // Adds the banner to the DOM if user has not made a choice
    const loadBanner = () => {
        if (!getCookie('userConsent')) {
            document.body.insertAdjacentHTML('beforeend', bannerHTML);
            attachEventListeners();
        }
    };

    // Attach event listeners to banner buttons
    const attachEventListeners = () => {
        const acceptButton = document.getElementById('accept-cookies');
        const rejectButton = document.getElementById('reject-cookies');

        if (acceptButton) {
            acceptButton.addEventListener('click', () => handleUserConsent(true));
        }

        if (rejectButton) {
            rejectButton.addEventListener('click', () => handleUserConsent(false));
        }
    };

    // Handle user's decision
    const handleUserConsent = (consentGiven) => {
        setCookie('userConsent', consentGiven ? 'accepted' : 'rejected', 365);
        removeBanner();
        console.log(`Cookie consent has been ${consentGiven ? 'accepted' : 'rejected'}.`);
    };

    // Remove the banner from the DOM
    const removeBanner = () => {
        const banner = document.getElementById('cookie-banner');
        if (banner) {
            banner.remove();
        }
    };

    // Function to set a cookie
    const setCookie = (name, value, days) => {
        try {
            const date = new Date();
            date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
            document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/;`;
        } catch (error) {
            console.error('Error setting cookie:', error);
        }
    };

    // Function to get a cookie by name
    const getCookie = (name) => {
        try {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                const [key, value] = cookie.trim().split('=');
                if (key === name) {
                    return value;
                }
            }
            return null;
        } catch (error) {
            console.error('Error retrieving cookie:', error);
            return null;
        }
    };

    // Load the cookie banner on page load
    document.addEventListener('DOMContentLoaded', loadBanner);
})();
```
