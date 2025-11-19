"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abubit.com
Prompt: Write a JavaScript function that tracks user consent for cookies, referencing the approach seen on abubit.com.
Generated: DETERMINISTIC_5ad6ecd4b6ea2164
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to manage user consent for cookies.
 * This implementation creates a cookie consent banner, tracks user consent, and stores consent status.
 * 
 * Dependencies: None
 * Usage: Include this script in your project to manage cookie consent.
 */

// Immediately Invoked Function Expression (IIFE) to avoid polluting the global scope
(function () {
  const COOKIE_NAME = 'cookieConsent';
  const COOKIE_EXPIRATION_DAYS = 365;

  /**
   * Utility function to set a cookie.
   * @param {string} name - The name of the cookie.
   * @param {string} value - The value to store in the cookie.
   * @param {number} days - The number of days until the cookie expires.
   */
  function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/`;
  }

  /**
   * Utility function to get the value of a cookie.
   * @param {string} name - The name of the cookie to retrieve.
   * @returns {string|null} - The value of the cookie or null if not found.
   */
  function getCookie(name) {
    const nameEQ = `${name}=`;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      if (cookie.indexOf(nameEQ) === 0) {
        return cookie.substring(nameEQ.length, cookie.length);
      }
    }
    return null;
  }

  /**
   * Function to create and show the cookie consent banner.
   * This function is only triggered if consent has not been provided.
   */
  function createCookieConsentBanner() {
    // Check if consent has already been given
    if (getCookie(COOKIE_NAME)) {
      return; // User has already given consent
    }

    // Create the banner element
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.style.position = 'fixed';
    banner.style.bottom = '0';
    banner.style.width = '100%';
    banner.style.backgroundColor = '#000';
    banner.style.color = '#fff';
    banner.style.padding = '10px';
    banner.style.textAlign = 'center';
    banner.style.zIndex = '1000';

    // Banner content
    banner.innerHTML = `
      <p>
        This website uses cookies to ensure you get the best experience on our website. 
        <a href="/privacy-policy" style="color: #ffd700;">Learn more</a>.
      </p>
      <button id="accept-cookies" style="margin: 5px; padding: 5px 10px; background-color: #28a745; color: #fff; border: none; cursor: pointer;">
        Accept
      </button>
      <button id="decline-cookies" style="margin: 5px; padding: 5px 10px; background-color: #dc3545; color: #fff; border: none; cursor: pointer;">
        Decline
      </button>
    `;

    // Append banner to the body
    document.body.appendChild(banner);

    // Add event listeners for buttons
    document.getElementById('accept-cookies').addEventListener('click', function () {
      setCookie(COOKIE_NAME, 'accepted', COOKIE_EXPIRATION_DAYS);
      document.body.removeChild(banner); // Remove banner after consent
    });

    document.getElementById('decline-cookies').addEventListener('click', function () {
      setCookie(COOKIE_NAME, 'declined', COOKIE_EXPIRATION_DAYS);
      document.body.removeChild(banner); // Remove banner after declining
    });
  }

  // Initialize cookie consent management
  document.addEventListener('DOMContentLoaded', createCookieConsentBanner);
})();
```
