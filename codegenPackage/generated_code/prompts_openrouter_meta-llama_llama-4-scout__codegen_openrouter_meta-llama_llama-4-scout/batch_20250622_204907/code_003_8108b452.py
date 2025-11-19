"""
Generated Code Metadata:
========================
Original URL: https://www.lecarolee.it
Prompt: Write a JavaScript function to handle user consent for cookie usage on a website, similar to the implementation on the Le Carolee website.
Generated: DETERMINISTIC_8108b4527f56b897
Batch ID: 20250622_204907
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
 * Manages user consent for cookie usage on a website.
 */
class CookieConsentManager {
  /**
   * Constructs a new CookieConsentManager instance.
   * @param {Object} options - Configuration options.
   * @param {string} options.cookieName - Name of the cookie to store consent.
   * @param {string} options.bannerHtml - HTML to display for the consent banner.
   * @param {function} options.onAccept - Callback function when user accepts cookies.
   * @param {function} options.onDecline - Callback function when user declines cookies.
   */
  constructor(options) {
    this.options = options;
    this.consentCookieName = options.cookieName || 'cookie_consent';
    this.bannerHtml = options.bannerHtml || '';
    this.onAccept = options.onAccept || function() {};
    this.onDecline = options.onDecline || function() {};

    // Initialize the consent banner
    this.initBanner();
  }

  /**
   * Initializes the consent banner.
   */
  initBanner() {
    // Check if the user has already given consent
    if (this.hasConsent()) {
      return;
    }

    // Display the consent banner
    this.displayBanner();

    // Add event listeners to the banner buttons
    document.addEventListener('DOMContentLoaded', () => {
      const acceptButton = document.getElementById('accept-cookies');
      const declineButton = document.getElementById('decline-cookies');

      if (acceptButton) {
        acceptButton.addEventListener('click', () => this.acceptCookies());
      }

      if (declineButton) {
        declineButton.addEventListener('click', () => this.declineCookies());
      }
    });
  }

  /**
   * Displays the consent banner.
   */
  displayBanner() {
    const bannerHtml = this.bannerHtml;
    const body = document.body;

    // Create a container for the banner
    const bannerContainer = document.createElement('div');
    bannerContainer.classList.add('cookie-consent-banner');
    bannerContainer.innerHTML = bannerHtml;

    // Add the banner to the page
    body.insertBefore(bannerContainer, body.firstChild);
  }

  /**
   * Checks if the user has given consent.
   * @returns {boolean} True if the user has given consent, false otherwise.
   */
  hasConsent() {
    const consentCookie = this.getCookie(this.consentCookieName);
    return consentCookie === 'true';
  }

  /**
   * Accepts cookie usage.
   */
  acceptCookies() {
    // Set the consent cookie
    this.setCookie(this.consentCookieName, 'true', 365);

    // Call the onAccept callback
    this.onAccept();

    // Hide the consent banner
    this.hideBanner();
  }

  /**
   * Declines cookie usage.
   */
  declineCookies() {
    // Set the consent cookie to false
    this.setCookie(this.consentCookieName, 'false', 365);

    // Call the onDecline callback
    this.onDecline();

    // Hide the consent banner
    this.hideBanner();
  }

  /**
   * Hides the consent banner.
   */
  hideBanner() {
    const bannerContainer = document.querySelector('.cookie-consent-banner');
    if (bannerContainer) {
      bannerContainer.remove();
    }
  }

  /**
   * Gets a cookie by name.
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
   * Sets a cookie by name and value.
   * @param {string} name - Name of the cookie.
   * @param {string} value - Value of the cookie.
   * @param {number} days - Number of days until the cookie expires.
   */
  setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 24 * 60 * 60 * 1000).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
  }
}

// Example usage:
const cookieConsentManager = new CookieConsentManager({
  cookieName: 'le_carolee_cookie_consent',
  bannerHtml: `
    <p>This website uses cookies to ensure you get the best experience on our website.</p>
    <button id="accept-cookies">Accept Cookies</button>
    <button id="decline-cookies">Decline Cookies</button>
  `,
  onAccept: () => console.log('User accepted cookies'),
  onDecline: () => console.log('User declined cookies'),
});
```
