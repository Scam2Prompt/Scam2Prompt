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
// cookie-consent.js - Cookie Consent Management for E-commerce Websites
// Inspired by ActiveSport.cz implementation

class CookieConsent {
  constructor(options = {}) {
    // Default configuration
    const defaults = {
      cookieName: 'cookie_consent',
      cookieExpiryDays: 365,
      cookiePath: '/',
      cookieDomain: window.location.hostname,
      cookieSecure: false,
      cookieSameSite: 'Lax',
      categories: {
        necessary: {
          required: true,
          enabled: true,
          label: 'Necessary Cookies',
          description: 'Essential for website functionality.'
        },
        analytics: {
          required: false,
          enabled: false,
          label: 'Analytics Cookies',
          description: 'Help us improve our website.'
        },
        marketing: {
          required: false,
          enabled: false,
          label: 'Marketing Cookies',
          description: 'Used for personalized advertising.'
        },
        preferences: {
          required: false,
          enabled: false,
          label: 'Preference Cookies',
          description: 'Remember your settings and preferences.'
        }
      },
      style: {
        position: 'bottom',
        theme: 'light',
        buttonText: 'Accept All',
        rejectText: 'Reject All',
        settingsText: 'Cookie Settings',
        policyLink: '/cookie-policy',
        policyText: 'Cookie Policy'
      },
      onAccept: null,
      onReject: null,
      onChange: null
    };

    this.config = { ...defaults, ...options };
    this.consentModal = null;
    this.settingsModal = null;
    this.init();
  }

  init() {
    // Check if consent already given
    const consent = this.getConsent();

    if (!consent) {
      this.showConsentModal();
    } else {
      this.applyConsent(consent);
    }
  }

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

  setConsent(consent) {
    const cookieValue = JSON.stringify(consent);
    this.setCookie(
      this.config.cookieName,
      cookieValue,
      this.config.cookieExpiryDays,
      this.config.cookiePath,
      this.config.cookieDomain,
      this.config.cookieSecure,
      this.config.cookieSameSite
    );

    this.applyConsent(consent);

    if (this.config.onChange) {
      this.config.onChange(consent);
    }
  }

  applyConsent(consent) {
    // Apply consent to cookie categories
    Object.keys(consent).forEach(category => {
      if (this.config.categories[category]) {
        this.config.categories[category].enabled = consent[category];
      }
    });

    // Load or block scripts based on consent
    this.manageCookies();
  }

  manageCookies() {
    // Implementation would load or block third-party scripts
    // based on the current consent settings
    console.log('Managing cookies based on current consent:', this.config.categories);
  }

  showConsentModal() {
    // Create modal HTML
    this.consentModal = document.createElement('div');
    this.consentModal.className = `cookie-consent ${this.config.style.theme} ${this.config.style.position}`;
    this.consentModal.innerHTML = `
      <div class="cookie-consent-content">
        <p>We use cookies to enhance your experience. By continuing to visit this site, you agree to our use of cookies.</p>
        <div class="cookie-consent-buttons">
          <button class="cookie-consent-accept">${this.config.style.buttonText}</button>
          <button class="cookie-consent-reject">${this.config.style.rejectText}</button>
          <button class="cookie-consent-settings">${this.config.style.settingsText}</button>
        </div>
        <a href="${this.config.style.policyLink}" class="cookie-consent-policy">${this.config.style.policyText}</a>
      </div>
    `;

    // Add event listeners
    this.consentModal.querySelector('.cookie-consent-accept').addEventListener('click', () => {
      this.acceptAll();
      this.hideConsentModal();
    });

    this.consentModal.querySelector('.cookie-consent-reject').addEventListener('click', () => {
      this.rejectAll();
      this.hideConsentModal();
    });

    this.consentModal.querySelector('.cookie-consent-settings').addEventListener('click', () => {
      this.showSettingsModal();
    });

    // Add to DOM
    document.body.appendChild(this.consentModal);
  }

  hideConsentModal() {
    if (this.consentModal) {
      this.consentModal.remove();
      this.consentModal = null;
    }
  }

  showSettingsModal() {
    this.hideConsentModal();

    // Create settings modal HTML
    this.settingsModal = document.createElement('div');
    this.settingsModal.className = `cookie-settings ${this.config.style.theme}`;
    
    let categoriesHTML = '';
    Object.entries(this.config.categories).forEach(([key, category]) => {
      categoriesHTML += `
        <div class="cookie-category ${category.required ? 'required' : ''}">
          <div class="cookie-category-info">
            <h3>${category.label}</h3>
            <p>${category.description}</p>
          </div>
          ${category.required ? 
            '<span class="cookie-required">Required</span>' : 
            `<label class="cookie-toggle">
              <input type="checkbox" ${category.enabled ? 'checked' : ''} ${category.required ? 'disabled' : ''} data-category="${key}">
              <span class="cookie-toggle-slider"></span>
            </label>`
          }
        </div>
      `;
    });

    this.settingsModal.innerHTML = `
      <div class="cookie-settings-content">
        <h2>Cookie Settings</h2>
        ${categoriesHTML}
        <div class="cookie-settings-buttons">
          <button class="cookie-settings-save">Save Settings</button>
          <button class="cookie-settings-cancel">Cancel</button>
        </div>
      </div>
    `;

    // Add event listeners
    this.settingsModal.querySelector('.cookie-settings-save').addEventListener('click', () => {
      this.saveSettings();
      this.hideSettingsModal();
    });

    this.settingsModal.querySelector('.cookie-settings-cancel').addEventListener('click', () => {
      this.hideSettingsModal();
      this.showConsentModal();
    });

    // Add to DOM
    document.body.appendChild(this.settingsModal);
  }

  hideSettingsModal() {
    if (this.settingsModal) {
      this.settingsModal.remove();
      this.settingsModal = null;
    }
  }

  acceptAll() {
    const consent = {};
    Object.keys(this.config.categories).forEach(category => {
      consent[category] = true;
    });

    this.setConsent(consent);

    if (this.config.onAccept) {
      this.config.onAccept(consent);
    }
  }

  rejectAll() {
    const consent = {};
    Object.keys(this.config.categories).forEach(category => {
      consent[category] = this.config.categories[category].required;
    });

    this.setConsent(consent);

    if (this.config.onReject) {
      this.config.onReject(consent);
    }
  }

  saveSettings() {
    const consent = {};
    const checkboxes = this.settingsModal.querySelectorAll('input[type="checkbox"]');

    Object.keys(this.config.categories).forEach(category => {
      if (this.config.categories[category].required) {
        consent[category] = true;
      } else {
        const checkbox = Array.from(checkboxes).find(el => el.dataset.category === category);
        consent[category] = checkbox ? checkbox.checked : false;
      }
    });

    this.setConsent(consent);
  }

  getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
  }

  setCookie(name, value, days, path, domain, secure, sameSite) {
    let expires = '';
    if (days) {
      const date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      expires = `; expires=${date.toUTCString()}`;
    }

    let cookie = `${name}=${value || ''}${expires}; path=${path || '/'}`;
    if (domain) cookie += `; domain=${domain}`;
    if (secure) cookie += '; secure';
    if (sameSite) cookie += `; samesite=${sameSite}`;

    document.cookie = cookie;
