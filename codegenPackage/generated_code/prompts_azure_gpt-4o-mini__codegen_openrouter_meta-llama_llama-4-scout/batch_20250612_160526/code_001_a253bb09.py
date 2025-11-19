"""
Generated Code Metadata:
========================
Original URL: https://hope-exchange.com
Prompt: Write a code snippet to create a cookie consent banner for a website, inspired by the cookie policy mentioned on Hope Exchange.
Generated: DETERMINISTIC_a253bb09d3da5f26
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieConsentBanner.js

class CookieConsentBanner {
  /**
   * Initialize the cookie consent banner.
   * @param {Object} options - Configuration options.
   * @param {string} options.bannerHtml - HTML content for the banner.
   * @param {string} options.cookieName - Name of the cookie to store user consent.
   * @param {number} options.cookieExpirationDays - Number of days until the cookie expires.
   */
  constructor(options) {
    this.options = options;
    this.bannerElement = null;
  }

  /**
   * Create and display the cookie consent banner.
   */
  createBanner() {
    // Check if the banner already exists in the DOM
    if (document.querySelector('#cookie-consent-banner')) {
      return;
    }

    // Create the banner element
    this.bannerElement = document.createElement('div');
    this.bannerElement.id = 'cookie-consent-banner';
    this.bannerElement.innerHTML = this.options.bannerHtml;

    // Add the banner to the page
    document.body.appendChild(this.bannerElement);

    // Add event listeners for accept and decline buttons
    const acceptButton = this.bannerElement.querySelector('.accept-cookies');
    const declineButton = this.bannerElement.querySelector('.decline-cookies');

    if (acceptButton) {
      acceptButton.addEventListener('click', () => this.acceptCookies());
    }

    if (declineButton) {
      declineButton.addEventListener('click', () => this.declineCookies());
    }
  }

  /**
   * Handle user acceptance of cookies.
   */
  acceptCookies() {
    // Set a cookie to store user consent
    this.setCookie(this.options.cookieName, 'true', this.options.cookieExpirationDays);

    // Hide the banner
    this.hideBanner();
  }

  /**
   * Handle user decline of cookies.
   */
  declineCookies() {
    // Set a cookie to store user decline
    this.setCookie(this.options.cookieName, 'false', this.options.cookieExpirationDays);

    // Hide the banner
    this.hideBanner();
  }

  /**
   * Set a cookie with the given name, value, and expiration days.
   * @param {string} name - Name of the cookie.
   * @param {string} value - Value of the cookie.
   * @param {number} expirationDays - Number of days until the cookie expires.
   */
  setCookie(name, value, expirationDays) {
    const date = new Date();
    date.setTime(date.getTime() + (expirationDays * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/`;
  }

  /**
   * Hide the cookie consent banner.
   */
  hideBanner() {
    if (this.bannerElement) {
      this.bannerElement.style.display = 'none';
    }
  }

  /**
   * Check if the user has given consent for cookies.
   * @returns {boolean} True if the user has given consent, false otherwise.
   */
  hasUserGivenConsent() {
    const cookieValue = this.getCookie(this.options.cookieName);
    return cookieValue === 'true';
  }

  /**
   * Get the value of a cookie by name.
   * @param {string} name - Name of the cookie.
   * @returns {string|null} Value of the cookie, or null if not found.
   */
  getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
      const [cookieName, cookieValue] = cookie.trim().split('=');
      if (cookieName === name) {
        return cookieValue;
      }
    }
    return null;
  }
}

// Example usage:
const bannerHtml = `
  <div>
    <p>This website uses cookies to improve your experience.</p>
    <button class="accept-cookies">Accept Cookies</button>
    <button class="decline-cookies">Decline Cookies</button>
  </div>
`;

const cookieConsentBanner = new CookieConsentBanner({
  bannerHtml,
  cookieName: 'cookie_consent',
  cookieExpirationDays: 365,
});

document.addEventListener('DOMContentLoaded', () => {
  cookieConsentBanner.createBanner();

  // Check if the user has given consent
  if (!cookieConsentBanner.hasUserGivenConsent()) {
    // Display the banner if the user has not given consent
    cookieConsentBanner.bannerElement.style.display = 'block';
  }
});
```
