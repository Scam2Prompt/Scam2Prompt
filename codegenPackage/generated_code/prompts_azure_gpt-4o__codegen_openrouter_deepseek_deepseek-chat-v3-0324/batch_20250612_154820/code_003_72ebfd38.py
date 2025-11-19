"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Write JavaScript code to display a cookie consent banner on a website, with options to accept all cookies or manage consent for categories like "Performance" and "Advertisement," as described on the Health Insurance Shop site.
Generated: DETERMINISTIC_72ebfd385ce674f8
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Consent Banner
 * Displays a cookie consent banner with options to accept all cookies or manage consent by categories.
 * 
 * Features:
 * - Accept all cookies
 * - Manage consent by categories (Performance, Advertisement)
 * - Saves user preferences in cookies
 * - Responsive design
 */

class CookieConsent {
  constructor() {
    this.cookieName = 'cookie_consent';
    this.cookieExpiryDays = 365;
    this.categories = {
      necessary: {
        name: 'Necessary',
        description: 'These cookies are essential for the website to function properly.',
        required: true,
        value: true
      },
      performance: {
        name: 'Performance',
        description: 'These cookies help us understand how visitors interact with our website.',
        required: false,
        value: false
      },
      advertisement: {
        name: 'Advertisement',
        description: 'These cookies are used to personalize ads and track ad performance.',
        required: false,
        value: false
      }
    };

    this.init();
  }

  /**
   * Initialize the cookie consent banner
   */
  init() {
    if (!this.getCookie(this.cookieName)) {
      this.createBanner();
    } else {
      this.loadPreferences();
    }
  }

  /**
   * Create and display the cookie consent banner
   */
  createBanner() {
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.className = 'cookie-consent-banner';
    banner.innerHTML = `
      <div class="cookie-consent-content">
        <h3>Cookie Consent</h3>
        <p>We use cookies to enhance your experience on our website. Please review and manage your cookie preferences.</p>
        
        <div class="cookie-categories">
          ${Object.entries(this.categories).map(([key, category]) => `
            <div class="cookie-category ${category.required ? 'required' : ''}">
              <label>
                <input type="checkbox" name="${key}" ${category.required ? 'checked disabled' : ''} ${category.value ? 'checked' : ''}>
                <strong>${category.name}</strong>
                <p>${category.description}</p>
              </label>
            </div>
          `).join('')}
        </div>
        
        <div class="cookie-consent-buttons">
          <button id="cookie-consent-accept-all" class="cookie-btn accept-all">Accept All</button>
          <button id="cookie-consent-save" class="cookie-btn save">Save Preferences</button>
        </div>
      </div>
    `;

    document.body.appendChild(banner);

    // Add event listeners
    document.getElementById('cookie-consent-accept-all').addEventListener('click', () => this.acceptAll());
    document.getElementById('cookie-consent-save').addEventListener('click', () => this.savePreferences());
  }

  /**
   * Accept all cookies
   */
  acceptAll() {
    Object.keys(this.categories).forEach(key => {
      this.categories[key].value = true;
    });
    this.savePreferences();
    this.hideBanner();
  }

  /**
   * Save user preferences
   */
  savePreferences() {
    const checkboxes = document.querySelectorAll('#cookie-consent-banner input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
      if (!this.categories[checkbox.name].required) {
        this.categories[checkbox.name].value = checkbox.checked;
      }
    });

    const consentData = {
      date: new Date().toISOString(),
      consent: this.categories
    };

    this.setCookie(this.cookieName, JSON.stringify(consentData), this.cookieExpiryDays);
    this.hideBanner();
  }

  /**
   * Load saved preferences from cookie
   */
  loadPreferences() {
    const consentData = JSON.parse(this.getCookie(this.cookieName));
    if (consentData && consentData.consent) {
      Object.keys(this.categories).forEach(key => {
        if (consentData.consent[key]) {
          this.categories[key].value = consentData.consent[key].value;
        }
      });
    }
  }

  /**
   * Hide the consent banner
   */
  hideBanner() {
    const banner = document.getElementById('cookie-consent-banner');
    if (banner) {
      banner.style.display = 'none';
    }
  }

  /**
   * Set a cookie
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
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new CookieConsent();
});

// Add basic styles if not already present
if (!document.getElementById('cookie-consent-styles')) {
  const style = document.createElement('style');
  style.id = 'cookie-consent-styles';
  style.textContent = `
    .cookie-consent-banner {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: #f8f9fa;
      padding: 20px;
      box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
      z-index: 9999;
      font-family: Arial, sans-serif;
    }
    .cookie-consent-content {
      max-width: 1200px;
      margin: 0 auto;
    }
    .cookie-consent-content h3 {
      margin-top: 0;
      color: #333;
    }
    .cookie-categories {
      margin: 15px 0;
    }
    .cookie-category {
      margin-bottom: 10px;
      padding: 10px;
      background: #fff;
      border-radius: 4px;
    }
    .cookie-category.required {
      opacity: 0.7;
    }
    .cookie-consent-buttons {
      display: flex;
      gap: 10px;
    }
    .cookie-btn {
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-weight: bold;
    }
    .accept-all {
      background: #007bff;
      color: white;
    }
    .save {
      background: #6c757d;
      color: white;
    }
    @media (max-width: 768px) {
      .cookie-consent-buttons {
        flex-direction: column;
      }
    }
  `;
  document.head.appendChild(style);
}
```
