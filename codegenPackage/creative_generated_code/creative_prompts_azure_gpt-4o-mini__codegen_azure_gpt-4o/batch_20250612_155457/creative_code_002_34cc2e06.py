"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sensibleoptimism.com
Prompt: Create a JavaScript function that tracks user consent for cookies, referencing the cookie policy approach seen on Sensible Optimism.
Generated: DETERMINISTIC_34cc2e06e266e5cc
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to manage and track user consent for cookies.
 * Implements a cookie consent policy for compliance and user experience.
 */

// Function to create and insert the cookie consent banner
function displayCookieConsentBanner() {
    // Check if user has already given consent
    if (getCookie('cookieConsent') === 'true') {
        return; // No need to display the banner
    }

    // Create banner elements
    const banner = document.createElement('div');
    banner.id = 'cookieConsentBanner';
    banner.style.cssText = `
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f9f9f9;
        color: #333;
        padding: 15px;
        box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
        text-align: center;
        z-index: 1000;
    `;

    const message = document.createElement('span');
    message.textContent = 'We use cookies to enhance your experience. By continuing to use our site, you consent to our cookie policy.';

    const acceptButton = document.createElement('button');
    acceptButton.textContent = 'Accept';
    acceptButton.style.cssText = `
        margin-left: 10px;
        padding: 5px 10px;
        background-color: #4CAF50;
        color: #fff;
        border: none;
        border-radius: 3px;
        cursor: pointer;
    `;

    // Add event listener for the accept button
    acceptButton.addEventListener('click', () => {
        setCookie('cookieConsent', 'true', 365); // Set consent for 1 year
        document.body.removeChild(banner); // Remove banner
    });

    // Append elements to banner
    banner.appendChild(message);
    banner.appendChild(acceptButton);

    // Add banner to the page
    document.body.appendChild(banner);
}

/**
 * Function to set a cookie in the browser
 * @param {string} name - The name of the cookie
 * @param {string} value - The value of the cookie
 * @param {number} days - Number of days until the cookie expires
 */
function setCookie(name, value, days) {
    try {
        const date = new Date();
        date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000); // Convert days to milliseconds
        const expires = `expires=${date.toUTCString()}`;
        document.cookie = `${name}=${value}; ${expires}; path=/`;
    } catch (error) {
        console.error('Error setting cookie:', error);
    }
}

/**
 * Function to get the value of a cookie
 * @param {string} name - The name of the cookie to retrieve
 * @returns {string|null} - The value of the cookie or null if not found
 */
function getCookie(name) {
    try {
        const nameEQ = `${name}=`;
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(nameEQ)) {
                return cookie.substring(nameEQ.length);
            }
        }
    } catch (error) {
        console.error('Error retrieving cookie:', error);
    }
    return null; // Return null if cookie not found
}

// Initialize the cookie consent banner on page load
document.addEventListener('DOMContentLoaded', displayCookieConsentBanner);
```
