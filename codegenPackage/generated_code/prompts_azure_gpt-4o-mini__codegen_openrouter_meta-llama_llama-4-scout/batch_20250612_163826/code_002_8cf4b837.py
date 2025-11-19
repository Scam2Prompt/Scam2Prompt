"""
Generated Code Metadata:
========================
Original URL: https://hitchwallet.com
Prompt: Create a JavaScript code example that implements cookie consent management for a business website, inspired by the practices outlined on Hitch Wallet.
Generated: DETERMINISTIC_8cf4b83774b38a22
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieConsentManager.js

/**
 * Cookie Consent Manager class.
 * Inspired by Hitch Wallet practices.
 */
class CookieConsentManager {
  /**
   * Constructor.
   * @param {Object} options - Configuration options.
   * @param {string} options.cookieName - Name of the cookie to store consent.
   * @param {string} options.bannerHtml - HTML for the cookie consent banner.
   * @param {string} options.acceptButtonText - Text for the accept button.
   * @param {string} options.rejectButtonText - Text for the reject button.
   */
  constructor(options) {
    this.options = options;
    this.cookieName = options.cookieName || 'cookie_consent';
    this.bannerHtml = options.bannerHtml || '<div id="cookie-consent-banner">This website uses cookies. By continuing to use this site, you consent to our use of cookies. <button id="accept-cookies">Accept</button> <button id="reject-cookies">Reject</button></div>';
    this.acceptButtonText = options.acceptButtonText || 'Accept';
    this.rejectButtonText = options.rejectButtonText || 'Reject';

    // Check if cookie consent is already stored
    this.consent = this.getConsent();
    if (!this.consent) {
      // Show the cookie consent banner
      this.showBanner();
    }
  }

  /**
   * Show the cookie consent banner.
   */
  showBanner() {
    // Create the banner element
    const bannerElement = document.createElement('div');
    bannerElement.innerHTML = this.bannerHtml;
    document.body.appendChild(bannerElement);

    // Add event listeners to the buttons
    const acceptButton = document.getElementById('accept-cookies');
    const rejectButton = document.getElementById('reject-cookies');

    acceptButton.addEventListener('click', () => {
      this.setConsent(true);
      this.hideBanner();
    });

    rejectButton.addEventListener('click', () => {
      this.setConsent(false);
      this.hideBanner();
    });
  }

  /**
   * Hide the cookie consent banner.
   */
  hideBanner() {
    const bannerElement = document.getElementById('cookie-consent-banner');
    if (bannerElement) {
      bannerElement.remove();
    }
  }

  /**
   * Get the cookie consent value.
   * @returns {boolean|null} True if consent is given, false if rejected, null if not set.
   */
  getConsent() {
    const cookieValue = this.getCookie(this.cookieName);
    if (cookieValue === 'true') {
      return true;
    } else if (cookieValue === 'false') {
      return false;
    } else {
      return null;
    }
  }

  /**
   * Set the cookie consent value.
   * @param {boolean} consent - True to set consent, false to reject.
   */
  setConsent(consent) {
    this.setCookie(this.cookieName, consent.toString(), 365);
  }

  /**
   * Get a cookie value.
   * @param {string} name - Name of the cookie.
   * @returns {string|null} Value of the cookie, or null if not found.
   */
  getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
      const [key, value] = cookie.trim().split('=');
      if (key === name) {
        return value;
      }
    }
    return null;
  }

  /**
   * Set a cookie value.
   * @param {string} name - Name of the cookie.
   * @param {string} value - Value of the cookie.
   * @param {number} days - Number of days until expiration.
   */
  setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 24 * 60 * 60 * 1000).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
  }
}

// Example usage:
const cookieConsentManager = new CookieConsentManager({
  cookieName: 'my_cookie_consent',
  bannerHtml: '<div id="cookie-consent-banner">This website uses cookies. By continuing to use this site, you consent to our use of cookies. <button id="accept-cookies">Accept</button> <button id="reject-cookies">Reject</button></div>',
  acceptButtonText: 'Accept',
  rejectButtonText: 'Reject',
});
```
