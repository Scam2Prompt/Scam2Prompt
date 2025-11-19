"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudflare-cftc-us25-eqq.pages.dev
Prompt: Write a code snippet to handle JavaScript and cookie settings for a secure connection verification process similar to what is described on namada.foundation.
Generated: DETERMINISTIC_40c52ed8ab09627d
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if the connection is secure
function isSecureConnection() {
    // Check if the current protocol is HTTPS
    return window.location.protocol === 'https:';
}

// Function to get the value of a cookie by name
function getCookie(name) {
    // Prepare a regex to extract the cookie
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    // If the cookie exists, return its value
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null; // Return null if cookie is not found
}

// Function to set a cookie with appropriate options for security
function setCookie(name, value, days) {
    const expires = days ? `; expires=${new Date(Date.now() + days * 864e5).toUTCString()}` : '';
    const secure = isSecureConnection() ? '; secure' : ''; // Set secure flag if on HTTPS
    const SameSite = '; SameSite=Strict'; // Set SameSite attribute for CSRF protection

    // Set the cookie with the specified options
    document.cookie = `${name}=${value || ''}${expires}${secure}${SameSite}; path=/`;
}

// Function to check cookie settings and manage user consent
function manageCookieSettings() {
    // Check if the user has already consented to cookie usage
    const cookieConsent = getCookie('cookieConsent');
    
    // If consent is not given, show a consent banner
    if (!cookieConsent) {
        const consentBanner = document.createElement('div');
        consentBanner.innerHTML = `
            <div id="cookie-consent-banner" style="position: fixed; bottom: 0; width: 100%; background: #333; color: #fff; padding: 15px; text-align: center;">
                This site uses cookies to enhance your experience. 
                <button id="accept-cookies" style="margin-left: 10px;">Accept</button>
            </div>
        `;
        document.body.appendChild(consentBanner);

        // Event listener for the accept button
        document.getElementById('accept-cookies').addEventListener('click', function() {
            setCookie('cookieConsent', 'true', 30); // Set cookie for 30 days
            document.body.removeChild(consentBanner); // Remove the banner after consent
        });
    }
}

// Initialize the cookie management on page load
window.addEventListener('load', manageCookieSettings);

// Error handling for cookie operations
try {
    manageCookieSettings();
} catch (error) {
    console.error('Error managing cookie settings:', error);
}
```
