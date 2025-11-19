"""
Generated Code Metadata:
========================
Original URL: https://ghozali-49z.pages.dev
Prompt: Develop a script to handle cookie preferences for a website related to a blockchain-based project like Ghozali 404.
Generated: DETERMINISTIC_b9bc24bdb2d3b8ee
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Preference Manager for a Blockchain-Based Website
 * 
 * This script handles cookie preferences for users visiting the website.
 * It allows users to accept or reject specific categories of cookies
 * and ensures compliance with privacy regulations like GDPR.
 * 
 * Author: [Your Name]
 * Date: [Today's Date]
 */

(function () {
  'use strict';

  // Constants for cookie categories
  const COOKIE_CATEGORIES = {
    essential: 'essential',
    analytics: 'analytics',
    marketing: 'marketing',
  };

  // Default cookie preferences
  const DEFAULT_PREFERENCES = {
    essential: true, // Essential cookies are always enabled
    analytics: false,
    marketing: false,
  };

  // Utility function to set a cookie
  function setCookie(name, value, days) {
    try {
      const date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      const expires = `expires=${date.toUTCString()}`;
      document.cookie = `${name}=${value};${expires};path=/`;
    } catch (error) {
      console.error('Error setting cookie:', error);
    }
  }

  // Utility function to get a cookie value
  function getCookie(name) {
    try {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(`${name}=`)) {
          return cookie.substring(name.length + 1);
        }
      }
      return null;
    } catch (error) {
      console.error('Error getting cookie:', error);
      return null;
    }
  }

  // Utility function to delete a cookie
  function deleteCookie(name) {
    setCookie(name, '', -1);
  }

  // Save user preferences to cookies
  function savePreferences(preferences) {
    try {
      setCookie('cookiePreferences', JSON.stringify(preferences), 365);
    } catch (error) {
      console.error('Error saving preferences:', error);
    }
  }

  // Load user preferences from cookies
  function loadPreferences() {
    try {
      const preferences = getCookie('cookiePreferences');
      return preferences ? JSON.parse(preferences) : DEFAULT_PREFERENCES;
    } catch (error) {
      console.error('Error loading preferences:', error);
      return DEFAULT_PREFERENCES;
    }
  }

  // Display cookie preference modal
  function showCookieModal() {
    const modal = document.createElement('div');
    modal.id = 'cookie-modal';
    modal.style.position = 'fixed';
    modal.style.bottom = '0';
    modal.style.left = '0';
    modal.style.width = '100%';
    modal.style.backgroundColor = '#fff';
    modal.style.borderTop = '1px solid #ccc';
    modal.style.padding = '20px';
    modal.style.boxShadow = '0 -2px 5px rgba(0,0,0,0.1)';
    modal.innerHTML = `
      <h3>Cookie Preferences</h3>
      <p>We use cookies to improve your experience. Please select your preferences:</p>
      <form id="cookie-form">
        <label>
          <input type="checkbox" name="essential" disabled checked />
          Essential Cookies (Required)
        </label><br />
        <label>
          <input type="checkbox" name="analytics" />
          Analytics Cookies
        </label><br />
        <label>
          <input type="checkbox" name="marketing" />
          Marketing Cookies
        </label><br />
        <button type="submit">Save Preferences</button>
      </form>
    `;
    document.body.appendChild(modal);

    const form = document.getElementById('cookie-form');
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const preferences = {
        essential: true,
        analytics: form.analytics.checked,
        marketing: form.marketing.checked,
      };
      savePreferences(preferences);
      document.body.removeChild(modal);
    });
  }

  // Initialize cookie preference manager
  function initCookieManager() {
    const preferences = loadPreferences();
    if (!getCookie('cookiePreferences')) {
      showCookieModal();
    }
    console.log('User cookie preferences:', preferences);
  }

  // Run the cookie manager
  document.addEventListener('DOMContentLoaded', initCookieManager);
})();
```
