"""
Generated Code Metadata:
========================
Original URL: https://plusmedica-shop.ch
Prompt: Generate code to implement a cookie consent management system for an e-commerce site, similar to the cookie settings described on the PlusMedica Shop website.
Generated: DETERMINISTIC_847f8bd33219521c
Batch ID: 20250612_150602
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
 * Cookie Consent Manager class.
 * Manages user cookie consent for an e-commerce site.
 */
class CookieConsentManager {
  /**
   * Constructor.
   * Initializes the cookie consent manager.
   */
  constructor() {
    this.COOKIE_CONSENT_KEY = 'cookie_consent';
    this.COOKIE_SETTINGS_KEY = 'cookie_settings';
    this.DEFAULT_COOKIE_SETTINGS = {
      essential: true,
      functional: false,
      performance: false,
      targeting: false,
    };
  }

  /**
   * Checks if the user has given consent for cookies.
   * @returns {boolean} True if the user has given consent, false otherwise.
   */
  hasConsent() {
    const consent = this.getCookie(this.COOKIE_CONSENT_KEY);
    return consent === 'true';
  }

  /**
   * Gets the user's cookie settings.
   * @returns {object} The user's cookie settings.
   */
  getCookieSettings() {
    const settings = this.getCookie(this.COOKIE_SETTINGS_KEY);
    return settings ? JSON.parse(settings) : this.DEFAULT_COOKIE_SETTINGS;
  }

  /**
   * Sets the user's cookie consent.
   * @param {boolean} consent True if the user has given consent, false otherwise.
   */
  setConsent(consent) {
    this.setCookie(this.COOKIE_CONSENT_KEY, consent.toString(), 365);
  }

  /**
   * Sets the user's cookie settings.
   * @param {object} settings The user's cookie settings.
   */
  setCookieSettings(settings) {
    this.setCookie(this.COOKIE_SETTINGS_KEY, JSON.stringify(settings), 365);
  }

  /**
   * Gets a cookie by name.
   * @param {string} name The name of the cookie.
   * @returns {string} The value of the cookie, or null if not found.
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
   * @param {string} name The name of the cookie.
   * @param {string} value The value of the cookie.
   * @param {number} days The number of days until the cookie expires.
   */
  setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 24 * 60 * 60 * 1000).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
  }

  /**
   * Revokes the user's cookie consent.
   */
  revokeConsent() {
    this.setConsent(false);
    this.setCookieSettings(this.DEFAULT_COOKIE_SETTINGS);
  }
}

// Example usage:
const cookieConsentManager = new CookieConsentManager();

// Check if the user has given consent
if (!cookieConsentManager.hasConsent()) {
  // Show the cookie consent banner
  console.log('Show cookie consent banner');
}

// Get the user's cookie settings
const cookieSettings = cookieConsentManager.getCookieSettings();
console.log(cookieSettings);

// Set the user's cookie consent and settings
cookieConsentManager.setConsent(true);
cookieConsentManager.setCookieSettings({
  essential: true,
  functional: true,
  performance: false,
  targeting: false,
});

// Revoke the user's cookie consent
cookieConsentManager.revokeConsent();
```

```html
<!-- cookie-consent-banner.html -->

<!-- Cookie consent banner -->
<div id="cookie-consent-banner">
  <p>
    We use cookies to ensure you get the best experience on our website. By
    continuing to use this site, you consent to our use of cookies.
  </p>
  <button id="accept-cookies">Accept Cookies</button>
  <button id="decline-cookies">Decline Cookies</button>
  <button id="manage-cookies">Manage Cookies</button>
</div>

<!-- Cookie settings modal -->
<div id="cookie-settings-modal" style="display: none;">
  <h2>Cookie Settings</h2>
  <form>
    <label>
      <input type="checkbox" id="essential-cookies" checked disabled>
      Essential Cookies
    </label>
    <br>
    <label>
      <input type="checkbox" id="functional-cookies">
      Functional Cookies
    </label>
    <br>
    <label>
      <input type="checkbox" id="performance-cookies">
      Performance Cookies
    </label>
    <br>
    <label>
      <input type="checkbox" id="targeting-cookies">
      Targeting Cookies
    </label>
    <br>
    <button id="save-cookie-settings">Save</button>
  </form>
</div>

<script src="cookie-consent-manager.js"></script>
<script>
  const cookieConsentManager = new CookieConsentManager();
  const cookieConsentBanner = document.getElementById('cookie-consent-banner');
  const acceptCookiesButton = document.getElementById('accept-cookies');
  const declineCookiesButton = document.getElementById('decline-cookies');
  const manageCookiesButton = document.getElementById('manage-cookies');
  const cookieSettingsModal = document.getElementById('cookie-settings-modal');
  const saveCookieSettingsButton = document.getElementById('save-cookie-settings');

  acceptCookiesButton.addEventListener('click', () => {
    cookieConsentManager.setConsent(true);
    cookieConsentBanner.style.display = 'none';
  });

  declineCookiesButton.addEventListener('click', () => {
    cookieConsentManager.setConsent(false);
    cookieConsentBanner.style.display = 'none';
  });

  manageCookiesButton.addEventListener('click', () => {
    cookieSettingsModal.style.display = 'block';
  });

  saveCookieSettingsButton.addEventListener('click', (e) => {
    e.preventDefault();
    const cookieSettings = {
      essential: true,
      functional: document.getElementById('functional-cookies').checked,
      performance: document.getElementById('performance-cookies').checked,
      targeting: document.getElementById('targeting-cookies').checked,
    };
    cookieConsentManager.setCookieSettings(cookieSettings);
    cookieSettingsModal.style.display = 'none';
  });
</script>
```
