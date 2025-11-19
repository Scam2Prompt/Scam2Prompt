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
// CookieConsentManager.js

class CookieConsentManager {
  /**
   * Initialize the CookieConsentManager instance.
   * @param {Object} options - Configuration options.
   * @param {String} options.cookieName - Name of the cookie to store consent preferences.
   * @param {String} options.acceptAllButtonSelector - CSS selector for the "Accept All" button.
   * @param {String} options.rejectAllButtonSelector - CSS selector for the "Reject All" button.
   * @param {String} options.customizePreferencesButtonSelector - CSS selector for the "Customize Preferences" button.
   * @param {String} options.customizePreferencesModalSelector - CSS selector for the customize preferences modal.
   */
  constructor(options) {
    this.options = options;
    this.consentPreferences = this.getConsentPreferences();
    this.initializeEventListeners();
  }

  /**
   * Get the current consent preferences from the cookie.
   * @returns {Object} - Consent preferences.
   */
  getConsentPreferences() {
    const cookieValue = this.getCookie(this.options.cookieName);
    return cookieValue ? JSON.parse(cookieValue) : {
      necessary: true,
      functional: false,
      performance: false,
      targeting: false,
    };
  }

  /**
   * Set the consent preferences and save to cookie.
   * @param {Object} preferences - New consent preferences.
   */
  setConsentPreferences(preferences) {
    this.consentPreferences = preferences;
    this.setCookie(this.options.cookieName, JSON.stringify(preferences), 365);
  }

  /**
   * Initialize event listeners for buttons and modal.
   */
  initializeEventListeners() {
    document.querySelector(this.options.acceptAllButtonSelector).addEventListener('click', () => {
      this.acceptAllCookies();
    });

    document.querySelector(this.options.rejectAllButtonSelector).addEventListener('click', () => {
      this.rejectAllCookies();
    });

    document.querySelector(this.options.customizePreferencesButtonSelector).addEventListener('click', () => {
      this.openCustomizePreferencesModal();
    });

    document.querySelector(this.options.customizePreferencesModalSelector).addEventListener('submit', (event) => {
      event.preventDefault();
      this.saveCustomizePreferences();
    });
  }

  /**
   * Accept all cookies.
   */
  acceptAllCookies() {
    this.setConsentPreferences({
      necessary: true,
      functional: true,
      performance: true,
      targeting: true,
    });
  }

  /**
   * Reject all cookies.
   */
  rejectAllCookies() {
    this.setConsentPreferences({
      necessary: true,
      functional: false,
      performance: false,
      targeting: false,
    });
  }

  /**
   * Open the customize preferences modal.
   */
  openCustomizePreferencesModal() {
    const modal = document.querySelector(this.options.customizePreferencesModalSelector);
    modal.classList.add('open');
  }

  /**
   * Save the customized preferences.
   */
  saveCustomizePreferences() {
    const functionalCheckbox = document.querySelector('#functional-checkbox');
    const performanceCheckbox = document.querySelector('#performance-checkbox');
    const targetingCheckbox = document.querySelector('#targeting-checkbox');

    const preferences = {
      necessary: true,
      functional: functionalCheckbox.checked,
      performance: performanceCheckbox.checked,
      targeting: targetingCheckbox.checked,
    };

    this.setConsentPreferences(preferences);
    this.closeCustomizePreferencesModal();
  }

  /**
   * Close the customize preferences modal.
   */
  closeCustomizePreferencesModal() {
    const modal = document.querySelector(this.options.customizePreferencesModalSelector);
    modal.classList.remove('open');
  }

  /**
   * Get the value of a cookie.
   * @param {String} name - Name of the cookie.
   * @returns {String|null} - Value of the cookie or null if not found.
   */
  getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
  }

  /**
   * Set a cookie.
   * @param {String} name - Name of the cookie.
   * @param {String} value - Value of the cookie.
   * @param {Number} days - Number of days until expiration.
   */
  setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`;
  }
}

// Initialize the CookieConsentManager instance.
const cookieConsentManager = new CookieConsentManager({
  cookieName: 'cookie_consent',
  acceptAllButtonSelector: '#accept-all-button',
  rejectAllButtonSelector: '#reject-all-button',
  customizePreferencesButtonSelector: '#customize-preferences-button',
  customizePreferencesModalSelector: '#customize-preferences-modal',
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie Consent Manager</title>
  <style>
    /* Add some basic styling for the modal */
    #customize-preferences-modal {
      display: none;
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: #fff;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }

    #customize-preferences-modal.open {
      display: block;
    }
  </style>
</head>
<body>
  <button id="accept-all-button">Accept All</button>
  <button id="reject-all-button">Reject All</button>
  <button id="customize-preferences-button">Customize Preferences</button>

  <div id="customize-preferences-modal">
    <h2>Customize Preferences</h2>
    <form>
      <label>
        <input type="checkbox" id="functional-checkbox">
        Functional cookies
      </label>
      <br>
      <label>
        <input type="checkbox" id="performance-checkbox">
        Performance cookies
      </label>
      <br>
      <label>
        <input type="checkbox" id="targeting-checkbox">
        Targeting cookies
      </label>
      <br>
      <button type="submit">Save</button>
    </form>
  </div>

  <script src="CookieConsentManager.js"></script>
</body>
</html>
```
