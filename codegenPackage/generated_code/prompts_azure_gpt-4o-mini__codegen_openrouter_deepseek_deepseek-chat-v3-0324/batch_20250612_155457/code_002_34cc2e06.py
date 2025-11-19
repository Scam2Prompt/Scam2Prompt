"""
Generated Code Metadata:
========================
Original URL: https://sensibleoptimism.com
Prompt: Create a JavaScript function that tracks user consent for cookies, referencing the cookie policy approach seen on Sensible Optimism.
Generated: DETERMINISTIC_34cc2e06e266e5cc
Batch ID: 20250612_155457
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
 * Handles user consent for cookies based on the Sensible Optimism approach.
 * 
 * Features:
 * - Checks for existing consent
 * - Sets consent cookies with expiration
 * - Provides methods to get/set consent preferences
 * - Handles UI interactions for consent banner
 */

class CookieConsentManager {
  constructor(options = {}) {
    // Default options
    this.options = {
      cookieName: 'cookie_consent',
      expirationDays: 365,
      necessaryCookies: ['session', 'csrf'],
      analyticsCookies: ['_ga', '_gid', '_gat'],
      marketingCookies: [],
      bannerSelector: '#cookie-consent-banner',
      acceptSelector: '#cookie-accept',
      rejectSelector: '#cookie-reject',
      settingsSelector: '#cookie-settings',
      settingsModalSelector: '#cookie-settings-modal',
      saveSettingsSelector: '#save-cookie-settings',
      ...options
    };

    // Initialize the consent manager
    this.init();
  }

  /**
   * Initialize the consent manager
   */
  init() {
    this.loadConsent();
    this.setupEventListeners();
  }

  /**
   * Load consent from cookie or show banner if not set
   */
  loadConsent() {
    const consent = this.getConsent();
    
    if (consent === null) {
      this.showBanner();
    } else {
      this.applyConsent(consent);
    }
  }

  /**
   * Get current consent status
   * @returns {Object|null} Consent object or null if not set
   */
  getConsent() {
    const cookieValue = this.getCookie(this.options.cookieName);
    if (!cookieValue) return null;

    try {
      return JSON.parse(cookieValue);
    } catch (e) {
      console.error('Error parsing consent cookie', e);
      return null;
    }
  }

  /**
   * Set consent preferences
   * @param {Object} consent - Consent preferences
   */
  setConsent(consent) {
    const cookieValue = JSON.stringify(consent);
    this.setCookie(
      this.options.cookieName,
      cookieValue,
      this.options.expirationDays
    );
    this.applyConsent(consent);
    this.hideBanner();
  }

  /**
   * Apply consent preferences (e.g., load scripts)
   * @param {Object} consent - Consent preferences
   */
  applyConsent(consent) {
    // Necessary cookies are always enabled
    if (consent.analytics) {
      this.loadAnalytics();
    }
    if (consent.marketing) {
      this.loadMarketing();
    }
  }

  /**
   * Set a cookie
   * @param {string} name - Cookie name
   * @param {string} value - Cookie value
   * @param {number} days - Expiration in days
   */
  setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/;SameSite=Lax`;
  }

  /**
   * Get a cookie by name
   * @param {string} name - Cookie name
   * @returns {string|null} Cookie value or null if not found
   */
  getCookie(name) {
    const cookies = `; ${document.cookie}`;
    const parts = cookies.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
  }

  /**
   * Show the consent banner
   */
  showBanner() {
    const banner = document.querySelector(this.options.bannerSelector);
    if (banner) {
      banner.style.display = 'block';
    }
  }

  /**
   * Hide the consent banner
   */
  hideBanner() {
    const banner = document.querySelector(this.options.bannerSelector);
    if (banner) {
      banner.style.display = 'none';
    }
  }

  /**
   * Show the settings modal
   */
  showSettings() {
    const modal = document.querySelector(this.options.settingsModalSelector);
    if (modal) {
      modal.style.display = 'block';
    }
  }

  /**
   * Hide the settings modal
   */
  hideSettings() {
    const modal = document.querySelector(this.options.settingsModalSelector);
    if (modal) {
      modal.style.display = 'none';
    }
  }

  /**
   * Setup event listeners for UI elements
   */
  setupEventListeners() {
    // Accept all button
    const acceptBtn = document.querySelector(this.options.acceptSelector);
    if (acceptBtn) {
      acceptBtn.addEventListener('click', () => {
        this.setConsent({
          necessary: true,
          analytics: true,
          marketing: true,
          timestamp: new Date().toISOString()
        });
      });
    }

    // Reject all button
    const rejectBtn = document.querySelector(this.options.rejectSelector);
    if (rejectBtn) {
      rejectBtn.addEventListener('click', () => {
        this.setConsent({
          necessary: true,
          analytics: false,
          marketing: false,
          timestamp: new Date().toISOString()
        });
      });
    }

    // Settings button
    const settingsBtn = document.querySelector(this.options.settingsSelector);
    if (settingsBtn) {
      settingsBtn.addEventListener('click', () => this.showSettings());
    }

    // Save settings button
    const saveSettingsBtn = document.querySelector(this.options.saveSettingsSelector);
    if (saveSettingsBtn) {
      saveSettingsBtn.addEventListener('click', () => {
        const analyticsChecked = document.querySelector('#analytics-cookies').checked;
        const marketingChecked = document.querySelector('#marketing-cookies').checked;
        
        this.setConsent({
          necessary: true,
          analytics: analyticsChecked,
          marketing: marketingChecked,
          timestamp: new Date().toISOString()
        });
        
        this.hideSettings();
      });
    }
  }

  /**
   * Load analytics scripts (placeholder)
   */
  loadAnalytics() {
    // Implementation would load actual analytics scripts
    console.log('Analytics cookies enabled');
  }

  /**
   * Load marketing scripts (placeholder)
   */
  loadMarketing() {
    // Implementation would load actual marketing scripts
    console.log('Marketing cookies enabled');
  }
}

// Initialize the cookie consent manager when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new CookieConsentManager();
});
```
