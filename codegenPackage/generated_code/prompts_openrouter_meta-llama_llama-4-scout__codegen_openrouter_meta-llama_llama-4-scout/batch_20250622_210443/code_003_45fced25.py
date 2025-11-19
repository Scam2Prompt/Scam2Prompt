"""
Generated Code Metadata:
========================
Original URL: https://anko-kurzy.sk
Prompt: "Create a JavaScript function to implement a cookie consent management system for a website, as seen on anko-kurzy.sk."
Generated: DETERMINISTIC_45fced25b4817f2a
Batch ID: 20250622_210443
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
 * Cookie Consent Management System
 * 
 * This script provides a basic implementation of a cookie consent management system.
 * It allows users to grant or deny consent for different types of cookies.
 */

// Define the CookieConsentManager class
class CookieConsentManager {
  /**
   * Constructor
   * 
   * Initializes the cookie consent manager with the given configuration.
   * 
   * @param {Object} config - Configuration object
   * @param {Array} config.cookieTypes - List of cookie types (e.g., 'essential', 'analytics', 'advertising')
   * @param {string} config.cookieName - Name of the cookie to store consent
   */
  constructor(config) {
    this.config = config;
    this.cookieTypes = config.cookieTypes;
    this.cookieName = config.cookieName || 'cookie_consent';
    this.consent = this.getConsent();
  }

  /**
   * Get the current consent status
   * 
   * @returns {Object} - Current consent status
   */
  getConsent() {
    const consentCookie = this.getCookie(this.cookieName);
    return consentCookie ? JSON.parse(consentCookie) : {};
  }

  /**
   * Set the consent status
   * 
   * @param {Object} consent - New consent status
   */
  setConsent(consent) {
    this.consent = consent;
    this.setCookie(this.cookieName, JSON.stringify(consent), 365);
  }

  /**
   * Get the value of a cookie
   * 
   * @param {string} name - Name of the cookie
   * @returns {string} - Value of the cookie
   */
  getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

  /**
   * Set the value of a cookie
   * 
   * @param {string} name - Name of the cookie
   * @param {string} value - Value of the cookie
   * @param {number} days - Expiration in days
   */
  setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`;
  }

  /**
   * Revoke consent for a specific cookie type
   * 
   * @param {string} cookieType - Type of cookie to revoke consent for
   */
  revokeConsent(cookieType) {
    const consent = { ...this.consent };
    delete consent[cookieType];
    this.setConsent(consent);
  }

  /**
   * Grant consent for a specific cookie type
   * 
   * @param {string} cookieType - Type of cookie to grant consent for
   */
  grantConsent(cookieType) {
    const consent = { ...this.consent };
    consent[cookieType] = true;
    this.setConsent(consent);
  }

  /**
   * Check if consent is given for a specific cookie type
   * 
   * @param {string} cookieType - Type of cookie to check
   * @returns {boolean} - True if consent is given, false otherwise
   */
  hasConsent(cookieType) {
    return !!this.consent[cookieType];
  }

  /**
   * Render the cookie consent banner
   */
  renderBanner() {
    const bannerHtml = `
      <div id="cookie-consent-banner">
        <p>This website uses cookies to ensure you get the best experience on our website.</p>
        ${this.cookieTypes.map((type) => `
          <label>
            <input type="checkbox" data-cookie-type="${type}" ${this.hasConsent(type) ? 'checked' : ''}>
            ${type.charAt(0).toUpperCase() + type.slice(1)} cookies
          </label>
        `).join('')}
        <button id="save-consent">Save Consent</button>
      </div>
    `;
    document.body.insertAdjacentHTML('beforeend', bannerHtml);

    const saveConsentButton = document.getElementById('save-consent');
    saveConsentButton.addEventListener('click', () => {
      const checkboxes = document.querySelectorAll('input[data-cookie-type]');
      const consent = {};
      checkboxes.forEach((checkbox) => {
        const cookieType = checkbox.getAttribute('data-cookie-type');
        consent[cookieType] = checkbox.checked;
      });
      this.setConsent(consent);
      document.getElementById('cookie-consent-banner').remove();
    });
  }
}

// Example usage
const config = {
  cookieTypes: ['essential', 'analytics', 'advertising'],
};

const cookieConsentManager = new CookieConsentManager(config);
cookieConsentManager.renderBanner();
```
