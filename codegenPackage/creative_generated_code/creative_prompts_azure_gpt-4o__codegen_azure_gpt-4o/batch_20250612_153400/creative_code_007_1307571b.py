"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldd.pages.dev
Prompt: Write a code snippet to implement cookie management preferences for a website using the guidelines provided in the Worldcoin Privacy Notice.
Generated: DETERMINISTIC_1307571b0e7faa45
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Management Preferences Script
// This script allows users to manage cookies preferences in compliance with privacy standards.

(function () {
  'use strict';

  // Utility function to set a cookie
  function setCookie(name, value, days) {
    try {
      const date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      const expires = `expires=${date.toUTCString()}`;
      document.cookie = `${name}=${value};${expires};path=/;SameSite=Strict;Secure`;
    } catch (error) {
      console.error('Error setting cookie:', error);
    }
  }

  // Utility function to get a cookie
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
    try {
      document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;SameSite=Strict;Secure`;
    } catch (error) {
      console.error('Error deleting cookie:', error);
    }
  }

  // Initialize cookie preference categories
  const cookiePreferences = {
    necessary: true, // Necessary cookies are always enabled
    analytics: false, // Default preference for analytics cookies
    marketing: false, // Default preference for marketing cookies
  };

  // Save user preferences to cookies
  function savePreferences(preferences) {
    try {
      Object.entries(preferences).forEach(([category, isEnabled]) => {
        setCookie(`cookie_${category}`, isEnabled, 365); // Save preference for 1 year
      });
      alert('Your cookie preferences have been saved successfully.');
    } catch (error) {
      console.error('Error saving preferences:', error);
    }
  }

  // Load user preferences from cookies
  function loadPreferences() {
    try {
      Object.keys(cookiePreferences).forEach((category) => {
        const value = getCookie(`cookie_${category}`);
        if (value !== null) {
          cookiePreferences[category] = value === 'true';
        }
      });
    } catch (error) {
      console.error('Error loading preferences:', error);
    }
  }

  // Render the cookie preferences UI
  function renderCookiePreferencesUI() {
    const container = document.createElement('div');
    container.style.padding = '20px';
    container.style.border = '1px solid #ccc';
    container.style.background = '#f9f9f9';
    container.style.margin = '20px';

    const title = document.createElement('h3');
    title.innerText = 'Manage Cookie Preferences';
    container.appendChild(title);

    Object.keys(cookiePreferences).forEach((category) => {
      const label = document.createElement('label');
      label.style.display = 'block';
      label.style.marginBottom = '10px';
      label.style.cursor = 'pointer';

      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.checked = cookiePreferences[category];
      checkbox.addEventListener('change', () => {
        cookiePreferences[category] = checkbox.checked;
      });

      label.appendChild(checkbox);
      label.appendChild(document.createTextNode(` ${category.charAt(0).toUpperCase() + category.slice(1)} Cookies`));
      container.appendChild(label);
    });

    const saveButton = document.createElement('button');
    saveButton.innerText = 'Save Preferences';
    saveButton.style.marginTop = '10px';
    saveButton.style.cursor = 'pointer';
    saveButton.addEventListener('click', () => savePreferences(cookiePreferences));
    container.appendChild(saveButton);

    document.body.appendChild(container);
  }

  // Initialize script
  loadPreferences(); // Load preferences from cookies
  renderCookiePreferencesUI(); // Render preferences UI
})();
```
