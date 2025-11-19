"""
Generated Code Metadata:
========================
Original URL: https://anko-kurzy.sk
Prompt: "Create a JavaScript function to implement a cookie consent management system for a website, as seen on anko-kurzy.sk."
Generated: DETERMINISTIC_45fced25b4817f2a
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Consent Management System
 * This script provides functionality to display a cookie consent banner,
 * manage user preferences, and store consent information in cookies.
 */

// Function to initialize the cookie consent system
function initializeCookieConsent() {
  // Check if consent has already been given
  const consent = getCookie('cookieConsent');
  if (!consent) {
    // If no consent, display the cookie consent banner
    displayCookieConsentBanner();
  }
}

/**
 * Function to display the cookie consent banner
 */
function displayCookieConsentBanner() {
  // Create the banner element
  const banner = document.createElement('div');
  banner.id = 'cookieConsentBanner';
  banner.style.position = 'fixed';
  banner.style.bottom = '0';
  banner.style.left = '0';
  banner.style.width = '100%';
  banner.style.backgroundColor = '#333';
  banner.style.color = '#fff';
  banner.style.padding = '15px';
  banner.style.textAlign = 'center';
  banner.style.zIndex = '1000';

  // Banner content
  banner.innerHTML = `
    <p>We use cookies to improve your experience on our website. By continuing, you agree to our use of cookies.</p>
    <button id="acceptCookies" style="margin-right: 10px; padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer;">Accept</button>
    <button id="declineCookies" style="padding: 10px 20px; background-color: #f44336; color: white; border: none; cursor: pointer;">Decline</button>
  `;

  // Append the banner to the body
  document.body.appendChild(banner);

  // Add event listeners for buttons
  document.getElementById('acceptCookies').addEventListener('click', () => {
    setCookie('cookieConsent', 'accepted', 365);
    removeCookieConsentBanner();
  });

  document.getElementById('declineCookies').addEventListener('click', () => {
    setCookie('cookieConsent', 'declined', 365);
    removeCookieConsentBanner();
  });
}

/**
 * Function to remove the cookie consent banner
 */
function removeCookieConsentBanner() {
  const banner = document.getElementById('cookieConsentBanner');
  if (banner) {
    banner.remove();
  }
}

/**
 * Function to set a cookie
 * @param {string} name - Name of the cookie
 * @param {string} value - Value of the cookie
 * @param {number} days - Expiration time in days
 */
function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
  const expires = `expires=${date.toUTCString()}`;
  document.cookie = `${name}=${value};${expires};path=/`;
}

/**
 * Function to get a cookie value
 * @param {string} name - Name of the cookie
 * @returns {string|null} - Value of the cookie or null if not found
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
 * Function to delete a cookie
 * @param {string} name - Name of the cookie
 */
function deleteCookie(name) {
  document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`;
}

// Initialize the cookie consent system on page load
document.addEventListener('DOMContentLoaded', initializeCookieConsent);
```
