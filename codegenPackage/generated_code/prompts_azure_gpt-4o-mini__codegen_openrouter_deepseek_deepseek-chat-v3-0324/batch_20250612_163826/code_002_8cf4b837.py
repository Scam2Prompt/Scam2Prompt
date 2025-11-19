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
/**
 * Cookie Consent Manager
 * Implements GDPR-compliant cookie consent management for a business website.
 * Inspired by Hitch Wallet's practices.
 */

class CookieConsentManager {
  /**
   * Initialize the cookie consent manager
   * @param {Object} options - Configuration options
   * @param {string} options.cookieName - Name of the consent cookie
   * @param {number} options.cookieExpiryDays - Cookie expiration in days
   * @param {string} options.bannerId - ID of the consent banner element
   * @param {string} options.acceptBtnId - ID of the accept button
   * @param {string} options.settingsBtnId - ID of the settings button
   * @param {string} options.settingsModalId - ID of the settings modal
   * @param {string} options.saveSettingsBtnId - ID of the save settings button
   */
  constructor(options) {
    this.cookieName = options.cookieName || 'cookie_consent';
    this.cookieExpiryDays = options.cookieExpiryDays || 365;
    this.bannerId = options.bannerId || 'cookie-consent-banner';
    this.acceptBtnId = options.acceptBtnId || 'cookie-accept-btn';
    this.settingsBtnId = options.settingsBtnId || 'cookie-settings-btn';
    this.settingsModalId = options.settingsModalId || 'cookie-settings-modal';
    this.saveSettingsBtnId = options.saveSettingsBtnId || 'cookie-save-settings-btn';
    this.cookieCategories = {
      necessary: true,
      analytics: false,
      marketing: false,
      preferences: false
    };

    this.init();
  }

  /**
   * Initialize the consent manager
   */
  init() {
    this.bindEvents();
    this.checkConsent();
  }

  /**
   * Bind DOM events
   */
  bindEvents() {
    document.addEventListener('DOMContentLoaded', () => {
      const acceptBtn = document.getElementById(this.acceptBtnId);
      const settingsBtn = document.getElementById(this.settingsBtnId);
      const saveSettingsBtn = document.getElementById(this.saveSettingsBtnId);

      if (acceptBtn) {
        acceptBtn.addEventListener('click', () => this.acceptAll());
      }

      if (settingsBtn) {
        settingsBtn.addEventListener('click', () => this.showSettings());
      }

      if (saveSettingsBtn) {
        saveSettingsBtn.addEventListener('click', () => this.saveSettings());
      }
    });
  }

  /**
   * Check if consent has been given
   */
  checkConsent() {
    const consentCookie = this.getCookie(this.cookieName);
    
    if (!consentCookie) {
      this.showBanner();
    } else {
      try {
        const consentData = JSON.parse(consentCookie);
        this.cookieCategories = {...this.cookieCategories, ...consentData};
        this.applyConsent();
      } catch (e) {
        console.error('Error parsing consent cookie:', e);
        this.showBanner();
      }
    }
  }

  /**
   * Show the consent banner
   */
  showBanner() {
    const banner = document.getElementById(this.bannerId);
    if (banner) {
      banner.style.display = 'block';
    }
  }

  /**
   * Hide the consent banner
   */
  hideBanner() {
    const banner = document.getElementById(this.bannerId);
    if (banner) {
      banner.style.display = 'none';
    }
  }

  /**
   * Show the settings modal
   */
  showSettings() {
    const modal = document.getElementById(this.settingsModalId);
    if (modal) {
      modal.style.display = 'block';
      this.populateSettingsForm();
    }
  }

  /**
   * Hide the settings modal
   */
  hideSettings() {
    const modal = document.getElementById(this.settingsModalId);
    if (modal) {
      modal.style.display = 'none';
    }
  }

  /**
   * Populate the settings form with current values
   */
  populateSettingsForm() {
    Object.keys(this.cookieCategories).forEach(category => {
      const element = document.getElementById(`cookie-${category}`);
      if (element) {
        element.checked = this.cookieCategories[category];
      }
    });
  }

  /**
   * Accept all cookie categories
   */
  acceptAll() {
    Object.keys(this.cookieCategories).forEach(category => {
      this.cookieCategories[category] = true;
    });
    this.setConsentCookie();
    this.hideBanner();
    this.applyConsent();
  }

  /**
   * Save user settings from the modal
   */
  saveSettings() {
    Object.keys(this.cookieCategories).forEach(category => {
      const element = document.getElementById(`cookie-${category}`);
      if (element) {
        this.cookieCategories[category] = element.checked;
      }
    });
    this.setConsentCookie();
    this.hideSettings();
    this.hideBanner();
    this.applyConsent();
  }

  /**
   * Set the consent cookie
   */
  setConsentCookie() {
    const expiryDate = new Date();
    expiryDate.setDate(expiryDate.getDate() + this.cookieExpiryDays);
    
    const cookieValue = JSON.stringify(this.cookieCategories);
    document.cookie = `${this.cookieName}=${cookieValue}; expires=${expiryDate.toUTCString()}; path=/; SameSite=Lax; Secure`;
  }

  /**
   * Get cookie value by name
   * @param {string} name - Cookie name
   * @returns {string|null} Cookie value or null if not found
   */
  getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
  }

  /**
   * Apply consent preferences by category
   */
  applyConsent() {
    // Implement category-specific logic here
    // Example: Load analytics scripts if analytics is enabled
    if (this.cookieCategories.analytics) {
      this.loadAnalytics();
    }
    
    if (this.cookieCategories.marketing) {
      this.loadMarketing();
    }
  }

  /**
   * Example: Load analytics scripts
   */
  loadAnalytics() {
    // Implementation for loading analytics scripts
    console.log('Loading analytics scripts...');
  }

  /**
   * Example: Load marketing scripts
   */
  loadMarketing() {
    // Implementation for loading marketing scripts
    console.log('Loading marketing scripts...');
  }
}

// Initialize the cookie consent manager when the script loads
document.addEventListener('DOMContentLoaded', () => {
  const cookieManager = new CookieConsentManager({
    cookieName: 'hitch_cookie_consent',
    cookieExpiryDays: 365,
    bannerId: 'cookie-consent-banner',
    acceptBtnId: 'cookie-accept-btn',
    settingsBtnId: 'cookie-settings-btn',
    settingsModalId: 'cookie-settings-modal',
    saveSettingsBtnId: 'cookie-save-settings-btn'
  });
});
```
