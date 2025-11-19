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
 * CookieConsentManager is a class that manages user consent for cookies.
 */
class CookieConsentManager {
    constructor() {
        this.consentKey = 'cookieConsent';
        this.consentDialogId = 'cookie-consent-dialog';
        this.init();
    }

    /**
     * Initializes the cookie consent manager by checking the current consent status
     * and displaying the consent dialog if necessary.
     */
    init() {
        const consent = this.getConsent();
        if (consent === null) {
            this.showConsentDialog();
        }
    }

    /**
     * Shows the cookie consent dialog to the user.
     */
    showConsentDialog() {
        const dialog = document.getElementById(this.consentDialogId);
        if (dialog) {
            dialog.style.display = 'block';
            const acceptButton = dialog.querySelector('.accept-cookies');
            const rejectButton = dialog.querySelector('.reject-cookies');

            if (acceptButton) {
                acceptButton.addEventListener('click', () => this.acceptCookies());
            }

            if (rejectButton) {
                rejectButton.addEventListener('click', () => this.rejectCookies());
            }
        } else {
            console.error('Consent dialog element not found: ' + this.consentDialogId);
        }
    }

    /**
     * Accepts cookies and saves the consent status in a cookie.
     */
    acceptCookies() {
        this.setConsent(true);
        this.hideConsentDialog();
    }

    /**
     * Rejects cookies and saves the consent status in a cookie.
     */
    rejectCookies() {
        this.setConsent(false);
        this.hideConsentDialog();
    }

    /**
     * Hides the cookie consent dialog.
     */
    hideConsentDialog() {
        const dialog = document.getElementById(this.consentDialogId);
        if (dialog) {
            dialog.style.display = 'none';
        }
    }

    /**
     * Sets the user's cookie consent status.
     * @param {boolean} consent - The user's consent status.
     */
    setConsent(consent) {
        const expires = new Date();
        expires.setFullYear(expires.getFullYear() + 1); // Set cookie to expire in 1 year
        document.cookie = `${this.consentKey}=${consent}; expires=${expires.toUTCString()}; path=/;`;
    }

    /**
     * Retrieves the user's cookie consent status.
     * @returns {boolean|null} - Returns true if consent is given, false if rejected, or null if not set.
     */
    getConsent() {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const [key, value] = cookie.trim().split('=');
            if (key === this.consentKey) {
                return value === 'true' ? true : false;
            }
        }
        return null; // Consent not set
    }
}

// Instantiate the CookieConsentManager on page load.
document.addEventListener('DOMContentLoaded', () => {
    new CookieConsentManager();
});
```

```html
<!-- Example of HTML structure for the cookie consent dialog -->
<div id="cookie-consent-dialog" style="display:none;">
    <p>We use cookies to improve your experience. Do you accept our cookie policy?</p>
    <button class="accept-cookies">Accept</button>
    <button class="reject-cookies">Reject</button>
</div>
```
