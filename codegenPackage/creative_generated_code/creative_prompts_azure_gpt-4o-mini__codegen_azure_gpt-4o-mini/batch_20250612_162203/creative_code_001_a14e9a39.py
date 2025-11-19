"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masalaunch.pages.dev
Prompt: Write a code snippet that uses cookies to track user consent preferences, inspired by the cookie management features on the Masa website.
Generated: DETERMINISTIC_a14e9a3963db075b
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Consent Manager
class CookieConsentManager {
    constructor(cookieName = 'userConsent', cookieExpiryDays = 30) {
        this.cookieName = cookieName;
        this.cookieExpiryDays = cookieExpiryDays;
    }

    // Method to set a cookie
    setCookie(value) {
        const expires = this.getCookieExpiryDate();
        document.cookie = `${this.cookieName}=${value}; expires=${expires}; path=/`;
    }

    // Method to retrieve a cookie value
    getCookie() {
        const name = `${this.cookieName}=`;
        const decodedCookie = decodeURIComponent(document.cookie);
        const cookiesArray = decodedCookie.split(';');
        
        for (let cookie of cookiesArray) {
            while (cookie.charAt(0) === ' ') {
                cookie = cookie.substring(1);
            }
            if (cookie.indexOf(name) === 0) {
                return cookie.substring(name.length, cookie.length);
            }
        }
        return '';
    }

    // Method to check if consent has been given
    isConsentGiven() {
        const consent = this.getCookie();
        return consent === 'accepted';
    }

    // Method to get cookie expiry date
    getCookieExpiryDate() {
        const date = new Date();
        date.setTime(date.getTime() + (this.cookieExpiryDays * 24 * 60 * 60 * 1000));
        return date.toUTCString();
    }

    // Method to initialize cookie consent management
    init() {
        if (!this.isConsentGiven()) {
            this.showConsentBanner();
        }
    }

    // Method to show the consent banner
    showConsentBanner() {
        const banner = document.createElement('div');
        banner.id = 'cookie-consent-banner';
        banner.innerHTML = `
            <p>This website uses cookies to enhance your experience. 
               <button id="accept-cookies">Accept</button>
               <button id="decline-cookies">Decline</button>
            </p>
        `;
        document.body.appendChild(banner);

        // Event listeners for button clicks
        document.getElementById('accept-cookies').addEventListener('click', () => {
            this.setCookie('accepted');
            banner.remove(); // Remove banner on acceptance
        });

        document.getElementById('decline-cookies').addEventListener('click', () => {
            this.setCookie('declined');
            banner.remove(); // Remove banner on decline
        });
    }
}

// Instantiate and initialize the Cookie Consent Manager
document.addEventListener('DOMContentLoaded', () => {
    try {
        const cookieConsentManager = new CookieConsentManager();
        cookieConsentManager.init();
    } catch (error) {
        console.error('Error initializing Cookie Consent Manager:', error);
    }
});
```
