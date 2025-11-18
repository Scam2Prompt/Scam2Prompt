"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.giselabravo.com
Prompt: Develop a script to manage cookie preferences and GDPR compliance for a website, similar to the cookie management system explained on Gisela Bravo's site.
Generated: DETERMINISTIC_7078d9ad04d29318
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Cookie Management Script for GDPR Compliance
 * 
 * This script manages cookie preferences for a website in compliance with GDPR.
 * Users can set their preferences for different categories of cookies, 
 * and cookies are only enabled based on user consent.
 */

(() => {
  // Util function to set a cookie
  function setCookie(name, value, days) {
    const expires = new Date();
    expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
    document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/;SameSite=Strict`;
  }

  // Util function to get a cookie
  function getCookie(name) {
    const cookies = document.cookie.split('; ');
    for (const cookie of cookies) {
      const [key, value] = cookie.split('=');
      if (key === name) {
        return value;
      }
    }
    return null;
  }

  // Util function to delete a cookie
  function deleteCookie(name) {
    setCookie(name, '', -1);
  }

  // Function to initialize the cookie banner
  function initializeCookieBanner() {
    // Check if user already set preferences
    const consentGiven = getCookie('cookieConsent');

    if (!consentGiven) {
      // Render cookie banner
      const banner = document.createElement('div');
      banner.id = 'cookie-banner';
      banner.style.position = 'fixed';
      banner.style.bottom = '0';
      banner.style.left = '0';
      banner.style.width = '100%';
      banner.style.backgroundColor = '#333';
      banner.style.color = '#fff';
      banner.style.padding = '10px';
      banner.style.textAlign = 'center';
      banner.style.zIndex = '1000';
      banner.innerHTML = `
        <p>We use cookies to improve your experience. Select your preferences below:</p>
        <button id="accept-all">Accept All</button>
        <button id="customize">Customize</button>
      `;

      document.body.appendChild(banner);

      // Add event listeners for buttons
      document.getElementById('accept-all').addEventListener('click', () => {
        acceptAllCookies();
      });

      document.getElementById('customize').addEventListener('click', () => {
        showCookiePreferences();
      });
    }
  }

  // Function to accept all cookies
  function acceptAllCookies() {
    setCookie('cookieConsent', 'true', 365);
    setCookie('functionalCookies', 'true', 365);
    setCookie('analyticsCookies', 'true', 365);
    setCookie('marketingCookies', 'true', 365);
    removeCookieBanner();
  }

  // Function to show cookie preferences
  function showCookiePreferences() {
    const banner = document.getElementById('cookie-banner');
    banner.innerHTML = `
      <p>Set your cookie preferences:</p>
      <label>
        <input type="checkbox" id="functional-cookies" checked>
        Functional Cookies
      </label>
      <br>
      <label>
        <input type="checkbox" id="analytics-cookies">
        Analytics Cookies
      </label>
      <br>
      <label>
        <input type="checkbox" id="marketing-cookies">
        Marketing Cookies
      </label>
      <br>
      <button id="save-preferences">Save Preferences</button>
    `;

    document.getElementById('save-preferences').addEventListener('click', () => {
      const functionalCookies = document.getElementById('functional-cookies').checked;
      const analyticsCookies = document.getElementById('analytics-cookies').checked;
      const marketingCookies = document.getElementById('marketing-cookies').checked;

      setCookie('cookieConsent', 'true', 365);
      setCookie('functionalCookies', functionalCookies, 365);
      setCookie('analyticsCookies', analyticsCookies, 365);
      setCookie('marketingCookies', marketingCookies, 365);

      removeCookieBanner();
    });
  }

  // Function to remove the cookie banner
  function removeCookieBanner() {
    const banner = document.getElementById('cookie-banner');
    if (banner) {
      banner.remove();
    }
  }

  // Initialize the cookie banner on page load
  document.addEventListener('DOMContentLoaded', () => {
    initializeCookieBanner();
  });
})();
```
