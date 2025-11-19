"""
Generated Code Metadata:
========================
Original URL: https://wholygood.com
Prompt: Generate a code snippet that implements cookie consent management for a website, similar to the approach mentioned on wholygood.com.
Generated: DETERMINISTIC_fa78a6f4aa87fe88
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// cookie-consent-manager.js

/**
 * Cookie Consent Manager
 * 
 * This script manages cookie consent for a website. It provides a banner
 * to inform users about cookie usage and allows them to opt-in or opt-out.
 */

// Cookie Consent Manager class
class CookieConsentManager {
  /**
   * Constructor
   * 
   * Initializes the cookie consent manager with the given options.
   * 
   * @param {Object} options - Options for the cookie consent manager
   * @param {String} options.bannerHtml - HTML for the cookie consent banner
   * @param {String} options.cookieName - Name of the cookie to store consent
   * @param {Number} options.expirationDays - Number of days until cookie expires
   */
  constructor(options) {
    this.options = options;
    this.bannerHtml = options.bannerHtml;
    this.cookieName = options.cookieName;
    this.expirationDays = options.expirationDays;

    // Check if cookie consent is already given
    this.hasConsent = this.getCookie(this.cookieName) === 'true';

    // Show banner if no consent is given
    if (!this.hasConsent) {
      this.showBanner();
    }
  }

  /**
   * Show cookie consent banner
   */
  showBanner() {
    // Create banner element
    const bannerElement = document.createElement('div');
    bannerElement.innerHTML = this.bannerHtml;
    bannerElement.classList.add('cookie-consent-banner');

    // Add event listeners to buttons
    const acceptButton = bannerElement.querySelector('.accept-cookies');
    const declineButton = bannerElement.querySelector('.decline-cookies');

    acceptButton.addEventListener('click', () => {
      this.setConsent(true);
      this.hideBanner();
    });

    declineButton.addEventListener('click', () => {
      this.setConsent(false);
      this.hideBanner();
    });

    // Add banner to page
    document.body.appendChild(bannerElement);
  }

  /**
   * Hide cookie consent banner
   */
  hideBanner() {
    const bannerElement = document.querySelector('.cookie-consent-banner');
    if (bannerElement) {
      bannerElement.remove();
    }
  }

  /**
   * Set cookie consent
   * 
   * @param {Boolean} consent - Whether to set consent to true or false
   */
  setConsent(consent) {
    this.hasConsent = consent;
    this.setCookie(this.cookieName, consent.toString(), this.expirationDays);
  }

  /**
   * Get cookie value
   * 
   * @param {String} name - Name of the cookie
   * @returns {String|null} Value of the cookie or null if not found
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
   * Set cookie value
   * 
   * @param {String} name - Name of the cookie
   * @param {String} value - Value of the cookie
   * @param {Number} days - Number of days until cookie expires
   */
  setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/`;
  }
}

// Example usage
const cookieConsentManager = new CookieConsentManager({
  bannerHtml: `
    <div>
      This website uses cookies to improve your experience.
      <button class="accept-cookies">Accept Cookies</button>
      <button class="decline-cookies">Decline Cookies</button>
    </div>
  `,
  cookieName: 'cookie_consent',
  expirationDays: 365,
});
```

```css
/* cookie-consent-banner.css */

.cookie-consent-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #fff;
  border-top: 1px solid #ddd;
  padding: 1em;
  text-align: center;
}

.cookie-consent-banner button {
  margin: 0 1em;
  padding: 0.5em 1em;
  border: none;
  border-radius: 0.25em;
  background-color: #4CAF50;
  color: #fff;
  cursor: pointer;
}

.cookie-consent-banner button:hover {
  background-color: #3e8e41;
}
```
