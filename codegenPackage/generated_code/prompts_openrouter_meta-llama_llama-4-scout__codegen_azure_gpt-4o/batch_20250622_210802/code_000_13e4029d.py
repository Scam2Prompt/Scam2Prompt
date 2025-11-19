"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: "Write a code snippet to implement a cookie consent management system that respects user preferences for necessary, functional, analytics, and advertisement cookies, similar to the one described on the Masa website."
Generated: DETERMINISTIC_13e4029df34569b4
Batch ID: 20250622_210802
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
 * This script manages user preferences for necessary, functional, analytics, and advertisement cookies.
 * It respects user choices and provides a clean interface for managing cookie preferences.
 */

// Utility function to set a cookie
function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
  document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`;
}

// Utility function to get a cookie
function getCookie(name) {
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
    const [key, value] = cookie.trim().split('=');
    if (key === name) {
      return value;
    }
  }
  return null;
}

// Utility function to delete a cookie
function deleteCookie(name) {
  document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`;
}

// Initialize cookie consent preferences
function initializeCookieConsent() {
  const consent = getCookie('cookieConsent');
  if (!consent) {
    showCookieConsentBanner();
  }
}

// Show cookie consent banner
function showCookieConsentBanner() {
  const banner = document.createElement('div');
  banner.id = 'cookieConsentBanner';
  banner.style.position = 'fixed';
  banner.style.bottom = '0';
  banner.style.width = '100%';
  banner.style.backgroundColor = '#f4f4f4';
  banner.style.padding = '10px';
  banner.style.boxShadow = '0 -2px 5px rgba(0,0,0,0.1)';
  banner.innerHTML = `
    <p>We use cookies to improve your experience. Manage your preferences below:</p>
    <button id="acceptNecessary">Accept Necessary</button>
    <button id="acceptFunctional">Accept Functional</button>
    <button id="acceptAnalytics">Accept Analytics</button>
    <button id="acceptAds">Accept Ads</button>
    <button id="rejectAll">Reject All</button>
  `;
  document.body.appendChild(banner);

  // Add event listeners for buttons
  document.getElementById('acceptNecessary').addEventListener('click', () => handleConsent('necessary'));
  document.getElementById('acceptFunctional').addEventListener('click', () => handleConsent('functional'));
  document.getElementById('acceptAnalytics').addEventListener('click', () => handleConsent('analytics'));
  document.getElementById('acceptAds').addEventListener('click', () => handleConsent('ads'));
  document.getElementById('rejectAll').addEventListener('click', () => handleConsent('rejectAll'));
}

// Handle user consent
function handleConsent(type) {
  switch (type) {
    case 'necessary':
      setCookie('cookieConsent', JSON.stringify({ necessary: true }), 365);
      break;
    case 'functional':
      setCookie('cookieConsent', JSON.stringify({ necessary: true, functional: true }), 365);
      break;
    case 'analytics':
      setCookie('cookieConsent', JSON.stringify({ necessary: true, analytics: true }), 365);
      break;
    case 'ads':
      setCookie('cookieConsent', JSON.stringify({ necessary: true, ads: true }), 365);
      break;
    case 'rejectAll':
      deleteCookie('cookieConsent');
      break;
    default:
      console.error('Invalid consent type');
  }
  removeCookieConsentBanner();
}

// Remove cookie consent banner
function removeCookieConsentBanner() {
  const banner = document.getElementById('cookieConsentBanner');
  if (banner) {
    banner.remove();
  }
}

// Check and apply cookie preferences
function applyCookiePreferences() {
  const consent = getCookie('cookieConsent');
  if (consent) {
    const preferences = JSON.parse(consent);
    if (preferences.analytics) {
      // Load analytics scripts
      console.log('Analytics cookies enabled');
    }
    if (preferences.ads) {
      // Load advertisement scripts
      console.log('Advertisement cookies enabled');
    }
    if (preferences.functional) {
      // Enable functional cookies
      console.log('Functional cookies enabled');
    }
  }
}

// Initialize the cookie consent system
document.addEventListener('DOMContentLoaded', () => {
  initializeCookieConsent();
  applyCookiePreferences();
});
```
