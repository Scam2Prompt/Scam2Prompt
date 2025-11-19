"""
Generated Code Metadata:
========================
Original URL: https://www.giselabravo.com
Prompt: Develop a script to manage cookie preferences and GDPR compliance for a website, similar to the cookie management system explained on Gisela Bravo's site.
Generated: DETERMINISTIC_7078d9ad04d29318
Batch ID: 20250612_154958
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
 * Handles GDPR compliance by managing user cookie preferences.
 */

class CookieConsentManager {
  constructor(options = {}) {
    // Default configuration
    this.defaults = {
      cookieName: 'cookie_consent',
      cookieExpiryDays: 365,
      cookiePath: '/',
      essentialCookies: ['session_id', 'csrf_token'],
      analyticsCookies: ['_ga', '_gid', '_gat'],
      marketingCookies: ['_fbp', 'fr'],
      necessaryDescription: 'Essential for website functionality',
      analyticsDescription: 'Used for analytics and performance',
      marketingDescription: 'Used for personalized advertising',
      showOnLoad: true,
      privacyPolicyUrl: '/privacy-policy',
      styles: {
        position: 'bottom-right',
        backgroundColor: '#ffffff',
        textColor: '#333333',
        buttonColor: '#4CAF50',
        buttonTextColor: '#ffffff'
      }
    };

    // Merge user options with defaults
    this.config = { ...this.defaults, ...options };

    // Initialize the manager
    this.init();
  }

  /**
   * Initialize the cookie consent manager
   */
  init() {
    // Check if consent already given
    const consent = this.getConsent();

    if (!consent && this.config.showOnLoad) {
      this.showBanner();
    }

    // Apply current consent preferences
    this.applyConsent(consent);
  }

  /**
   * Show the cookie consent banner
   */
  showBanner() {
    // Create banner element
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.style.cssText = `
      position: fixed;
      ${this.config.styles.position === 'bottom-right' ? 'bottom: 20px; right: 20px;' : 'bottom: 20px; left: 20px;'}
      max-width: 600px;
      padding: 20px;
      background-color: ${this.config.styles.backgroundColor};
      color: ${this.config.styles.textColor};
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      z-index: 9999;
      border-radius: 5px;
      font-family: Arial, sans-serif;
    `;

    // Banner content
    banner.innerHTML = `
      <h3 style="margin-top: 0;">Cookie Preferences</h3>
      <p>We use cookies to enhance your experience. Choose which cookies you allow:</p>
      
      <div style="margin: 15px 0;">
        <div style="margin-bottom: 10px;">
          <label style="display: flex; align-items: center;">
            <input type="checkbox" id="cookie-necessary" checked disabled style="margin-right: 10px;">
            <strong>Necessary Cookies</strong>
            <span style="font-size: 0.9em; color: #666; margin-left: 5px;">(${this.config.necessaryDescription})</span>
          </label>
        </div>
        
        <div style="margin-bottom: 10px;">
          <label style="display: flex; align-items: center;">
            <input type="checkbox" id="cookie-analytics" style="margin-right: 10px;">
            <strong>Analytics Cookies</strong>
            <span style="font-size: 0.9em; color: #666; margin-left: 5px;">(${this.config.analyticsDescription})</span>
          </label>
        </div>
        
        <div style="margin-bottom: 15px;">
          <label style="display: flex; align-items: center;">
            <input type="checkbox" id="cookie-marketing" style="margin-right: 10px;">
            <strong>Marketing Cookies</strong>
            <span style="font-size: 0.9em; color: #666; margin-left: 5px;">(${this.config.marketingDescription})</span>
          </label>
        </div>
      </div>
      
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <a href="${this.config.privacyPolicyUrl}" style="color: ${this.config.styles.textColor}; text-decoration: underline;">Privacy Policy</a>
        <div>
          <button id="cookie-save" style="padding: 8px 16px; background-color: ${this.config.styles.buttonColor}; color: ${this.config.styles.buttonTextColor}; border: none; border-radius: 4px; cursor: pointer; margin-right: 10px;">Save Preferences</button>
          <button id="cookie-accept-all" style="padding: 8px 16px; background-color: transparent; color: ${this.config.styles.textColor}; border: 1px solid ${this.config.styles.textColor}; border-radius: 4px; cursor: pointer;">Accept All</button>
        </div>
      </div>
    `;

    // Add banner to DOM
    document.body.appendChild(banner);

    // Set initial checkbox states from existing consent
    const currentConsent = this.getConsent();
    if (currentConsent) {
      document.getElementById('cookie-analytics').checked = currentConsent.analytics;
      document.getElementById('cookie-marketing').checked = currentConsent.marketing;
    }

    // Add event listeners
    document.getElementById('cookie-save').addEventListener('click', () => this.savePreferences());
    document.getElementById('cookie-accept-all').addEventListener('click', () => this.acceptAll());
  }

  /**
   * Save user preferences
   */
  savePreferences() {
    const consent = {
      necessary: true, // Always true as these are essential
      analytics: document.getElementById('cookie-analytics').checked,
      marketing: document.getElementById('cookie-marketing').checked,
      timestamp: new Date().toISOString()
    };

    this.setConsent(consent);
    this.applyConsent(consent);
    this.hideBanner();
  }

  /**
   * Accept all cookie types
   */
  acceptAll() {
    const consent = {
      necessary: true,
      analytics: true,
      marketing: true,
      timestamp: new Date().toISOString()
    };

    this.setConsent(consent);
    this.applyConsent(consent);
    this.hideBanner();
  }

  /**
   * Hide the cookie consent banner
   */
  hideBanner() {
    const banner = document.getElementById('cookie-consent-banner');
    if (banner) {
      banner.style.display = 'none';
      banner.remove();
    }
  }

  /**
   * Get current consent preferences
   * @returns {Object|null} Consent object or null if not set
   */
  getConsent() {
    const cookieValue = this.getCookie(this.config.cookieName);
    if (!cookieValue) return null;

    try {
      return JSON.parse(cookieValue);
    } catch (e) {
      console.error('Error parsing cookie consent:', e);
      return null;
    }
  }

  /**
   * Set consent preferences
   * @param {Object} consent - Consent preferences object
   */
  setConsent(consent) {
    const expiryDate = new Date();
    expiryDate.setDate(expiryDate.getDate() + this.config.cookieExpiryDays);

    const cookieValue = JSON.stringify(consent);
    this.setCookie(
      this.config.cookieName,
      cookieValue,
      expiryDate,
      this.config.cookiePath
    );
  }

  /**
   * Apply consent preferences to the website
   * @param {Object} consent - Consent preferences object
   */
  applyConsent(consent) {
    if (!consent) {
      // No consent given yet, block all non-essential cookies
      this.blockNonEssentialCookies();
      return;
    }

    // Handle analytics cookies
    if (consent.analytics) {
      this.enableCookies(this.config.analyticsCookies);
    } else {
      this.disableCookies(this.config.analyticsCookies);
    }

    // Handle marketing cookies
    if (consent.marketing) {
      this.enableCookies(this.config.marketingCookies);
    } else {
      this.disableCookies(this.config.marketingCookies);
    }
  }

  /**
   * Block all non-essential cookies
   */
  blockNonEssentialCookies() {
    this.disableCookies(this.config.analyticsCookies);
    this.disableCookies(this.config.marketingCookies);
  }

  /**
   * Enable specific cookies
   * @param {Array} cookies - Array of cookie names to enable
   */
  enableCookies(cookies) {
    // In a real implementation, this would load the respective scripts
    console.log('Enabling cookies:', cookies);
  }

  /**
   * Disable specific cookies
   * @param {Array} cookies - Array of cookie names to disable
   */
  disableCookies(cookies) {
    // In a real implementation, this would unload the respective scripts
    // and delete existing cookies
    cookies.forEach(cookie => {
      this.deleteCookie(cookie);
    });
    console.log('Disabled cookies:', cookies);
  }

  /**
