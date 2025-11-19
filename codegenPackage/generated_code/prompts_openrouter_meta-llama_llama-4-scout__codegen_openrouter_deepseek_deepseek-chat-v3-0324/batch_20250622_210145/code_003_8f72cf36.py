"""
Generated Code Metadata:
========================
Original URL: https://sensibleoptimism.com
Prompt: Develop a JavaScript function to handle cookie consent for a website, similar to how sensibleoptimism.com manages user data with cookies.
Generated: DETERMINISTIC_8f72cf360481c9ec
Batch ID: 20250622_210145
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
 * Handles user consent for cookies on a website.
 * Similar to sensibleoptimism.com's approach.
 */

class CookieConsent {
  constructor(options = {}) {
    // Default options
    this.defaults = {
      cookieName: 'cookie_consent',
      cookieExpiryDays: 365,
      cookiePath: '/',
      cookieDomain: window.location.hostname,
      cookieSecure: window.location.protocol === 'https:',
      cookieSameSite: 'Lax',
      categories: {
        necessary: {
          name: 'Necessary',
          description: 'Essential cookies for website functionality',
          required: true,
          active: true
        },
        analytics: {
          name: 'Analytics',
          description: 'Cookies for website analytics and performance',
          required: false,
          active: false
        },
        marketing: {
          name: 'Marketing',
          description: 'Cookies for marketing and tracking',
          required: false,
          active: false
        }
      },
      ui: {
        containerSelector: '#cookie-consent-container',
        acceptAllSelector: '#cookie-consent-accept-all',
        acceptSelectedSelector: '#cookie-consent-accept-selected',
        rejectAllSelector: '#cookie-consent-reject-all',
        settingsSelector: '#cookie-consent-settings',
        settingsModalSelector: '#cookie-consent-modal',
        saveSettingsSelector: '#cookie-consent-save-settings',
        categoryToggleSelector: '.cookie-consent-category-toggle'
      }
    };

    // Merge user options with defaults
    this.options = { ...this.defaults, ...options };

    // Initialize
    this.init();
  }

  /**
   * Initialize the cookie consent manager
   */
  init() {
    // Check if consent already exists
    const consent = this.getConsent();

    if (!consent) {
      // Show UI if no consent exists
      this.showConsentUI();
    } else {
      // Apply existing consent
      this.applyConsent(consent);
    }

    // Set up event listeners
    this.setupEventListeners();
  }

  /**
   * Show the consent UI
   */
  showConsentUI() {
    const container = document.querySelector(this.options.ui.containerSelector);
    if (container) {
      container.style.display = 'block';
    }
  }

  /**
   * Hide the consent UI
   */
  hideConsentUI() {
    const container = document.querySelector(this.options.ui.containerSelector);
    if (container) {
      container.style.display = 'none';
    }
  }

  /**
   * Show the settings modal
   */
  showSettingsModal() {
    const modal = document.querySelector(this.options.ui.settingsModalSelector);
    if (modal) {
      modal.style.display = 'block';
    }
  }

  /**
   * Hide the settings modal
   */
  hideSettingsModal() {
    const modal = document.querySelector(this.options.ui.settingsModalSelector);
    if (modal) {
      modal.style.display = 'none';
    }
  }

  /**
   * Set up event listeners for UI elements
   */
  setupEventListeners() {
    // Accept all cookies
    const acceptAllBtn = document.querySelector(this.options.ui.acceptAllSelector);
    if (acceptAllBtn) {
      acceptAllBtn.addEventListener('click', () => {
        this.acceptAll();
      });
    }

    // Accept selected cookies
    const acceptSelectedBtn = document.querySelector(this.options.ui.acceptSelectedSelector);
    if (acceptSelectedBtn) {
      acceptSelectedBtn.addEventListener('click', () => {
        this.acceptSelected();
      });
    }

    // Reject all cookies
    const rejectAllBtn = document.querySelector(this.options.ui.rejectAllSelector);
    if (rejectAllBtn) {
      rejectAllBtn.addEventListener('click', () => {
        this.rejectAll();
      });
    }

    // Open settings modal
    const settingsBtn = document.querySelector(this.options.ui.settingsSelector);
    if (settingsBtn) {
      settingsBtn.addEventListener('click', () => {
        this.showSettingsModal();
      });
    }

    // Save settings
    const saveSettingsBtn = document.querySelector(this.options.ui.saveSettingsSelector);
    if (saveSettingsBtn) {
      saveSettingsBtn.addEventListener('click', () => {
        this.saveSettings();
      });
    }

    // Category toggles
    const categoryToggles = document.querySelectorAll(this.options.ui.categoryToggleSelector);
    categoryToggles.forEach(toggle => {
      toggle.addEventListener('change', (e) => {
        const category = e.target.dataset.category;
        if (category) {
          this.toggleCategory(category, e.target.checked);
        }
      });
    });
  }

  /**
   * Accept all cookies
   */
  acceptAll() {
    const consent = {};
    Object.keys(this.options.categories).forEach(category => {
      consent[category] = true;
    });
    this.setConsent(consent);
    this.hideConsentUI();
    this.applyConsent(consent);
  }

  /**
   * Accept selected cookies from settings modal
   */
  acceptSelected() {
    const consent = {};
    Object.keys(this.options.categories).forEach(category => {
      const toggle = document.querySelector(`[data-category="${category}"]`);
      if (toggle) {
        consent[category] = toggle.checked || this.options.categories[category].required;
      } else {
        consent[category] = this.options.categories[category].required;
      }
    });
    this.setConsent(consent);
    this.hideConsentUI();
    this.hideSettingsModal();
    this.applyConsent(consent);
  }

  /**
   * Reject all non-essential cookies
   */
  rejectAll() {
    const consent = {};
    Object.keys(this.options.categories).forEach(category => {
      consent[category] = this.options.categories[category].required;
    });
    this.setConsent(consent);
    this.hideConsentUI();
    this.applyConsent(consent);
  }

  /**
   * Save settings from modal
   */
  saveSettings() {
    this.acceptSelected();
  }

  /**
   * Toggle a category's active state
   * @param {string} category - The category to toggle
   * @param {boolean} state - The new state
   */
  toggleCategory(category, state) {
    if (this.options.categories[category] && !this.options.categories[category].required) {
      this.options.categories[category].active = state;
    }
  }

  /**
   * Set the consent cookie
   * @param {object} consent - Consent object containing category states
   */
  setConsent(consent) {
    const expiryDate = new Date();
    expiryDate.setDate(expiryDate.getDate() + this.options.cookieExpiryDays);

    const cookieValue = JSON.stringify(consent);
    const cookieParts = [
      `${this.options.cookieName}=${encodeURIComponent(cookieValue)}`,
      `expires=${expiryDate.toUTCString()}`,
      `path=${this.options.cookiePath}`,
      `domain=${this.options.cookieDomain}`,
      `SameSite=${this.options.cookieSameSite}`
    ];

    if (this.options.cookieSecure) {
      cookieParts.push('Secure');
    }

    document.cookie = cookieParts.join('; ');
  }

  /**
   * Get the current consent
   * @returns {object|null} The consent object or null if not set
   */
  getConsent() {
    const cookie = document.cookie
      .split('; ')
      .find(row => row.startsWith(`${this.options.cookieName}=`));

    if (cookie) {
      try {
        const cookieValue = decodeURIComponent(cookie.split('=')[1]);
        return JSON.parse(cookieValue);
      } catch (e) {
        console.error('Error parsing cookie consent:', e);
        return null;
      }
    }
    return null;
  }

  /**
   * Apply the consent settings
   * @param {object} consent - The consent object to apply
   */
  applyConsent(consent) {
    // Here you would typically load/unload scripts based on consent
    // For example:
    // if (consent.analytics) {
    //   loadGoogleAnalytics();
    // } else {
    //   disableGoogleAnalytics();
    // }
    
    // Dispatch an event to notify other parts of the application
    const event = new CustomEvent('cookieConsentChanged', { detail: consent });
    document.dispatchEvent(event);
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new CookieConsent();
});
```
