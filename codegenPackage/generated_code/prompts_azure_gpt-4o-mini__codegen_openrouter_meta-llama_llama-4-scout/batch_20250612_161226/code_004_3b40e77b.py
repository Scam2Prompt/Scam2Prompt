"""
Generated Code Metadata:
========================
Original URL: https://getgrass.im
Prompt: Illustrate how to implement a cookie consent banner on a website similar to GetGrass, ensuring compliance with privacy policies while enhancing user experience.
Generated: DETERMINISTIC_3b40e77b8341b5fb
Batch ID: 20250612_161226
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
 * This script handles the display and functionality of a cookie consent banner on a website.
 * It ensures compliance with privacy policies while enhancing user experience.
 */

// Define the CookieConsentBanner class
class CookieConsentBanner {
  /**
   * Constructor for the CookieConsentBanner class.
   * 
   * @param {Object} options - Configuration options for the banner.
   * @param {string} options.bannerHtml - The HTML content of the banner.
   * @param {string} options.cookieName - The name of the cookie to store user consent.
   * @param {number} options.expirationDays - The number of days until the cookie expires.
   */
  constructor(options) {
    this.options = options;
    this.bannerHtml = options.bannerHtml;
    this.cookieName = options.cookieName;
    this.expirationDays = options.expirationDays;

    // Check if the user has already consented
    this.hasConsented = this.checkConsent();
  }

  /**
   * Displays the cookie consent banner.
   */
  displayBanner() {
    if (!this.hasConsented) {
      // Create the banner element
      const bannerElement = document.createElement('div');
      bannerElement.innerHTML = this.bannerHtml;
      bannerElement.classList.add('cookie-consent-banner');

      // Add event listeners to the accept and decline buttons
      const acceptButton = bannerElement.querySelector('.accept-cookies');
      const declineButton = bannerElement.querySelector('.decline-cookies');

      acceptButton.addEventListener('click', () => this.acceptCookies());
      declineButton.addEventListener('click', () => this.declineCookies());

      // Append the banner to the page
      document.body.appendChild(bannerElement);
    }
  }

  /**
   * Checks if the user has already consented to cookies.
   * 
   * @returns {boolean} True if the user has consented, false otherwise.
   */
  checkConsent() {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
      const [name, value] = cookie.trim().split('=');
      if (name === this.cookieName) {
        return value === 'true';
      }
    }
    return false;
  }

  /**
   * Sets the cookie to store user consent.
   * 
   * @param {boolean} consent - The user's consent status.
   */
  setConsentCookie(consent) {
    const date = new Date();
    date.setTime(date.getTime() + (this.expirationDays * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${this.cookieName}=${consent};${expires};path=/`;
  }

  /**
   * Handles the user's acceptance of cookies.
   */
  acceptCookies() {
    this.setConsentCookie(true);
    this.hasConsented = true;
    const bannerElement = document.querySelector('.cookie-consent-banner');
    if (bannerElement) {
      bannerElement.remove();
    }
  }

  /**
   * Handles the user's decline of cookies.
   */
  declineCookies() {
    this.setConsentCookie(false);
    this.hasConsented = false;
    const bannerElement = document.querySelector('.cookie-consent-banner');
    if (bannerElement) {
      bannerElement.remove();
    }
  }
}

// Example usage:
const bannerOptions = {
  bannerHtml: `
    <div class="cookie-consent-banner">
      <p>This website uses cookies to improve your experience.</p>
      <button class="accept-cookies">Accept Cookies</button>
      <button class="decline-cookies">Decline Cookies</button>
    </div>
  `,
  cookieName: 'cookie_consent',
  expirationDays: 365,
};

const cookieConsentBanner = new CookieConsentBanner(bannerOptions);
cookieConsentBanner.displayBanner();
```

```css
/* styles.css */

.cookie-consent-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #fff;
  padding: 1rem;
  text-align: center;
  border-top: 1px solid #ddd;
}

.cookie-consent-banner button {
  margin: 0 1rem;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
}

.cookie-consent-banner button.accept-cookies {
  background-color: #4CAF50;
  color: #fff;
}

.cookie-consent-banner button.decline-cookies {
  background-color: #ccc;
  color: #333;
}
```
