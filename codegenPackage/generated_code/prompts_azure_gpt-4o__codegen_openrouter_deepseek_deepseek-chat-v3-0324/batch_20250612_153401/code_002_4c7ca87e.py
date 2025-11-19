"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Generate code to manage user consent preferences for cookies, including functionality for "Accept All," "Reject All," and "Customize Preferences," as outlined on the Masa website.
Generated: DETERMINISTIC_4c7ca87e0028e9d7
Batch ID: 20250612_153401
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
 * Handles user consent preferences for cookies with options to:
 * - Accept All
 * - Reject All
 * - Customize Preferences
 */

class CookieConsentManager {
  constructor() {
    this.cookieCategories = {
      necessary: {
        name: 'Necessary',
        description: 'Essential cookies for website functionality',
        required: true,
        enabled: true
      },
      analytics: {
        name: 'Analytics',
        description: 'Cookies for website usage analytics',
        required: false,
        enabled: false
      },
      marketing: {
        name: 'Marketing',
        description: 'Cookies for personalized advertising',
        required: false,
        enabled: false
      },
      preferences: {
        name: 'Preferences',
        description: 'Cookies for remembering user preferences',
        required: false,
        enabled: false
      }
    };

    this.cookieName = 'cookie_consent_preferences';
    this.cookieExpiryDays = 365;
    this.consentGiven = false;

    this.init();
  }

  /**
   * Initialize the cookie consent manager
   */
  init() {
    this.loadPreferences();
    this.setupEventListeners();
    this.showBannerIfNeeded();
  }

  /**
   * Load saved cookie preferences from cookie
   */
  loadPreferences() {
    const savedPreferences = this.getCookie(this.cookieName);
    
    if (savedPreferences) {
      try {
        const parsedPreferences = JSON.parse(savedPreferences);
        this.consentGiven = parsedPreferences.consentGiven || false;
        
        for (const category in this.cookieCategories) {
          if (parsedPreferences[category] !== undefined) {
            this.cookieCategories[category].enabled = parsedPreferences[category];
          }
        }
      } catch (e) {
        console.error('Error parsing cookie preferences:', e);
      }
    }
  }

  /**
   * Save current preferences to cookie
   */
  savePreferences() {
    const preferences = {
      consentGiven: this.consentGiven,
      timestamp: new Date().toISOString()
    };

    for (const category in this.cookieCategories) {
      preferences[category] = this.cookieCategories[category].enabled;
    }

    this.setCookie(
      this.cookieName,
      JSON.stringify(preferences),
      this.cookieExpiryDays
    );
  }

  /**
   * Set a cookie with given name, value and expiry days
   * @param {string} name - Cookie name
   * @param {string} value - Cookie value
   * @param {number} days - Expiry in days
   */
  setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/;SameSite=Lax`;
  }

  /**
   * Get cookie value by name
   * @param {string} name - Cookie name
   * @returns {string|null} Cookie value or null if not found
   */
  getCookie(name) {
    const nameEQ = `${name}=`;
    const cookies = document.cookie.split(';');
    
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i];
      while (cookie.charAt(0) === ' ') {
        cookie = cookie.substring(1);
      }
      if (cookie.indexOf(nameEQ) === 0) {
        return cookie.substring(nameEQ.length);
      }
    }
    return null;
  }

  /**
   * Delete cookie by name
   * @param {string} name - Cookie name
   */
  deleteCookie(name) {
    this.setCookie(name, '', -1);
  }

  /**
   * Show consent banner if consent hasn't been given
   */
  showBannerIfNeeded() {
    if (!this.consentGiven) {
      this.renderBanner();
    }
  }

  /**
   * Render the consent banner
   */
  renderBanner() {
    const bannerHTML = `
      <div id="cookie-consent-banner" class="cookie-consent-banner">
        <div class="cookie-consent-content">
          <h3>Cookie Preferences</h3>
          <p>We use cookies to enhance your experience. Choose which cookies you allow us to use.</p>
          
