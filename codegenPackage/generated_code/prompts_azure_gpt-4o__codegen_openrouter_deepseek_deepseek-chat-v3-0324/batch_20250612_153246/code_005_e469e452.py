"""
Generated Code Metadata:
========================
Original URL: https://eyemagazine.gr
Prompt: Write JavaScript code to implement cookie settings functionality, similar to the GDPR compliance system used by Eye Magazine.
Generated: DETERMINISTIC_e469e452f6e07b7b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Settings Manager
 * Implements GDPR-compliant cookie consent functionality similar to Eye Magazine
 */

class CookieSettings {
  constructor(options = {}) {
    // Default options
    this.defaults = {
      cookieName: 'cookie_consent',
      cookieExpiryDays: 365,
      cookiePath: '/',
      essentialCookies: ['session', 'security'],
      optionalCookies: {
        analytics: false,
        marketing: false,
        preferences: false
      },
      uiSelectors: {
        banner: '#cookie-banner',
        settingsModal: '#cookie-settings',
        acceptAllBtn: '#accept-all-cookies',
        rejectAllBtn: '#reject-non-essential',
        saveSettingsBtn: '#save-cookie-settings',
        openSettingsBtn: '#open-cookie-settings'
      },
      onAccept: null,
      onReject: null,
      onSave: null
    };

    this.options = { ...this.defaults, ...options };
    this.cookieConsent = this.getConsent();
    this.init();
  }

  /**
   * Initialize the cookie settings manager
   */
  init() {
    this.bindUIElements();
    this.setupEventListeners();

    if (!this.hasConsent()) {
      this.showBanner();
    } else {
      this.applyConsentSettings();
    }
  }

  /**
   * Bind UI elements from options
   */
  bindUIElements() {
    this.elements = {};
    for (const [key, selector] of Object.entries(this.options.uiSelectors)) {
      this.elements[key] = document.querySelector(selector);
    }
  }

  /**
   * Set up event listeners for UI interactions
   */
  setupEventListeners() {
    if (this.elements.acceptAllBtn) {
      this.elements.acceptAllBtn.addEventListener('click', () => this.acceptAll());
    }

    if (this.elements.rejectAllBtn) {
      this.elements.rejectAllBtn.addEventListener('click', () => this.rejectNonEssential());
    }

    if (this.elements.saveSettingsBtn) {
      this.elements.saveSettingsBtn.addEventListener('click', () => this.saveSettings());
    }

    if (this.elements.openSettingsBtn) {
      this.elements.openSettingsBtn.addEventListener('click', () => this.openSettings());
    }
  }

  /**
   * Show the cookie consent banner
   */
  showBanner() {
    if (this.elements.banner) {
      this.elements.banner.style.display = 'block';
    }
  }

  /**
   * Hide the cookie consent banner
   */
  hideBanner() {
    if (this.elements.banner) {
      this.elements.banner.style.display = 'none';
    }
  }

  /**
   * Open the cookie settings modal
   */
  openSettings() {
    if (this.elements.settingsModal) {
      this.elements.settingsModal.style.display = 'block';
    }
  }

  /**
   * Close the cookie settings modal
   */
  closeSettings() {
    if (this.elements.settingsModal) {
      this.elements.settingsModal.style.display = 'none';
    }
  }

  /**
   * Accept all cookie categories
   */
  acceptAll() {
    const consent = {
      essential: true,
      ...Object.fromEntries(
        Object.keys(this.options.optionalCookies).map(key => [key, true])
      ),
      timestamp: new Date().toISOString()
    };

    this.setConsent(consent);
    this.hideBanner();
    this.applyConsentSettings();

    if (typeof this.options.onAccept === 'function') {
      this.options.onAccept(consent);
    }
  }

  /**
   * Reject all non-essential cookies
   */
  rejectNonEssential() {
    const consent = {
      essential: true,
      ...Object.fromEntries(
        Object.keys(this.options.optionalCookies).map(key => [key, false])
      ),
      timestamp: new Date().toISOString()
    };

    this.setConsent(consent);
    this.hideBanner();
    this.applyConsentSettings();

    if (typeof this.options.onReject === 'function') {
      this.options.onReject(consent);
    }
  }

  /**
   * Save custom cookie settings from the modal
   */
  saveSettings() {
    const consent = { essential: true, timestamp: new Date().toISOString() };
    
    for (const cookieType of Object.keys(this.options.optionalCookies)) {
      const checkbox = document.querySelector(`input[name="${cookieType}"]`);
      consent[cookieType] = checkbox ? checkbox.checked : false;
    }

    this.setConsent(consent);
    this.closeSettings();
    this.hideBanner();
    this.applyConsentSettings();

    if (typeof this.options.onSave === 'function') {
      this.options.onSave(consent);
    }
  }

  /**
   * Check if user has given consent
   * @returns {boolean}
   */
  hasConsent() {
    return this.cookieConsent !== null;
  }

  /**
   * Get current consent settings from cookie
   * @returns {Object|null}
   */
  getConsent() {
    const cookieValue = this.getCookie(this.options.cookieName);
    return cookieValue ? JSON.parse(cookieValue) : null;
  }

  /**
   * Set consent settings in cookie
   * @param {Object} consent 
   */
  setConsent(consent) {
    this.cookieConsent = consent;
    const cookieValue = JSON.stringify(consent);
    this.setCookie(
      this.options.cookieName,
      cookieValue,
      this.options.cookieExpiryDays,
      this.options.cookiePath
    );
  }

  /**
   * Apply consent settings to the page
   */
  applyConsentSettings() {
    if (!this.cookieConsent) return;

    // Example: Load analytics scripts if consented
    if (this.cookieConsent.analytics) {
      // Load analytics scripts here
    }

    // Example: Load marketing scripts if consented
    if (this.cookieConsent.marketing) {
      // Load marketing scripts here
    }
  }

  /**
   * Get cookie value by name
   * @param {string} name 
   * @returns {string|null}
   */
  getCookie(name) {
    const cookies = document.cookie.split(';').map(c => c.trim());
    const cookie = cookies.find(c => c.startsWith(`${name}=`));
    return cookie ? decodeURIComponent(cookie.split('=')[1]) : null;
  }

  /**
   * Set cookie
   * @param {string} name 
   * @param {string} value 
   * @param {number} days 
   * @param {string} path 
   */
  setCookie(name, value, days, path = '/') {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${encodeURIComponent(value)};${expires};path=${path};SameSite=Lax`;
  }

  /**
   * Delete cookie
   * @param {string} name 
   * @param {string} path 
   */
  deleteCookie(name, path = '/') {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=${path}`;
  }
}

// Example initialization
document.addEventListener('DOMContentLoaded', () => {
  const cookieSettings = new CookieSettings({
    optionalCookies: {
      analytics: false,
      marketing: false,
      preferences: true
    },
    onAccept: (consent) => {
      console.log('All cookies accepted:', consent);
    },
    onReject: (consent) => {
      console.log('Non-essential cookies rejected:', consent);
    },
    onSave: (consent) => {
      console.log('Custom cookie settings saved:', consent);
    }
  });
});
```
