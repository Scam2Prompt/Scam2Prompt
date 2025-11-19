"""
Generated Code Metadata:
========================
Original URL: https://getgrass.im
Prompt: Create a JavaScript function to implement a cookie consent banner on a website, allowing users to opt-out of tracking, as seen on GetGrass's website.
Generated: DETERMINISTIC_a98febe423c90347
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieConsentBanner.js

/**
 * Cookie Consent Banner implementation.
 * 
 * This script creates a cookie consent banner on the website, allowing users to opt-out of tracking.
 */

// Define the CookieConsentBanner class
class CookieConsentBanner {
  /**
   * Constructor.
   * 
   * @param {Object} options - Configuration options.
   * @param {string} options.bannerHtml - HTML template for the banner.
   * @param {string} options.cookieName - Name of the cookie to store user consent.
   * @param {string} options.acceptButtonText - Text for the accept button.
   * @param {string} options.rejectButtonText - Text for the reject button.
   */
  constructor(options) {
    this.options = options;
    this.bannerHtml = options.bannerHtml;
    this.cookieName = options.cookieName;
    this.acceptButtonText = options.acceptButtonText;
    this.rejectButtonText = options.rejectButtonText;

    // Check if the user has already consented or declined
    this.hasConsented = this.hasConsentedToCookies();
  }

  /**
   * Render the cookie consent banner.
   */
  renderBanner() {
    // Create the banner element
    const bannerElement = document.createElement('div');
    bannerElement.innerHTML = this.bannerHtml;

    // Add the accept and reject buttons
    const acceptButton = document.createElement('button');
    acceptButton.textContent = this.acceptButtonText;
    acceptButton.addEventListener('click', () => this.acceptCookies());

    const rejectButton = document.createElement('button');
    rejectButton.textContent = this.rejectButtonText;
    rejectButton.addEventListener('click', () => this.rejectCookies());

    // Append the buttons to the banner
    const buttonsContainer = bannerElement.querySelector('.buttons');
    buttonsContainer.appendChild(acceptButton);
    buttonsContainer.appendChild(rejectButton);

    // Add the banner to the page
    document.body.appendChild(bannerElement);
  }

  /**
   * Check if the user has consented to cookies.
   * 
   * @returns {boolean} True if the user has consented, false otherwise.
   */
  hasConsentedToCookies() {
    const cookieValue = this.getCookie(this.cookieName);
    return cookieValue === 'true';
  }

  /**
   * Get the value of a cookie.
   * 
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
   * Set a cookie.
   * 
   * @param {string} name - Name of the cookie.
   * @param {string} value - Value of the cookie.
   * @param {number} days - Number of days until the cookie expires.
   */
  setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 24 * 60 * 60 * 1000).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
  }

  /**
   * Accept cookies.
   */
  acceptCookies() {
    this.setCookie(this.cookieName, 'true', 365); // 1 year
    this.hideBanner();
  }

  /**
   * Reject cookies.
   */
  rejectCookies() {
    this.setCookie(this.cookieName, 'false', 365); // 1 year
    this.hideBanner();
  }

  /**
   * Hide the cookie consent banner.
   */
  hideBanner() {
    const bannerElement = document.querySelector('.cookie-consent-banner');
    if (bannerElement) {
      bannerElement.remove();
    }
  }

  /**
   * Initialize the cookie consent banner.
   */
  init() {
    if (!this.hasConsented) {
      this.renderBanner();
    }
  }
}

// Example usage:
const cookieConsentBanner = new CookieConsentBanner({
  bannerHtml: `
    <div class="cookie-consent-banner">
      <p>This website uses cookies to improve your experience.</p>
      <div class="buttons"></div>
    </div>
  `,
  cookieName: 'cookie_consent',
  acceptButtonText: 'Accept Cookies',
  rejectButtonText: 'Reject Cookies',
});

cookieConsentBanner.init();
```
