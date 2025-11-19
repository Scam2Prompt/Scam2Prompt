"""
Generated Code Metadata:
========================
Original URL: https://activesport.cz
Prompt: Write a script to integrate cookie consent management into an e-commerce website, referencing the detailed cookie policy implementation on ActiveSport.cz.
Generated: DETERMINISTIC_3ca24325c04bead3
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// cookieConsent.js

/**
 * Cookie Consent Management Script
 * 
 * This script integrates cookie consent management into an e-commerce website.
 * It follows the implementation guidelines of ActiveSport.cz.
 */

// Define the CookieConsent class
class CookieConsent {
  /**
   * Constructor
   * 
   * Initializes the cookie consent management system.
   * 
   * @param {object} options - Configuration options
   * @param {string} options.cookieName - Name of the cookie to store consent
   * @param {string} options.cookieDomain - Domain to set the cookie for
   * @param {number} options.expirationDays - Number of days until the cookie expires
   */
  constructor(options) {
    this.options = options;
    this.consent = this.getConsent();
  }

  /**
   * Get the current consent status
   * 
   * Retrieves the current consent status from the cookie.
   * 
   * @returns {boolean} True if consent is given, false otherwise
   */
  getConsent() {
    const cookie = this.getCookie(this.options.cookieName);
    return cookie ? cookie === 'true' : false;
  }

  /**
   * Set the consent status
   * 
   * Sets the consent status in the cookie.
   * 
   * @param {boolean} consent - New consent status
   */
  setConsent(consent) {
    this.consent = consent;
    this.setCookie(this.options.cookieName, consent.toString(), this.options.expirationDays);
  }

  /**
   * Get a cookie by name
   * 
   * Retrieves a cookie by its name.
   * 
   * @param {string} name - Name of the cookie
   * @returns {string|null} Value of the cookie or null if not found
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
   * Set a cookie
   * 
   * Sets a cookie with the given name, value, and expiration days.
   * 
   * @param {string} name - Name of the cookie
   * @param {string} value - Value of the cookie
   * @param {number} days - Number of days until the cookie expires
   */
  setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = `${name}=${value};expires=${date.toUTCString()};domain=${this.options.cookieDomain};path=/`;
  }

  /**
   * Show the cookie consent banner
   * 
   * Displays the cookie consent banner if consent is not given.
   */
  showBanner() {
    if (!this.consent) {
      const banner = document.createElement('div');
      banner.classList.add('cookie-consent-banner');
      banner.innerHTML = `
        <p>This website uses cookies to ensure you get the best experience on our website.</p>
        <button id="accept-cookies">Accept Cookies</button>
        <button id="decline-cookies">Decline Cookies</button>
      `;
      document.body.appendChild(banner);

      document.getElementById('accept-cookies').addEventListener('click', () => {
        this.setConsent(true);
        banner.remove();
      });

      document.getElementById('decline-cookies').addEventListener('click', () => {
        this.setConsent(false);
        banner.remove();
      });
    }
  }
}

// Initialize the cookie consent management system
const cookieConsent = new CookieConsent({
  cookieName: 'cookie_consent',
  cookieDomain: 'example.com',
  expirationDays: 365
});

// Show the cookie consent banner
cookieConsent.showBanner();
```

```css
/* cookieConsent.css */

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

.cookie-consent-banner p {
  margin-bottom: 1em;
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
