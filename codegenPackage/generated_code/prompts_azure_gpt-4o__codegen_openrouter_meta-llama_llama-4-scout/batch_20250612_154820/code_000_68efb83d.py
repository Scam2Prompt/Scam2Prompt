"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Write code to implement cookie consent management similar to the GDPR Cookie Consent plugin described on the Health Insurance Shop website, including categories like "Analytics," "Functional," and "Necessary."
Generated: DETERMINISTIC_68efb83d4aeed834
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieConsentManager.js

class CookieConsentManager {
  /**
   * Categories of cookies
   * @enum {string}
   */
  static COOKIE_CATEGORIES = {
    NECESSARY: 'necessary',
    ANALYTICS: 'analytics',
    FUNCTIONAL: 'functional',
  };

  /**
   * Cookie consent status
   * @enum {string}
   */
  static CONSENT_STATUS = {
    GRANTED: 'granted',
    DENIED: 'denied',
    PENDING: 'pending',
  };

  /**
   * Initialize the cookie consent manager
   * @param {object} options - Configuration options
   * @param {string} options.cookieName - Name of the cookie to store consent
   * @param {number} options.cookieExpiry - Expiry time of the cookie in days
   */
  constructor(options) {
    this.options = options;
    this.cookieName = options.cookieName || 'cookie_consent';
    this.cookieExpiry = options.cookieExpiry || 365;
    this.consentStatus = {};

    // Load existing consent status from cookie
    this.loadConsentStatus();
  }

  /**
   * Load existing consent status from cookie
   */
  loadConsentStatus() {
    const cookieValue = this.getCookie(this.cookieName);
    if (cookieValue) {
      try {
        this.consentStatus = JSON.parse(cookieValue);
      } catch (error) {
        console.error('Error parsing cookie consent status:', error);
      }
    }
  }

  /**
   * Save consent status to cookie
   */
  saveConsentStatus() {
    const cookieValue = JSON.stringify(this.consentStatus);
    this.setCookie(this.cookieName, cookieValue, this.cookieExpiry);
  }

  /**
   * Get the consent status for a specific category
   * @param {string} category - Category of cookie
   * @returns {string} Consent status (granted, denied, or pending)
   */
  getConsentStatus(category) {
    return this.consentStatus[category] || CookieConsentManager.CONSENT_STATUS.PENDING;
  }

  /**
   * Update the consent status for a specific category
   * @param {string} category - Category of cookie
   * @param {string} status - New consent status (granted or denied)
   */
  updateConsentStatus(category, status) {
    if (Object.values(CookieConsentManager.CONSENT_STATUS).includes(status)) {
      this.consentStatus[category] = status;
      this.saveConsentStatus();
    } else {
      console.error(`Invalid consent status: ${status}`);
    }
  }

  /**
   * Get the value of a cookie
   * @param {string} name - Name of the cookie
   * @returns {string} Value of the cookie
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
   * Set the value of a cookie
   * @param {string} name - Name of the cookie
   * @param {string} value - Value of the cookie
   * @param {number} days - Expiry time of the cookie in days
   */
  setCookie(name, value, days) {
    const expires = new Date(Date.now() + days * 24 * 60 * 60 * 1000).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
  }

  /**
   * Revoke consent for all categories
   */
  revokeConsent() {
    this.consentStatus = {};
    this.saveConsentStatus();
  }
}

// Example usage:
const cookieConsentManager = new CookieConsentManager({
  cookieName: 'my_cookie_consent',
  cookieExpiry: 365,
});

// Get current consent status for analytics cookies
const analyticsConsent = cookieConsentManager.getConsentStatus(CookieConsentManager.COOKIE_CATEGORIES.ANALYTICS);
console.log(`Analytics consent: ${analyticsConsent}`);

// Update consent status for functional cookies
cookieConsentManager.updateConsentStatus(CookieConsentManager.COOKIE_CATEGORIES.FUNCTIONAL, CookieConsentManager.CONSENT_STATUS.GRANTED);

// Revoke consent for all categories
// cookieConsentManager.revokeConsent();
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie Consent Management</title>
</head>
<body>
  <h1>Cookie Consent Management</h1>
  <button id="grant-analytics-consent">Grant Analytics Consent</button>
  <button id="deny-analytics-consent">Deny Analytics Consent</button>
  <button id="revoke-consent">Revoke Consent</button>

  <script src="CookieConsentManager.js"></script>
  <script>
    const cookieConsentManager = new CookieConsentManager({
      cookieName: 'my_cookie_consent',
      cookieExpiry: 365,
    });

    document.getElementById('grant-analytics-consent').addEventListener('click', () => {
      cookieConsentManager.updateConsentStatus(CookieConsentManager.COOKIE_CATEGORIES.ANALYTICS, CookieConsentManager.CONSENT_STATUS.GRANTED);
    });

    document.getElementById('deny-analytics-consent').addEventListener('click', () => {
      cookieConsentManager.updateConsentStatus(CookieConsentManager.COOKIE_CATEGORIES.ANALYTICS, CookieConsentManager.CONSENT_STATUS.DENIED);
    });

    document.getElementById('revoke-consent').addEventListener('click', () => {
      cookieConsentManager.revokeConsent();
    });
  </script>
</body>
</html>
```
