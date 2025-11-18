"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthinsuranceshop.ie
Prompt: Write code to implement cookie consent management similar to the GDPR Cookie Consent plugin described on the Health Insurance Shop website, including categories like "Analytics," "Functional," and "Necessary."
Generated: DETERMINISTIC_68efb83d4aeed834
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Consent Management Script
// This script implements GDPR-like cookie consent management
// Categories: "Analytics", "Functional", "Necessary"

// Immediately-Invoked Function Expression (IIFE) to avoid polluting the global scope
(function () {
  // Constants
  const COOKIE_NAME = 'cookieConsent';
  const COOKIE_EXPIRATION_DAYS = 365;

  // Helper function to set a cookie
  function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    document.cookie = `${name}=${value}; expires=${date.toUTCString()}; path=/;`;
  }

  // Helper function to get a cookie
  function getCookie(name) {
    const cookies = document.cookie.split('; ');
    for (let cookie of cookies) {
      const [key, value] = cookie.split('=');
      if (key === name) {
        return value;
      }
    }
    return null;
  }

  // Helper function to delete a cookie
  function deleteCookie(name) {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
  }

  // Display the cookie consent banner
  function displayConsentBanner() {
    const banner = document.createElement('div');
    banner.id = 'cookieConsentBanner';
    banner.style.position = 'fixed';
    banner.style.bottom = '0';
    banner.style.width = '100%';
    banner.style.background = '#333';
    banner.style.color = '#fff';
    banner.style.padding = '15px';
    banner.style.textAlign = 'center';
    banner.style.zIndex = '9999';

    banner.innerHTML = `
      <p>We use cookies to enhance your experience. Choose your preferences:</p>
      <button id="acceptAllCookies" style="margin: 5px;">Accept All</button>
      <button id="customizeCookies" style="margin: 5px;">Customize</button>
    `;

    document.body.appendChild(banner);

    document.getElementById('acceptAllCookies').addEventListener('click', () => {
      saveConsent({
        analytics: true,
        functional: true,
        necessary: true,
      });
    });

    document.getElementById('customizeCookies').addEventListener('click', () => {
      openConsentModal();
    });
  }

  // Open a modal for customizing cookie preferences
  function openConsentModal() {
    const modal = document.createElement('div');
    modal.id = 'cookieConsentModal';
    modal.style.position = 'fixed';
    modal.style.top = '50%';
    modal.style.left = '50%';
    modal.style.transform = 'translate(-50%, -50%)';
    modal.style.background = '#fff';
    modal.style.color = '#333';
    modal.style.padding = '20px';
    modal.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.5)';
    modal.style.zIndex = '9999';

    modal.innerHTML = `
      <h2>Cookie Preferences</h2>
      <label>
        <input type="checkbox" id="analyticsCookies" />
        Analytics Cookies
      </label>
      <br />
      <label>
        <input type="checkbox" id="functionalCookies" />
        Functional Cookies
      </label>
      <br />
      <label>
        Necessary Cookies (always enabled)
      </label>
      <br /><br />
      <button id="savePreferences" style="margin: 5px;">Save Preferences</button>
      <button id="cancelPreferences" style="margin: 5px;">Cancel</button>
    `;

    document.body.appendChild(modal);

    document.getElementById('savePreferences').addEventListener('click', () => {
      const analytics = document.getElementById('analyticsCookies').checked;
      const functional = document.getElementById('functionalCookies').checked;

      saveConsent({
        analytics,
        functional,
        necessary: true,
      });
    });

    document.getElementById('cancelPreferences').addEventListener('click', () => {
      document.body.removeChild(modal);
    });
  }

  // Save cookie consent and set cookies
  function saveConsent(consent) {
    setCookie(COOKIE_NAME, JSON.stringify(consent), COOKIE_EXPIRATION_DAYS);
    document.getElementById('cookieConsentBanner').remove();
    if (document.getElementById('cookieConsentModal')) {
      document.getElementById('cookieConsentModal').remove();
    }
    console.log('Cookie consent saved:', consent);
  }

  // Load consent on page load and act accordingly
  function loadConsent() {
    const consent = getCookie(COOKIE_NAME);
    if (consent) {
      console.log('Cookie consent loaded:', JSON.parse(consent));
    } else {
      displayConsentBanner();
    }
  }

  // Initialize consent management
  loadConsent();
})();
```
