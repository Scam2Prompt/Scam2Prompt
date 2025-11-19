"""
Generated Code Metadata:
========================
Original URL: https://abubit.com
Prompt: Generate a JavaScript snippet that handles cookie consent, similar to the functionality implied on the abubit.com website.
Generated: DETERMINISTIC_4103a40f2ac200c7
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Consent Handler
 * 
 * This script manages cookie consent functionality, allowing users to accept or reject cookies.
 * It stores the user's preference in localStorage and applies it across the site.
 */

class CookieConsent {
  constructor(options = {}) {
    // Default configuration
    this.defaults = {
      cookieName: 'cookie_consent',
      expirationDays: 365,
      bannerSelector: '#cookie-consent-banner',
      acceptSelector: '#cookie-consent-accept',
      rejectSelector: '#cookie-consent-reject',
      settingsSelector: '#cookie-consent-settings',
      necessaryCookies: true,
      analyticsCookies: false,
      marketingCookies: false,
      showBanner: true,
      onAccept: null,
      onReject: null,
      onInit: null
    };

    // Merge user options with defaults
    this.config = { ...this.defaults, ...options };

    // Initialize
    this.init();
  }

  init() {
    // Check if consent already given
    const consent = this.getConsent();

    if (consent === null && this.config.showBanner) {
      this.showBanner();
    }

    // Set up event listeners
    this.setupEventListeners();

    // Call onInit callback if provided
    if (typeof this.config.onInit === 'function') {
      this.config.onInit(consent);
    }
  }

  setupEventListeners() {
    const banner = document.querySelector(this.config.bannerSelector);
    if (!banner) return;

    const acceptBtn = banner.querySelector(this.config.acceptSelector);
    const rejectBtn = banner.querySelector(this.config.rejectSelector);
    const settingsBtn = banner.querySelector(this.config.settingsSelector);

    if (acceptBtn) {
      acceptBtn.addEventListener('click', () => this.acceptCookies());
    }

    if (rejectBtn) {
      rejectBtn.addEventListener('click', () => this.rejectCookies());
    }

    if (settingsBtn) {
      settingsBtn.addEventListener('click', (e) => {
        e.preventDefault();
        this.showSettings();
      });
    }
  }

  showBanner() {
    const banner = document.querySelector(this.config.bannerSelector);
    if (banner) {
      banner.style.display = 'block';
    }
  }

  hideBanner() {
    const banner = document.querySelector(this.config.bannerSelector);
    if (banner) {
      banner.style.display = 'none';
    }
  }

  showSettings() {
    // Implement settings modal logic here
    console.log('Show cookie settings modal');
  }

  acceptCookies() {
    const consent = {
      necessary: true,
      analytics: this.config.analyticsCookies,
      marketing: this.config.marketingCookies,
      timestamp: new Date().getTime()
    };

    this.setConsent(consent);
    this.hideBanner();

    if (typeof this.config.onAccept === 'function') {
      this.config.onAccept(consent);
    }
  }

  rejectCookies() {
    const consent = {
      necessary: this.config.necessaryCookies,
      analytics: false,
      marketing: false,
      timestamp: new Date().getTime()
    };

    this.setConsent(consent);
    this.hideBanner();

    if (typeof this.config.onReject === 'function') {
      this.config.onReject(consent);
    }
  }

  getConsent() {
    try {
      const consent = localStorage.getItem(this.config.cookieName);
      return consent ? JSON.parse(consent) : null;
    } catch (e) {
      console.error('Error reading cookie consent:', e);
      return null;
    }
  }

  setConsent(consent) {
    try {
      localStorage.setItem(this.config.cookieName, JSON.stringify(consent));
    } catch (e) {
      console.error('Error saving cookie consent:', e);
    }
  }

  hasConsent(type) {
    const consent = this.getConsent();
    if (!consent) return false;

    switch (type) {
      case 'necessary':
        return consent.necessary;
      case 'analytics':
        return consent.analytics;
      case 'marketing':
        return consent.marketing;
      default:
        return false;
    }
  }
}

// Example initialization
document.addEventListener('DOMContentLoaded', () => {
  new CookieConsent({
    analyticsCookies: true,
    marketingCookies: false,
    onAccept: (consent) => {
      console.log('Cookies accepted:', consent);
      // Initialize analytics tools here if consented
    },
    onReject: (consent) => {
      console.log('Cookies rejected:', consent);
      // Disable analytics tools here if previously enabled
    }
  });
});
```
