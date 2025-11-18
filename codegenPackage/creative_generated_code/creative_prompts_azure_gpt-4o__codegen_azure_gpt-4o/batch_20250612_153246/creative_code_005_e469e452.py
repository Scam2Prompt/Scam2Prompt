"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eyemagazine.gr
Prompt: Write JavaScript code to implement cookie settings functionality, similar to the GDPR compliance system used by Eye Magazine.
Generated: DETERMINISTIC_e469e452f6e07b7b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Cookie Settings Functionality
 * This script implements cookie settings functionality for GDPR compliance.
 * Users can choose to accept or reject cookies based on preferences.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Constants for cookie categories
const COOKIE_CATEGORIES = {
  NECESSARY: 'necessary',
  ANALYTICS: 'analytics',
  MARKETING: 'marketing',
};

// Utility to set a cookie
function setCookie(name, value, days) {
  try {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/;SameSite=Strict`;
  } catch (error) {
    console.error('Error setting cookie:', error);
  }
}

// Utility to get a cookie by name
function getCookie(name) {
  try {
    const cookies = document.cookie.split('; ');
    const cookie = cookies.find(row => row.startsWith(name + '='));
    return cookie ? cookie.split('=')[1] : null;
  } catch (error) {
    console.error('Error getting cookie:', error);
    return null;
  }
}

// Utility to delete a cookie
function deleteCookie(name) {
  try {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;SameSite=Strict`;
  } catch (error) {
    console.error('Error deleting cookie:', error);
  }
}

// Initialize cookie settings modal
function initCookieSettings() {
  const cookieSettingsModal = document.createElement('div');
  cookieSettingsModal.id = 'cookie-settings-modal';
  cookieSettingsModal.style.position = 'fixed';
  cookieSettingsModal.style.bottom = '20px';
  cookieSettingsModal.style.right = '20px';
  cookieSettingsModal.style.padding = '15px';
  cookieSettingsModal.style.backgroundColor = '#fff';
  cookieSettingsModal.style.border = '1px solid #ccc';
  cookieSettingsModal.style.boxShadow = '0 4px 10px rgba(0, 0, 0, 0.2)';
  cookieSettingsModal.innerHTML = `
    <h3>Cookie Preferences</h3>
    <p>Select which cookies you want to allow:</p>
    <form id="cookie-settings-form">
      <label>
        <input type="checkbox" name="necessary" disabled checked />
        Necessary Cookies (Always enabled)
      </label><br />
      <label>
        <input type="checkbox" name="analytics" />
        Analytics Cookies
      </label><br />
      <label>
        <input type="checkbox" name="marketing" />
        Marketing Cookies
      </label><br />
      <button type="button" id="save-cookie-settings">Save Preferences</button>
    </form>
  `;
  document.body.appendChild(cookieSettingsModal);

  const saveButton = document.getElementById('save-cookie-settings');
  saveButton.addEventListener('click', saveCookiePreferences);
}

// Save cookie preferences
function saveCookiePreferences() {
  const form = document.getElementById('cookie-settings-form');
  const preferences = {
    [COOKIE_CATEGORIES.NECESSARY]: true, // Necessary cookies are always enabled
    [COOKIE_CATEGORIES.ANALYTICS]: form.analytics.checked,
    [COOKIE_CATEGORIES.MARKETING]: form.marketing.checked,
  };

  // Save preferences to cookies
  for (const [category, isEnabled] of Object.entries(preferences)) {
    setCookie(`cookie_${category}`, isEnabled ? 'enabled' : 'disabled', 365);
  }

  alert('Your cookie preferences have been saved.');
  document.getElementById('cookie-settings-modal').remove();
}

// Check if preferences already exist
function checkExistingPreferences() {
  const necessaryCookie = getCookie(`cookie_${COOKIE_CATEGORIES.NECESSARY}`);
  const analyticsCookie = getCookie(`cookie_${COOKIE_CATEGORIES.ANALYTICS}`);
  const marketingCookie = getCookie(`cookie_${COOKIE_CATEGORIES.MARKETING}`);

  if (!necessaryCookie || !analyticsCookie || !marketingCookie) {
    initCookieSettings(); // Show settings modal if preferences are not set
  }
}

// Initialize cookie functionality on page load
document.addEventListener('DOMContentLoaded', () => {
  checkExistingPreferences(); // Check for existing preferences
});
```