          <div class="cookie-consent-actions">
            <button id="cookie-consent-accept-all" class="cookie-consent-btn primary">Accept All</button>
            <button id="cookie-consent-customize" class="cookie-consent-btn secondary">Customize</button>
            <button id="cookie-consent-reject-all" class="cookie-consent-btn secondary">Reject All</button>
          </div>
        </div>
      </div>
    `;

    document.body.insertAdjacentHTML('beforeend', bannerHTML);
  }

  /**
   * Render the customization modal
   */
  renderCustomizationModal() {
    let categoriesHTML = '';
    
    for (const category in this.cookieCategories) {
      const cat = this.cookieCategories[category];
      categoriesHTML += `
        <div class="cookie-category">
          <div class="cookie-category-header">
            <h4>${cat.name}</h4>
            <label class="switch">
              <input type="checkbox" id="cookie-consent-${category}" ${cat.enabled ? 'checked' : ''} ${cat.required ? 'disabled' : ''}>
              <span class="slider round ${cat.required ? 'disabled' : ''}"></span>
            </label>
          </div>
          <p>${cat.description}</p>
          ${cat.required ? '<p class="required-notice">(Always enabled)</p>' : ''}
        </div>
      `;
    }

    const modalHTML = `
      <div id="cookie-consent-modal" class="cookie-consent-modal">
        <div class="cookie-consent-modal-content">
          <div class="cookie-consent-modal-header">
            <h3>Customize Cookie Preferences</h3>
            <button id="cookie-consent-modal-close" class="cookie-consent-modal-close">&times;</button>
          </div>
          <div class="cookie-consent-modal-body">
            ${categoriesHTML}
          </div>
          <div class="cookie-consent-modal-footer">
            <button id="cookie-consent-save" class="cookie-consent-btn primary">Save Preferences</button>
          </div>
        </div>
      </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHTML);
  }

  /**
   * Setup event listeners for buttons and interactions
   */
  setupEventListeners() {
    document.addEventListener('click', (e) => {
      // Handle Accept All button
      if (e.target.matches('#cookie-consent-accept-all')) {
        this.acceptAll();
      }
      
      // Handle Reject All button
      if (e.target.matches('#cookie-consent-reject-all')) {
        this.rejectAll();
      }
      
      // Handle Customize button
      if (e.target.matches('#cookie-consent-customize')) {
        this.renderCustomizationModal();
      }
      
      // Handle Modal Close button
      if (e.target.matches('#cookie-consent-modal-close')) {
        this.closeModal();
      }
      
      // Handle Save Preferences button
      if (e.target.matches('#cookie-consent-save')) {
        this.saveCustomPreferences();
      }
    });
  }

  /**
   * Accept all cookie categories
   */
  acceptAll() {
    for (const category in this.cookieCategories) {
      this.cookieCategories[category].enabled = true;
    }
    
    this.consentGiven = true;
    this.savePreferences();
    this.removeBanner();
    this.triggerConsentEvent();
  }

  /**
   * Reject all non-essential cookie categories
   */
  rejectAll() {
    for (const category in this.cookieCategories) {
      if (!this.cookieCategories[category].required) {
        this.cookieCategories[category].enabled = false;
      }
    }
    
    this.consentGiven = true;
    this.savePreferences();
    this.removeBanner();
    this.triggerConsentEvent();
  }

  /**
   * Save customized preferences from modal
   */
  saveCustomPreferences() {
    for (const category in this.cookieCategories) {
      if (!this.cookieCategories[category].required) {
        const checkbox = document.getElementById(`cookie-consent-${category}`);
        if (checkbox) {
          this.cookieCategories[category].enabled = checkbox.checked;
        }
      }
    }
    
    this.consentGiven = true;
    this.savePreferences();
    this.closeModal();
    this.removeBanner();
    this.triggerConsentEvent();
  }

  /**
   * Close the customization modal
   */
  closeModal() {
    const modal = document.getElementById('cookie-consent-modal');
    if
