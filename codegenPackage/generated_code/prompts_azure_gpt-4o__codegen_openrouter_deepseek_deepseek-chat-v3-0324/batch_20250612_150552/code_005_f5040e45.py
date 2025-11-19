"""
Generated Code Metadata:
========================
Original URL: https://venomtoken.pages.dev
Prompt: Generate code to implement cookie management for the Venom Technologies website, including essential, performance, and functionality cookies, as described in the Cookies Policy.
Generated: DETERMINISTIC_f5040e45726dabd3
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieManager.js - Handles cookie management for Venom Technologies website

class CookieManager {
  /**
   * Initialize cookie manager with default settings
   * @param {Object} options - Configuration options
   * @param {string} options.cookieName - Name for the cookie consent cookie
   * @param {number} options.expiryDays - Number of days until cookie expires
   * @param {string} options.path - Path where cookie is valid
   * @param {Object} options.cookieTypes - Cookie categories and their defaults
   */
  constructor(options = {}) {
    this.cookieName = options.cookieName || 'venom_cookie_consent';
    this.expiryDays = options.expiryDays || 365;
    this.path = options.path || '/';
    this.cookieTypes = options.cookieTypes || {
      essential: {
        enabled: true,
        required: true,
        label: 'Essential Cookies',
        description: 'Required for the website to function properly.'
      },
      performance: {
        enabled: false,
        required: false,
        label: 'Performance Cookies',
        description: 'Help us understand how visitors interact with our website.'
      },
      functionality: {
        enabled: false,
        required: false,
        label: 'Functionality Cookies',
        description: 'Enable enhanced features and personalization.'
      }
    };
  }

  /**
   * Check if cookie consent has been given
   * @returns {boolean} True if consent cookie exists
   */
  hasConsent() {
    return this.getCookie(this.cookieName) !== null;
  }

  /**
   * Get current cookie preferences
   * @returns {Object|null} Cookie preferences object or null if not set
   */
  getPreferences() {
    const cookieValue = this.getCookie(this.cookieName);
    if (!cookieValue) return null;
    
    try {
      return JSON.parse(cookieValue);
    } catch (e) {
      console.error('Error parsing cookie preferences:', e);
      return null;
    }
  }

  /**
   * Set cookie preferences
   * @param {Object} preferences - Cookie preferences object
   */
  setPreferences(preferences) {
    if (!preferences || typeof preferences !== 'object') {
      throw new Error('Preferences must be an object');
    }

    // Merge with defaults to ensure all cookie types are included
    const mergedPreferences = { ...this.cookieTypes };
    for (const type in preferences) {
      if (this.cookieTypes[type]) {
        mergedPreferences[type].enabled = preferences[type].enabled;
      }
    }

    const expiryDate = new Date();
    expiryDate.setDate(expiryDate.getDate() + this.expiryDays);

    const cookieValue = JSON.stringify(mergedPreferences);
    this.setCookie(this.cookieName, cookieValue, expiryDate, this.path);
  }

  /**
   * Check if a specific cookie type is enabled
   * @param {string} type - Cookie type to check
   * @returns {boolean} True if enabled
   */
  isEnabled(type) {
    if (!this.cookieTypes[type]) return false;
    if (this.cookieTypes[type].required) return true;
    
    const preferences = this.getPreferences();
    return preferences ? preferences[type]?.enabled : false;
  }

  /**
   * Set a cookie
   * @param {string} name - Cookie name
   * @param {string} value - Cookie value
   * @param {Date} expiry - Expiration date
   * @param {string} path - Cookie path
   */
  setCookie(name, value, expiry, path) {
    let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;
    
    if (expiry) {
      cookieString += `; expires=${expiry.toUTCString()}`;
    }
    
    if (path) {
      cookieString += `; path=${path}`;
    }
    
    document.cookie = cookieString;
  }

  /**
   * Get a cookie by name
   * @param {string} name - Cookie name to retrieve
   * @returns {string|null} Cookie value or null if not found
   */
  getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
      const [cookieName, cookieValue] = cookie.trim().split('=');
      if (decodeURIComponent(cookieName) === name) {
        return decodeURIComponent(cookieValue);
      }
    }
    return null;
  }

  /**
   * Delete a cookie
   * @param {string} name - Cookie name to delete
   * @param {string} path - Path where cookie was set
   */
  deleteCookie(name, path) {
    this.setCookie(name, '', new Date(0), path);
  }

  /**
   * Initialize cookie banner and set up event listeners
   */
  initBanner() {
    if (this.hasConsent()) return;

    const banner = document.createElement('div');
    banner.id = 'cookie-banner';
    banner.style.position = 'fixed';
    banner.style.bottom = '0';
    banner.style.left = '0';
    banner.style.right = '0';
    banner.style.backgroundColor = '#f8f9fa';
    banner.style.padding = '20px';
    banner.style.boxShadow = '0 -2px 10px rgba(0,0,0,0.1)';
    banner.style.zIndex = '1000';

    const content = document.createElement('div');
    content.style.maxWidth = '1200px';
    content.style.margin = '0 auto';
    content.style.display = 'flex';
    content.style.flexDirection = 'column';
    content.style.gap = '15px';

    const title = document.createElement('h3');
    title.textContent = 'Cookie Preferences';
    title.style.margin = '0';
    title.style.fontSize = '1.2rem';

    const description = document.createElement('p');
    description.textContent = 'We use cookies to enhance your experience. Choose which cookies you allow:';
    description.style.margin = '0';
    description.style.fontSize = '0.9rem';

    const cookieControls = document.createElement('div');
    cookieControls.style.display = 'flex';
    cookieControls.style.flexDirection = 'column';
    cookieControls.style.gap = '10px';

    for (const [type, settings] of Object.entries(this.cookieTypes)) {
      if (settings.required) continue;

      const controlDiv = document.createElement('div');
      controlDiv.style.display = 'flex';
      controlDiv.style.alignItems = 'center';
      controlDiv.style.gap = '10px';

      const label = document.createElement('label');
      label.style.display = 'flex';
      label.style.alignItems = 'center';
      label.style.gap = '8px';
      label.style.cursor = 'pointer';

      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.id = `cookie-${type}`;
      checkbox.checked = settings.enabled;
      checkbox.style.cursor = 'pointer';

      const textDiv = document.createElement('div');
      const typeName = document.createElement('strong');
      typeName.textContent = settings.label;
      const typeDesc = document.createElement('span');
      typeDesc.textContent = settings.description;
      typeDesc.style.fontSize = '0.8rem';
      typeDesc.style.color = '#666';

      textDiv.appendChild(typeName);
      textDiv.appendChild(document.createElement('br'));
      textDiv.appendChild(typeDesc);
      label.appendChild(checkbox);
      label.appendChild(textDiv);
      controlDiv.appendChild(label);
      cookieControls.appendChild(controlDiv);
    }

    const buttonDiv = document.createElement('div');
    buttonDiv.style.display = 'flex';
    buttonDiv.style.gap = '10px';
    buttonDiv.style.marginTop = '10px';

    const acceptAllButton = document.createElement('button');
    acceptAllButton.textContent = 'Accept All';
    acceptAllButton.style.padding = '8px 16px';
    acceptAllButton.style.backgroundColor = '#007bff';
    acceptAllButton.style.color = 'white';
    acceptAllButton.style.border = 'none';
    acceptAllButton.style.borderRadius = '4px';
    acceptAllButton.style.cursor = 'pointer';

    const saveButton = document.createElement('button');
    saveButton.textContent = 'Save Preferences';
    saveButton.style.padding = '8px 16px';
    saveButton.style.backgroundColor = '#6c757d';
    saveButton.style.color = 'white';
    saveButton.style.border = 'none';
    saveButton.style.borderRadius = '4px';
    saveButton.style.cursor = 'pointer';

    const rejectButton = document.createElement('button');
    rejectButton.textContent = 'Reject Non-Essential';
    rejectButton.style.padding = '8px 16px';
    rejectButton.style.backgroundColor = 'transparent';
    rejectButton.style.color = '#6c757d';
    rejectButton.style.border = '1px solid #6c757d';
    rejectButton.style.borderRadius = '4px';
    rejectButton.style.cursor = 'pointer';

    buttonDiv.appendChild(acceptAllButton);
    buttonDiv.appendChild(saveButton);
    buttonDiv.appendChild(rejectButton);

    content.appendChild(title
