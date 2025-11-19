"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: How would you implement a system to opt-out of non-essential cookies while still allowing users to enjoy the benefits of a web application, like Masa's approach to cookie usage?
Generated: DETERMINISTIC_da30e27fd3a5b769
Batch ID: 20250622_210802
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
  constructor() {
    this.essentialCookies = ['session_id', 'user_token', 'csrf_token'];
    this.nonEssentialCookies = ['_ga', '_gid', '_gat', '_fbp', '_fbc'];
    this.consentKey = 'cookie_consent';
    this.initialize();
  }

  initialize() {
    this.loadConsent();
    this.setupUI();
  }

  loadConsent() {
    const consent = localStorage.getItem(this.consentKey);
    if (consent === null) {
      this.showBanner();
    } else {
      this.applyConsent(JSON.parse(consent));
    }
  }

  saveConsent(consent) {
    localStorage.setItem(this.consentKey, JSON.stringify(consent));
    this.applyConsent(consent);
  }

  applyConsent(consent) {
    if (!consent) {
      this.clearNonEssentialCookies();
    }
    this.updateCookieSettings(consent);
  }

  clearNonEssentialCookies() {
    this.nonEssentialCookies.forEach(cookie => {
      document.cookie = `${cookie}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    });
  }

  updateCookieSettings(consent) {
    const event = new CustomEvent('cookieConsentUpdated', { detail: { consent } });
    document.dispatchEvent(event);
  }

  setupUI() {
    const banner = document.createElement('div');
    banner.id = 'cookie-banner';
    banner.innerHTML = `
      <div class="cookie-content">
        <p>We use cookies to enhance your experience. Some cookies are essential, while others help us improve our services.</p>
        <div class="cookie-buttons">
          <button id="accept-all">Accept All</button>
          <button id="essential-only">Essential Only</button>
          <button id="customize">Customize</button>
        </div>
      </div>
    `;
    document.body.appendChild(banner);

    document.getElementById('accept-all').addEventListener('click', () => {
      this.saveConsent(true);
      banner.style.display = 'none';
    });

    document.getElementById('essential-only').addEventListener('click', () => {
      this.saveConsent(false);
      banner.style.display = 'none';
    });

    document.getElementById('customize').addEventListener('click', () => {
      this.showCustomizeModal();
    });
  }

  showBanner() {
    const banner = document.getElementById('cookie-banner');
    if (banner) banner.style.display = 'block';
  }

  showCustomizeModal() {
    const modal = document.createElement('div');
    modal.id = 'cookie-modal';
    modal.innerHTML = `
      <div class="modal-content">
        <h2>Cookie Preferences</h2>
        <div class="cookie-options">
          <div class="cookie-option">
            <input type="checkbox" id="analytics" checked disabled>
            <label for="analytics">Essential Cookies (Required)</label>
          </div>
          <div class="cookie-option">
            <input type="checkbox" id="marketing" checked>
            <label for="marketing">Marketing Cookies</label>
          </div>
          <div class="cookie-option">
            <input type="checkbox" id="performance" checked>
            <label for="performance">Performance Cookies</label>
          </div>
        </div>
        <div class="modal-buttons">
          <button id="save-preferences">Save Preferences</button>
          <button id="cancel-modal">Cancel</button>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    document.getElementById('save-preferences').addEventListener('click', () => {
      const marketing = document.getElementById('marketing').checked;
      const performance = document.getElementById('performance').checked;
      this.saveConsent(marketing || performance);
      modal.remove();
      document.getElementById('cookie-banner').style.display = 'none';
    });

    document.getElementById('cancel-modal').addEventListener('click', () => {
      modal.remove();
    });
  }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new CookieConsentManager();
});

// Example usage in other parts of the application
document.addEventListener('cookieConsentUpdated', (e) => {
  const { consent } = e.detail;
  if (consent) {
    // Initialize analytics/marketing scripts
    console.log('Non-essential cookies enabled');
  } else {
    // Disable analytics/marketing scripts
    console.log('Only essential cookies enabled');
  }
});
```

```css
/* cookie-consent.css */
#cookie-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: #f8f9fa;
  padding: 20px;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  display: none;
}

.cookie-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.cookie-buttons button {
  margin-left: 10px;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

#accept-all {
  background: #007bff;
  color: white;
}

#essential-only {
  background: #6c757d;
  color: white;
}

#customize {
  background: transparent;
  border: 1px solid #6c757d;
  color: #6c757d;
}

#cookie-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1001;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  max-width: 500px;
  width: 100%;
}

.cookie-option {
  margin: 15px 0;
}

.modal-buttons {
  margin-top: 20px;
  text-align: right;
}

.modal-buttons button {
  padding: 8px 16px;
  margin-left: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

#save-preferences {
  background: #007bff;
  color: white;
}

#cancel-modal {
  background: #6c757d;
  color: white;
}
```
